import time
import datetime
import json
import requests
import os

from pydoctordroid.protos.ingestion import schema_pb2 as schema__pb2
from pydoctordroid.utils.proto_utils import proto_to_json

class DroidEvents():

	def __init__(self):
		self.setup = False
		self.org_name = os.environ.get('ORG_NAME')
		self.hostname = os.environ.get('DRDROID_HOSTNAME')
		if self.org_name and self.hostname:
			self.setup = True
			self.PUBLISH_ENDPOINT = "{}/w/agent/push_events".format(self.hostname)
			self.headers = {'Content-Type': 'application/json', 'X-REQUEST-ORG': self.org_name}


	def assign_value(self, value_object, value_passed):
		value_passed_type = type(value_passed)

		if value_passed_type == int:
			value_object.int_value = value_passed

		elif value_passed_type == float:
			value_object.double_value = value_passed

		elif value_passed_type == bool:
			value_object.bool_value = value_passed

		elif value_passed_type == str:
			value_object.string_value = value_passed

		elif value_passed_type == bytes:
			value_object.bytes_value = value_passed

		else:
			value_object.string_value = str(value_passed)


	def publish(self, wf_name, wf_state, kv_pairs, event_time=None):

		if not self.setup:
			return

		payloadRequest = schema__pb2.WEPayloadIngestionRequest()
		wePayload = payloadRequest.data
		wEvent = wePayload.events.add()

		wEvent.state = wf_state

		workflow = wEvent.workflow
		workflow.name = wf_name

		if kv_pairs:
			for kv in kv_pairs:
				_kv = wEvent.kvs.add()
				_kv.key = kv[0]
				_v = _kv.value
				self.assign_value(_v, kv[1])

		timestamp = wEvent.timestamp

		# Take event_time passed, else use current time. Use current time in case of an exception
		try:
			if event_time:
				timestamp.seconds = int(event_time)
			else:
				timestamp.seconds = int(time.time())
		except:
			timestamp.seconds = int(time.time())

		self.send_http(payloadRequest)


	def send_http(self, proto_payload_request):
		payload_string = proto_to_json(proto_payload_request)
		# print(payload_string)
		resp = requests.post(self.PUBLISH_ENDPOINT, headers=self.headers, data=payload_string)
		print("Send HTTP Status Code: {}".format(resp.status_code))
		print("Send HTTP Body: {}".format(resp.text))

