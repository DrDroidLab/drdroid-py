import json
from datetime import datetime, timezone
from typing import Any, Dict, List

EventType = Dict


def event(workflow: str, state: str, payload: dict, event_time: datetime = None) -> EventType:
    return {
        'workflow': {'name': workflow},
        'state': state,
        'timestamp': event_time or datetime.now(timezone.utc),
        'payload': {key: value for key, value in payload.items() if isinstance(key, str)}
    }


_valid_type = [bool, int, str, float, list, tuple, set, datetime, dict]


class EventSerializer(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, datetime):
            print("WOW")
            fmt = '%Y-%m-%dT%H:%M:%S.%fZ'
            return o.strftime(fmt)
        elif isinstance(o, set):
            return list(o)
        else:
            return {key: value for key, value in o.__dict__.items() if type(value) in _valid_type}

        return super().default(o)


def serialize_events(events: List[EventType]):
    event_data = {'data': {'events': events}}
    return json.dumps(event_data, separators=(',', ':'), cls=EventSerializer)
