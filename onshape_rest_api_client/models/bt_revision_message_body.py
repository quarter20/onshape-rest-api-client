from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTRevisionMessageBody")


@_attrs_define
class BTRevisionMessageBody:
    """
    Attributes:
        app_element_session_id (str | Unset):
        comment_id (str | Unset):
        data (str | Unset):
        document_id (str | Unset):
        document_state (str | Unset):
        document_type (int | Unset):
        element_id (str | Unset):
        entry_id (str | Unset):
        entry_type (str | Unset):
        event (str | Unset):
        message_id (str | Unset):
        metadata_object_type (str | Unset):
        new_permission_set (list[str] | Unset):
        old_permission_set (list[str] | Unset):
        part_id (str | Unset):
        part_identity (str | Unset):
        part_number (str | Unset):
        resource_type (str | Unset):
        share_action (str | Unset):
        timestamp (datetime.datetime | Unset):
        translation_id (str | Unset):
        user_id (str | Unset):
        version_id (str | Unset):
        webhook_id (str | Unset):
        workspace_id (str | Unset):
        element_type (int | Unset):
        is_from_initial_state (bool | Unset):
        is_to_terminal_state (bool | Unset):
        release_id (str | Unset):
        status (str | Unset):
        transition_name (str | Unset):
        revision_id (str | Unset):
    """

    app_element_session_id: str | Unset = UNSET
    comment_id: str | Unset = UNSET
    data: str | Unset = UNSET
    document_id: str | Unset = UNSET
    document_state: str | Unset = UNSET
    document_type: int | Unset = UNSET
    element_id: str | Unset = UNSET
    entry_id: str | Unset = UNSET
    entry_type: str | Unset = UNSET
    event: str | Unset = UNSET
    message_id: str | Unset = UNSET
    metadata_object_type: str | Unset = UNSET
    new_permission_set: list[str] | Unset = UNSET
    old_permission_set: list[str] | Unset = UNSET
    part_id: str | Unset = UNSET
    part_identity: str | Unset = UNSET
    part_number: str | Unset = UNSET
    resource_type: str | Unset = UNSET
    share_action: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    translation_id: str | Unset = UNSET
    user_id: str | Unset = UNSET
    version_id: str | Unset = UNSET
    webhook_id: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    element_type: int | Unset = UNSET
    is_from_initial_state: bool | Unset = UNSET
    is_to_terminal_state: bool | Unset = UNSET
    release_id: str | Unset = UNSET
    status: str | Unset = UNSET
    transition_name: str | Unset = UNSET
    revision_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_element_session_id = self.app_element_session_id

        comment_id = self.comment_id

        data = self.data

        document_id = self.document_id

        document_state = self.document_state

        document_type = self.document_type

        element_id = self.element_id

        entry_id = self.entry_id

        entry_type = self.entry_type

        event = self.event

        message_id = self.message_id

        metadata_object_type = self.metadata_object_type

        new_permission_set: list[str] | Unset = UNSET
        if not isinstance(self.new_permission_set, Unset):
            new_permission_set = self.new_permission_set

        old_permission_set: list[str] | Unset = UNSET
        if not isinstance(self.old_permission_set, Unset):
            old_permission_set = self.old_permission_set

        part_id = self.part_id

        part_identity = self.part_identity

        part_number = self.part_number

        resource_type = self.resource_type

        share_action = self.share_action

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        translation_id = self.translation_id

        user_id = self.user_id

        version_id = self.version_id

        webhook_id = self.webhook_id

        workspace_id = self.workspace_id

        element_type = self.element_type

        is_from_initial_state = self.is_from_initial_state

        is_to_terminal_state = self.is_to_terminal_state

        release_id = self.release_id

        status = self.status

        transition_name = self.transition_name

        revision_id = self.revision_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_element_session_id is not UNSET:
            field_dict["appElementSessionId"] = app_element_session_id
        if comment_id is not UNSET:
            field_dict["commentId"] = comment_id
        if data is not UNSET:
            field_dict["data"] = data
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if document_state is not UNSET:
            field_dict["documentState"] = document_state
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if entry_id is not UNSET:
            field_dict["entryId"] = entry_id
        if entry_type is not UNSET:
            field_dict["entryType"] = entry_type
        if event is not UNSET:
            field_dict["event"] = event
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if metadata_object_type is not UNSET:
            field_dict["metadataObjectType"] = metadata_object_type
        if new_permission_set is not UNSET:
            field_dict["newPermissionSet"] = new_permission_set
        if old_permission_set is not UNSET:
            field_dict["oldPermissionSet"] = old_permission_set
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_identity is not UNSET:
            field_dict["partIdentity"] = part_identity
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if share_action is not UNSET:
            field_dict["shareAction"] = share_action
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if translation_id is not UNSET:
            field_dict["translationId"] = translation_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if webhook_id is not UNSET:
            field_dict["webhookId"] = webhook_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if element_type is not UNSET:
            field_dict["elementType"] = element_type
        if is_from_initial_state is not UNSET:
            field_dict["isFromInitialState"] = is_from_initial_state
        if is_to_terminal_state is not UNSET:
            field_dict["isToTerminalState"] = is_to_terminal_state
        if release_id is not UNSET:
            field_dict["releaseId"] = release_id
        if status is not UNSET:
            field_dict["status"] = status
        if transition_name is not UNSET:
            field_dict["transitionName"] = transition_name
        if revision_id is not UNSET:
            field_dict["revisionId"] = revision_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_element_session_id = d.pop("appElementSessionId", UNSET)

        comment_id = d.pop("commentId", UNSET)

        data = d.pop("data", UNSET)

        document_id = d.pop("documentId", UNSET)

        document_state = d.pop("documentState", UNSET)

        document_type = d.pop("documentType", UNSET)

        element_id = d.pop("elementId", UNSET)

        entry_id = d.pop("entryId", UNSET)

        entry_type = d.pop("entryType", UNSET)

        event = d.pop("event", UNSET)

        message_id = d.pop("messageId", UNSET)

        metadata_object_type = d.pop("metadataObjectType", UNSET)

        new_permission_set = cast(list[str], d.pop("newPermissionSet", UNSET))

        old_permission_set = cast(list[str], d.pop("oldPermissionSet", UNSET))

        part_id = d.pop("partId", UNSET)

        part_identity = d.pop("partIdentity", UNSET)

        part_number = d.pop("partNumber", UNSET)

        resource_type = d.pop("resourceType", UNSET)

        share_action = d.pop("shareAction", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        translation_id = d.pop("translationId", UNSET)

        user_id = d.pop("userId", UNSET)

        version_id = d.pop("versionId", UNSET)

        webhook_id = d.pop("webhookId", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        element_type = d.pop("elementType", UNSET)

        is_from_initial_state = d.pop("isFromInitialState", UNSET)

        is_to_terminal_state = d.pop("isToTerminalState", UNSET)

        release_id = d.pop("releaseId", UNSET)

        status = d.pop("status", UNSET)

        transition_name = d.pop("transitionName", UNSET)

        revision_id = d.pop("revisionId", UNSET)

        bt_revision_message_body = cls(
            app_element_session_id=app_element_session_id,
            comment_id=comment_id,
            data=data,
            document_id=document_id,
            document_state=document_state,
            document_type=document_type,
            element_id=element_id,
            entry_id=entry_id,
            entry_type=entry_type,
            event=event,
            message_id=message_id,
            metadata_object_type=metadata_object_type,
            new_permission_set=new_permission_set,
            old_permission_set=old_permission_set,
            part_id=part_id,
            part_identity=part_identity,
            part_number=part_number,
            resource_type=resource_type,
            share_action=share_action,
            timestamp=timestamp,
            translation_id=translation_id,
            user_id=user_id,
            version_id=version_id,
            webhook_id=webhook_id,
            workspace_id=workspace_id,
            element_type=element_type,
            is_from_initial_state=is_from_initial_state,
            is_to_terminal_state=is_to_terminal_state,
            release_id=release_id,
            status=status,
            transition_name=transition_name,
            revision_id=revision_id,
        )

        bt_revision_message_body.additional_properties = d
        return bt_revision_message_body

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
