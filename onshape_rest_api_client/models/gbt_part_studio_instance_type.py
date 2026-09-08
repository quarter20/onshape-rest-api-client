from enum import StrEnum


class GBTPartStudioInstanceType(StrEnum):
    COMPOSITE = "COMPOSITE"
    PART = "PART"
    SKETCH = "SKETCH"
    SURFACE = "SURFACE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
