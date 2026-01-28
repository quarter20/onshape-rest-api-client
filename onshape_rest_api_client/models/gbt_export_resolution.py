from enum import Enum


class GBTExportResolution(str, Enum):
    COARSE = "COARSE"
    FINE = "FINE"
    MEDIUM = "MEDIUM"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
