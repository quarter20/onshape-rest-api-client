from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BTAssemblyInstanceDesignatorParamsDesignators")


@_attrs_define
class BTAssemblyInstanceDesignatorParamsDesignators:
    """Map of top-level instance IDs of this assembly to designator values. Occurrence paths (IDs joined by '.') are not
    accepted; to set a designator on an instance inside a sub-assembly, call this endpoint on the sub-assembly that
    directly contains it. Maximum allowed length of a designator is 64 characters. Markup characters ('<' and '>') are
    not allowed. Set an empty string to clear the designator.

    """

    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_assembly_instance_designator_params_designators = cls()

        bt_assembly_instance_designator_params_designators.additional_properties = d
        return bt_assembly_instance_designator_params_designators

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
