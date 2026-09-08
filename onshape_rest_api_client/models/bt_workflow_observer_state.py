from enum import StrEnum


class BTWorkflowObserverState(StrEnum):
    APPROVED = "APPROVED"
    NONE = "NONE"
    OVERRIDDEN = "OVERRIDDEN"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
