from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyRole")


@_attrs_define
class CompanyRole:
    """
    Attributes:
        admin (bool | Unset):
        company_id (str | Unset):
        company_name (str | Unset):
        guest (bool | Unset):
        light (bool | Unset):
    """

    admin: bool | Unset = UNSET
    company_id: str | Unset = UNSET
    company_name: str | Unset = UNSET
    guest: bool | Unset = UNSET
    light: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin = self.admin

        company_id = self.company_id

        company_name = self.company_name

        guest = self.guest

        light = self.light

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin is not UNSET:
            field_dict["admin"] = admin
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if guest is not UNSET:
            field_dict["guest"] = guest
        if light is not UNSET:
            field_dict["light"] = light

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        admin = d.pop("admin", UNSET)

        company_id = d.pop("companyId", UNSET)

        company_name = d.pop("companyName", UNSET)

        guest = d.pop("guest", UNSET)

        light = d.pop("light", UNSET)

        company_role = cls(
            admin=admin,
            company_id=company_id,
            company_name=company_name,
            guest=guest,
            light=light,
        )

        company_role.additional_properties = d
        return company_role

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
