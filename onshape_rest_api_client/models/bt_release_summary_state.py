from enum import Enum


class BTReleaseSummaryState(str, Enum):
    DEGRADED_POSTCOMMIT = "DEGRADED_POSTCOMMIT"
    FAILED = "FAILED"
    FAILED_POSTCOMMIT = "FAILED_POSTCOMMIT"
    FAILED_PRECOMMIT = "FAILED_PRECOMMIT"
    HEALTHY = "HEALTHY"
    IN_PROGRESS = "IN_PROGRESS"

    def __str__(self) -> str:
        return str(self.value)
