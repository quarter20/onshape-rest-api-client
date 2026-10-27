from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BTStdVersionReplaceInfoElementIdToReplacementCount")


@_attrs_define
class BTStdVersionReplaceInfoElementIdToReplacementCount:
    """Map from the element ID of each modified Feature Studio to the number of import versions replaced in it. Feature
    Studios with no replacements are omitted.

    """

    additional_properties: dict[str, int] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_std_version_replace_info_element_id_to_replacement_count = cls()

        bt_std_version_replace_info_element_id_to_replacement_count.additional_properties = d
        return bt_std_version_replace_info_element_id_to_replacement_count

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> int:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
