from enum import StrEnum


class GBTPatternType(StrEnum):
    CIRCULAR = "CIRCULAR"
    LINEAR = "LINEAR"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
