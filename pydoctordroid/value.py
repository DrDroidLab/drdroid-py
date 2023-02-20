import abc
from collections.abc import Iterable
from datetime import datetime, timezone
from typing import Dict

_VALID_TYPES = [bool, str, int, float, datetime, list, tuple, set, dict, Iterable]


class ValueFactory:
    @staticmethod
    def value(obj):
        if isinstance(obj, bool):
            return BoolValue(obj)
        elif isinstance(obj, str):
            return StringValue(obj)
        elif isinstance(obj, int):
            return LongValue(obj)
        elif isinstance(obj, float):
            return DoubleValue(obj)
        elif isinstance(obj, bytes):
            return BytesValue(obj)
        elif isinstance(obj, datetime):
            return DatetimeValue(obj)
        elif isinstance(obj, dict):
            return DictValue(obj)
        elif isinstance(obj, Iterable):
            return ArrayValue(obj)
        return ObjValue(obj)


class InvalidValueTypeError(ValueError):
    pass


class Value(abc.ABC):
    key = ''
    instance_type = None
    _value = None

    def value(self) -> Dict:
        return {
            self.key: self._value
        }


class PrimitiveValue(Value):
    def __init__(self, value):
        if self.instance_type and not isinstance(value, self.instance_type):
            raise InvalidValueTypeError(f'expected value of type {self.instance_type}')
        self._value = value


class KeyValue(Value):
    def __init__(self, key: str, value):
        self._value = value
        self._key = key

    def value(self) -> Dict:
        return {
            'key': self._key,
            'value': self._value
        }


class StringValue(PrimitiveValue):
    key = 'string_value'
    instance_type = str


class BoolValue(PrimitiveValue):
    key = 'bool_value'
    instance_type = bool


class LongValue(PrimitiveValue):
    key = 'int_value'
    instance_type = int


class DoubleValue(PrimitiveValue):
    key = 'double_value'
    instance_type = float


class BytesValue(PrimitiveValue):
    key = 'bytes_value'
    instance_type = bytes


class DatetimeValue(Value):
    key = 'string_value'
    fmt = '%Y-%m-%dT%H:%M:%S.%fZ'

    def __init__(self, value):
        if not isinstance(value, datetime):
            raise InvalidValueTypeError('expected value of type Dict')
        self._value = value.astimezone(timezone.utc).strftime(self.fmt)
        return


class ArrayValue(Value):
    key = 'array_value'

    def __init__(self, value):
        if not isinstance(value, Iterable):
            raise InvalidValueTypeError('expected value of type Iterable')
        self._value = [ValueFactory.value(elem) for elem in value]
        return

    def value(self) -> Dict:
        return {
            self.key: {
                'values': self._value
            }
        }


class DictValue(Value):
    key = 'kvlist_value'

    def __init__(self, value):
        if not isinstance(value, Dict):
            raise InvalidValueTypeError('expected value of type Dict')
        self._value = [KeyValue(key, ValueFactory.value(value)) for key, value in value.items() if
                       type(value) in _VALID_TYPES or isinstance(type, Iterable)]
        return

    def value(self) -> Dict:
        return {
            self.key: {
                'values': self._value
            }
        }


class ObjValue(Value):
    key = 'kvlist_value'

    def __init__(self, value):
        self._value = [KeyValue(key, ValueFactory.value(value)) for key, value in value.__dict__.items() if
                       type(value) in _VALID_TYPES or isinstance(type, Iterable)]
        return

    def value(self) -> Dict:
        return {
            self.key: {
                'values': self._value
            }
        }


def process_payload(payload: Dict):
    return [KeyValue(key, ValueFactory.value(value)) for key, value in payload.items() if isinstance(key, str)]
