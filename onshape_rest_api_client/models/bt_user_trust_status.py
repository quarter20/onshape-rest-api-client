from enum import StrEnum


class BTUserTrustStatus(StrEnum):
    MALICIOUS = "MALICIOUS"
    TRUSTED = "TRUSTED"
    UNREVIEWED = "UNREVIEWED"

    def __str__(self) -> str:
        return str(self.value)
