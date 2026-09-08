from enum import StrEnum


class GBTExportUnit(StrEnum):
    CENTIMETER = "CENTIMETER"
    FOOT = "FOOT"
    INCH = "INCH"
    METER = "METER"
    MILLIMETER = "MILLIMETER"
    UNKNOWN = "UNKNOWN"
    YARD = "YARD"

    def __str__(self) -> str:
        return str(self.value)
