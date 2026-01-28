from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTComputedConfigurationInputSpec2525")


@_attrs_define
class BTComputedConfigurationInputSpec2525:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        input_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    input_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        input_id = self.input_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if input_id is not UNSET:
            field_dict["inputId"] = input_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        input_id = d.pop("inputId", UNSET)

        bt_computed_configuration_input_spec_2525 = cls(
            bt_type=bt_type,
            input_id=input_id,
        )

        bt_computed_configuration_input_spec_2525.additional_properties = d
        return bt_computed_configuration_input_spec_2525

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
