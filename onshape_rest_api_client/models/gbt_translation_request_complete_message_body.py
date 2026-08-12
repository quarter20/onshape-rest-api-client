from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GBTTranslationRequestCompleteMessageBody")


@_attrs_define
class GBTTranslationRequestCompleteMessageBody:
    """
    Attributes:
        app_element_session_id (str | Unset):
        data (str | Unset):
        document_id (str | Unset):
        event (str | Unset):
        message_id (str | Unset):
        timestamp (datetime.datetime | Unset):
        translation_id (str | Unset):
        user_id (str | Unset):
        webhook_id (str | Unset):
        workspace_id (str | Unset):
    """

    app_element_session_id: str | Unset = UNSET
    data: str | Unset = UNSET
    document_id: str | Unset = UNSET
    event: str | Unset = UNSET
    message_id: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    translation_id: str | Unset = UNSET
    user_id: str | Unset = UNSET
    webhook_id: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_element_session_id = self.app_element_session_id

        data = self.data

        document_id = self.document_id

        event = self.event

        message_id = self.message_id

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        translation_id = self.translation_id

        user_id = self.user_id

        webhook_id = self.webhook_id

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_element_session_id is not UNSET:
            field_dict["appElementSessionId"] = app_element_session_id
        if data is not UNSET:
            field_dict["data"] = data
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if event is not UNSET:
            field_dict["event"] = event
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if translation_id is not UNSET:
            field_dict["translationId"] = translation_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if webhook_id is not UNSET:
            field_dict["webhookId"] = webhook_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_element_session_id = d.pop("appElementSessionId", UNSET)

        data = d.pop("data", UNSET)

        document_id = d.pop("documentId", UNSET)

        event = d.pop("event", UNSET)

        message_id = d.pop("messageId", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = datetime.datetime.fromisoformat(_timestamp)

        translation_id = d.pop("translationId", UNSET)

        user_id = d.pop("userId", UNSET)

        webhook_id = d.pop("webhookId", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        gbt_translation_request_complete_message_body = cls(
            app_element_session_id=app_element_session_id,
            data=data,
            document_id=document_id,
            event=event,
            message_id=message_id,
            timestamp=timestamp,
            translation_id=translation_id,
            user_id=user_id,
            webhook_id=webhook_id,
            workspace_id=workspace_id,
        )

        gbt_translation_request_complete_message_body.additional_properties = d
        return gbt_translation_request_complete_message_body

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
