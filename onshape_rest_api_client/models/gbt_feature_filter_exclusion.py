from enum import StrEnum


class GBTFeatureFilterExclusion(StrEnum):
    EXCLUDE_EVERYTHING_ELSE = "EXCLUDE_EVERYTHING_ELSE"
    EXCLUDE_THIS = "EXCLUDE_THIS"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
