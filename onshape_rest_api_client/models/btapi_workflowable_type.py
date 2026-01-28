from enum import Enum


class BTAPIWorkflowableType(str, Enum):
    ASSIGNMENT = "ASSIGNMENT"
    OBSOLETION = "OBSOLETION"
    RELEASE = "RELEASE"
    TASK = "TASK"

    def __str__(self) -> str:
        return str(self.value)
