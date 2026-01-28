from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTParameterVisibilityOnEqual180")


@_attrs_define
class BTParameterVisibilityOnEqual180:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        self_or_child_always_visible (bool | Unset):
        in_array (bool | Unset):
        parameter_id (str | Unset):
        value (str | Unset):
    """

    bt_type: str | Unset = UNSET
    self_or_child_always_visible: bool | Unset = UNSET
    in_array: bool | Unset = UNSET
    parameter_id: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        self_or_child_always_visible = self.self_or_child_always_visible

        in_array = self.in_array

        parameter_id = self.parameter_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if self_or_child_always_visible is not UNSET:
            field_dict["selfOrChildAlwaysVisible"] = self_or_child_always_visible
        if in_array is not UNSET:
            field_dict["inArray"] = in_array
        if parameter_id is not UNSET:
            field_dict["parameterId"] = parameter_id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        self_or_child_always_visible = d.pop("selfOrChildAlwaysVisible", UNSET)

        in_array = d.pop("inArray", UNSET)

        parameter_id = d.pop("parameterId", UNSET)

        value = d.pop("value", UNSET)

        bt_parameter_visibility_on_equal_180 = cls(
            bt_type=bt_type,
            self_or_child_always_visible=self_or_child_always_visible,
            in_array=in_array,
            parameter_id=parameter_id,
            value=value,
        )

        bt_parameter_visibility_on_equal_180.additional_properties = d
        return bt_parameter_visibility_on_equal_180

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
