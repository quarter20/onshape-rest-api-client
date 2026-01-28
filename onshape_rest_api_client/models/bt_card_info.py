from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_address_info import BTAddressInfo


T = TypeVar("T", bound="BTCardInfo")


@_attrs_define
class BTCardInfo:
    """
    Attributes:
        billing_address (BTAddressInfo | Unset):
        exp_month (int | Unset):
        exp_year (int | Unset):
        last4 (str | Unset):
        type_ (str | Unset):
    """

    billing_address: BTAddressInfo | Unset = UNSET
    exp_month: int | Unset = UNSET
    exp_year: int | Unset = UNSET
    last4: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        billing_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.billing_address, Unset):
            billing_address = self.billing_address.to_dict()

        exp_month = self.exp_month

        exp_year = self.exp_year

        last4 = self.last4

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billing_address is not UNSET:
            field_dict["billingAddress"] = billing_address
        if exp_month is not UNSET:
            field_dict["expMonth"] = exp_month
        if exp_year is not UNSET:
            field_dict["expYear"] = exp_year
        if last4 is not UNSET:
            field_dict["last4"] = last4
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_address_info import BTAddressInfo

        d = dict(src_dict)
        _billing_address = d.pop("billingAddress", UNSET)
        billing_address: BTAddressInfo | Unset
        if isinstance(_billing_address, Unset):
            billing_address = UNSET
        else:
            billing_address = BTAddressInfo.from_dict(_billing_address)

        exp_month = d.pop("expMonth", UNSET)

        exp_year = d.pop("expYear", UNSET)

        last4 = d.pop("last4", UNSET)

        type_ = d.pop("type", UNSET)

        bt_card_info = cls(
            billing_address=billing_address,
            exp_month=exp_month,
            exp_year=exp_year,
            last4=last4,
            type_=type_,
        )

        bt_card_info.additional_properties = d
        return bt_card_info

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
