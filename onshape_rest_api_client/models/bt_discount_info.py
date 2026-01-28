from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_user_summary_info import BTUserSummaryInfo


T = TypeVar("T", bound="BTDiscountInfo")


@_attrs_define
class BTDiscountInfo:
    """
    Attributes:
        account_balance (int | Unset):
        amount_off (int | Unset):
        coupon_type (int | Unset):
        coupon_valid_months (int | Unset):
        created_at (datetime.datetime | Unset):
        created_by (BTUserSummaryInfo | Unset):
        expires_at (datetime.datetime | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        owner_id (str | Unset):
        percent_off (int | Unset):
        plan_id (str | Unset):
        trial_end_date (str | Unset):
        used_at (datetime.datetime | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    account_balance: int | Unset = UNSET
    amount_off: int | Unset = UNSET
    coupon_type: int | Unset = UNSET
    coupon_valid_months: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by: BTUserSummaryInfo | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    percent_off: int | Unset = UNSET
    plan_id: str | Unset = UNSET
    trial_end_date: str | Unset = UNSET
    used_at: datetime.datetime | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_balance = self.account_balance

        amount_off = self.amount_off

        coupon_type = self.coupon_type

        coupon_valid_months = self.coupon_valid_months

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        href = self.href

        id = self.id

        name = self.name

        owner_id = self.owner_id

        percent_off = self.percent_off

        plan_id = self.plan_id

        trial_end_date = self.trial_end_date

        used_at: str | Unset = UNSET
        if not isinstance(self.used_at, Unset):
            used_at = self.used_at.isoformat()

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_balance is not UNSET:
            field_dict["accountBalance"] = account_balance
        if amount_off is not UNSET:
            field_dict["amountOff"] = amount_off
        if coupon_type is not UNSET:
            field_dict["couponType"] = coupon_type
        if coupon_valid_months is not UNSET:
            field_dict["couponValidMonths"] = coupon_valid_months
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if percent_off is not UNSET:
            field_dict["percentOff"] = percent_off
        if plan_id is not UNSET:
            field_dict["planId"] = plan_id
        if trial_end_date is not UNSET:
            field_dict["trialEndDate"] = trial_end_date
        if used_at is not UNSET:
            field_dict["usedAt"] = used_at
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_user_summary_info import BTUserSummaryInfo

        d = dict(src_dict)
        account_balance = d.pop("accountBalance", UNSET)

        amount_off = d.pop("amountOff", UNSET)

        coupon_type = d.pop("couponType", UNSET)

        coupon_valid_months = d.pop("couponValidMonths", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _created_by = d.pop("createdBy", UNSET)
        created_by: BTUserSummaryInfo | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = BTUserSummaryInfo.from_dict(_created_by)

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        percent_off = d.pop("percentOff", UNSET)

        plan_id = d.pop("planId", UNSET)

        trial_end_date = d.pop("trialEndDate", UNSET)

        _used_at = d.pop("usedAt", UNSET)
        used_at: datetime.datetime | Unset
        if isinstance(_used_at, Unset):
            used_at = UNSET
        else:
            used_at = isoparse(_used_at)

        view_ref = d.pop("viewRef", UNSET)

        bt_discount_info = cls(
            account_balance=account_balance,
            amount_off=amount_off,
            coupon_type=coupon_type,
            coupon_valid_months=coupon_valid_months,
            created_at=created_at,
            created_by=created_by,
            expires_at=expires_at,
            href=href,
            id=id,
            name=name,
            owner_id=owner_id,
            percent_off=percent_off,
            plan_id=plan_id,
            trial_end_date=trial_end_date,
            used_at=used_at,
            view_ref=view_ref,
        )

        bt_discount_info.additional_properties = d
        return bt_discount_info

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
