from enum import StrEnum


class BTAppModificationRequestState(StrEnum):
    ACTIVE = "ACTIVE"
    DONE = "DONE"
    FAILED = "FAILED"

    def __str__(self) -> str:
        return str(self.value)
