from enum import Enum


class BTMergeStrategy(str, Enum):
    KEEP = "KEEP"
    MERGE = "MERGE"
    REPLACE = "REPLACE"

    def __str__(self) -> str:
        return str(self.value)
