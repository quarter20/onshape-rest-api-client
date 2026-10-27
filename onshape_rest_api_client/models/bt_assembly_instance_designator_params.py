from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bt_assembly_instance_designator_params_designators import (
        BTAssemblyInstanceDesignatorParamsDesignators,
    )


T = TypeVar("T", bound="BTAssemblyInstanceDesignatorParams")


@_attrs_define
class BTAssemblyInstanceDesignatorParams:
    """
    Attributes:
        designators (BTAssemblyInstanceDesignatorParamsDesignators): Map of top-level instance IDs of this assembly to
            designator values. Occurrence paths (IDs joined by '.') are not accepted; to set a designator on an instance
            inside a sub-assembly, call this endpoint on the sub-assembly that directly contains it. Maximum allowed length
            of a designator is 64 characters. Markup characters ('<' and '>') are not allowed. Set an empty string to clear
            the designator.
    """

    designators: BTAssemblyInstanceDesignatorParamsDesignators
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        designators = self.designators.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "designators": designators,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_assembly_instance_designator_params_designators import (
            BTAssemblyInstanceDesignatorParamsDesignators,  # noqa: PLC0415
        )

        d = dict(src_dict)
        designators = BTAssemblyInstanceDesignatorParamsDesignators.from_dict(d.pop("designators"))

        bt_assembly_instance_designator_params = cls(
            designators=designators,
        )

        bt_assembly_instance_designator_params.additional_properties = d
        return bt_assembly_instance_designator_params

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
