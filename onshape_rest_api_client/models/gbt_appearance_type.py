from enum import StrEnum


class GBTAppearanceType(StrEnum):
    SKETCH = "SKETCH"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
