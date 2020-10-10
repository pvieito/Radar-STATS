from typing import *

from Modules.ExposureNotification.exposure_notification_io import ExposureNotificationServiceKeysDownloader

_corona_warn_app_server_diagnosis_keys_endpoint_path = \
    "/version/v1/diagnosis-keys/country/{country}/date/{upload_date_string}"

_corona_warn_app_default_server_endpoint_url = \
    "https://svc90.main.px.t-online.de"
_corona_warn_app_default_country = "DE"


class CoronaWarnAppServiceKeysDownloader(ExposureNotificationServiceKeysDownloader):
    def generate_exposure_keys_export_endpoints_with_parameters(
            self, server_endpoint_url: str = None, country: str = None, **kwargs) -> List[dict]:
        if server_endpoint_url is None:
            server_endpoint_url = _corona_warn_app_default_server_endpoint_url
        if country is None:
            country = _corona_warn_app_default_country

        exposure_keys_export_endpoints = []
        dates = self.get_dates_from_parameters(**kwargs)
        for date in dates:
            upload_date_string = date.strftime("%Y-%m-%d")
            diagnosis_keys_endpoint_url = \
                server_endpoint_url + \
                _corona_warn_app_server_diagnosis_keys_endpoint_path
            exposure_keys_export_endpoint = diagnosis_keys_endpoint_url.format(
                country=country, upload_date_string=upload_date_string)
            exposure_keys_export_endpoints.append(dict(
                endpoint=exposure_keys_export_endpoint,
                country=country,
                upload_date=upload_date_string,
                server_endpoint_url=server_endpoint_url,
            ))
        return exposure_keys_export_endpoints
