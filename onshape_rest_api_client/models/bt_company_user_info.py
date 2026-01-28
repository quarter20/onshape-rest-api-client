from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_role_priority import UserRolePriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_company_summary_info import BTCompanySummaryInfo
    from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo


T = TypeVar("T", bound="BTCompanyUserInfo")


@_attrs_define
class BTCompanyUserInfo:
    """
    Attributes:
        admin (bool | Unset):
        company (BTCompanySummaryInfo | Unset):
        date_added (datetime.datetime | Unset):
        documentation_name_override (str | Unset):
        guest (bool | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        last_login_time (datetime.datetime | Unset):
        light (bool | Unset):
        name (str | Unset): Name of the resource.
        state (int | Unset):
        user (BTUserBasicSummaryInfo | Unset):
        user_role_priority (UserRolePriority | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    admin: bool | Unset = UNSET
    company: BTCompanySummaryInfo | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    documentation_name_override: str | Unset = UNSET
    guest: bool | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    last_login_time: datetime.datetime | Unset = UNSET
    light: bool | Unset = UNSET
    name: str | Unset = UNSET
    state: int | Unset = UNSET
    user: BTUserBasicSummaryInfo | Unset = UNSET
    user_role_priority: UserRolePriority | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin = self.admin

        company: dict[str, Any] | Unset = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        documentation_name_override = self.documentation_name_override

        guest = self.guest

        href = self.href

        id = self.id

        last_login_time: str | Unset = UNSET
        if not isinstance(self.last_login_time, Unset):
            last_login_time = self.last_login_time.isoformat()

        light = self.light

        name = self.name

        state = self.state

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        user_role_priority: str | Unset = UNSET
        if not isinstance(self.user_role_priority, Unset):
            user_role_priority = self.user_role_priority.value

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin is not UNSET:
            field_dict["admin"] = admin
        if company is not UNSET:
            field_dict["company"] = company
        if date_added is not UNSET:
            field_dict["dateAdded_"] = date_added
        if documentation_name_override is not UNSET:
            field_dict["documentationNameOverride"] = documentation_name_override
        if guest is not UNSET:
            field_dict["guest"] = guest
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if last_login_time is not UNSET:
            field_dict["lastLoginTime"] = last_login_time
        if light is not UNSET:
            field_dict["light"] = light
        if name is not UNSET:
            field_dict["name"] = name
        if state is not UNSET:
            field_dict["state"] = state
        if user is not UNSET:
            field_dict["user"] = user
        if user_role_priority is not UNSET:
            field_dict["userRolePriority"] = user_role_priority
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_company_summary_info import BTCompanySummaryInfo
        from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo

        d = dict(src_dict)
        admin = d.pop("admin", UNSET)

        _company = d.pop("company", UNSET)
        company: BTCompanySummaryInfo | Unset
        if isinstance(_company, Unset):
            company = UNSET
        else:
            company = BTCompanySummaryInfo.from_dict(_company)

        _date_added = d.pop("dateAdded_", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        documentation_name_override = d.pop("documentationNameOverride", UNSET)

        guest = d.pop("guest", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _last_login_time = d.pop("lastLoginTime", UNSET)
        last_login_time: datetime.datetime | Unset
        if isinstance(_last_login_time, Unset):
            last_login_time = UNSET
        else:
            last_login_time = isoparse(_last_login_time)

        light = d.pop("light", UNSET)

        name = d.pop("name", UNSET)

        state = d.pop("state", UNSET)

        _user = d.pop("user", UNSET)
        user: BTUserBasicSummaryInfo | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = BTUserBasicSummaryInfo.from_dict(_user)

        _user_role_priority = d.pop("userRolePriority", UNSET)
        user_role_priority: UserRolePriority | Unset
        if isinstance(_user_role_priority, Unset):
            user_role_priority = UNSET
        else:
            user_role_priority = UserRolePriority(_user_role_priority)

        view_ref = d.pop("viewRef", UNSET)

        bt_company_user_info = cls(
            admin=admin,
            company=company,
            date_added=date_added,
            documentation_name_override=documentation_name_override,
            guest=guest,
            href=href,
            id=id,
            last_login_time=last_login_time,
            light=light,
            name=name,
            state=state,
            user=user,
            user_role_priority=user_role_priority,
            view_ref=view_ref,
        )

        bt_company_user_info.additional_properties = d
        return bt_company_user_info

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
