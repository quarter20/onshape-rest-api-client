from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_external_element_reference_info import BTExternalElementReferenceInfo
    from ..models.bt_library_material_info import BTLibraryMaterialInfo
    from ..models.bt_material_property_definition_info import BTMaterialPropertyDefinitionInfo


T = TypeVar("T", bound="BTMaterialLibraryInfo")


@_attrs_define
class BTMaterialLibraryInfo:
    """
    Attributes:
        description (str | Unset):
        display_name (str | Unset):
        external_element_reference (BTExternalElementReferenceInfo | Unset):
        materials (list[BTLibraryMaterialInfo] | Unset):
        name (str | Unset):
        property_definitions (list[BTMaterialPropertyDefinitionInfo] | Unset):
        versioned (bool | Unset):
    """

    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    external_element_reference: BTExternalElementReferenceInfo | Unset = UNSET
    materials: list[BTLibraryMaterialInfo] | Unset = UNSET
    name: str | Unset = UNSET
    property_definitions: list[BTMaterialPropertyDefinitionInfo] | Unset = UNSET
    versioned: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        display_name = self.display_name

        external_element_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_element_reference, Unset):
            external_element_reference = self.external_element_reference.to_dict()

        materials: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.materials, Unset):
            materials = []
            for materials_item_data in self.materials:
                materials_item = materials_item_data.to_dict()
                materials.append(materials_item)

        name = self.name

        property_definitions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.property_definitions, Unset):
            property_definitions = []
            for property_definitions_item_data in self.property_definitions:
                property_definitions_item = property_definitions_item_data.to_dict()
                property_definitions.append(property_definitions_item)

        versioned = self.versioned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if external_element_reference is not UNSET:
            field_dict["externalElementReference"] = external_element_reference
        if materials is not UNSET:
            field_dict["materials"] = materials
        if name is not UNSET:
            field_dict["name"] = name
        if property_definitions is not UNSET:
            field_dict["propertyDefinitions"] = property_definitions
        if versioned is not UNSET:
            field_dict["versioned"] = versioned

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_external_element_reference_info import BTExternalElementReferenceInfo
        from ..models.bt_library_material_info import BTLibraryMaterialInfo
        from ..models.bt_material_property_definition_info import BTMaterialPropertyDefinitionInfo

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        _external_element_reference = d.pop("externalElementReference", UNSET)
        external_element_reference: BTExternalElementReferenceInfo | Unset
        if isinstance(_external_element_reference, Unset):
            external_element_reference = UNSET
        else:
            external_element_reference = BTExternalElementReferenceInfo.from_dict(_external_element_reference)

        _materials = d.pop("materials", UNSET)
        materials: list[BTLibraryMaterialInfo] | Unset = UNSET
        if _materials is not UNSET:
            materials = []
            for materials_item_data in _materials:
                materials_item = BTLibraryMaterialInfo.from_dict(materials_item_data)

                materials.append(materials_item)

        name = d.pop("name", UNSET)

        _property_definitions = d.pop("propertyDefinitions", UNSET)
        property_definitions: list[BTMaterialPropertyDefinitionInfo] | Unset = UNSET
        if _property_definitions is not UNSET:
            property_definitions = []
            for property_definitions_item_data in _property_definitions:
                property_definitions_item = BTMaterialPropertyDefinitionInfo.from_dict(property_definitions_item_data)

                property_definitions.append(property_definitions_item)

        versioned = d.pop("versioned", UNSET)

        bt_material_library_info = cls(
            description=description,
            display_name=display_name,
            external_element_reference=external_element_reference,
            materials=materials,
            name=name,
            property_definitions=property_definitions,
            versioned=versioned,
        )

        bt_material_library_info.additional_properties = d
        return bt_material_library_info

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
