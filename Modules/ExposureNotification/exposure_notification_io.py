import logging
from typing import *

import pandas as pd

from .Backends.corona_warn_app import CoronaWarnAppBackendClient
from .Backends.dp3t import DP3TBackendClient
from .Backends.immuni import ImmuniBackendClient

_backend_clients = [
    DP3TBackendClient(
        backend_identifier="ES",
        server_endpoint_url="https://radarcovid.covid19.gob.es/dp3t"),
    DP3TBackendClient(
        backend_identifier="ES@PRE",
        server_endpoint_url="https://radarcovidpre.covid19.gob.es/dp3t"),
    DP3TBackendClient(
        backend_identifier="CH",
        server_endpoint_url="https://www.pt.bfs.admin.ch"),
    DP3TBackendClient(
        backend_identifier="PT",
        server_endpoint_url="https://stayaway.incm.pt"),
    DP3TBackendClient(
        backend_identifier="EE",
        server_endpoint_url="https://enapi.sm.ee/authorization"),
    DP3TBackendClient(
        backend_identifier="MT",
        server_endpoint_url="https://mt-dpppt-ws.azurewebsites.net"),
    CoronaWarnAppBackendClient(
        backend_identifier="DE",
        server_endpoint_url="https://svc90.main.px.t-online.de",
        target_country="DE"),
    CoronaWarnAppBackendClient(
        backend_identifier="DE-ES",
        server_endpoint_url="https://svc90.main.px.t-online.de",
        target_country="ES"),
    CoronaWarnAppBackendClient(
        backend_identifier="DE-IE",
        server_endpoint_url="https://svc90.main.px.t-online.de",
        target_country="IE"),
    CoronaWarnAppBackendClient(
        backend_identifier="DE-IT",
        server_endpoint_url="https://svc90.main.px.t-online.de",
        target_country="IT"),
    CoronaWarnAppBackendClient(
        backend_identifier="BE",
        server_endpoint_url="https://c19distcdn-prd.ixor.be",
        target_country="BE"),
    CoronaWarnAppBackendClient(
        backend_identifier="BE@TST",
        server_endpoint_url="https://c19distcdn-tst.ixor.be",
        target_country="BE"),
    ImmuniBackendClient(
        backend_identifier="IT",
        server_endpoint_url="https://get.immuni.gov.it"),
    ImmuniBackendClient(
        backend_identifier="IT-IT",
        server_endpoint_url="https://get.immuni.gov.it",
        eu_country="IT"),
    ImmuniBackendClient(
        backend_identifier="IT-ES",
        server_endpoint_url="https://get.immuni.gov.it",
        eu_country="ES"),
    ImmuniBackendClient(
        backend_identifier="IT-IE",
        server_endpoint_url="https://get.immuni.gov.it",
        eu_country="IE"),
    ImmuniBackendClient(
        backend_identifier="IT-DE",
        server_endpoint_url="https://get.immuni.gov.it",
        eu_country="DE"),
]
_default_backend_identifiers = [
    "ES", "ES@PRE", "CH", "PT", "EE", "MT",  # DP3T
    "DE", "DE-ES", "DE-IE", "DE-IT", "BE", "BE@TST",  # Corona-Warn-App
    "IT", "IT-IT", "IT-ES", "IT-IE", "IT-DE",  # Immuni
]


def get_backend_client_with_identifier(*, backend_identifier: str):
    for backend_client in _backend_clients:
        if backend_identifier == backend_client.backend_identifier:
            return backend_client
    raise ValueError(f"Backend client with identifier '{backend_identifier}' not available.")


def download_exposure_keys_from_backends(
        *, backend_identifiers=None, fail_on_error_backend_identifiers=None, **kwargs) -> List[dict]:
    if backend_identifiers is None:
        backend_identifiers = _default_backend_identifiers

    exposure_keys_df = pd.DataFrame()
    for backend_identifier in backend_identifiers:
        backend_client = get_backend_client_with_identifier(backend_identifier=backend_identifier)

        try:
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
