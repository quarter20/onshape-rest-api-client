from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_enum_option_range_3741 import BTEnumOptionRange3741


T = TypeVar("T", bound="BTParameterVisibilityInRange2980")


@_attrs_define
class BTParameterVisibilityInRange2980:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        self_or_child_always_visible (bool | Unset):
        option_range (BTEnumOptionRange3741 | Unset):
        parameter_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    self_or_child_always_visible: bool | Unset = UNSET
    option_range: BTEnumOptionRange3741 | Unset = UNSET
    parameter_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        self_or_child_always_visible = self.self_or_child_always_visible

        option_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.option_range, Unset):
            option_range = self.option_range.to_dict()

        parameter_id = self.parameter_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if self_or_child_always_visible is not UNSET:
            field_dict["selfOrChildAlwaysVisible"] = self_or_child_always_visible
        if option_range is not UNSET:
            field_dict["optionRange"] = option_range
        if parameter_id is not UNSET:
            field_dict["parameterId"] = parameter_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_enum_option_range_3741 import BTEnumOptionRange3741

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        self_or_child_always_visible = d.pop("selfOrChildAlwaysVisible", UNSET)

        _option_range = d.pop("optionRange", UNSET)
        option_range: BTEnumOptionRange3741 | Unset
        if isinstance(_option_range, Unset):
            option_range = UNSET
        else:
            option_range = BTEnumOptionRange3741.from_dict(_option_range)

        parameter_id = d.pop("parameterId", UNSET)

        bt_parameter_visibility_in_range_2980 = cls(
            bt_type=bt_type,
            self_or_child_always_visible=self_or_child_always_visible,
            option_range=option_range,
            parameter_id=parameter_id,
        )

        bt_parameter_visibility_in_range_2980.additional_properties = d
        return bt_parameter_visibility_in_range_2980

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
