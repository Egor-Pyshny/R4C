class SerialFormatException(Exception):
    def __init__(self) -> None:
        super().__init__("Serial format is incorrect")
