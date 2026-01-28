from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_owner_info import BTOwnerInfo


T = TypeVar("T", bound="BTCopyDocumentInfo")


@_attrs_define
class BTCopyDocumentInfo:
    """
    Attributes:
        new_document_id (str | Unset):
        new_document_name (str | Unset):
        new_owner (BTOwnerInfo | Unset):
        new_parent_id (str | Unset):
        new_project_id (str | Unset):
        new_workspace_id (str | Unset):
    """

    new_document_id: str | Unset = UNSET
    new_document_name: str | Unset = UNSET
    new_owner: BTOwnerInfo | Unset = UNSET
    new_parent_id: str | Unset = UNSET
    new_project_id: str | Unset = UNSET
    new_workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_document_id = self.new_document_id

        new_document_name = self.new_document_name

        new_owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new_owner, Unset):
            new_owner = self.new_owner.to_dict()

        new_parent_id = self.new_parent_id

        new_project_id = self.new_project_id

        new_workspace_id = self.new_workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_document_id is not UNSET:
            field_dict["newDocumentId"] = new_document_id
        if new_document_name is not UNSET:
            field_dict["newDocumentName"] = new_document_name
        if new_owner is not UNSET:
            field_dict["newOwner"] = new_owner
        if new_parent_id is not UNSET:
            field_dict["newParentId"] = new_parent_id
        if new_project_id is not UNSET:
            field_dict["newProjectId"] = new_project_id
        if new_workspace_id is not UNSET:
            field_dict["newWorkspaceId"] = new_workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_owner_info import BTOwnerInfo

        d = dict(src_dict)
        new_document_id = d.pop("newDocumentId", UNSET)

        new_document_name = d.pop("newDocumentName", UNSET)

        _new_owner = d.pop("newOwner", UNSET)
        new_owner: BTOwnerInfo | Unset
        if isinstance(_new_owner, Unset):
            new_owner = UNSET
        else:
            new_owner = BTOwnerInfo.from_dict(_new_owner)

        new_parent_id = d.pop("newParentId", UNSET)

        new_project_id = d.pop("newProjectId", UNSET)

        new_workspace_id = d.pop("newWorkspaceId", UNSET)

        bt_copy_document_info = cls(
            new_document_id=new_document_id,
            new_document_name=new_document_name,
            new_owner=new_owner,
            new_parent_id=new_parent_id,
            new_project_id=new_project_id,
            new_workspace_id=new_workspace_id,
        )

        bt_copy_document_info.additional_properties = d
        return bt_copy_document_info

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
