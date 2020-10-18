from typing import *

from .base import BaseBackendKeysDownloader

_corona_warn_app_server_diagnosis_keys_endpoint_path = \
    "/version/v1/diagnosis-keys/country/{country}/date/{upload_date_string}"


class CoronaWarnAppBackendKeysDownloader(BaseBackendKeysDownloader):
    def __init__(self, target_country: str, **kwargs):
        super().__init__(**kwargs)
        self.target_country = target_country

    def generate_exposure_keys_export_endpoints_with_parameters(
            self, **kwargs) -> List[dict]:
        exposure_keys_export_endpoints = []
        dates = self.get_dates_from_parameters(**kwargs)
        for date in dates:
            upload_date_string = date.strftime("%Y-%m-%d")
            diagnosis_keys_endpoint_url = \
                self.server_endpoint_url + \
                _corona_warn_app_server_diagnosis_keys_endpoint_path
            exposure_keys_export_endpoint = diagnosis_keys_endpoint_url.format(
                country=self.target_country, upload_date_string=upload_date_string)
            exposure_keys_export_endpoints.append(dict(
                endpoint=exposure_keys_export_endpoint,
                country=self.target_country,
                upload_date=upload_date_string,
                endpoint_identifier_components=[
                    self.target_country,
                    upload_date_string
                ],
            ))
        return exposure_keys_export_endpoints
