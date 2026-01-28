from enum import Enum


class BTUserAppSettingOperationType(str, Enum):
    ADD = "ADD"
    REMOVE = "REMOVE"
    UPDATE = "UPDATE"

    def __str__(self) -> str:
        return str(self.value)
