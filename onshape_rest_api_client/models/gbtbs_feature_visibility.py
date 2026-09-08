from enum import StrEnum


class GBTBSFeatureVisibility(StrEnum):
    HIDDEN = "HIDDEN"
    UNKNOWN = "UNKNOWN"
    UNSET = "UNSET"
    VISIBLE = "VISIBLE"

    def __str__(self) -> str:
        return str(self.value)
