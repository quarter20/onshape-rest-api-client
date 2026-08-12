from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_library_material_info_property_values import BTLibraryMaterialInfoPropertyValues


T = TypeVar("T", bound="BTLibraryMaterialInfo")


@_attrs_define
class BTLibraryMaterialInfo:
    """
    Attributes:
        category (str | Unset):
        display_name (str | Unset):
        id (str | Unset):
        property_values (BTLibraryMaterialInfoPropertyValues | Unset):
    """

    category: str | Unset = UNSET
    display_name: str | Unset = UNSET
    id: str | Unset = UNSET
    property_values: BTLibraryMaterialInfoPropertyValues | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        display_name = self.display_name

        id = self.id

        property_values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.property_values, Unset):
            property_values = self.property_values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if id is not UNSET:
            field_dict["id"] = id
        if property_values is not UNSET:
            field_dict["propertyValues"] = property_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_library_material_info_property_values import BTLibraryMaterialInfoPropertyValues

        d = dict(src_dict)
        category = d.pop("category", UNSET)

        display_name = d.pop("displayName", UNSET)

        id = d.pop("id", UNSET)

        _property_values = d.pop("propertyValues", UNSET)
        property_values: BTLibraryMaterialInfoPropertyValues | Unset
        if isinstance(_property_values, Unset):
            property_values = UNSET
        else:
            property_values = BTLibraryMaterialInfoPropertyValues.from_dict(_property_values)

        bt_library_material_info = cls(
            category=category,
            display_name=display_name,
            id=id,
            property_values=property_values,
        )

        bt_library_material_info.additional_properties = d
        return bt_library_material_info

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
