from enum import Enum


class GBTNoticeType(str, Enum):
    EXECUTION = "EXECUTION"
    MODELING = "MODELING"
    OTHER = "OTHER"
    PARSE = "PARSE"
    SEMANTIC = "SEMANTIC"
    TEST = "TEST"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
