from enum import Enum


class GBTFilterFlattenedGeometryOptions(str, Enum):
    FLATTENED_ONLY = "FLATTENED_ONLY"
    MODEL_AND_FLATTENED = "MODEL_AND_FLATTENED"
    MODEL_ONLY = "MODEL_ONLY"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
