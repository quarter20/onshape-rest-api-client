from enum import Enum


class VersionAlias(str, Enum):
    LAST_BUILD = "LAST_BUILD"
    LAST_MINOR = "LAST_MINOR"

    def __str__(self) -> str:
        return str(self.value)
