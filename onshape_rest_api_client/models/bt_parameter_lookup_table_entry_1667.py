from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTParameterLookupTableEntry1667")


@_attrs_define
class BTParameterLookupTableEntry1667:
    """
    Attributes:
        additional_localized_strings (int | Unset):
        bt_type (str | Unset): Type of JSON object.
        label (str | Unset):
        localizable_name (str | Unset):
        localized_label (str | Unset):
        localized_name (str | Unset):
        strings_to_localize (list[str] | Unset):
    """

    additional_localized_strings: int | Unset = UNSET
    bt_type: str | Unset = UNSET
    label: str | Unset = UNSET
    localizable_name: str | Unset = UNSET
    localized_label: str | Unset = UNSET
    localized_name: str | Unset = UNSET
    strings_to_localize: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_localized_strings = self.additional_localized_strings

        bt_type = self.bt_type

        label = self.label

        localizable_name = self.localizable_name

        localized_label = self.localized_label

        localized_name = self.localized_name

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
        if label is not UNSET:
            field_dict["label"] = label
        if localizable_name is not UNSET:
            field_dict["localizableName"] = localizable_name
        if localized_label is not UNSET:
            field_dict["localizedLabel"] = localized_label
        if localized_name is not UNSET:
            field_dict["localizedName"] = localized_name
        if strings_to_localize is not UNSET:
            field_dict["stringsToLocalize"] = strings_to_localize

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        additional_localized_strings = d.pop("additionalLocalizedStrings", UNSET)

        bt_type = d.pop("btType", UNSET)

        label = d.pop("label", UNSET)

        localizable_name = d.pop("localizableName", UNSET)

        localized_label = d.pop("localizedLabel", UNSET)

        localized_name = d.pop("localizedName", UNSET)

        strings_to_localize = cast(list[str], d.pop("stringsToLocalize", UNSET))

        bt_parameter_lookup_table_entry_1667 = cls(
            additional_localized_strings=additional_localized_strings,
            bt_type=bt_type,
            label=label,
            localizable_name=localizable_name,
            localized_label=localized_label,
            localized_name=localized_name,
            strings_to_localize=strings_to_localize,
        )

        bt_parameter_lookup_table_entry_1667.additional_properties = d
        return bt_parameter_lookup_table_entry_1667

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
