from enum import StrEnum


class BTAssemblyInstanceType(StrEnum):
    ASSEMBLY = "Assembly"
    FEATURE = "Feature"
    PART = "Part"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
