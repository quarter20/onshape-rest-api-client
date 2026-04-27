from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_metadata_enum_value_info import BTMetadataEnumValueInfo


T = TypeVar("T", bound="BTSelectedMetadataEnumValue")


@_attrs_define
class BTSelectedMetadataEnumValue:
    """
    Attributes:
        enum_options (list[BTMetadataEnumValueInfo] | Unset):
        selected_value (str | Unset):
    """

    enum_options: list[BTMetadataEnumValueInfo] | Unset = UNSET
    selected_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enum_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.enum_options, Unset):
            enum_options = []
            for enum_options_item_data in self.enum_options:
                enum_options_item = enum_options_item_data.to_dict()
                enum_options.append(enum_options_item)

        selected_value = self.selected_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enum_options is not UNSET:
            field_dict["enumOptions"] = enum_options
        if selected_value is not UNSET:
            field_dict["selectedValue"] = selected_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_metadata_enum_value_info import BTMetadataEnumValueInfo

        d = dict(src_dict)
        _enum_options = d.pop("enumOptions", UNSET)
        enum_options: list[BTMetadataEnumValueInfo] | Unset = UNSET
        if _enum_options is not UNSET:
            enum_options = []
            for enum_options_item_data in _enum_options:
                enum_options_item = BTMetadataEnumValueInfo.from_dict(enum_options_item_data)

                enum_options.append(enum_options_item)

        selected_value = d.pop("selectedValue", UNSET)

        bt_selected_metadata_enum_value = cls(
            enum_options=enum_options,
            selected_value=selected_value,
        )

        bt_selected_metadata_enum_value.additional_properties = d
        return bt_selected_metadata_enum_value

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
