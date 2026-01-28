from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bt_base_entity_appearance_entry_3607 import BTBaseEntityAppearanceEntry3607


T = TypeVar("T", bound="BTBaseEntityAppearanceSettings1391ColorIdToBaseEntityAppearanceEntry")


@_attrs_define
class BTBaseEntityAppearanceSettings1391ColorIdToBaseEntityAppearanceEntry:
    """ """

    additional_properties: dict[str, BTBaseEntityAppearanceEntry3607] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_base_entity_appearance_entry_3607 import BTBaseEntityAppearanceEntry3607

        d = dict(src_dict)
        bt_base_entity_appearance_settings_1391_color_id_to_base_entity_appearance_entry = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = BTBaseEntityAppearanceEntry3607.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        bt_base_entity_appearance_settings_1391_color_id_to_base_entity_appearance_entry.additional_properties = (
            additional_properties
        )
        return bt_base_entity_appearance_settings_1391_color_id_to_base_entity_appearance_entry

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> BTBaseEntityAppearanceEntry3607:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: BTBaseEntityAppearanceEntry3607) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
