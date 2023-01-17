from typing import Dict

from google.protobuf.json_format import MessageToJson, Parse, MessageToDict, ParseDict
from google.protobuf.message import Message
from google.protobuf.struct_pb2 import Value


class ProtoException(ValueError):
    pass


def proto_to_json(obj: Message, use_snake_case: bool = True) -> str:
    if not obj:
        raise ProtoException('Trying to serialize None obj')
    try:
        text = MessageToJson(obj, preserving_proto_field_name=use_snake_case)
    except Exception as e:
        raise ProtoException(f'Error serializing proto message: {e}')
    return text


def proto_to_dict(obj: Message, use_snake_case: bool = True) -> str:
    if not obj:
        raise ProtoException('Trying to serialize None obj')
    try:
        message_dict = MessageToDict(obj, preserving_proto_field_name=use_snake_case)
    except Exception as e:
        raise ProtoException(f'Error converting proto message to dict: {e}')
    return message_dict


def json_to_proto(text: str, proto_clazz, ignore_unknown_fields=True) -> Message:
    if proto_clazz:
        msg = proto_clazz()
    else:
        raise ProtoException('No message class defined')

    try:
        msg = Parse(text, msg, ignore_unknown_fields)
    except Exception as e:
        raise ProtoException(f'Error while parsing text: {e}')
    return msg


def dict_to_proto(d: Dict, proto_clazz, ignore_unknown_fields=True) -> Message:
    if proto_clazz:
        msg = proto_clazz()
    else:
        raise ProtoException('No message class defined')

    try:
        msg = ParseDict(d, msg, ignore_unknown_fields)
    except Exception as e:
        raise ProtoException(f'Error while parsing text: {e}')
    return msg


def get_value(v: Value):
    which_one_of = v.WhichOneof('kind')
    if which_one_of in ('string_value', 'number_value', 'bool_value'):
        return getattr(v, v.WhichOneof('kind'))
    elif which_one_of == 'list_value':
        return [get_value(value) for value in getattr(v, v.WhichOneof('kind')).values]
    return None