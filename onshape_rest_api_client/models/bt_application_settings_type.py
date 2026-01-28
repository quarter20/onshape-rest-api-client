from enum import Enum


class BTApplicationSettingsType(str, Enum):
    COMPANY = "COMPANY"
    TEAM = "TEAM"
    USER = "USER"

    def __str__(self) -> str:
        return str(self.value)
