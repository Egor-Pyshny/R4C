from typing import List


class MultiException(Exception):
    def __init__(self, exceptions: List[BaseException]) -> None:
        self.exceptions = exceptions
