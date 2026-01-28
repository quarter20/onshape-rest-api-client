from enum import Enum


class GBTRadiusDisplay(str, Enum):
    DIAMETRAL = "DIAMETRAL"
    NONE = "NONE"
    RADIAL = "RADIAL"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
