from enum import Enum


class GBTRhinoVersions(str, Enum):
    UNKNOWN = "UNKNOWN"
    V2 = "V2"
    V3 = "V3"
    V4 = "V4"
    V5 = "V5"
    V6 = "V6"
    V7 = "V7"
    V8 = "V8"

    def __str__(self) -> str:
        return str(self.value)
