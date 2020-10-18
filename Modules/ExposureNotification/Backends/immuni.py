from typing import *

import requests

from .base import BaseBackendKeysDownloader

_immuni_server_keys_endpoint_path = "/v1/keys/"
_immuni_server_keys_eu_country_endpoint_path = "/v1/keys/eu/{eu_country}/"


class ImmuniBackendKeysDownloader(BaseBackendKeysDownloader):
    def __init__(
            self, backend_identifier: str, server_endpoint_url: str, eu_country: str = None):
        super().__init__(backend_identifier=backend_identifier)
        self.server_endpoint_url = server_endpoint_url
        self.eu_country = eu_country

    def generate_exposure_keys_export_endpoints_with_parameters(self, **kwargs) -> List[dict]:
        if self.eu_country:
            server_keys_endpoint_path = \
                _immuni_server_keys_eu_country_endpoint_path.format(eu_country=self.eu_country)
            endpoint_identifier_eu_country = self.eu_country
        else:
            server_keys_endpoint_path = _immuni_server_keys_endpoint_path
            endpoint_identifier_eu_country = "BASE"
        server_keys_endpoint_url = self.server_endpoint_url + server_keys_endpoint_path
        server_keys_index_endpoint_url = server_keys_endpoint_url + "index"

        response = requests.get(server_keys_index_endpoint_url)
        response.raise_for_status()
        response_result = response.json()
        oldest_batch_id = response_result["oldest"]
        newest_batch_id = response_result["newest"]

        exposure_keys_export_endpoints = []
        for batch_id in range(oldest_batch_id, newest_batch_id + 1):
            exposure_keys_export_endpoint = server_keys_endpoint_url + str(batch_id)
            exposure_keys_export_endpoints.append(dict(
                endpoint=exposure_keys_export_endpoint,
                server_endpoint_url=self.server_endpoint_url,
                eu_country=self.eu_country,
                batch_id=batch_id,
                endpoint_identifier_components=[
                    endpoint_identifier_eu_country,
                    batch_id
                ],
            ))
        return exposure_keys_export_endpoints
