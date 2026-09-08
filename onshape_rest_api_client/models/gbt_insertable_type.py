from enum import StrEnum


class GBTInsertableType(StrEnum):
    COMPOSITE_PARTS = "COMPOSITE_PARTS"
    FLATTENED_PARTS = "FLATTENED_PARTS"
    PARAMETRIC_PART_STUDIOS = "PARAMETRIC_PART_STUDIOS"
    PARTS = "PARTS"
    PART_STUDIOS = "PART_STUDIOS"
    SKETCHES = "SKETCHES"
    SURFACES = "SURFACES"
    UNKNOWN = "UNKNOWN"
    WIRES = "WIRES"

    def __str__(self) -> str:
        return str(self.value)
