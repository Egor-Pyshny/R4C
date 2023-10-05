from typing import Any
from typing import Dict

from django.db.models import QuerySet
from django.db.models.signals import post_init
from django.dispatch import receiver

from orders.models import Order
from robots.models import Robot


@receiver(post_init, sender=Order)
def find_robot(sender: Any, instance: Order, **kwargs: Dict[str, Any]) -> None:
    serial = instance.serial
    robots: QuerySet = Robot.objects.filter(
        serial=serial, sold=False, blocked=False
    )
    if robots.exists():
        instance.robot = robots[0]
