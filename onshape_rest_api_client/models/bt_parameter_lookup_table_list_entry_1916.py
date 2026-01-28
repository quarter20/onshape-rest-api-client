from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_parameter_lookup_table_entry_1667 import BTParameterLookupTableEntry1667


T = TypeVar("T", bound="BTParameterLookupTableListEntry1916")


@_attrs_define
class BTParameterLookupTableListEntry1916:
    """
    Attributes:
        additional_localized_strings (int | Unset):
        bt_type (str | Unset): Type of JSON object.
        default_index (int | Unset):
        display_name (str | Unset):
        entries (list[BTParameterLookupTableEntry1667] | Unset):
        label (str | Unset):
        localizable_name (str | Unset):
        localized_label (str | Unset):
        localized_name (str | Unset):
        name (str | Unset):
        strings_to_localize (list[str] | Unset):
    """

    additional_localized_strings: int | Unset = UNSET
    bt_type: str | Unset = UNSET
    default_index: int | Unset = UNSET
    display_name: str | Unset = UNSET
    entries: list[BTParameterLookupTableEntry1667] | Unset = UNSET
    label: str | Unset = UNSET
    localizable_name: str | Unset = UNSET
    localized_label: str | Unset = UNSET
    localized_name: str | Unset = UNSET
    name: str | Unset = UNSET
    strings_to_localize: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_localized_strings = self.additional_localized_strings

        bt_type = self.bt_type

        default_index = self.default_index

        display_name = self.display_name

        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        label = self.label

        localizable_name = self.localizable_name

        localized_label = self.localized_label

        localized_name = self.localized_name

        name = self.name

        strings_to_localize: list[str] | Unset = UNSET
        if not isinstance(self.strings_to_localize, Unset):
            strings_to_localize = self.strings_to_localize

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_localized_strings is not UNSET:
            field_dict["additionalLocalizedStrings"] = additional_localized_strings
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if default_index is not UNSET:
            field_dict["defaultIndex"] = default_index
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if entries is not UNSET:
            field_dict["entries"] = entries
        if label is not UNSET:
            field_dict["label"] = label
        if localizable_name is not UNSET:
            field_dict["localizableName"] = localizable_name
        if localized_label is not UNSET:
            field_dict["localizedLabel"] = localized_label
        if localized_name is not UNSET:
            field_dict["localizedName"] = localized_name
        if name is not UNSET:
            field_dict["name"] = name
        if strings_to_localize is not UNSET:
            field_dict["stringsToLocalize"] = strings_to_localize

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_parameter_lookup_table_entry_1667 import BTParameterLookupTableEntry1667

        d = dict(src_dict)
        additional_localized_strings = d.pop("additionalLocalizedStrings", UNSET)

        bt_type = d.pop("btType", UNSET)

        default_index = d.pop("defaultIndex", UNSET)

        display_name = d.pop("displayName", UNSET)

        _entries = d.pop("entries", UNSET)
        entries: list[BTParameterLookupTableEntry1667] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = BTParameterLookupTableEntry1667.from_dict(entries_item_data)

                entries.append(entries_item)

        label = d.pop("label", UNSET)

        localizable_name = d.pop("localizableName", UNSET)

        localized_label = d.pop("localizedLabel", UNSET)

        localized_name = d.pop("localizedName", UNSET)

        name = d.pop("name", UNSET)

        strings_to_localize = cast(list[str], d.pop("stringsToLocalize", UNSET))

        bt_parameter_lookup_table_list_entry_1916 = cls(
            additional_localized_strings=additional_localized_strings,
            bt_type=bt_type,
            default_index=default_index,
            display_name=display_name,
            entries=entries,
            label=label,
            localizable_name=localizable_name,
            localized_label=localized_label,
            localized_name=localized_name,
            name=name,
            strings_to_localize=strings_to_localize,
        )

        bt_parameter_lookup_table_list_entry_1916.additional_properties = d
        return bt_parameter_lookup_table_list_entry_1916

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
