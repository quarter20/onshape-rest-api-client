from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_external_element_reference_info import BTExternalElementReferenceInfo
    from ..models.bt_part_material_property_info import BTPartMaterialPropertyInfo


T = TypeVar("T", bound="BTPartMaterialInfo")


@_attrs_define
class BTPartMaterialInfo:
    """
    Attributes:
        display_name (str | Unset):
        id (str | Unset):
        library_name (str | Unset):
        library_reference (BTExternalElementReferenceInfo | Unset):
        properties (list[BTPartMaterialPropertyInfo] | Unset):
    """

    display_name: str | Unset = UNSET
    id: str | Unset = UNSET
    library_name: str | Unset = UNSET
    library_reference: BTExternalElementReferenceInfo | Unset = UNSET
    properties: list[BTPartMaterialPropertyInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        id = self.id

        library_name = self.library_name

        library_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.library_reference, Unset):
            library_reference = self.library_reference.to_dict()

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if id is not UNSET:
            field_dict["id"] = id
        if library_name is not UNSET:
            field_dict["libraryName"] = library_name
        if library_reference is not UNSET:
            field_dict["libraryReference"] = library_reference
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_external_element_reference_info import BTExternalElementReferenceInfo
        from ..models.bt_part_material_property_info import BTPartMaterialPropertyInfo

        d = dict(src_dict)
        display_name = d.pop("displayName", UNSET)

        id = d.pop("id", UNSET)

        library_name = d.pop("libraryName", UNSET)

        _library_reference = d.pop("libraryReference", UNSET)
        library_reference: BTExternalElementReferenceInfo | Unset
        if isinstance(_library_reference, Unset):
            library_reference = UNSET
        else:
            library_reference = BTExternalElementReferenceInfo.from_dict(_library_reference)

        _properties = d.pop("properties", UNSET)
        properties: list[BTPartMaterialPropertyInfo] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = BTPartMaterialPropertyInfo.from_dict(properties_item_data)

                properties.append(properties_item)

        bt_part_material_info = cls(
            display_name=display_name,
            id=id,
            library_name=library_name,
            library_reference=library_reference,
            properties=properties,
        )

        bt_part_material_info.additional_properties = d
        return bt_part_material_info

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
