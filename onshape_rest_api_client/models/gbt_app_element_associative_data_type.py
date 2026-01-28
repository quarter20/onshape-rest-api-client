from enum import Enum


class GBTAppElementAssociativeDataType(str, Enum):
    MODEL_DEFINITION_ENTITY = "MODEL_DEFINITION_ENTITY"
    MODEL_DEFINITION_FEATURE = "MODEL_DEFINITION_FEATURE"
    MODEL_TOPOLOGY = "MODEL_TOPOLOGY"
    ONSHAPE_DRAWING_VIEW = "ONSHAPE_DRAWING_VIEW"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
