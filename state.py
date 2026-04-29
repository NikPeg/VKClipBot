import json
import os
from datetime import datetime

_STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state.json")
_FMT = "%Y-%m-%d %H:%M:%S"


def get_last_time_post(default: datetime) -> datetime:
    try:
        with open(_STATE_FILE) as f:
            return datetime.strptime(json.load(f)["last_time_post"], _FMT)
    except (FileNotFoundError, KeyError, ValueError):
        return default


def set_last_time_post(dt: datetime) -> None:
    try:
        with open(_STATE_FILE) as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    data["last_time_post"] = dt.strftime(_FMT)
    with open(_STATE_FILE, "w") as f:
        json.dump(data, f, indent=2)
