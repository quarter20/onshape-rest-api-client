from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_share_entry_params import BTShareEntryParams


T = TypeVar("T", bound="BTShareParams")


@_attrs_define
class BTShareParams:
    """
    Attributes:
        connection_id (str | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        encoded_configuration (str | Unset):
        entries (list[BTShareEntryParams] | Unset):
        folder_id (str | Unset):
        message (str | Unset):
        permission (int | Unset):
        permission_set (list[str] | Unset):
        update (bool | Unset):
        workspace_id (str | Unset):
    """

    connection_id: str | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    encoded_configuration: str | Unset = UNSET
    entries: list[BTShareEntryParams] | Unset = UNSET
    folder_id: str | Unset = UNSET
    message: str | Unset = UNSET
    permission: int | Unset = UNSET
    permission_set: list[str] | Unset = UNSET
    update: bool | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connection_id = self.connection_id

        document_id = self.document_id

        element_id = self.element_id

        encoded_configuration = self.encoded_configuration

        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        folder_id = self.folder_id

        message = self.message

        permission = self.permission

        permission_set: list[str] | Unset = UNSET
        if not isinstance(self.permission_set, Unset):
            permission_set = self.permission_set

        update = self.update

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if encoded_configuration is not UNSET:
            field_dict["encodedConfiguration"] = encoded_configuration
        if entries is not UNSET:
            field_dict["entries"] = entries
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if message is not UNSET:
            field_dict["message"] = message
        if permission is not UNSET:
            field_dict["permission"] = permission
        if permission_set is not UNSET:
            field_dict["permissionSet"] = permission_set
        if update is not UNSET:
            field_dict["update"] = update
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_share_entry_params import BTShareEntryParams

        d = dict(src_dict)
        connection_id = d.pop("connectionId", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        encoded_configuration = d.pop("encodedConfiguration", UNSET)

        _entries = d.pop("entries", UNSET)
        entries: list[BTShareEntryParams] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = BTShareEntryParams.from_dict(entries_item_data)

                entries.append(entries_item)

        folder_id = d.pop("folderId", UNSET)

        message = d.pop("message", UNSET)

        permission = d.pop("permission", UNSET)

        permission_set = cast(list[str], d.pop("permissionSet", UNSET))

        update = d.pop("update", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_share_params = cls(
            connection_id=connection_id,
            document_id=document_id,
            element_id=element_id,
            encoded_configuration=encoded_configuration,
            entries=entries,
            folder_id=folder_id,
            message=message,
            permission=permission,
            permission_set=permission_set,
            update=update,
            workspace_id=workspace_id,
        )

        bt_share_params.additional_properties = d
        return bt_share_params

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
