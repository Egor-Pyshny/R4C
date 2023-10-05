class NotEnoughDataException(Exception):
    def __init__(self, param: str) -> None:
        super().__init__(f"Parameter <{param}> is not filled in")
