from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTReleaseItemErrorInfo")


@_attrs_define
class BTReleaseItemErrorInfo:
    """
    Attributes:
        change_task_id (str | Unset):
        document_id (str | Unset):
        message (str | Unset):
        ordinal (int | Unset):
        pending_task_id (str | Unset):
        pending_task_object_id (str | Unset):
        pending_task_type (str | Unset):
        reject_allowed (bool | Unset):
        release_id (str | Unset):
        severity (int | Unset):
        version_id (str | Unset):
        workspace_id (str | Unset):
    """

    change_task_id: str | Unset = UNSET
    document_id: str | Unset = UNSET
    message: str | Unset = UNSET
    ordinal: int | Unset = UNSET
    pending_task_id: str | Unset = UNSET
    pending_task_object_id: str | Unset = UNSET
    pending_task_type: str | Unset = UNSET
    reject_allowed: bool | Unset = UNSET
    release_id: str | Unset = UNSET
    severity: int | Unset = UNSET
    version_id: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change_task_id = self.change_task_id

        document_id = self.document_id

        message = self.message

        ordinal = self.ordinal

        pending_task_id = self.pending_task_id

        pending_task_object_id = self.pending_task_object_id

        pending_task_type = self.pending_task_type

        reject_allowed = self.reject_allowed

        release_id = self.release_id

        severity = self.severity

        version_id = self.version_id

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if change_task_id is not UNSET:
            field_dict["changeTaskId"] = change_task_id
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if message is not UNSET:
            field_dict["message"] = message
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if pending_task_id is not UNSET:
            field_dict["pendingTaskId"] = pending_task_id
        if pending_task_object_id is not UNSET:
            field_dict["pendingTaskObjectId"] = pending_task_object_id
        if pending_task_type is not UNSET:
            field_dict["pendingTaskType"] = pending_task_type
        if reject_allowed is not UNSET:
            field_dict["rejectAllowed"] = reject_allowed
        if release_id is not UNSET:
            field_dict["releaseId"] = release_id
        if severity is not UNSET:
            field_dict["severity"] = severity
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        change_task_id = d.pop("changeTaskId", UNSET)

        document_id = d.pop("documentId", UNSET)

        message = d.pop("message", UNSET)

        ordinal = d.pop("ordinal", UNSET)

        pending_task_id = d.pop("pendingTaskId", UNSET)

        pending_task_object_id = d.pop("pendingTaskObjectId", UNSET)

        pending_task_type = d.pop("pendingTaskType", UNSET)

        reject_allowed = d.pop("rejectAllowed", UNSET)

        release_id = d.pop("releaseId", UNSET)

        severity = d.pop("severity", UNSET)

        version_id = d.pop("versionId", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_release_item_error_info = cls(
            change_task_id=change_task_id,
            document_id=document_id,
            message=message,
            ordinal=ordinal,
            pending_task_id=pending_task_id,
            pending_task_object_id=pending_task_object_id,
            pending_task_type=pending_task_type,
            reject_allowed=reject_allowed,
            release_id=release_id,
            severity=severity,
            version_id=version_id,
            workspace_id=workspace_id,
        )

        bt_release_item_error_info.additional_properties = d
        return bt_release_item_error_info

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
