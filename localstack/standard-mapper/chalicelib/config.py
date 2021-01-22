import logging
import os

from chalicelib import APP_NAME, APP_VERSION

_CONFIG = None


class Configuration:
    # APP
    APP_ENV = 'development'
    APP_NAME = ''
    APP_VERSION = ''

    # LOG
    LOG_LEVEL = logging.INFO

    # NEW RELIC
    NEW_RELIC_DEVELOPER_MODE = 'development'
    NEW_RELIC_LICENSE_KEY = "license_key"
    NEW_RELIC_LOG_HOST = "https://log-api.newrelic.com/log/v1"

    def __init__(self):
        # APP
        self.APP_ENV = os.getenv("APP_ENV") if 'APP_ENV' in os.environ else 'development'
        self.APP_NAME = APP_NAME
        self.APP_VERSION = APP_VERSION
        self.LOG_LEVEL = os.getenv("LOG_LEVEL") if 'LOG_LEVEL' in os.environ else self.LOG_LEVEL



def get_config():
    global _CONFIG
    if not _CONFIG:
        config = Configuration()
    else:
        config = _CONFIG
    return config