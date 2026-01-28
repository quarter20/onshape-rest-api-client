from enum import Enum


class EditType(str, Enum):
    CHANGE = "CHANGE"
    CHANGE_FIELD = "CHANGE_FIELD"
    DELETION = "DELETION"
    INSERTION = "INSERTION"
    LIST = "LIST"
    MOVE = "MOVE"
    NEW_ROOT = "NEW_ROOT"
    NOTHING = "NOTHING"

    def __str__(self) -> str:
        return str(self.value)
