import datetime
from typing import *

import pytz

from .base import BaseBackendKeysDownloader

_dp3t_server_exposed_endpoint_path = "/v1/gaen/exposed/"

_unix_epoch_datetime = datetime.datetime(year=1970, month=1, day=1, tzinfo=pytz.utc)


class DP3TBackendKeysDownloader(BaseBackendKeysDownloader):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def generate_exposure_keys_export_endpoints_with_parameters(self, **kwargs) -> List[dict]:
        exposure_keys_export_endpoints = []
        dates = self.get_dates_from_parameters(**kwargs)
        for date in dates:
            generation_datetime = datetime.datetime(
                year=date.year,
                month=date.month,
                day=date.day,
                tzinfo=pytz.utc)
            generation_date_string = generation_datetime.strftime("%Y-%m-%d")
            generation_datetime_in_epoch_seconds = \
                int((generation_datetime - _unix_epoch_datetime).total_seconds())
            endpoint_timestamp = str(generation_datetime_in_epoch_seconds) + "000"
            exposure_keys_export_endpoint = \
                self.server_endpoint_url + _dp3t_server_exposed_endpoint_path + endpoint_timestamp
            exposure_keys_export_endpoints.append(dict(
                endpoint=exposure_keys_export_endpoint,
                generation_date=generation_date_string,
                endpoint_identifier_components=[
                    generation_date_string
                ],
            ))
        return exposure_keys_export_endpoints
