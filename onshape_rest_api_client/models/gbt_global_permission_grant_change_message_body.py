from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GBTGlobalPermissionGrantChangeMessageBody")


@_attrs_define
class GBTGlobalPermissionGrantChangeMessageBody:
    """
    Attributes:
        app_element_session_id (str | Unset):
        company_id (str | Unset):
        data (str | Unset):
        event (str | Unset):
        global_permission (int | Unset):
        identity_id (str | Unset):
        identity_type (int | Unset):
        is_granted (bool | Unset):
        message_id (str | Unset):
        timestamp (datetime.datetime | Unset):
        user_id (str | Unset):
        webhook_id (str | Unset):
    """

    app_element_session_id: str | Unset = UNSET
    company_id: str | Unset = UNSET
    data: str | Unset = UNSET
    event: str | Unset = UNSET
    global_permission: int | Unset = UNSET
    identity_id: str | Unset = UNSET
    identity_type: int | Unset = UNSET
    is_granted: bool | Unset = UNSET
    message_id: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    user_id: str | Unset = UNSET
    webhook_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_element_session_id = self.app_element_session_id

        company_id = self.company_id

        data = self.data

        event = self.event

        global_permission = self.global_permission

        identity_id = self.identity_id

        identity_type = self.identity_type

        is_granted = self.is_granted

        message_id = self.message_id

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        user_id = self.user_id

        webhook_id = self.webhook_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_element_session_id is not UNSET:
            field_dict["appElementSessionId"] = app_element_session_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if data is not UNSET:
            field_dict["data"] = data
        if event is not UNSET:
            field_dict["event"] = event
        if global_permission is not UNSET:
            field_dict["globalPermission"] = global_permission
        if identity_id is not UNSET:
            field_dict["identityId"] = identity_id
        if identity_type is not UNSET:
            field_dict["identityType"] = identity_type
        if is_granted is not UNSET:
            field_dict["isGranted"] = is_granted
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if webhook_id is not UNSET:
            field_dict["webhookId"] = webhook_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_element_session_id = d.pop("appElementSessionId", UNSET)

        company_id = d.pop("companyId", UNSET)

        data = d.pop("data", UNSET)

        event = d.pop("event", UNSET)

        global_permission = d.pop("globalPermission", UNSET)

        identity_id = d.pop("identityId", UNSET)

        identity_type = d.pop("identityType", UNSET)

        is_granted = d.pop("isGranted", UNSET)

        message_id = d.pop("messageId", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = datetime.datetime.fromisoformat(_timestamp)

        user_id = d.pop("userId", UNSET)

        webhook_id = d.pop("webhookId", UNSET)

        gbt_global_permission_grant_change_message_body = cls(
            app_element_session_id=app_element_session_id,
            company_id=company_id,
            data=data,
            event=event,
            global_permission=global_permission,
            identity_id=identity_id,
            identity_type=identity_type,
            is_granted=is_granted,
            message_id=message_id,
            timestamp=timestamp,
            user_id=user_id,
            webhook_id=webhook_id,
        )

        gbt_global_permission_grant_change_message_body.additional_properties = d
        return gbt_global_permission_grant_change_message_body

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
