from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTPendingUpgradeInfo")


@_attrs_define
class BTPendingUpgradeInfo:
    """
    Attributes:
        scheduled_time (datetime.datetime | Unset):
        version (int | Unset):
    """

    scheduled_time: datetime.datetime | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scheduled_time: str | Unset = UNSET
        if not isinstance(self.scheduled_time, Unset):
            scheduled_time = self.scheduled_time.isoformat()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scheduled_time is not UNSET:
            field_dict["scheduledTime"] = scheduled_time
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _scheduled_time = d.pop("scheduledTime", UNSET)
        scheduled_time: datetime.datetime | Unset
        if isinstance(_scheduled_time, Unset):
            scheduled_time = UNSET
        else:
            scheduled_time = isoparse(_scheduled_time)

        version = d.pop("version", UNSET)

        bt_pending_upgrade_info = cls(
            scheduled_time=scheduled_time,
            version=version,
        )

        bt_pending_upgrade_info.additional_properties = d
        return bt_pending_upgrade_info

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
