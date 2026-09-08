from enum import StrEnum


class GBTSimulationContactBehavior(StrEnum):
    FUSE_IN_CONTACT = "FUSE_IN_CONTACT"
    FUSE_IN_CONTACT_AND_USE_MATES = "FUSE_IN_CONTACT_AND_USE_MATES"
    MATES_ONLY = "MATES_ONLY"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
