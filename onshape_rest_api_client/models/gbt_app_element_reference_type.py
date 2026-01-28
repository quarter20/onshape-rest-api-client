from enum import Enum


class GBTAppElementReferenceType(str, Enum):
    ASSEMBLY = "ASSEMBLY"
    COMPOSITE_PART = "COMPOSITE_PART"
    CURVE = "CURVE"
    FLATTENED_PART = "FLATTENED_PART"
    MESH_PART = "MESH_PART"
    PART = "PART"
    PARTSTUDIO = "PARTSTUDIO"
    SKETCH = "SKETCH"
    SURFACE = "SURFACE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
