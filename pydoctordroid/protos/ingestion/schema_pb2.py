# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/ingestion/schema.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dprotos/ingestion/schema.proto\x12\x10protos.ingestion\x1a\x1fgoogle/protobuf/timestamp.proto\"\x82\x01\n\x05Value\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12\x14\n\nbool_value\x18\x02 \x01(\x08H\x00\x12\x13\n\tint_value\x18\x03 \x01(\x03H\x00\x12\x16\n\x0c\x64ouble_value\x18\x04 \x01(\x01H\x00\x12\x15\n\x0b\x62ytes_value\x18\x07 \x01(\x0cH\x00\x42\x07\n\x05value\"?\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.protos.ingestion.Value\"\x18\n\x08Workflow\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x9d\x01\n\x06WEvent\x12,\n\x08workflow\x18\x01 \x01(\x0b\x32\x1a.protos.ingestion.Workflow\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05state\x18\x03 \x01(\t\x12\'\n\x03kvs\x18\x04 \x03(\x0b\x32\x1a.protos.ingestion.KeyValue\"5\n\tWEPayload\x12(\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x18.protos.ingestion.WEvent\"F\n\x19WEPayloadIngestionRequest\x12)\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x1b.protos.ingestion.WEPayload\"+\n\x1aWEPayloadIngestionResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.ingestion.schema_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VALUE._serialized_start=85
  _VALUE._serialized_end=215
  _KEYVALUE._serialized_start=217
  _KEYVALUE._serialized_end=280
  _WORKFLOW._serialized_start=282
  _WORKFLOW._serialized_end=306
  _WEVENT._serialized_start=309
  _WEVENT._serialized_end=466
  _WEPAYLOAD._serialized_start=468
  _WEPAYLOAD._serialized_end=521
  _WEPAYLOADINGESTIONREQUEST._serialized_start=523
  _WEPAYLOADINGESTIONREQUEST._serialized_end=593
  _WEPAYLOADINGESTIONRESPONSE._serialized_start=595
  _WEPAYLOADINGESTIONRESPONSE._serialized_end=638
# @@protoc_insertion_point(module_scope)
