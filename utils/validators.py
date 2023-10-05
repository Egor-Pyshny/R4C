import json
from datetime import datetime
from re import match
from typing import Dict
from typing import List

from django.core.handlers.wsgi import WSGIRequest

from utils.custom_exceptions.MailFormatException import MailFormatException
from utils.custom_exceptions.MultiException import MultiException
from utils.custom_exceptions.NotEnoughDataException import (
    NotEnoughDataException,
)
from utils.custom_exceptions.SerialFormatException import SerialFormatException
from utils.custom_exceptions.WrongLengthException import WrongLengthException


def validate_order_data(request: WSGIRequest) -> Dict[str, str]:
    data: Dict[str, str] = json.loads(request.body)
    exceptions: List[BaseException] = []
    if not (email := data.get("email")):
        exceptions.append(NotEnoughDataException("email"))
    elif "@" not in email:
        exceptions.append(MailFormatException())
    if not (serial := data.get("serial")):
        exceptions.append(NotEnoughDataException("serial"))
    elif not (match(r"^[A-Za-z0-9]{2}-[A-Za-z0-9]{2}$", serial)):
        exceptions.append(SerialFormatException())
    if len(exceptions) != 0:
        raise MultiException(exceptions)
    return data


def validate_robot_data(request: WSGIRequest) -> Dict[str, str]:
    data: Dict[str, str] = json.loads(request.body)
    exceptions: List[BaseException] = []
    if not (model := data.get("model")):
        exceptions.append(NotEnoughDataException("model"))
    elif len(model) != 2:
        exceptions.append(WrongLengthException("model", 2))
    if not (version := data.get("version")):
        exceptions.append(NotEnoughDataException("version"))
    elif len(version) != 2:
        exceptions.append(WrongLengthException("model", 2))
    if not (date := data.get("created")):
        exceptions.append(NotEnoughDataException("created"))
    else:
        try:
            datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        except ValueError as e:
            exceptions.append(e)
    if len(exceptions) != 0:
        raise MultiException(exceptions)
    return data
