from enum import Enum


class BTDiffInfoCollectionType(str, Enum):
    CURVES = "curves"
    MATECONNECTORS = "mateConnectors"
    PARTS = "parts"
    PLANES = "planes"
    POINTS = "points"
    SKETCHES = "sketches"
    SURFACES = "surfaces"

    def __str__(self) -> str:
        return str(self.value)
