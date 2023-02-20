import abc
from abc import abstractmethod

import urllib3

from pydoctordroid._events import serialize_events


class EventExporter(abc.ABC):
    @abstractmethod
    def export(self, event):
        pass


class HttpEventExporter(EventExporter):
    def __init__(self, token, hostname, logger):
        self._pool = urllib3.PoolManager(
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {token}'
            },
            timeout=urllib3.Timeout(connect=1.0, read=2.0)
        )

        self._endpoint = f"{hostname}/w/agent/push_events"
        self._logger = logger

        return

    def export(self, event):
        payload = serialize_events([event])
        try:
            response = self._pool.request(
                "POST",
                self._endpoint,
                body=payload,
            )
            if response.status == 200:
                self._logger.debug(msg='Event exported successfully')
            elif response.status == 401:
                self._logger.debug(msg='Error exporting event: Request Unauthorized. Validate auth token.')

            response.close()
        except Exception as e:
            self._logger.debug(msg=f'{e}')
