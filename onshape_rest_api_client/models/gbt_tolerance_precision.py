from enum import StrEnum


class GBTTolerancePrecision(StrEnum):
    DEFAULT = "DEFAULT"
    HUNDREDTHS = "HUNDREDTHS"
    HUNDRED_THOUSANDTHS = "HUNDRED_THOUSANDTHS"
    MILLIONTHS = "MILLIONTHS"
    ONES = "ONES"
    TENTHS = "TENTHS"
    TEN_THOUSANDTHS = "TEN_THOUSANDTHS"
    THOUSANDTHS = "THOUSANDTHS"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
