from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTCompanyUserParams")


@_attrs_define
class BTCompanyUserParams:
    """
    Attributes:
        admin (bool | Unset): Indicates the user is an admin if true.
        company_id (str | Unset): Company ID of the user.
        documentation_name_override (str | Unset): String to override documentation name.
        email (str | Unset): Email ID of the company user.
        global_permissions (list[int] | Unset): List of global permissions to grant. See [Onshape Help: Global
            Permissions](https://cad.onshape.com/help/Content/Plans/global_permissions.htm#Assignin) for details on each of
            the available permissions.
             * `0`: Manage role based access control
             * `1`: Manage users, teams, and aliases
             * `2`: Enterprise administrator
             * `3`: Permanently delete
             * `4`: Analytics administrator
             * `5`: Invite guest users
             * `6`: Create projects
             * `7`: Approve releases
             * `8`: Enable link sharing
             * `9`: Create releases
             * `10`: Allow access to the App Store
             * `11`: Create documents and folders in the Enterprise root
             * `12`: Allow access to public documents
             * `17`: Manage non-geometric items
             * `18`: Manage workflows
             * `19`: Transfer documents out of Enterprise
             * `20`: Sync to Arena
             * `21`: Create tasks
             * `22`: Manage standard content metadata
             * `23`: Workspace protection permissions
             * `24`: Import files
             * `25`: Use revision tools  * `26`: Export files
        guest (bool | Unset): Indicates the user is a guest user if true.
        light (bool | Unset): Indicates the user is a light user if true.
    """

    admin: bool | Unset = UNSET
    company_id: str | Unset = UNSET
    documentation_name_override: str | Unset = UNSET
    email: str | Unset = UNSET
    global_permissions: list[int] | Unset = UNSET
    guest: bool | Unset = UNSET
    light: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin = self.admin

        company_id = self.company_id

        documentation_name_override = self.documentation_name_override

        email = self.email

        global_permissions: list[int] | Unset = UNSET
        if not isinstance(self.global_permissions, Unset):
            global_permissions = self.global_permissions

        guest = self.guest

        light = self.light

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin is not UNSET:
            field_dict["admin"] = admin
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if documentation_name_override is not UNSET:
            field_dict["documentationNameOverride"] = documentation_name_override
        if email is not UNSET:
            field_dict["email"] = email
        if global_permissions is not UNSET:
            field_dict["globalPermissions"] = global_permissions
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

        documentation_name_override = d.pop("documentationNameOverride", UNSET)

        email = d.pop("email", UNSET)

        global_permissions = cast(list[int], d.pop("globalPermissions", UNSET))

        guest = d.pop("guest", UNSET)

        light = d.pop("light", UNSET)

        bt_company_user_params = cls(
            admin=admin,
            company_id=company_id,
            documentation_name_override=documentation_name_override,
            email=email,
            global_permissions=global_permissions,
            guest=guest,
            light=light,
        )

        bt_company_user_params.additional_properties = d
        return bt_company_user_params

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
