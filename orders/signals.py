import os
from datetime import datetime
from datetime import timedelta
from typing import Any
from typing import Dict

from django.core.mail import send_mail
from django.db.models import QuerySet
from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.models import Order
from robots.models import Robot


@receiver(post_save, sender=Robot)
def create_profile(
    sender: Any, instance: Robot, created: Any, **kwargs: Dict[str, Any]
) -> None:
    serial = instance.serial
    orders: QuerySet = Order.objects.filter(serial=serial).reverse()
    if orders.exists():
        order: Order = orders[0]
        instance.blocked = True
        order.waiting_answer = True
        now = datetime.now()
        now = now.replace(minute=0, second=0, microsecond=0)
        order.waiting_until = now + timedelta(days=1)
        model, version = order.serial.split("-")
        send_mail(
            "Your robot is available now",
            "Good afternoon!\n"
            f"Not long ago you expressed interest in our robot model {model}, version {version}.\n"
            f"This robot is available now and reserved for you until {order.waiting_until}.\n"
            "If this option suits you, please contact us.",
            os.environ.get("EMAIL_HOST_USER"),
            [order.customer.email],
            fail_silently=True,
        )
