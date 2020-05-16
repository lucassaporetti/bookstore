import re
from datetime import datetime
from typing import Type

from src.core.tools import is_integer, is_float


def validate_string(string: str, pattern: str, min_len: int = 0, max_len: int = 30):
    str_len = len(string)
    return min_len <= str_len <= max_len and bool(re.match(pattern, string))


def validate_int(number: str, min_value: int = 0, max_value: int = 1000000):
    return is_integer(number) and min_value <= int(number) <= max_value


def validate_float(number: str, min_value: float = 0, max_value: float = 1000000):
    return is_float(number) and min_value <= float(number) <= max_value


def validate_enum(name: str, enum_type: Type):
    return name.upper() in enum_type.__dict__


def validate_date(date_text: str, fmt: str):
    try:
        datetime.strptime(date_text, fmt)
        return True
    except ValueError:
        return False
