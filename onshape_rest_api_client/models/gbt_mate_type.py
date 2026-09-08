from enum import StrEnum


class GBTMateType(StrEnum):
    BALL = "BALL"
    CYLINDRICAL = "CYLINDRICAL"
    FASTENED = "FASTENED"
    PARALLEL = "PARALLEL"
    PIN_SLOT = "PIN_SLOT"
    PLANAR = "PLANAR"
    REVOLUTE = "REVOLUTE"
    SLIDER = "SLIDER"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
