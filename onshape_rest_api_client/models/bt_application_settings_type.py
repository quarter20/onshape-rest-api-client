from enum import StrEnum


class BTApplicationSettingsType(StrEnum):
    COMPANY = "COMPANY"
    TEAM = "TEAM"
    USER = "USER"

    def __str__(self) -> str:
        return str(self.value)
