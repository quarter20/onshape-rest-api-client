from enum import StrEnum


class BTComputedAssemblyPropertyErrorPolicy(StrEnum):
    EXCLUDEFROMCOMPUTATION = "ExcludeFromComputation"
    PROPAGATEERROR = "PropagateError"
    TREATASFALSE = "TreatAsFalse"
    TREATASTRUE = "TreatAsTrue"
    TREATASZERO = "TreatAsZero"

    def __str__(self) -> str:
        return str(self.value)
