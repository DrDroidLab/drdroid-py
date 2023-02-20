import json
from datetime import datetime, timezone
from typing import Any, Dict, List

from pydoctordroid.value import process_payload, Value

EventType = Dict


def event(workflow: str, state: str, payload: dict, event_time: datetime = None) -> EventType:
    return {
        'workflow': {'name': workflow},
        'state': state,
        'timestamp': (event_time or datetime.now(timezone.utc)),
        'kvs': process_payload(payload)
    }


# Missing array type checks
_valid_type = [bool, int, str, float, list, tuple, set, datetime, dict]


class EventSerializer(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, datetime):
            fmt = '%Y-%m-%dT%H:%M:%S.%fZ'
            return o.astimezone(timezone.utc).strftime(fmt)
        elif isinstance(o, set):
            return list(o)
        elif isinstance(o, Value):
            return o.value()

        return super().default(o)


def serialize_events(events: List[EventType]):
    event_data = {'data': {'events': events}}
    return json.dumps(event_data, separators=(',', ':'), cls=EventSerializer)
