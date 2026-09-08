from enum import StrEnum


class BTMergeStrategy(StrEnum):
    KEEP = "KEEP"
    MERGE = "MERGE"
    REPLACE = "REPLACE"

    def __str__(self) -> str:
        return str(self.value)
