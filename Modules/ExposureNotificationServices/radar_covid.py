from typing import *

from Modules.ExposureNotificationServices.dp3t import DP3TServiceKeysDownloader

_radar_covid_dp3t_server_endpoint_url = "https://radarcovid.covid19.gob.es/dp3t"


class RadarCOVIDServiceKeysDownloader(DP3TServiceKeysDownloader):
    def generate_exposure_keys_export_endpoints_with_parameters(self, **kwargs) -> List[dict]:
        return super(RadarCOVIDServiceKeysDownloader, self) \
            .generate_exposure_keys_export_endpoints_with_parameters(
            server_endpoint_url=_radar_covid_dp3t_server_endpoint_url, **kwargs)
