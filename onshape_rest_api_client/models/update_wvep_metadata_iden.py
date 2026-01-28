from enum import Enum


class UpdateWVEPMetadataIden(str, Enum):
    P = "p"
    PI = "pi"

    def __str__(self) -> str:
        return str(self.value)
