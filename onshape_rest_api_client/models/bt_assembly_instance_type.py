from enum import Enum


class BTAssemblyInstanceType(str, Enum):
    ASSEMBLY = "Assembly"
    FEATURE = "Feature"
    PART = "Part"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
