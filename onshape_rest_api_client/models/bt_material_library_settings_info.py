from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_material_library_metadata_info import BTMaterialLibraryMetadataInfo


T = TypeVar("T", bound="BTMaterialLibrarySettingsInfo")


@_attrs_define
class BTMaterialLibrarySettingsInfo:
    """
    Attributes:
        company_libraries (list[BTMaterialLibraryMetadataInfo] | Unset):
        libraries (list[BTMaterialLibraryMetadataInfo] | Unset):
    """

    company_libraries: list[BTMaterialLibraryMetadataInfo] | Unset = UNSET
    libraries: list[BTMaterialLibraryMetadataInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_libraries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.company_libraries, Unset):
            company_libraries = []
            for company_libraries_item_data in self.company_libraries:
                company_libraries_item = company_libraries_item_data.to_dict()
                company_libraries.append(company_libraries_item)

        libraries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.libraries, Unset):
            libraries = []
            for libraries_item_data in self.libraries:
                libraries_item = libraries_item_data.to_dict()
                libraries.append(libraries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_libraries is not UNSET:
            field_dict["companyLibraries"] = company_libraries
        if libraries is not UNSET:
            field_dict["libraries"] = libraries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_material_library_metadata_info import BTMaterialLibraryMetadataInfo

        d = dict(src_dict)
        _company_libraries = d.pop("companyLibraries", UNSET)
        company_libraries: list[BTMaterialLibraryMetadataInfo] | Unset = UNSET
        if _company_libraries is not UNSET:
            company_libraries = []
            for company_libraries_item_data in _company_libraries:
                company_libraries_item = BTMaterialLibraryMetadataInfo.from_dict(company_libraries_item_data)

                company_libraries.append(company_libraries_item)

        _libraries = d.pop("libraries", UNSET)
        libraries: list[BTMaterialLibraryMetadataInfo] | Unset = UNSET
        if _libraries is not UNSET:
            libraries = []
            for libraries_item_data in _libraries:
                libraries_item = BTMaterialLibraryMetadataInfo.from_dict(libraries_item_data)

                libraries.append(libraries_item)

        bt_material_library_settings_info = cls(
            company_libraries=company_libraries,
            libraries=libraries,
        )

        bt_material_library_settings_info.additional_properties = d
        return bt_material_library_settings_info

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
