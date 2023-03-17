import json
from datetime import datetime, timezone
from typing import Any, Dict, List

from pydoctordroid._value import process_payload, Value

EventType = Dict


def create_event(name: str, payload: dict, event_time: datetime = None) -> EventType:
    return {
        'name': name,
        'timestamp': (event_time or datetime.now(timezone.utc)),
        'kvs': process_payload(payload or {})
    }


class EventEncoder(json.JSONEncoder):
    fmt = '%Y-%m-%dT%H:%M:%S.%fZ'

    def default(self, o: Any) -> Any:
        if isinstance(o, Value):
            return o.value()
        elif isinstance(o, datetime):
            return o.astimezone(timezone.utc).strftime(self.fmt)
        elif isinstance(o, set):
            return list(o)

        return super().default(o)


def serialize_events(events: List[EventType]):
    event_data = {'data': {'events': events}}
    return json.dumps(event_data, separators=(',', ':'), cls=EventEncoder)
