from enum import Enum


class GBTPartStudioInstanceType(str, Enum):
    COMPOSITE = "COMPOSITE"
    PART = "PART"
    SKETCH = "SKETCH"
    SURFACE = "SURFACE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
