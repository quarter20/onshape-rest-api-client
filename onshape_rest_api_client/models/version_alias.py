from enum import StrEnum


class VersionAlias(StrEnum):
    LAST_BUILD = "LAST_BUILD"
    LAST_MINOR = "LAST_MINOR"

    def __str__(self) -> str:
        return str(self.value)
