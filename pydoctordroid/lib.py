import os
from datetime import datetime

from pydoctordroid._event_exporter import HttpEventExporter
from pydoctordroid._events import create_event
from pydoctordroid._logger import setup_logger

_DRDROID_AUTH_TOKEN_ENV = 'DRDROID_AUTH_TOKEN'
_DRDROID_HOSTNAME_ENV = 'DRDROID_HOSTNAME'
_DRDROID_SERVICE_NAME_ENV = 'DRDROID_SERVICE_NAME'
_DRDROID_SERVICE_NAME_KEY = '$drd_service_name'
_DRDROID_DEBUG = 'DRDROID_DEBUG'

logger = setup_logger(debug=os.environ.get(_DRDROID_DEBUG, False))


class DrDroid:
    def __init__(
            self,
            token: str = '',
            endpoint: str = 'https://ingest.drdroid.io',
            debug: bool = False,
            logger=None
    ):
        self._setup = False
        self._token = os.environ.get(_DRDROID_AUTH_TOKEN_ENV, token)
        self._hostname = os.environ.get(_DRDROID_HOSTNAME_ENV, endpoint)
        self._service_name = os.environ.get(_DRDROID_SERVICE_NAME_ENV, "")
        if logger:
            self._logger = logger
        elif os.environ.get(_DRDROID_DEBUG, debug):
            self._logger = setup_logger('drdroid.sdk.instance', True)
        else:
            self._logger = setup_logger('drdroid.sdk.instance', False)

        self._event_exporter = HttpEventExporter(self._token, self._hostname, self._logger)
        if self._event_exporter:
            self._setup = True
        return

    def publish(self, name: str, payload: dict = None, event_time: datetime = None):
        if not self._setup:
            return
        try:
            if self._service_name is not None:
                payload[_DRDROID_SERVICE_NAME_KEY] = self._service_name
            event = create_event(name, payload, event_time)
            self._event_exporter.export(event)
        except Exception as e:
            self._logger.debug(msg=f'Error exporting event: {e}')
        return


class _Global:
    def __init__(self):
        self._instance = DrDroid(logger=logger)

    def setup(self, *args, **kwargs):
        self._instance = DrDroid(*args, *kwargs)

    def publish(self, *args, **kwargs):
        self._instance.publish(*args, **kwargs)


drdroid = _Global()


def setup(token: str, endpoint: str):
    drdroid.setup(token, endpoint)


def publish(name: str, payload: dict = None, event_time: datetime = None):
    drdroid.publish(name, payload, event_time)
