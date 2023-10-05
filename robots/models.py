# type: ignore
from uuid import uuid4

from django.db import models


class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False)
    model = models.CharField(max_length=2, blank=False, null=False)
    version = models.CharField(max_length=2, blank=False, null=False)
    created = models.DateTimeField(blank=False, null=False)
    id = models.UUIDField(default=uuid4, primary_key=True, null=False)
    blocked = models.BooleanField(default=False, null=False)
    sold = models.BooleanField(default=False, null=False)

    @staticmethod
    def fetch_data():
        qs = Robot.objects.all()
        for robot in qs.iterator(chunk_size=10000):
            yield robot
