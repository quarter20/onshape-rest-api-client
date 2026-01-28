from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bt_parameter_visibility_condition_177 import BTParameterVisibilityCondition177


T = TypeVar("T", bound="BTParameterSpecEnum171EnumValueToVisibilityCondition")


@_attrs_define
class BTParameterSpecEnum171EnumValueToVisibilityCondition:
    """ """

    additional_properties: dict[str, BTParameterVisibilityCondition177] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_parameter_visibility_condition_177 import BTParameterVisibilityCondition177

        d = dict(src_dict)
        bt_parameter_spec_enum_171_enum_value_to_visibility_condition = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = BTParameterVisibilityCondition177.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        bt_parameter_spec_enum_171_enum_value_to_visibility_condition.additional_properties = additional_properties
        return bt_parameter_spec_enum_171_enum_value_to_visibility_condition

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> BTParameterVisibilityCondition177:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: BTParameterVisibilityCondition177) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
