from enum import Enum


class BTRestoreStrategy(str, Enum):
    KEEP = "KEEP"
    REPLACE = "REPLACE"

    def __str__(self) -> str:
        return str(self.value)
