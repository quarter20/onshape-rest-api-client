from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAddressInfo")


@_attrs_define
class BTAddressInfo:
    """
    Attributes:
        address (str | Unset):
        city (str | Unset):
        country (str | Unset):
        country_code (str | Unset):
        id (str | Unset):
        state (str | Unset):
        state_code (str | Unset):
        zip_ (str | Unset):
    """

    address: str | Unset = UNSET
    city: str | Unset = UNSET
    country: str | Unset = UNSET
    country_code: str | Unset = UNSET
    id: str | Unset = UNSET
    state: str | Unset = UNSET
    state_code: str | Unset = UNSET
    zip_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        city = self.city

        country = self.country

        country_code = self.country_code

        id = self.id

        state = self.state

        state_code = self.state_code

        zip_ = self.zip_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if id is not UNSET:
            field_dict["id"] = id
        if state is not UNSET:
            field_dict["state"] = state
        if state_code is not UNSET:
            field_dict["stateCode"] = state_code
        if zip_ is not UNSET:
            field_dict["zip"] = zip_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        country_code = d.pop("countryCode", UNSET)

        id = d.pop("id", UNSET)

        state = d.pop("state", UNSET)

        state_code = d.pop("stateCode", UNSET)

        zip_ = d.pop("zip", UNSET)

        bt_address_info = cls(
            address=address,
            city=city,
            country=country,
            country_code=country_code,
            id=id,
            state=state,
            state_code=state_code,
            zip_=zip_,
        )

        bt_address_info.additional_properties = d
        return bt_address_info

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
