from enum import Enum


class GBTPartStudioItemType(str, Enum):
    COMPOSITE_PART = "COMPOSITE_PART"
    CONSTRUCTION_PLANE = "CONSTRUCTION_PLANE"
    ENTIRE_PART_STUDIO = "ENTIRE_PART_STUDIO"
    FLATTENED_SHEET_METAL = "FLATTENED_SHEET_METAL"
    MESH = "MESH"
    SKETCH = "SKETCH"
    SOLID = "SOLID"
    SURFACE = "SURFACE"
    UNKNOWN = "UNKNOWN"
    WIRE = "WIRE"

    def __str__(self) -> str:
        return str(self.value)
