from typing import *

from .base import BaseBackendKeysDownloader

_corona_warn_app_server_diagnosis_keys_endpoint_path = \
    "/version/v1/diagnosis-keys/country/{country}/date"


class CoronaWarnAppBackendKeysDownloader(BaseBackendKeysDownloader):
    def __init__(self, target_country: str, **kwargs):
        super().__init__(**kwargs)
        self.target_country = target_country

    def generate_exposure_keys_export_endpoints_with_parameters(
            self, **kwargs) -> List[dict]:
        diagnosis_keys_endpoint_url = \
            self.server_endpoint_url + \
            _corona_warn_app_server_diagnosis_keys_endpoint_path.format(
                country=self.target_country)

        response = self.send_get_request(diagnosis_keys_endpoint_url)
        response.raise_for_status()
        upload_dates = response.json()

        exposure_keys_export_endpoints = []
        for upload_date in upload_dates:
            exposure_keys_export_endpoint = \
                diagnosis_keys_endpoint_url + "/" + upload_date
            exposure_keys_export_endpoints.append(dict(
                endpoint=exposure_keys_export_endpoint,
                country=self.target_country,
                upload_date=upload_date,
                endpoint_identifier_components=[
                    self.target_country,
                    upload_date
                ],
            ))
        return exposure_keys_export_endpoints
