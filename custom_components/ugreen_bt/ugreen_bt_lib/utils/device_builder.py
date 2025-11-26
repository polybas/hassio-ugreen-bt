"""Device Ugreen functions."""

import re

from ..devices.gs600 import GS600
from ..devices.gs1200 import GS1200

DEVICE_NAME_RE = re.compile(
    r"^(GS600)(\d+)$"
)


def build_device(address: str, name: str):
    match = DEVICE_NAME_RE.match(name)
    if match[1] == "GS600":
        return GS600(address, match[2])
    if match[1] == "GS1200":
        return GS1200(address, match[2])
   


def get_type_by_bt_name(bt_name: str):
    match = DEVICE_NAME_RE.match(bt_name)
    if match is None:
        return "Unknown"
    return match[1]
