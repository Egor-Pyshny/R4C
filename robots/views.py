import os

from django.core.handlers.wsgi import WSGIRequest
from django.http import FileResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from robots.models import Robot
from utils.error_handlers import error_handler
from utils.excel_functions import create_report
from utils.validators import validate_robot_data


@csrf_exempt
@error_handler
@require_http_methods(["PUT"])
def add(request: WSGIRequest) -> JsonResponse:
    data = validate_robot_data(request)
    data["serial"] = data["model"] + "-" + data["version"]
    robot = Robot(
        serial=data["serial"],
        model=data["model"],
        version=data["version"],
        created=data["created"],
    )
    robot.save()
    return JsonResponse(data={}, status=201)


@error_handler
@require_http_methods(["GET"])
def report(request: WSGIRequest) -> FileResponse:
    create_report()
    return FileResponse(
        open(str(os.environ.get("PATH_FOR_ROBOT_REPORT")), "rb")
    )
