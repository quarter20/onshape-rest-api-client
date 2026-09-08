from enum import StrEnum


class BTTransitionType(StrEnum):
    APPROVE = "APPROVE"
    APPROVE_DIRECT = "APPROVE_DIRECT"
    COMMENT = "COMMENT"
    DEFAULT = "DEFAULT"
    DELETE = "DELETE"
    REASSIGN_TASK = "REASSIGN_TASK"
    REJECT = "REJECT"
    SUBMIT = "SUBMIT"

    def __str__(self) -> str:
        return str(self.value)
