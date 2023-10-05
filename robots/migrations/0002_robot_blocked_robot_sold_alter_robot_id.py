# Generated by Django 4.2.5 on 2023-10-05 18:19

import uuid

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("robots", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="robot",
            name="blocked",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="robot",
            name="sold",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="robot",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False
            ),
        ),
    ]
