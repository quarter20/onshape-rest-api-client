from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.job_type import JobType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTPLMMessageBody")


@_attrs_define
class BTPLMMessageBody:
    """Webhook notification payload for all PLM related notifications.

    Attributes:
        app_element_session_id (str | Unset):
        data (str | Unset):
        document_id (str | Unset): Background PLM job's document ID.
        event (str | Unset):
        job_id (str | Unset): ID of the background PLM job that was created.
        job_type (JobType | Unset): All types of PLM background jobs
        message_id (str | Unset):
        settings_disabled (bool | Unset): Whether PLM integration was disabled.
        settings_modified (bool | Unset): Whether PLM integration settings parameters were modified.
        timestamp (datetime.datetime | Unset):
        webhook_id (str | Unset):
    """

    app_element_session_id: str | Unset = UNSET
    data: str | Unset = UNSET
    document_id: str | Unset = UNSET
    event: str | Unset = UNSET
    job_id: str | Unset = UNSET
    job_type: JobType | Unset = UNSET
    message_id: str | Unset = UNSET
    settings_disabled: bool | Unset = UNSET
    settings_modified: bool | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    webhook_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_element_session_id = self.app_element_session_id

        data = self.data

        document_id = self.document_id

        event = self.event

        job_id = self.job_id

        job_type: str | Unset = UNSET
        if not isinstance(self.job_type, Unset):
            job_type = self.job_type.value

        message_id = self.message_id

        settings_disabled = self.settings_disabled

        settings_modified = self.settings_modified

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        webhook_id = self.webhook_id

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
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if job_type is not UNSET:
            field_dict["jobType"] = job_type
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if settings_disabled is not UNSET:
            field_dict["settingsDisabled"] = settings_disabled
        if settings_modified is not UNSET:
            field_dict["settingsModified"] = settings_modified
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if webhook_id is not UNSET:
            field_dict["webhookId"] = webhook_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_element_session_id = d.pop("appElementSessionId", UNSET)

        data = d.pop("data", UNSET)

        document_id = d.pop("documentId", UNSET)

        event = d.pop("event", UNSET)

        job_id = d.pop("jobId", UNSET)

        _job_type = d.pop("jobType", UNSET)
        job_type: JobType | Unset
        if isinstance(_job_type, Unset):
            job_type = UNSET
        else:
            job_type = JobType(_job_type)

        message_id = d.pop("messageId", UNSET)

        settings_disabled = d.pop("settingsDisabled", UNSET)

        settings_modified = d.pop("settingsModified", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        webhook_id = d.pop("webhookId", UNSET)

        btplm_message_body = cls(
            app_element_session_id=app_element_session_id,
            data=data,
            document_id=document_id,
            event=event,
            job_id=job_id,
            job_type=job_type,
            message_id=message_id,
            settings_disabled=settings_disabled,
            settings_modified=settings_modified,
            timestamp=timestamp,
            webhook_id=webhook_id,
        )

        btplm_message_body.additional_properties = d
        return btplm_message_body

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
