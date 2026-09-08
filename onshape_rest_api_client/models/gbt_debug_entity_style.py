from enum import StrEnum


class GBTDebugEntityStyle(StrEnum):
    DEFAULT = "DEFAULT"
    ERROR = "ERROR"
    STAR = "STAR"
    UNKNOWN = "UNKNOWN"
    WITH_START = "WITH_START"

    def __str__(self) -> str:
        return str(self.value)
