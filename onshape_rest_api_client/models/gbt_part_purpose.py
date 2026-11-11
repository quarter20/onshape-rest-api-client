from enum import StrEnum


class GBTPartPurpose(StrEnum):
    STANDARD_CONTENT_PART = "STANDARD_CONTENT_PART"
    UNKNOWN = "UNKNOWN"
    UNMARKED = "UNMARKED"

    def __str__(self) -> str:
        return str(self.value)
