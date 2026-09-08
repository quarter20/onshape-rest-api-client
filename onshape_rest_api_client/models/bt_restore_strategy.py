from enum import StrEnum


class BTRestoreStrategy(StrEnum):
    KEEP = "KEEP"
    REPLACE = "REPLACE"

    def __str__(self) -> str:
        return str(self.value)
