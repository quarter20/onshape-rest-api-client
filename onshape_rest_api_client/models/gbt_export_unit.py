from enum import Enum


class GBTExportUnit(str, Enum):
    CENTIMETER = "CENTIMETER"
    FOOT = "FOOT"
    INCH = "INCH"
    METER = "METER"
    MILLIMETER = "MILLIMETER"
    UNKNOWN = "UNKNOWN"
    YARD = "YARD"

    def __str__(self) -> str:
        return str(self.value)
