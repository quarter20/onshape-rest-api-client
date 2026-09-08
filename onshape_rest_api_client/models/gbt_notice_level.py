from enum import StrEnum


class GBTNoticeLevel(StrEnum):
    ERROR = "ERROR"
    INFO = "INFO"
    INTERNAL = "INTERNAL"
    UNKNOWN = "UNKNOWN"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
