from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTStandardContentParameterIdAndValue")


@_attrs_define
class BTStandardContentParameterIdAndValue:
    """Parameters that drive configuration. Used to specify the standard content component to which the custom parameter
    values are associated.

        Attributes:
            parameter_id (str | Unset):
            value (str | Unset):
    """

    parameter_id: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameter_id = self.parameter_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parameter_id is not UNSET:
            field_dict["parameterId"] = parameter_id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parameter_id = d.pop("parameterId", UNSET)

        value = d.pop("value", UNSET)

        bt_standard_content_parameter_id_and_value = cls(
            parameter_id=parameter_id,
            value=value,
        )

        bt_standard_content_parameter_id_and_value.additional_properties = d
        return bt_standard_content_parameter_id_and_value

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
