from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_discount_metadata import BTDiscountMetadata
    from ..models.bt_discount_owner_id_plan_id import BTDiscountOwnerIdPlanId


T = TypeVar("T", bound="BTDiscount")


@_attrs_define
class BTDiscount:
    """
    Attributes:
        account_balance (int | Unset):
        amount_off (int | Unset):
        amount_off_currency (str | Unset):
        coupon_type (int | Unset):
        coupon_valid_months (int | Unset):
        created_at (datetime.datetime | Unset):
        created_by (str | Unset):
        description (str | Unset):
        expires_at (datetime.datetime | Unset):
        id (BTDiscountOwnerIdPlanId | Unset):
        metadata (BTDiscountMetadata | Unset):
        modified_at (datetime.datetime | Unset):
        modified_by (str | Unset):
        name (str | Unset):
        new (bool | Unset):
        percent_off (int | Unset):
        trial_end_date (str | Unset):
        used_at (datetime.datetime | Unset):
    """

    account_balance: int | Unset = UNSET
    amount_off: int | Unset = UNSET
    amount_off_currency: str | Unset = UNSET
    coupon_type: int | Unset = UNSET
    coupon_valid_months: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by: str | Unset = UNSET
    description: str | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    id: BTDiscountOwnerIdPlanId | Unset = UNSET
    metadata: BTDiscountMetadata | Unset = UNSET
    modified_at: datetime.datetime | Unset = UNSET
    modified_by: str | Unset = UNSET
    name: str | Unset = UNSET
    new: bool | Unset = UNSET
    percent_off: int | Unset = UNSET
    trial_end_date: str | Unset = UNSET
    used_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_balance = self.account_balance

        amount_off = self.amount_off

        amount_off_currency = self.amount_off_currency

        coupon_type = self.coupon_type

        coupon_valid_months = self.coupon_valid_months

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by = self.created_by

        description = self.description

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = self.id.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        modified_at: str | Unset = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        modified_by = self.modified_by

        name = self.name

        new = self.new

        percent_off = self.percent_off

        trial_end_date = self.trial_end_date

        used_at: str | Unset = UNSET
        if not isinstance(self.used_at, Unset):
            used_at = self.used_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_balance is not UNSET:
            field_dict["accountBalance"] = account_balance
        if amount_off is not UNSET:
            field_dict["amountOff"] = amount_off
        if amount_off_currency is not UNSET:
            field_dict["amountOffCurrency"] = amount_off_currency
        if coupon_type is not UNSET:
            field_dict["couponType"] = coupon_type
        if coupon_valid_months is not UNSET:
            field_dict["couponValidMonths"] = coupon_valid_months
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if name is not UNSET:
            field_dict["name"] = name
        if new is not UNSET:
            field_dict["new"] = new
        if percent_off is not UNSET:
            field_dict["percentOff"] = percent_off
        if trial_end_date is not UNSET:
            field_dict["trialEndDate"] = trial_end_date
        if used_at is not UNSET:
            field_dict["usedAt"] = used_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_discount_metadata import BTDiscountMetadata
        from ..models.bt_discount_owner_id_plan_id import BTDiscountOwnerIdPlanId

        d = dict(src_dict)
        account_balance = d.pop("accountBalance", UNSET)

        amount_off = d.pop("amountOff", UNSET)

        amount_off_currency = d.pop("amountOffCurrency", UNSET)

        coupon_type = d.pop("couponType", UNSET)

        coupon_valid_months = d.pop("couponValidMonths", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        created_by = d.pop("createdBy", UNSET)

        description = d.pop("description", UNSET)

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        _id = d.pop("id", UNSET)
        id: BTDiscountOwnerIdPlanId | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = BTDiscountOwnerIdPlanId.from_dict(_id)

        _metadata = d.pop("metadata", UNSET)
        metadata: BTDiscountMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = BTDiscountMetadata.from_dict(_metadata)

        _modified_at = d.pop("modifiedAt", UNSET)
        modified_at: datetime.datetime | Unset
        if isinstance(_modified_at, Unset):
            modified_at = UNSET
        else:
            modified_at = isoparse(_modified_at)

        modified_by = d.pop("modifiedBy", UNSET)

        name = d.pop("name", UNSET)

        new = d.pop("new", UNSET)

        percent_off = d.pop("percentOff", UNSET)

        trial_end_date = d.pop("trialEndDate", UNSET)

        _used_at = d.pop("usedAt", UNSET)
        used_at: datetime.datetime | Unset
        if isinstance(_used_at, Unset):
            used_at = UNSET
        else:
            used_at = isoparse(_used_at)

        bt_discount = cls(
            account_balance=account_balance,
            amount_off=amount_off,
            amount_off_currency=amount_off_currency,
            coupon_type=coupon_type,
            coupon_valid_months=coupon_valid_months,
            created_at=created_at,
            created_by=created_by,
            description=description,
            expires_at=expires_at,
            id=id,
            metadata=metadata,
            modified_at=modified_at,
            modified_by=modified_by,
            name=name,
            new=new,
            percent_off=percent_off,
            trial_end_date=trial_end_date,
            used_at=used_at,
        )

        bt_discount.additional_properties = d
        return bt_discount

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
