from enum import Enum


class BTMergeUpgradeType(str, Enum):
    SOURCE = "SOURCE"
    SOURCE_AND_TARGET = "SOURCE_AND_TARGET"
    TARGET = "TARGET"

    def __str__(self) -> str:
        return str(self.value)
