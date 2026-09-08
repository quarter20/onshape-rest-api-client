from enum import StrEnum


class GBTNodeStatusType(StrEnum):
    ERROR = "ERROR"
    INFO = "INFO"
    OK = "OK"
    UNKNOWN = "UNKNOWN"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
