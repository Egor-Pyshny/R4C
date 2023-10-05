import json
from datetime import datetime
from typing import Dict
from typing import List

from django.core.handlers.wsgi import WSGIRequest

from utils.custom_exceptions.MultiException import MultiException
from utils.custom_exceptions.NotEnoughDataException import (
    NotEnoughDataException,
)
from utils.custom_exceptions.WrongLengthException import WrongLengthException


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
