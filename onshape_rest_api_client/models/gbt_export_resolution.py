from enum import StrEnum


class GBTExportResolution(StrEnum):
    COARSE = "COARSE"
    FINE = "FINE"
    MEDIUM = "MEDIUM"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
