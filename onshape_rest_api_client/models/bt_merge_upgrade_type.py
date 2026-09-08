from enum import StrEnum


class BTMergeUpgradeType(StrEnum):
    SOURCE = "SOURCE"
    SOURCE_AND_TARGET = "SOURCE_AND_TARGET"
    TARGET = "TARGET"

    def __str__(self) -> str:
        return str(self.value)
