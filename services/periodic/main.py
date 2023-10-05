from celery import Celery
from celery.schedules import crontab

app = Celery(
    "periodic.r4cs",
    broker="redis://broker:6379/",
)
app.set_default()


@app.task
def check_orders() -> None:
    import os
    from datetime import datetime

    from orders.models import Order
    from utils.mailer import send_mail

    now = datetime.now().replace(minute=0, second=0, microsecond=0)
    for order in Order.fetch_data():
        waiting_until: datetime | None = order.waiting_until
        if (waiting_until is not None) and (now > waiting_until):
            order.waiting_answer = False
            order.waiting_until = None
            order.robot.blocked = False
            send_mail(
                "Timeout expired.",
                "Unfortunately, the booking period for your robot has expired.\n"
                "If you are still interested in our product, please place a new order on our website.",
                os.environ.get("EMAIL_HOST_USER"),
                [order.customer.email],
                fail_silently=False,
            )


@app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **_kwargs: dict) -> None:
    sender.add_periodic_task(
        crontab(hour="*/1", minute="0"),
        check_orders,
    )
