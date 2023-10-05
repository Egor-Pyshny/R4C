import os
from email.errors import MessageError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from smtplib import SMTPException
from typing import Any
from typing import List


def send_mail(
    subject: Any,
    message: Any,
    from_mail: Any,
    recipient_list: List[str],
    fail_silently: bool = False,
) -> None:
    try:
        msg = MIMEMultipart()
        msg["From"] = from_mail
        msg["To"] = ", ".join(recipient_list)
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))
        smtp = SMTP(str(os.environ.get("EMAIL_HOST")), int((os.environ.get("EMAIL_PORT"))))  # type: ignore
        smtp.starttls()
        smtp.login(
            str(os.environ.get("EMAIL_HOST_USER")),
            str(os.environ.get("EMAIL_HOST_PASSWORD")),
        )
        smtp.sendmail(from_mail, recipient_list, msg.as_string())
        smtp.quit()
    except (SMTPException, MessageError) as e:
        try:
            smtp.quit()
        except (AttributeError, NameError):
            pass
        if not fail_silently:
            raise e
