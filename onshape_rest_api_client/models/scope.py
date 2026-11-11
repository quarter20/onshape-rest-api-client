from enum import StrEnum


class Scope(StrEnum):
    USER = "USER"

    def __str__(self) -> str:
        return str(self.value)
