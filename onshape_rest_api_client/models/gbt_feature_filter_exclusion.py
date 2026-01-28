from enum import Enum


class GBTFeatureFilterExclusion(str, Enum):
    EXCLUDE_EVERYTHING_ELSE = "EXCLUDE_EVERYTHING_ELSE"
    EXCLUDE_THIS = "EXCLUDE_THIS"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
