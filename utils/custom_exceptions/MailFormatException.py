class MailFormatException(Exception):
    def __init__(self) -> None:
        super().__init__("Email format is incorrect")
