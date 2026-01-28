from enum import Enum


class BTWorkflowObserverState(str, Enum):
    APPROVED = "APPROVED"
    NONE = "NONE"
    OVERRIDDEN = "OVERRIDDEN"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
