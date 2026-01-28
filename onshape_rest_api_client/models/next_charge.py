from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="NextCharge")


@_attrs_define
class NextCharge:
    """
    Attributes:
        amount (int | Unset):
        current_period_end (datetime.datetime | Unset):
        interval (str | Unset):
        total (int | Unset):
    """

    amount: int | Unset = UNSET
    current_period_end: datetime.datetime | Unset = UNSET
    interval: str | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        current_period_end: str | Unset = UNSET
        if not isinstance(self.current_period_end, Unset):
            current_period_end = self.current_period_end.isoformat()

        interval = self.interval

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if current_period_end is not UNSET:
            field_dict["currentPeriodEnd"] = current_period_end
        if interval is not UNSET:
            field_dict["interval"] = interval
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        _current_period_end = d.pop("currentPeriodEnd", UNSET)
        current_period_end: datetime.datetime | Unset
        if isinstance(_current_period_end, Unset):
            current_period_end = UNSET
        else:
            current_period_end = isoparse(_current_period_end)

        interval = d.pop("interval", UNSET)

        total = d.pop("total", UNSET)

        next_charge = cls(
            amount=amount,
            current_period_end=current_period_end,
            interval=interval,
            total=total,
        )

        next_charge.additional_properties = d
        return next_charge

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
