from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GBTAddUserToCompanyMessageBody")


@_attrs_define
class GBTAddUserToCompanyMessageBody:
    """
    Attributes:
        app_element_session_id (str | Unset):
        company_id (str | Unset):
        data (str | Unset):
        event (str | Unset):
        message_id (str | Unset):
        target_user_id (str | Unset):
        timestamp (datetime.datetime | Unset):
        webhook_id (str | Unset):
    """

    app_element_session_id: str | Unset = UNSET
    company_id: str | Unset = UNSET
    data: str | Unset = UNSET
    event: str | Unset = UNSET
    message_id: str | Unset = UNSET
    target_user_id: str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    webhook_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_element_session_id = self.app_element_session_id

        company_id = self.company_id

        data = self.data

        event = self.event

        message_id = self.message_id

        target_user_id = self.target_user_id

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

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
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if target_user_id is not UNSET:
            field_dict["targetUserId"] = target_user_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
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

        message_id = d.pop("messageId", UNSET)

        target_user_id = d.pop("targetUserId", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = datetime.datetime.fromisoformat(_timestamp)

        webhook_id = d.pop("webhookId", UNSET)

        gbt_add_user_to_company_message_body = cls(
            app_element_session_id=app_element_session_id,
            company_id=company_id,
            data=data,
            event=event,
            message_id=message_id,
            target_user_id=target_user_id,
            timestamp=timestamp,
            webhook_id=webhook_id,
        )

        gbt_add_user_to_company_message_body.additional_properties = d
        return gbt_add_user_to_company_message_body

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
