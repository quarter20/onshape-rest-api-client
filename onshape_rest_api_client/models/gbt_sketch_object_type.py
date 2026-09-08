from enum import StrEnum


class GBTSketchObjectType(StrEnum):
    ANY_SKETCH_OBJECT = "ANY_SKETCH_OBJECT"
    NOT_SKETCH_OBJECT = "NOT_SKETCH_OBJECT"
    UNKNOWN = "UNKNOWN"
    USER_ENTITY = "USER_ENTITY"
    WHOLE_SKETCH = "WHOLE_SKETCH"

    def __str__(self) -> str:
        return str(self.value)
