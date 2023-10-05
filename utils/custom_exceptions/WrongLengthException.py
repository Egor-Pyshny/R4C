class WrongLengthException(Exception):
    def __init__(self, param: str, expected_length: int) -> None:
        super().__init__(
            f"Length of <{param}> is {len(param)} but should be {expected_length}"
        )
