from enum import Enum


class In(str, Enum):
    COOKIE = "COOKIE"
    HEADER = "HEADER"
    QUERY = "QUERY"

    def __str__(self) -> str:
        return str(self.value)
