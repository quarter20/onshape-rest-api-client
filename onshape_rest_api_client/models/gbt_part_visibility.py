from enum import StrEnum


class GBTPartVisibility(StrEnum):
    HIDDEN = "HIDDEN"
    UNKNOWN = "UNKNOWN"
    UNSPECIFIED = "UNSPECIFIED"
    VISIBLE = "VISIBLE"

    def __str__(self) -> str:
        return str(self.value)
