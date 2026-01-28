from enum import Enum


class GBTAppearanceType(str, Enum):
    SKETCH = "SKETCH"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
