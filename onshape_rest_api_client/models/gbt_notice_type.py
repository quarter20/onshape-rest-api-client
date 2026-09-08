from enum import StrEnum


class GBTNoticeType(StrEnum):
    EXECUTION = "EXECUTION"
    MODELING = "MODELING"
    OTHER = "OTHER"
    PARSE = "PARSE"
    SEMANTIC = "SEMANTIC"
    TEST = "TEST"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
