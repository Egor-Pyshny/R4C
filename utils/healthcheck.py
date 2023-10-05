from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse


def healthcheck(request: WSGIRequest) -> JsonResponse | None:
    return JsonResponse("Server is healthy", safe=False)
