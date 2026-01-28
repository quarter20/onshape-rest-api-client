from enum import Enum


class GBTDataItemFormat(str, Enum):
    JSON = "JSON"
    OBJ_MTL_ZIP = "OBJ_MTL_ZIP"
    ONSHAPE = "ONSHAPE"
    STL = "STL"
    UNKNOWN = "UNKNOWN"
    XMM = "XMM"
    X_B = "X_B"
    X_T = "X_T"
    X_T_XMM_ZIP = "X_T_XMM_ZIP"
    ZIP = "ZIP"

    def __str__(self) -> str:
        return str(self.value)
