import datetime
import os

import requests

from pydoctordroid.events import event, serialize_events


class DroidEvents:
    def __init__(self):
        self.setup = False
        self.org_name = os.environ.get('ORG_NAME')
        self.hostname = os.environ.get('DRDROID_HOSTNAME')
        if self.org_name and self.hostname:
            self.setup = True
            self.PUBLISH_ENDPOINT = "{}/w/agent/push_events".format(self.hostname)
            self.headers = {'Content-Type': 'application/json', 'X-REQUEST-ORG': self.org_name}

    def publish(self, wf_name: str, wf_state: str, payload: dict, event_time: datetime = None):
        if not self.setup:
            return

        e = event(wf_name, wf_state, payload, event_time)

        try:
            self.send_http(e)
        except:
            pass

    def send_http(self, proto_payload_request):
        payload_string = serialize_events([proto_payload_request])
        # print(payload_string)
        resp = requests.post(self.PUBLISH_ENDPOINT, headers=self.headers, data=payload_string)
        # print("Send HTTP Status Code: {}".format(resp.status_code))
        # print("Send HTTP Body: {}".format(resp.text))
