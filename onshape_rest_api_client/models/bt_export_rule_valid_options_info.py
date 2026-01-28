from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_export_rule_hardcoded_property_info import BTExportRuleHardcodedPropertyInfo
    from ..models.bt_export_rule_valid_options_info_property_context_display_map import (
        BTExportRuleValidOptionsInfoPropertyContextDisplayMap,
    )


T = TypeVar("T", bound="BTExportRuleValidOptionsInfo")


@_attrs_define
class BTExportRuleValidOptionsInfo:
    """
    Attributes:
        convention_placeholder (str | Unset):
        hardcoded_properties (list[BTExportRuleHardcodedPropertyInfo] | Unset):
        property_context_display_map (BTExportRuleValidOptionsInfoPropertyContextDisplayMap | Unset):
        valid_object_types (list[int] | Unset):
    """

    convention_placeholder: str | Unset = UNSET
    hardcoded_properties: list[BTExportRuleHardcodedPropertyInfo] | Unset = UNSET
    property_context_display_map: BTExportRuleValidOptionsInfoPropertyContextDisplayMap | Unset = UNSET
    valid_object_types: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        convention_placeholder = self.convention_placeholder

        hardcoded_properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hardcoded_properties, Unset):
            hardcoded_properties = []
            for hardcoded_properties_item_data in self.hardcoded_properties:
                hardcoded_properties_item = hardcoded_properties_item_data.to_dict()
                hardcoded_properties.append(hardcoded_properties_item)

        property_context_display_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.property_context_display_map, Unset):
            property_context_display_map = self.property_context_display_map.to_dict()

        valid_object_types: list[int] | Unset = UNSET
        if not isinstance(self.valid_object_types, Unset):
            valid_object_types = self.valid_object_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if convention_placeholder is not UNSET:
            field_dict["conventionPlaceholder"] = convention_placeholder
        if hardcoded_properties is not UNSET:
            field_dict["hardcodedProperties"] = hardcoded_properties
        if property_context_display_map is not UNSET:
            field_dict["propertyContextDisplayMap"] = property_context_display_map
        if valid_object_types is not UNSET:
            field_dict["validObjectTypes"] = valid_object_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_export_rule_hardcoded_property_info import BTExportRuleHardcodedPropertyInfo
        from ..models.bt_export_rule_valid_options_info_property_context_display_map import (
            BTExportRuleValidOptionsInfoPropertyContextDisplayMap,
        )

        d = dict(src_dict)
        convention_placeholder = d.pop("conventionPlaceholder", UNSET)

        _hardcoded_properties = d.pop("hardcodedProperties", UNSET)
        hardcoded_properties: list[BTExportRuleHardcodedPropertyInfo] | Unset = UNSET
        if _hardcoded_properties is not UNSET:
            hardcoded_properties = []
            for hardcoded_properties_item_data in _hardcoded_properties:
                hardcoded_properties_item = BTExportRuleHardcodedPropertyInfo.from_dict(hardcoded_properties_item_data)

                hardcoded_properties.append(hardcoded_properties_item)

        _property_context_display_map = d.pop("propertyContextDisplayMap", UNSET)
        property_context_display_map: BTExportRuleValidOptionsInfoPropertyContextDisplayMap | Unset
        if isinstance(_property_context_display_map, Unset):
            property_context_display_map = UNSET
        else:
            property_context_display_map = BTExportRuleValidOptionsInfoPropertyContextDisplayMap.from_dict(
                _property_context_display_map
            )

        valid_object_types = cast(list[int], d.pop("validObjectTypes", UNSET))

        bt_export_rule_valid_options_info = cls(
            convention_placeholder=convention_placeholder,
            hardcoded_properties=hardcoded_properties,
            property_context_display_map=property_context_display_map,
            valid_object_types=valid_object_types,
        )

        bt_export_rule_valid_options_info.additional_properties = d
        return bt_export_rule_valid_options_info

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
