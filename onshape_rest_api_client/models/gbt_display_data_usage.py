from enum import Enum


class GBTDisplayDataUsage(str, Enum):
    BASE = "BASE"
    COMPARE_TARGET = "COMPARE_TARGET"
    PREVIEW_AFTER = "PREVIEW_AFTER"
    PREVIEW_BEFORE = "PREVIEW_BEFORE"
    PREVIEW_FINAL = "PREVIEW_FINAL"
    REFERENCE_REPAIR = "REFERENCE_REPAIR"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
