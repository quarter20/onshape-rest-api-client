from enum import StrEnum


class GBTWeldJointType(StrEnum):
    DOUBLE_BEVEL_GROOVE = "DOUBLE_BEVEL_GROOVE"
    DOUBLE_FLARE_BEVEL = "DOUBLE_FLARE_BEVEL"
    DOUBLE_FLARE_V = "DOUBLE_FLARE_V"
    DOUBLE_J_GROOVE = "DOUBLE_J_GROOVE"
    DOUBLE_U_GROOVE = "DOUBLE_U_GROOVE"
    DOUBLE_V_GROOVE = "DOUBLE_V_GROOVE"
    NONE = "NONE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
