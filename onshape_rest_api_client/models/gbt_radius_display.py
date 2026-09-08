from enum import StrEnum


class GBTRadiusDisplay(StrEnum):
    DIAMETRAL = "DIAMETRAL"
    NONE = "NONE"
    RADIAL = "RADIAL"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
