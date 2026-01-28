from enum import Enum


class GBTSimulationContactBehavior(str, Enum):
    FUSE_IN_CONTACT = "FUSE_IN_CONTACT"
    FUSE_IN_CONTACT_AND_USE_MATES = "FUSE_IN_CONTACT_AND_USE_MATES"
    MATES_ONLY = "MATES_ONLY"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
