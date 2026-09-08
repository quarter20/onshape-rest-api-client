from enum import StrEnum


class GBTAssemblySimulationType(StrEnum):
    CONTACT_ANALYSIS = "CONTACT_ANALYSIS"
    LINEAR_STATIC = "LINEAR_STATIC"
    MODAL = "MODAL"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
