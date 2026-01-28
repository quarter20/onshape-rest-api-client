from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTWorkflowMessageBody")


@_attrs_define
class BTWorkflowMessageBody:
    """
    Attributes:
        app_element_session_id (str | Unset):
        data (str | Unset):
        event (str | Unset):
        message_id (str | Unset):
        object_id (str | Unset):
        object_type (str | Unset):
        timestamp (datetime.datetime | Unset):
        transition_name (str | Unset):
        webhook_id (str | Unset):
        workflow_id (str | Unset):
    """

    app_element_session_id: str | Unset = UNSET
    data: str | Unset = UNSET
    event: str | Unset = UNSET
    message_id: str | Unset = UNSET
    object_id: str | Unset = UNSET
    object_type: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    transition_name: str | Unset = UNSET
    webhook_id: str | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_element_session_id = self.app_element_session_id

        data = self.data

        event = self.event

        message_id = self.message_id

        object_id = self.object_id

        object_type = self.object_type

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        transition_name = self.transition_name

        webhook_id = self.webhook_id

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_element_session_id is not UNSET:
            field_dict["appElementSessionId"] = app_element_session_id
        if data is not UNSET:
            field_dict["data"] = data
        if event is not UNSET:
            field_dict["event"] = event
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if transition_name is not UNSET:
            field_dict["transitionName"] = transition_name
        if webhook_id is not UNSET:
            field_dict["webhookId"] = webhook_id
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_element_session_id = d.pop("appElementSessionId", UNSET)

        data = d.pop("data", UNSET)

        event = d.pop("event", UNSET)

        message_id = d.pop("messageId", UNSET)

        object_id = d.pop("objectId", UNSET)

        object_type = d.pop("objectType", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        transition_name = d.pop("transitionName", UNSET)

        webhook_id = d.pop("webhookId", UNSET)

        workflow_id = d.pop("workflowId", UNSET)

        bt_workflow_message_body = cls(
            app_element_session_id=app_element_session_id,
            data=data,
            event=event,
            message_id=message_id,
            object_id=object_id,
            object_type=object_type,
            timestamp=timestamp,
            transition_name=transition_name,
            webhook_id=webhook_id,
            workflow_id=workflow_id,
        )

        bt_workflow_message_body.additional_properties = d
        return bt_workflow_message_body

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
