from enum import Enum


class GBTNoticeLevel(str, Enum):
    ERROR = "ERROR"
    INFO = "INFO"
    INTERNAL = "INTERNAL"
    UNKNOWN = "UNKNOWN"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
