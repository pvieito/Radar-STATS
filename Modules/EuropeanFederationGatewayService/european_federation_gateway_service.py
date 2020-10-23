from typing import *

from Modules.ExposureNotification import exposure_notification_io

_efgs_supported_countries_backend_identifier = "DE"


def get_supported_countries() -> List[str]:
    efgs_backend_client = exposure_notification_io.get_backend_client_with_identifier(
        backend_identifier=_efgs_supported_countries_backend_identifier)
    efgs_app_config = efgs_backend_client.download_app_config()
    return efgs_app_config.supportedCountries
