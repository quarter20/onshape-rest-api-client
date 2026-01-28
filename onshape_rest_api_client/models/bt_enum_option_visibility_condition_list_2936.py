from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_enum_option_visibility_condition_3455 import BTEnumOptionVisibilityCondition3455


T = TypeVar("T", bound="BTEnumOptionVisibilityConditionList2936")


@_attrs_define
class BTEnumOptionVisibilityConditionList2936:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        visibility_conditions (list[BTEnumOptionVisibilityCondition3455] | Unset):
    """

    bt_type: str | Unset = UNSET
    visibility_conditions: list[BTEnumOptionVisibilityCondition3455] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        visibility_conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.visibility_conditions, Unset):
            visibility_conditions = []
            for visibility_conditions_item_data in self.visibility_conditions:
                visibility_conditions_item = visibility_conditions_item_data.to_dict()
                visibility_conditions.append(visibility_conditions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if visibility_conditions is not UNSET:
            field_dict["visibilityConditions"] = visibility_conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_enum_option_visibility_condition_3455 import BTEnumOptionVisibilityCondition3455

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _visibility_conditions = d.pop("visibilityConditions", UNSET)
        visibility_conditions: list[BTEnumOptionVisibilityCondition3455] | Unset = UNSET
        if _visibility_conditions is not UNSET:
            visibility_conditions = []
            for visibility_conditions_item_data in _visibility_conditions:
                visibility_conditions_item = BTEnumOptionVisibilityCondition3455.from_dict(
                    visibility_conditions_item_data
                )

                visibility_conditions.append(visibility_conditions_item)

        bt_enum_option_visibility_condition_list_2936 = cls(
            bt_type=bt_type,
            visibility_conditions=visibility_conditions,
        )

        bt_enum_option_visibility_condition_list_2936.additional_properties = d
        return bt_enum_option_visibility_condition_list_2936

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
