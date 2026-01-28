from enum import Enum


class GBTAssemblySimulationType(str, Enum):
    CONTACT_ANALYSIS = "CONTACT_ANALYSIS"
    LINEAR_STATIC = "LINEAR_STATIC"
    MODAL = "MODAL"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
