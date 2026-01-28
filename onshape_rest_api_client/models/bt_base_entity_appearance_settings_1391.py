from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_base_entity_appearance_settings_1391_color_id_to_base_entity_appearance_entry import (
        BTBaseEntityAppearanceSettings1391ColorIdToBaseEntityAppearanceEntry,
    )


T = TypeVar("T", bound="BTBaseEntityAppearanceSettings1391")


@_attrs_define
class BTBaseEntityAppearanceSettings1391:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        color_id_to_base_entity_appearance_entry (BTBaseEntityAppearanceSettings1391ColorIdToBaseEntityAppearanceEntry |
            Unset):
        is_noop (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    color_id_to_base_entity_appearance_entry: (
        BTBaseEntityAppearanceSettings1391ColorIdToBaseEntityAppearanceEntry | Unset
    ) = UNSET
    is_noop: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        color_id_to_base_entity_appearance_entry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.color_id_to_base_entity_appearance_entry, Unset):
            color_id_to_base_entity_appearance_entry = self.color_id_to_base_entity_appearance_entry.to_dict()

        is_noop = self.is_noop

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if color_id_to_base_entity_appearance_entry is not UNSET:
            field_dict["colorIdToBaseEntityAppearanceEntry"] = color_id_to_base_entity_appearance_entry
        if is_noop is not UNSET:
            field_dict["isNoop"] = is_noop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_base_entity_appearance_settings_1391_color_id_to_base_entity_appearance_entry import (
            BTBaseEntityAppearanceSettings1391ColorIdToBaseEntityAppearanceEntry,
        )

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _color_id_to_base_entity_appearance_entry = d.pop("colorIdToBaseEntityAppearanceEntry", UNSET)
        color_id_to_base_entity_appearance_entry: (
            BTBaseEntityAppearanceSettings1391ColorIdToBaseEntityAppearanceEntry | Unset
        )
        if isinstance(_color_id_to_base_entity_appearance_entry, Unset):
            color_id_to_base_entity_appearance_entry = UNSET
        else:
            color_id_to_base_entity_appearance_entry = (
                BTBaseEntityAppearanceSettings1391ColorIdToBaseEntityAppearanceEntry.from_dict(
                    _color_id_to_base_entity_appearance_entry
                )
            )

        is_noop = d.pop("isNoop", UNSET)

        bt_base_entity_appearance_settings_1391 = cls(
            bt_type=bt_type,
            color_id_to_base_entity_appearance_entry=color_id_to_base_entity_appearance_entry,
            is_noop=is_noop,
        )

        bt_base_entity_appearance_settings_1391.additional_properties = d
        return bt_base_entity_appearance_settings_1391

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
