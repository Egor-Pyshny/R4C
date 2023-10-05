from json import JSONDecodeError
from typing import Any
from typing import Callable
from typing import Dict
from typing import Tuple

from django.http import FileResponse
from django.http import JsonResponse

from utils.custom_exceptions.MultiException import MultiException


def error_handler(func: Callable) -> Callable:
    def wrapper(
        *args: Tuple[Any, ...], **kwargs: Dict[str, Any]
    ) -> JsonResponse | FileResponse | None:
        try:
            result: JsonResponse | FileResponse | None = func(*args, **kwargs)
            return result
        except MultiException as e:
            response = {}
            for i, exception in enumerate(e.exceptions):
                response[f"exception_{i}"] = exception.args[0]
            return JsonResponse(data=response, status=400)
        except JSONDecodeError:
            response = {"exception": "It's not JSON format"}
            return JsonResponse(data=response, status=400)
        except Exception as e:
            response = {
                "exception_type": str(type(e)),
                "exception": str(e.args),
            }
            return JsonResponse(data=response, status=500)

    return wrapper
