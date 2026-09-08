from enum import StrEnum


class BTAppElementErrorCode(StrEnum):
    INCONSISTENT_CHANGES = "INCONSISTENT_CHANGES"
    NOT_FOUND = "NOT_FOUND"
    OK = "OK"
    TRANSACTION_CONFLICT = "TRANSACTION_CONFLICT"

    def __str__(self) -> str:
        return str(self.value)
