from enum import StrEnum


class GBTAssemblyFeatureDisplayStatus(StrEnum):
    ERROR = "ERROR"
    OK = "OK"
    SUPPRESSED = "SUPPRESSED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
