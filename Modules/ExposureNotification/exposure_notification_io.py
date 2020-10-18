import logging
from typing import *

import pandas as pd

from .Backends.corona_warn_app import CoronaWarnAppBackendKeysDownloader
from .Backends.dp3t import DP3TBackendKeysDownloader
from .Backends.immuni import ImmuniBackendKeysDownloader

_backend_keys_downloaders = [
    DP3TBackendKeysDownloader(
        backend_identifier="ES",
        server_endpoint_url="https://radarcovid.covid19.gob.es/dp3t"),
    DP3TBackendKeysDownloader(
        backend_identifier="ES@PRE",
        server_endpoint_url="https://radarcovidpre.covid19.gob.es/dp3t"),
    DP3TBackendKeysDownloader(
        backend_identifier="CH",
        server_endpoint_url="https://www.pt.bfs.admin.ch"),
    DP3TBackendKeysDownloader(
        backend_identifier="PT",
        server_endpoint_url="https://stayaway.incm.pt"),
    DP3TBackendKeysDownloader(
        backend_identifier="EE",
        server_endpoint_url="https://enapi.sm.ee/authorization"),
    DP3TBackendKeysDownloader(
        backend_identifier="MT",
        server_endpoint_url="https://mt-dpppt-ws.azurewebsites.net"),
    CoronaWarnAppBackendKeysDownloader(
        backend_identifier="DE",
        server_endpoint_url="https://svc90.main.px.t-online.de",
        target_country="DE"),
    CoronaWarnAppBackendKeysDownloader(
        backend_identifier="DE-IE",
        server_endpoint_url="https://svc90.main.px.t-online.de",
        target_country="IE"),
    CoronaWarnAppBackendKeysDownloader(
        backend_identifier="DE-ES",
        server_endpoint_url="https://svc90.main.px.t-online.de",
        target_country="ES"),
    CoronaWarnAppBackendKeysDownloader(
        backend_identifier="BE",
        server_endpoint_url="https://c19distcdn-prd.ixor.be",
        target_country="BE",
        use_proxy_if_available=True),
    ImmuniBackendKeysDownloader(
        backend_identifier="IT",
        server_endpoint_url="https://get.immuni.gov.it",
        use_proxy_if_available=True),
    ImmuniBackendKeysDownloader(
        backend_identifier="IT-ES",
        server_endpoint_url="https://get.immuni.gov.it",
        eu_country="ES",
        use_proxy_if_available=True),
    ImmuniBackendKeysDownloader(
        backend_identifier="IT-IE",
        server_endpoint_url="https://get.immuni.gov.it",
        eu_country="IE",
        use_proxy_if_available=True),
]
_default_backend_identifiers = \
    ["ES", "ES@PRE", "CH", "PT", "EE", "MT", "BE", "DE-IE", "DE-ES", "IT", "IT-ES", "IT-IE"]


def download_exposure_keys_from_backends(
        *, backend_identifiers=None, fail_on_error_backend_identifiers=None, **kwargs) -> List[dict]:
    if backend_identifiers is None:
        backend_identifiers = _default_backend_identifiers

    exposure_keys_df = pd.DataFrame()
    for downloader in _backend_keys_downloaders:
        if backend_identifiers and downloader.backend_identifier not in backend_identifiers:
            continue

        try:
            backend_exposure_keys_df = downloader.download_exposure_keys_with_parameters(**kwargs)
            exposure_keys_df = exposure_keys_df.append(backend_exposure_keys_df)
        except Exception as e:
            if fail_on_error_backend_identifiers and \
                    downloader.backend_identifier in fail_on_error_backend_identifiers:
                raise e
            logging.warning(
                f"Error downloading exposure keys from "
                f"backend '{downloader.backend_identifier}': {repr(e)}", exc_info=True)
    return exposure_keys_df
