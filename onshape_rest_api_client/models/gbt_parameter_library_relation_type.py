from enum import Enum


class GBTParameterLibraryRelationType(str, Enum):
    CONTROLLED = "CONTROLLED"
    NONE = "NONE"
    OVERRIDE = "OVERRIDE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
