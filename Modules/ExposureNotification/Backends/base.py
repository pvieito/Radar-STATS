import datetime
import io
import logging
import os
import tempfile
import uuid
import zipfile
from typing import *

import pandas as pd
import requests

from Modules.ExposureNotification import exposure_notification_exceptions
from Modules.ExposureNotification.ProtocolBuffers.ExposureNotification import TemporaryExposureKeyExport_pb2

maximum_key_rolling_period = 24 * 60  # 24h in 10 min intervals
maximum_key_rolling_period_in_seconds = 24 * 60 * 60

_protobuf_export_file_name = "export.bin"


class BaseBackendClient:
    def __init__(
            self, *, backend_identifier: str, server_endpoint_url: str = None,
            use_proxy_if_available=None, proxy_url=None):
        self.backend_identifier = backend_identifier
        self.server_endpoint_url = server_endpoint_url
        self.use_proxy_if_available = use_proxy_if_available
        self.proxy_url = proxy_url

    def generate_exposure_keys_export_endpoints_with_parameters(self, **kwargs) -> List[dict]:
        raise NotImplemented()

    def get_supported_countries(self, **kwargs) -> List[str]:
        raise NotImplemented()

    def download_exposure_keys_with_parameters(
            self, **kwargs) -> pd.DataFrame:
        endpoints_with_parameters = \
            self.generate_exposure_keys_export_endpoints_with_parameters(**kwargs)

        exposure_keys_df = pd.DataFrame()
        for endpoint_with_parameters in endpoints_with_parameters:
            try:
                endpoint = endpoint_with_parameters.pop("endpoint")
                endpoint_exposure_keys_df = self._download_exposure_keys_from_endpoint_with_parameters(
                    endpoint=endpoint, parameters=endpoint_with_parameters, **kwargs)
                exposure_keys_df = exposure_keys_df.append(endpoint_exposure_keys_df)
            except exposure_notification_exceptions.NoKeysFoundException as e:
                logging.warning(repr(e))

        if not exposure_keys_df.empty:
            valid_generation_dates = self.get_generation_dates_from_parameters(
                as_string=True, **kwargs)
            exposure_keys_df = exposure_keys_df[
                exposure_keys_df.generation_date_string.isin(valid_generation_dates)]

        return exposure_keys_df

    def _download_exposure_keys_from_endpoint_with_parameters(
            self, endpoint, parameters=None, save_raw_zip_path_prefix=None, **_kwargs) -> pd.DataFrame:
        if parameters is None:
            parameters = dict()
        parameters = parameters.copy()
        parameters.update(dict(
            backend_identifier=self.backend_identifier,
            server_endpoint_url=self.server_endpoint_url))

        logging.info(f"Downloading TEKs from '{endpoint}' (parameters: {parameters})...")
        no_keys_found_exception = \
            exposure_notification_exceptions.NoKeysFoundException(
                f"No exposure keys found on endpoint '{endpoint}' (parameters: {parameters}).")
        request_response = self.send_get_request(url=endpoint)
        try:
            request_response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if request_response.status_code == 404:
                raise no_keys_found_exception
            else:
                raise e
        file_bytes = request_response.content

        if save_raw_zip_path_prefix:
            endpoint_identifier_components = \
                [self.backend_identifier] + parameters["endpoint_identifier_components"]
            endpoint_identifier_components = "-".join(map(str, endpoint_identifier_components))
            raw_zip_path = self.backend_identifier + f"/Current/TEKs-{endpoint_identifier_components}.zip"
            raw_zip_path = save_raw_zip_path_prefix + raw_zip_path
            os.makedirs(os.path.dirname(raw_zip_path), exist_ok=True)
            with open(raw_zip_path, "wb") as f:
                f.write(file_bytes)

        if len(file_bytes) == 0:
            raise no_keys_found_exception

        return self._parse_exposure_keys_export_file(file_bytes=file_bytes)

    def _parse_exposure_keys_export_file(self, *, file_bytes: bytes = None) -> pd.DataFrame:
        exposure_keys = []

        g = self.load_object_from_signed_and_compressed_protobuf(
            file_bytes=file_bytes,
            protobuf_class=TemporaryExposureKeyExport_pb2.TemporaryExposureKeyExport,
            remove_prefix=16)
        start_timestamp = str(g.start_timestamp)
        end_timestamp = str(g.end_timestamp)
        region = str(g.region).upper()
        verification_key_version = str(g.signature_infos[0].verification_key_version).upper()
        verification_key_id = str(g.signature_infos[0].verification_key_id).upper()
        signature_algorithm = str(g.signature_infos[0].signature_algorithm).upper()

        logging_details = []
        logging_details.append(f"Exposure Key File")
        logging_details.append(f"Timestamp Range: {start_timestamp} -> {end_timestamp}")
        logging_details.append(f"Region: {region}")
        logging_details.append("")
        logging_details.append("Signature Details:")
        logging_details.append(f"Verification Key Version: {verification_key_version}")
        logging_details.append(f"Verification Key ID: {verification_key_id}")
        logging_details.append(f"Signature Algorithm: {signature_algorithm}")
        logging_details.append("")
        logging_details.append(f"Exposure Keys ({len(g.keys)}):")

        for key in g.keys:
            key_rolling_start_timestamp = \
                key.rolling_start_interval_number * 10 * 60
            key_rolling_period_in_seconds = key.rolling_period * 10 * 60
            if key_rolling_period_in_seconds > maximum_key_rolling_period_in_seconds:
                raise Exception(
                    f"Invalid key 'key_rolling_period': "
                    f"{key_rolling_period_in_seconds}s "
                    f"(expected: <={maximum_key_rolling_period_in_seconds}s)")

            generation_datetime = \
                datetime.datetime.utcfromtimestamp(key_rolling_start_timestamp)
            generation_date_string = generation_datetime.strftime("%Y-%m-%d")

            key_uuid = uuid.UUID(bytes=key.key_data)
            exposure_keys.append(dict(
                generation_datetime=generation_datetime,
                generation_date_string=generation_date_string,
                region=str(g.region).upper(),
                verification_key_version=str(g.signature_infos[0].verification_key_version).upper(),
                verification_key_id=str(g.signature_infos[0].verification_key_id).upper(),
                signature_algorithm=str(g.signature_infos[0].signature_algorithm).upper(),
                key_data=key_uuid,
                rolling_start_interval_number=key.rolling_start_interval_number,
                rolling_period=key.rolling_period,
                transmission_risk_level=key.transmission_risk_level,
            ))
            logging_details.append(
                f"{key_uuid} (rolling start interval number: {key_rolling_start_timestamp}, "
                f"rolling period: {key_rolling_period_in_seconds}s, "
                f"report type: {key.report_type})")

        logging_details = "\n".join(logging_details)
        logging.info(logging_details)

        exposure_keys_df = pd.DataFrame.from_records(exposure_keys)
        exposure_keys_df["backend_identifier"] = self.backend_identifier
        return exposure_keys_df

    @staticmethod
    def load_object_from_signed_and_compressed_protobuf(file_bytes: bytes, protobuf_class, remove_prefix=None):
        with io.BytesIO(file_bytes) as f:
            with zipfile.ZipFile(f, "r") as z:
                temporary_directory = tempfile.gettempdir()
                temporary_directory_uuid = str(uuid.uuid4()).upper()
                temporary_directory = os.path.join(temporary_directory, temporary_directory_uuid)

                z.extractall(temporary_directory)

                protobuf_file_path = \
                    os.path.join(temporary_directory, _protobuf_export_file_name)
                with open(protobuf_file_path, "rb") as p:
                    g = protobuf_class()
                    if remove_prefix:
                        p.read(remove_prefix)
                    g.ParseFromString(p.read())
        return g

    @staticmethod
    def send_get_request(url, **kwargs):
        return requests.get(url, **kwargs)

    @staticmethod
    def get_generation_dates_from_parameters(
            *, generation_dates: List[datetime.datetime] = None,
            generation_days: int = None, as_string: bool = None, **_kwargs):
        if isinstance(generation_dates, datetime.datetime):
            generation_dates = [generation_dates]
        else:
            if generation_days is None:
                generation_days = 14
            now_datetime = datetime.datetime.utcnow()
            generation_dates = [now_datetime - datetime.timedelta(days=i) for i in range(generation_days)]

        if as_string:
            generation_dates = list(map(lambda x: x.strftime("%Y-%m-%d"), generation_dates))

        return generation_dates
