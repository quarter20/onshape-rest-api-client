from enum import Enum


class BTOldPermission(str, Enum):
    ANONYMOUS_ACCESS = "ANONYMOUS_ACCESS"
    COMMENT = "COMMENT"
    FULL = "FULL"
    NOACCESS = "NOACCESS"
    OWNER = "OWNER"
    READ = "READ"
    READ_COPY_EXPORT = "READ_COPY_EXPORT"
    RESHARE = "RESHARE"
    WRITE = "WRITE"

    def __str__(self) -> str:
        return str(self.value)
