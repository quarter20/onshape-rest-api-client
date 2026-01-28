from enum import Enum


class GBTAssemblyFeatureDisplayStatus(str, Enum):
    ERROR = "ERROR"
    OK = "OK"
    SUPPRESSED = "SUPPRESSED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
