import datetime
from typing import *

import pytz

from .base import BaseBackendClient

_dp3t_server_exposed_endpoint_path = "/v{version}/gaen/exposed/"

_unix_epoch_datetime = datetime.datetime(year=1970, month=1, day=1, tzinfo=pytz.utc)


class DP3TBackendClient(BaseBackendClient):
    def __init__(self, version=None, origin_country=None, **kwargs):
        if version is None:
            version = 1
        self.version = version
        self.origin_country = origin_country
        super().__init__(**kwargs)

    def generate_exposure_keys_export_endpoints_with_parameters(self, **kwargs) -> List[dict]:
        exposure_keys_export_endpoints = []
        exposed_endpoint_path = \
            self.server_endpoint_url + _dp3t_server_exposed_endpoint_path.format(version=self.version)
        if self.version == 1:
            generation_dates = self.get_generation_dates_from_parameters(**kwargs)
            for generation_date in generation_dates:
                generation_datetime = datetime.datetime(
                    year=generation_date.year,
                    month=generation_date.month,
                    day=generation_date.day,
                    tzinfo=pytz.utc)
                generation_date_string = generation_datetime.strftime("%Y-%m-%d")
                generation_datetime_in_epoch_seconds = \
                    int((generation_datetime - _unix_epoch_datetime).total_seconds())
                endpoint_timestamp = str(generation_datetime_in_epoch_seconds) + "000"
                exposure_keys_export_endpoint = exposed_endpoint_path + endpoint_timestamp
                exposure_keys_export_endpoints.append(dict(
                    endpoint=exposure_keys_export_endpoint,
                    generation_date=generation_date_string,
                    endpoint_identifier_components=[
                        generation_date_string
                    ],
                ))
        elif self.version == 2:
            exposure_keys_export_endpoint = exposed_endpoint_path
            if self.origin_country:
                exposure_keys_export_endpoint += "?originCountries=" + self.origin_country
            exposure_keys_export_endpoints.append(dict(
                endpoint=exposure_keys_export_endpoint,
                origin_country=self.origin_country,
                endpoint_identifier_components=[
                    self.origin_country
                ],
            ))
        else:
            raise NotImplementedError(f"Unsupported DP3T version '{self.version}'.")
        return exposure_keys_export_endpoints
