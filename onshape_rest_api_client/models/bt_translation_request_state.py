from enum import Enum


class BTTranslationRequestState(str, Enum):
    ACTIVE = "ACTIVE"
    DONE = "DONE"
    FAILED = "FAILED"

    def __str__(self) -> str:
        return str(self.value)
