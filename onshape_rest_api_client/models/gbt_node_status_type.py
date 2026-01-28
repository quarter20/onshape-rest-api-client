from enum import Enum


class GBTNodeStatusType(str, Enum):
    ERROR = "ERROR"
    INFO = "INFO"
    OK = "OK"
    UNKNOWN = "UNKNOWN"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
