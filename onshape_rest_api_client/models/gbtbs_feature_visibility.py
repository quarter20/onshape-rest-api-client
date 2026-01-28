from enum import Enum


class GBTBSFeatureVisibility(str, Enum):
    HIDDEN = "HIDDEN"
    UNKNOWN = "UNKNOWN"
    UNSET = "UNSET"
    VISIBLE = "VISIBLE"

    def __str__(self) -> str:
        return str(self.value)
