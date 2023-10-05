from django.apps import AppConfig


class RobotsConfig(AppConfig):
    name = "robots"

    def ready(self) -> None:
        from . import signals  # noqa:F401
