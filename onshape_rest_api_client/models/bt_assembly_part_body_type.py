from enum import Enum


class BTAssemblyPartBodyType(str, Enum):
    COMPOSITE = "composite"
    SHEET = "sheet"
    SOLID = "solid"

    def __str__(self) -> str:
        return str(self.value)
