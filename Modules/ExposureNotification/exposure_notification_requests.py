import os

import requests


def get(url, **kwargs):
    kwargs = kwargs.copy()
    if os.environ["EXPOSURE_NOTIFICATION_REQUESTS__USE_TOR_PROXY"]:
        kwargs.update(dict(proxies={
            "http": "socks5://127.0.0.1:9050",
            "https": "socks5://127.0.0.1:9050",
        }))
    return requests.get(url, **kwargs)
