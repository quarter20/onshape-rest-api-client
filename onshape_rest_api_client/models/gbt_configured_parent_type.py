from enum import StrEnum


class GBTConfiguredParentType(StrEnum):
    FEATURE = "FEATURE"
    INSTANCE = "INSTANCE"
    MATE = "MATE"
    MATE_CONNECTOR = "MATE_CONNECTOR"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
