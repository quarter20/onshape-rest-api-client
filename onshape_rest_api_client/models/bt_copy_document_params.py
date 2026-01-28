from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTCopyDocumentParams")


@_attrs_define
class BTCopyDocumentParams:
    """Options for the new copied document.

    Attributes:
        is_public (bool | Unset): `true` to make the new document public.
        new_name (str | Unset): Name for the new document.
        owner_id (str | Unset): Owner of the new document. Can be a [user ID](#/User/sessionInfo) or [company
            ID](#/Company/findCompany), depending on `ownerTypeIndex`.
        owner_type_index (int | Unset): Type of owner. `0: User, 1: Company`
        parent_id (str | Unset): Optionally add the new document to the specified folder. Provide the folder ID as the
            parent ID.
        project_id (str | Unset): Optionally add the new document to the specified project.
        repoint_app_element_version_refs (bool | Unset): `true` to re-point version references in application elements
            to the initial version in the new document.
    """

    is_public: bool | Unset = UNSET
    new_name: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type_index: int | Unset = UNSET
    parent_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    repoint_app_element_version_refs: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_public = self.is_public

        new_name = self.new_name

        owner_id = self.owner_id

        owner_type_index = self.owner_type_index

        parent_id = self.parent_id

        project_id = self.project_id

        repoint_app_element_version_refs = self.repoint_app_element_version_refs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if new_name is not UNSET:
            field_dict["newName"] = new_name
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if owner_type_index is not UNSET:
            field_dict["ownerTypeIndex"] = owner_type_index
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if repoint_app_element_version_refs is not UNSET:
            field_dict["repointAppElementVersionRefs"] = repoint_app_element_version_refs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_public = d.pop("isPublic", UNSET)

        new_name = d.pop("newName", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        owner_type_index = d.pop("ownerTypeIndex", UNSET)

        parent_id = d.pop("parentId", UNSET)

        project_id = d.pop("projectId", UNSET)

        repoint_app_element_version_refs = d.pop("repointAppElementVersionRefs", UNSET)

        bt_copy_document_params = cls(
            is_public=is_public,
            new_name=new_name,
            owner_id=owner_id,
            owner_type_index=owner_type_index,
            parent_id=parent_id,
            project_id=project_id,
            repoint_app_element_version_refs=repoint_app_element_version_refs,
        )

        bt_copy_document_params.additional_properties = d
        return bt_copy_document_params

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
