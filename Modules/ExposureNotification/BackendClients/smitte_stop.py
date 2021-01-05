import logging
from typing import *

from .base import BaseBackendClient

_smitte_stop_server_diagnositic_keys_endpoint_path = "/v1/diagnostickeys/"
_smitte_stop_server_authorization_mobile_header_name = "Authorization_Mobile"
_smitte_stop_server_authorization_mobile_header_value = "68iXQyxZOy"
_smitte_stop_server_authorization_headers = {
    _smitte_stop_server_authorization_mobile_header_name:
        _smitte_stop_server_authorization_mobile_header_value
}


class SmitteStopBackendClient(BaseBackendClient):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def generate_exposure_keys_export_endpoints_with_parameters(self, **kwargs) -> List[dict]:
        server_keys_endpoint_url = \
            self.server_endpoint_url + _smitte_stop_server_diagnositic_keys_endpoint_path

        upload_dates = self.get_generation_dates_from_parameters(**kwargs)
        exposure_keys_export_endpoints = []
        for upload_datetime in upload_dates:
            upload_date_string = upload_datetime.strftime("%Y-%m-%d")
            current_chunk = 0
            while current_chunk is not None:
                try:
                    endpoint_url = server_keys_endpoint_url + f"{upload_date_string}:{current_chunk}.zip"
                    response = self.send_get_request(url=endpoint_url)
                    response.raise_for_status()
                    exposure_keys_export_endpoints.append(dict(
                        endpoint=endpoint_url,
                        upload_date=upload_date_string,
                        chunk=current_chunk,
                        endpoint_identifier_components=[
                            upload_date_string,
                            current_chunk
                        ],
                    ))
                    if response.headers.get("FinalForTheDay"):
                        current_chunk = None
                    else:
                        current_chunk += 1
                except Exception as e:
                    logging.warning(
                        f"Error loading keys for date '{upload_date_string}' "
                        f"and chunk {current_chunk}: {repr(e)}")
                    current_chunk = None

        return exposure_keys_export_endpoints

    @staticmethod
    def send_get_request(url, **kwargs):
        kwargs = kwargs.copy()
        kwargs.update(headers=_smitte_stop_server_authorization_headers)
        return super(SmitteStopBackendClient, SmitteStopBackendClient) \
            .send_get_request(url=url, **kwargs)
