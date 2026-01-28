from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTTrialInfo")


@_attrs_define
class BTTrialInfo:
    """
    Attributes:
        paid_customer_in_past (bool | Unset):
        plan_id (str | Unset):
        plan_interval (str | Unset):
        seats (int | Unset):
        trial_days_remaining (int | Unset):
        trial_end_date (datetime.datetime | Unset):
        trial_start_date (datetime.datetime | Unset):
    """

    paid_customer_in_past: bool | Unset = UNSET
    plan_id: str | Unset = UNSET
    plan_interval: str | Unset = UNSET
    seats: int | Unset = UNSET
    trial_days_remaining: int | Unset = UNSET
    trial_end_date: datetime.datetime | Unset = UNSET
    trial_start_date: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        paid_customer_in_past = self.paid_customer_in_past

        plan_id = self.plan_id

        plan_interval = self.plan_interval

        seats = self.seats

        trial_days_remaining = self.trial_days_remaining

        trial_end_date: str | Unset = UNSET
        if not isinstance(self.trial_end_date, Unset):
            trial_end_date = self.trial_end_date.isoformat()

        trial_start_date: str | Unset = UNSET
        if not isinstance(self.trial_start_date, Unset):
            trial_start_date = self.trial_start_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if paid_customer_in_past is not UNSET:
            field_dict["paidCustomerInPast"] = paid_customer_in_past
        if plan_id is not UNSET:
            field_dict["planId"] = plan_id
        if plan_interval is not UNSET:
            field_dict["planInterval"] = plan_interval
        if seats is not UNSET:
            field_dict["seats"] = seats
        if trial_days_remaining is not UNSET:
            field_dict["trialDaysRemaining"] = trial_days_remaining
        if trial_end_date is not UNSET:
            field_dict["trialEndDate"] = trial_end_date
        if trial_start_date is not UNSET:
            field_dict["trialStartDate"] = trial_start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        paid_customer_in_past = d.pop("paidCustomerInPast", UNSET)

        plan_id = d.pop("planId", UNSET)

        plan_interval = d.pop("planInterval", UNSET)

        seats = d.pop("seats", UNSET)

        trial_days_remaining = d.pop("trialDaysRemaining", UNSET)

        _trial_end_date = d.pop("trialEndDate", UNSET)
        trial_end_date: datetime.datetime | Unset
        if isinstance(_trial_end_date, Unset):
            trial_end_date = UNSET
        else:
            trial_end_date = isoparse(_trial_end_date)

        _trial_start_date = d.pop("trialStartDate", UNSET)
        trial_start_date: datetime.datetime | Unset
        if isinstance(_trial_start_date, Unset):
            trial_start_date = UNSET
        else:
            trial_start_date = isoparse(_trial_start_date)

        bt_trial_info = cls(
            paid_customer_in_past=paid_customer_in_past,
            plan_id=plan_id,
            plan_interval=plan_interval,
            seats=seats,
            trial_days_remaining=trial_days_remaining,
            trial_end_date=trial_end_date,
            trial_start_date=trial_start_date,
        )

        bt_trial_info.additional_properties = d
        return bt_trial_info

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
