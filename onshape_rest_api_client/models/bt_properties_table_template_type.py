from enum import Enum


class BTPropertiesTableTemplateType(str, Enum):
    BOM = "BOM"
    INSPECTION_TABLE = "INSPECTION_TABLE"
    REVISION_TABLE = "REVISION_TABLE"

    def __str__(self) -> str:
        return str(self.value)
