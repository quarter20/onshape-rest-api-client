from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTPartMaterialPropertyInfo")


@_attrs_define
class BTPartMaterialPropertyInfo:
    """
    Attributes:
        category (str | Unset):
        description (str | Unset):
        display_name (str | Unset):
        name (str | Unset):
        type_ (str | Unset):
        units (str | Unset):
        value (str | Unset):
    """

    category: str | Unset = UNSET
    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    units: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        description = self.description

        display_name = self.display_name

        name = self.name

        type_ = self.type_

        units = self.units

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if units is not UNSET:
            field_dict["units"] = units
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        units = d.pop("units", UNSET)

        value = d.pop("value", UNSET)

        bt_part_material_property_info = cls(
            category=category,
            description=description,
            display_name=display_name,
            name=name,
            type_=type_,
            units=units,
            value=value,
        )

        bt_part_material_property_info.additional_properties = d
        return bt_part_material_property_info

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
