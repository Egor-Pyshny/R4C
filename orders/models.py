# type: ignore
from uuid import uuid4

from django.db import models

from customers.models import Customer
from robots.models import Robot


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, null=False, on_delete=models.CASCADE
    )
    serial = models.CharField(max_length=5, null=True)
    robot = models.ForeignKey(Robot, null=True, on_delete=models.PROTECT)
    waiting_answer = models.BooleanField(null=True)
    waiting_until = models.DateTimeField(null=True)
    id = models.UUIDField(default=uuid4, primary_key=True)

    @staticmethod
    def fetch_data():
        qs = Order.objects.all()
        for order in qs.iterator(chunk_size=1000):
            yield order
