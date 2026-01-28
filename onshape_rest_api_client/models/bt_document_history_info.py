from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTDocumentHistoryInfo")


@_attrs_define
class BTDocumentHistoryInfo:
    """
    Attributes:
        can_be_restored (bool | Unset):
        date (datetime.datetime | Unset):
        description (str | Unset):
        microversion_id (str | Unset):
        next_microversion_id (str | Unset):
        restore_id (str | Unset): If this microversion is the result of a restore from another microversion, the
            restoreId will be the microversion Id of the original microversion that was restored. Otherwise this id will not
            be included within the response.
        user_id (str | Unset):
        username (str | Unset):
    """

    can_be_restored: bool | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    microversion_id: str | Unset = UNSET
    next_microversion_id: str | Unset = UNSET
    restore_id: str | Unset = UNSET
    user_id: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_be_restored = self.can_be_restored

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        description = self.description

        microversion_id = self.microversion_id

        next_microversion_id = self.next_microversion_id

        restore_id = self.restore_id

        user_id = self.user_id

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_be_restored is not UNSET:
            field_dict["canBeRestored"] = can_be_restored
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id
        if next_microversion_id is not UNSET:
            field_dict["nextMicroversionId"] = next_microversion_id
        if restore_id is not UNSET:
            field_dict["restoreId"] = restore_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_be_restored = d.pop("canBeRestored", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        description = d.pop("description", UNSET)

        microversion_id = d.pop("microversionId", UNSET)

        next_microversion_id = d.pop("nextMicroversionId", UNSET)

        restore_id = d.pop("restoreId", UNSET)

        user_id = d.pop("userId", UNSET)

        username = d.pop("username", UNSET)

        bt_document_history_info = cls(
            can_be_restored=can_be_restored,
            date=date,
            description=description,
            microversion_id=microversion_id,
            next_microversion_id=next_microversion_id,
            restore_id=restore_id,
            user_id=user_id,
            username=username,
        )

        bt_document_history_info.additional_properties = d
        return bt_document_history_info

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
