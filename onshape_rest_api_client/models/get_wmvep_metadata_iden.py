from enum import Enum


class GetWMVEPMetadataIden(str, Enum):
    P = "p"
    PI = "pi"

    def __str__(self) -> str:
        return str(self.value)
