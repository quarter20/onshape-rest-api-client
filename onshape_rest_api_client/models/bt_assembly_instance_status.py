from enum import StrEnum


class BTAssemblyInstanceStatus(StrEnum):
    DELETEDELEMENT = "DeletedElement"

    def __str__(self) -> str:
        return str(self.value)
