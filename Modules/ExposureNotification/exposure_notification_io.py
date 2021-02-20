import datetime
import logging
from typing import *

import pandas as pd

from .BackendClients.corona_warn_app import CoronaWarnAppBackendClient
from .BackendClients.dp3t import DP3TBackendClient
from .BackendClients.immuni import ImmuniBackendClient
from .BackendClients.smitte_stop import SmitteStopBackendClient
from .SourceRegionsProviders.efgs import EFGSSourceRegionsProvider

_backend_clients = [
    DP3TBackendClient(
        backend_identifier="ES",
        server_endpoint_url="https://radarcovid.covid19.gob.es/dp3t",
        version=2,
        origin_country="ES",
        source_regions_provider=EFGSSourceRegionsProvider(
            native_region="ES",
            native_periods=[
                (datetime.date(2020, 12, 3), datetime.date(2020, 12, 4)),
                (datetime.date(2021, 2, 20), datetime.date.max),
            ])),
    DP3TBackendClient(
        backend_identifier="ES@PRE",
        server_endpoint_url="https://radarcovidpre.covid19.gob.es/dp3t"),
    DP3TBackendClient(
        backend_identifier="IT@ES",
        server_endpoint_url="https://radarcovid.covid19.gob.es/dp3t",
        version=2,
        origin_country="IT"),
    DP3TBackendClient(
        backend_identifier="DE@ES",
        server_endpoint_url="https://radarcovid.covid19.gob.es/dp3t",
        version=2,
        origin_country="DE"),
    DP3TBackendClient(
        backend_identifier="PT@ES",
        server_endpoint_url="https://radarcovid.covid19.gob.es/dp3t",
        version=2,
        origin_country="PT"),
    DP3TBackendClient(
        backend_identifier="CH",
        server_endpoint_url="https://www.pt.bfs.admin.ch"),
    DP3TBackendClient(
        backend_identifier="PT",
        server_endpoint_url="https://stayaway.incm.pt",
        source_regions_provider=EFGSSourceRegionsProvider(native_region="PT")),
    DP3TBackendClient(
        backend_identifier="EE",
        server_endpoint_url="https://enapi.sm.ee/authorization",
        source_regions_provider=EFGSSourceRegionsProvider(native_region="EE")),
    DP3TBackendClient(
        backend_identifier="MT",
        server_endpoint_url="https://mt-dpppt-ws.azurewebsites.net"),
    CoronaWarnAppBackendClient(
        backend_identifier="DE",
        server_endpoint_url="https://svc90.main.px.t-online.de",
        target_country="DE",
        source_regions_provider=EFGSSourceRegionsProvider(native_region="DE")),
    CoronaWarnAppBackendClient(
        backend_identifier="BE",
        server_endpoint_url="https://c19distcdn-prd.ixor.be",
        target_country="BE",
        source_regions_provider=EFGSSourceRegionsProvider(native_region="BE")),
    CoronaWarnAppBackendClient(
        backend_identifier="BE@TST",
        server_endpoint_url="https://c19distcdn-tst.ixor.be",
        target_country="BE"),
    ImmuniBackendClient(
        backend_identifier="IT",
        server_endpoint_url="https://get.immuni.gov.it",
        source_regions_provider=EFGSSourceRegionsProvider(native_region="IT")),
    SmitteStopBackendClient(
        backend_identifier="DK",
        server_endpoint_url="https://app.smittestop.dk/API",
        source_regions_provider=EFGSSourceRegionsProvider(native_region="DK")),
]
_default_backend_identifiers = [
    "ES", "ES@PRE", "IT@ES", "DE@ES", "PT@ES",  # DP3T v2
    "CH", "PT", "EE", "MT",  # DP3T v1
    "DE",  # Corona-Warn-App
]


def get_backend_client_with_identifier(*, backend_identifier: str):
    for backend_client in _backend_clients:
        if backend_identifier == backend_client.backend_identifier:
            return backend_client
    raise ValueError(f"Backend client with identifier '{backend_identifier}' not available.")


def download_exposure_keys_from_backends(
        *, backend_identifiers=None, fail_on_error_backend_identifiers=None,
        save_raw_zip_backend_identifiers=None, save_raw_zip_path_prefix=None, **kwargs) -> List[dict]:
    if backend_identifiers is None:
        backend_identifiers = _default_backend_identifiers
    if save_raw_zip_backend_identifiers is None:
        save_raw_zip_backend_identifiers = backend_identifiers

    exposure_keys_df = pd.DataFrame()
    for backend_identifier in backend_identifiers:
        backend_client = get_backend_client_with_identifier(backend_identifier=backend_identifier)

        try:
            backend_kwargs = kwargs.copy()
            if save_raw_zip_path_prefix and backend_identifier in save_raw_zip_backend_identifiers:
                backend_kwargs.update(dict(save_raw_zip_path_prefix=save_raw_zip_path_prefix))
            backend_exposure_keys_df = backend_client.download_exposure_keys_with_parameters(**kwargs)
            exposure_keys_df = exposure_keys_df.append(backend_exposure_keys_df)
        except Exception as e:
            if fail_on_error_backend_identifiers and \
                    backend_client.backend_identifier in fail_on_error_backend_identifiers:
                raise e
            logging.warning(
                f"Error downloading exposure keys from "
                f"backend '{backend_client.backend_identifier}': {repr(e)}", exc_info=True)
    return exposure_keys_df
