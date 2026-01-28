from enum import Enum


class BTAssemblyInstanceStatus(str, Enum):
    DELETEDELEMENT = "DeletedElement"

    def __str__(self) -> str:
        return str(self.value)
