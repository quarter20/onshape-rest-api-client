from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.bt_application_settings_type import BTApplicationSettingsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTUserAppMessageBody")


@_attrs_define
class BTUserAppMessageBody:
    """
    Attributes:
        app_element_session_id (str | Unset):
        client_id (str | Unset):
        data (str | Unset):
        event (str | Unset):
        identity_id (str | Unset):
        message_id (str | Unset):
        setting_type (BTApplicationSettingsType | Unset):
        timestamp (datetime.datetime | Unset):
        webhook_id (str | Unset):
    """

    app_element_session_id: str | Unset = UNSET
    client_id: str | Unset = UNSET
    data: str | Unset = UNSET
    event: str | Unset = UNSET
    identity_id: str | Unset = UNSET
    message_id: str | Unset = UNSET
    setting_type: BTApplicationSettingsType | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    webhook_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_element_session_id = self.app_element_session_id

        client_id = self.client_id

        data = self.data

        event = self.event

        identity_id = self.identity_id

        message_id = self.message_id

        setting_type: str | Unset = UNSET
        if not isinstance(self.setting_type, Unset):
            setting_type = self.setting_type.value

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        webhook_id = self.webhook_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_element_session_id is not UNSET:
            field_dict["appElementSessionId"] = app_element_session_id
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if data is not UNSET:
            field_dict["data"] = data
        if event is not UNSET:
            field_dict["event"] = event
        if identity_id is not UNSET:
            field_dict["identityId"] = identity_id
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if setting_type is not UNSET:
            field_dict["settingType"] = setting_type
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if webhook_id is not UNSET:
            field_dict["webhookId"] = webhook_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_element_session_id = d.pop("appElementSessionId", UNSET)

        client_id = d.pop("clientId", UNSET)

        data = d.pop("data", UNSET)

        event = d.pop("event", UNSET)

        identity_id = d.pop("identityId", UNSET)

        message_id = d.pop("messageId", UNSET)

        _setting_type = d.pop("settingType", UNSET)
        setting_type: BTApplicationSettingsType | Unset
        if isinstance(_setting_type, Unset):
            setting_type = UNSET
        else:
            setting_type = BTApplicationSettingsType(_setting_type)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        webhook_id = d.pop("webhookId", UNSET)

        bt_user_app_message_body = cls(
            app_element_session_id=app_element_session_id,
            client_id=client_id,
            data=data,
            event=event,
            identity_id=identity_id,
            message_id=message_id,
            setting_type=setting_type,
            timestamp=timestamp,
            webhook_id=webhook_id,
        )

        bt_user_app_message_body.additional_properties = d
        return bt_user_app_message_body

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
