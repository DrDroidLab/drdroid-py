from collections.abc import Iterable
from datetime import datetime
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


class Value:
    key = ''
    typecheck = None
    _value = None

    def __init__(self, value):
        if self.typecheck and not isinstance(value, self.typecheck):
            raise InvalidValueTypeError(f'expected value of type {self.typecheck}')
        self._value = self.process(value)

    @classmethod
    def process(cls, value):
        return value

    def value(self) -> Dict:
        return {
            self.key: self._value
        }


class StringValue(Value):
    key = 'string_value'
    typecheck = str


class BoolValue(Value):
    key = 'bool_value'
    typecheck = bool


class LongValue(Value):
    key = 'int_value'
    typecheck = int


class DoubleValue(Value):
    key = 'double_value'
    typecheck = float


class BytesValue(Value):
    key = 'bytes_value'
    typecheck = bytes


class KeyValue(Value):
    typecheck = Value

    def __init__(self, key: str, value: Value):
        super().__init__(value)
        self._key = key

    def value(self) -> Dict:
        return {
            'key': self._key,
            'value': self._value
        }


class DatetimeValue(StringValue):
    typecheck = datetime


class ArrayValue(Value):
    key = 'array_value'
    typecheck = Iterable

    @classmethod
    def process(cls, value):
        return [ValueFactory.value(elem) for elem in value]

    def value(self) -> Dict:
        return {
            self.key: {
                'values': self._value
            }
        }


class KVListValue(Value):
    key = 'kvlist_value'

    def value(self) -> Dict:
        return {
            self.key: {
                'values': self._value
            }
        }


class DictValue(KVListValue):
    typecheck = dict

    @classmethod
    def process(cls, value):
        return [KeyValue(key, ValueFactory.value(value)) for key, value in value.items() if
                type(value) in _VALID_TYPES or isinstance(type, Iterable)]


class ObjValue(KVListValue):
    typecheck = None

    @classmethod
    def process(cls, value):
        return [KeyValue(key, ValueFactory.value(value)) for key, value in value.__dict__.items() if
                type(value) in _VALID_TYPES or isinstance(type, Iterable)]


def process_payload(payload: Dict):
    return [KeyValue(key, ValueFactory.value(value)) for key, value in payload.items() if isinstance(key, str)]
