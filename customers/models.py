# type: ignore
from django.db import models


class Customer(models.Model):
    email = models.EmailField(
        max_length=255, unique=True, blank=False, null=False, primary_key=True
    )
