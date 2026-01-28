from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BTPartMetadataInfoPropertySourceTypes")


@_attrs_define
class BTPartMetadataInfoPropertySourceTypes:
    """`0: AUTOMATIC` Set automatically, like a part name |
    `1: MERGED` Merged from another Part Studio | `2: FEATURE` Custom feature | `3: UNCONFIGURED` | `4: CONFIGURED` |
    `5: STANDARD_CONTENT` | `6: DEFAULT` Applied from metadata property configuration | `7: COMPUTED` Non-overridden,
    non-configured, computed property |
    `8: COMPUTED_CONFIGURED` Property is computed in this configuration; may also be configured in other configurations
    `9: IMPORT` Imported properties are handled separately

    """

    additional_properties: dict[str, int] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_part_metadata_info_property_source_types = cls()

        bt_part_metadata_info_property_source_types.additional_properties = d
        return bt_part_metadata_info_property_source_types

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
