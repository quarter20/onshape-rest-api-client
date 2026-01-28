from enum import Enum


class GBTSubAssemblyLockType(str, Enum):
    CURRENT_POSITION = "CURRENT_POSITION"
    NAMED_POSIITION = "NAMED_POSIITION"
    SUB_ASSEMBLY_POSITION = "SUB_ASSEMBLY_POSITION"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
