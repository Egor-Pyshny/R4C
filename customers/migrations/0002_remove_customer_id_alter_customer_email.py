# Generated by Django 4.2.5 on 2023-10-05 18:19

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("customers", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="id",
        ),
        migrations.AlterField(
            model_name="customer",
            name="email",
            field=models.EmailField(
                max_length=255, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
