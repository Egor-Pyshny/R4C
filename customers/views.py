from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from customers.models import Customer
from orders.models import Order
from utils.error_handlers import error_handler
from utils.validators import validate_order_data


@csrf_exempt
@error_handler
@require_http_methods(["POST"])
def make_order(request: WSGIRequest) -> JsonResponse:
    data = validate_order_data(request)
    customer = Customer(email=data["email"])
    customer.save()
    order = Order(
        customer=customer,
        serial=data["serial"],
    )
    if order.robot is not None:
        order.robot.sold = True
        response = {
            "message": "Your order is ready",
        }
        order.delete()
    else:
        order.save()
        response = {
            "message": "Unfortunately, we dont have such robot now, "
            "your order is already in the queue and when this "
            "robot will be in stock we will send you mail.",
        }
    return JsonResponse(data=response, status=200)
