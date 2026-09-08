from enum import StrEnum


class BTTranslationRequestState(StrEnum):
    ACTIVE = "ACTIVE"
    DONE = "DONE"
    FAILED = "FAILED"

    def __str__(self) -> str:
        return str(self.value)
