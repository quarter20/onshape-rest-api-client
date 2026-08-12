from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTMaterialPropertyDefinitionInfo")


@_attrs_define
class BTMaterialPropertyDefinitionInfo:
    """
    Attributes:
        category (str | Unset):
        description (str | Unset):
        display_name (str | Unset):
        display_units (str | Unset):
        name (str | Unset):
        type_ (str | Unset):
        units (str | Unset):
        units_choices (list[str] | Unset):
    """

    category: str | Unset = UNSET
    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    display_units: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    units: str | Unset = UNSET
    units_choices: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        description = self.description

        display_name = self.display_name

        display_units = self.display_units

        name = self.name

        type_ = self.type_

        units = self.units

        units_choices: list[str] | Unset = UNSET
        if not isinstance(self.units_choices, Unset):
            units_choices = self.units_choices

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_units is not UNSET:
            field_dict["displayUnits"] = display_units
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if units is not UNSET:
            field_dict["units"] = units
        if units_choices is not UNSET:
            field_dict["unitsChoices"] = units_choices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_units = d.pop("displayUnits", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        units = d.pop("units", UNSET)

        units_choices = cast(list[str], d.pop("unitsChoices", UNSET))

        bt_material_property_definition_info = cls(
            category=category,
            description=description,
            display_name=display_name,
            display_units=display_units,
            name=name,
            type_=type_,
            units=units,
            units_choices=units_choices,
        )

        bt_material_property_definition_info.additional_properties = d
        return bt_material_property_definition_info

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
