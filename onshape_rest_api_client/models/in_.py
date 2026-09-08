from enum import StrEnum


class In(StrEnum):
    COOKIE = "COOKIE"
    HEADER = "HEADER"
    QUERY = "QUERY"

    def __str__(self) -> str:
        return str(self.value)
