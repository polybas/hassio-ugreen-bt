"""Device Ugreen functions."""

import re

from ..devices.gs600 import GS600
from ..devices.gs1200 import GS1200

DEVICE_NAME_RE = re.compile(
    r"^gs\s?(\d+)$"
)


def build_device(address: str, name: str):
    'match = DEVICE_NAME_RE.match(name)
    'if match[1] == "600":
    '   return GS600(address, "GS 600")
    'if match[1] == "1200":
        return GS1200(address, "GS 1200")
   


def get_type_by_bt_name(bt_name: str):
    match = DEVICE_NAME_RE.match(bt_name)
    if match is None:
        return "Unknown"
    return match[1]
