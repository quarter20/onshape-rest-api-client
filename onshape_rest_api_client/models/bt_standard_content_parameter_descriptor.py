from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTStandardContentParameterDescriptor")


@_attrs_define
class BTStandardContentParameterDescriptor:
    """
    Attributes:
        display_name (str | Unset):
        parameter_id (str | Unset):
        parameter_values (list[str] | Unset):
    """

    display_name: str | Unset = UNSET
    parameter_id: str | Unset = UNSET
    parameter_values: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        parameter_id = self.parameter_id

        parameter_values: list[str] | Unset = UNSET
        if not isinstance(self.parameter_values, Unset):
            parameter_values = self.parameter_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if parameter_id is not UNSET:
            field_dict["parameterId"] = parameter_id
        if parameter_values is not UNSET:
            field_dict["parameterValues"] = parameter_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName", UNSET)

        parameter_id = d.pop("parameterId", UNSET)

        parameter_values = cast(list[str], d.pop("parameterValues", UNSET))

        bt_standard_content_parameter_descriptor = cls(
            display_name=display_name,
            parameter_id=parameter_id,
            parameter_values=parameter_values,
        )

        bt_standard_content_parameter_descriptor.additional_properties = d
        return bt_standard_content_parameter_descriptor

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
