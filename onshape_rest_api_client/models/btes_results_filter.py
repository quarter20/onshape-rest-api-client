from enum import Enum


class BTESResultsFilter(str, Enum):
    ALL = "ALL"
    LATEST = "LATEST"
    LATEST_PER_HIT = "LATEST_PER_HIT"

    def __str__(self) -> str:
        return str(self.value)
