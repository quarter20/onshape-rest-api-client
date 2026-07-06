from enum import Enum


class GBTParameterLibraryRelationType(str, Enum):
    DEFAULT = "DEFAULT"
    IGNORE_LIBRARY_VALUES = "IGNORE_LIBRARY_VALUES"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
