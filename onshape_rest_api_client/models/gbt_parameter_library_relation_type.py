from enum import StrEnum


class GBTParameterLibraryRelationType(StrEnum):
    DEFAULT = "DEFAULT"
    IGNORE_LIBRARY_VALUES = "IGNORE_LIBRARY_VALUES"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
