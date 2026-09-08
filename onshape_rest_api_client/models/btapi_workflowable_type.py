from enum import StrEnum


class BTAPIWorkflowableType(StrEnum):
    ASSIGNMENT = "ASSIGNMENT"
    OBSOLETION = "OBSOLETION"
    RELEASE = "RELEASE"
    TASK = "TASK"

    def __str__(self) -> str:
        return str(self.value)
