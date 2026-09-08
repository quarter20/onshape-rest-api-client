from enum import StrEnum


class BTAssemblyPartBodyType(StrEnum):
    COMPOSITE = "composite"
    SHEET = "sheet"
    SOLID = "solid"

    def __str__(self) -> str:
        return str(self.value)
