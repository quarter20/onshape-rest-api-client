from enum import StrEnum


class GBTTessellationSettingEnum(StrEnum):
    AUTO = "AUTO"
    COARSE = "COARSE"
    CURVATURE_VISUALIZATION = "CURVATURE_VISUALIZATION"
    FINE = "FINE"
    MEDIUM = "MEDIUM"
    UNKNOWN = "UNKNOWN"
    VERY_FINE = "VERY_FINE"

    def __str__(self) -> str:
        return str(self.value)
