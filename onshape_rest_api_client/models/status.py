from enum import StrEnum


class Status(StrEnum):
    DB_MAX_NUMBER_ITEMS_EXCEEDED = "DB_MAX_NUMBER_ITEMS_EXCEEDED"
    DB_TIMEOUT = "DB_TIMEOUT"

    def __str__(self) -> str:
        return str(self.value)
