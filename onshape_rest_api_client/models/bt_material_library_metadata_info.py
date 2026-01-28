from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTMaterialLibraryMetadataInfo")


@_attrs_define
class BTMaterialLibraryMetadataInfo:
    """
    Attributes:
        document_id (str | Unset):
        document_name (str | Unset):
        element_id (str | Unset):
        is_public (bool | Unset):
        library_name (str | Unset):
        owner_name (str | Unset):
        version_id (str | Unset):
        workspace_id (str | Unset):
    """

    document_id: str | Unset = UNSET
    document_name: str | Unset = UNSET
    element_id: str | Unset = UNSET
    is_public: bool | Unset = UNSET
    library_name: str | Unset = UNSET
    owner_name: str | Unset = UNSET
    version_id: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        document_name = self.document_name

        element_id = self.element_id

        is_public = self.is_public

        library_name = self.library_name

        owner_name = self.owner_name

        version_id = self.version_id

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if document_name is not UNSET:
            field_dict["documentName"] = document_name
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if library_name is not UNSET:
            field_dict["libraryName"] = library_name
        if owner_name is not UNSET:
            field_dict["ownerName"] = owner_name
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_id = d.pop("documentId", UNSET)

        document_name = d.pop("documentName", UNSET)

        element_id = d.pop("elementId", UNSET)

        is_public = d.pop("isPublic", UNSET)

        library_name = d.pop("libraryName", UNSET)

        owner_name = d.pop("ownerName", UNSET)

        version_id = d.pop("versionId", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_material_library_metadata_info = cls(
            document_id=document_id,
            document_name=document_name,
            element_id=element_id,
            is_public=is_public,
            library_name=library_name,
            owner_name=owner_name,
            version_id=version_id,
            workspace_id=workspace_id,
        )

        bt_material_library_metadata_info.additional_properties = d
        return bt_material_library_metadata_info

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
