from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_company_summary_info import BTCompanySummaryInfo
    from ..models.global_permission_info import GlobalPermissionInfo


T = TypeVar("T", bound="BTTaskUserSummaryInfo")


@_attrs_define
class BTTaskUserSummaryInfo:
    """
    Attributes:
        acted (bool | Unset):
        company (BTCompanySummaryInfo | Unset):
        documentation_name (str | Unset):
        documentation_name_override (str | Unset):
        email (str | Unset):
        first_name (str | Unset):
        global_permissions (GlobalPermissionInfo | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        image (str | Unset):
        invitation_state (int | Unset):
        is_external (bool | Unset):
        is_guest (bool | Unset):
        is_light (bool | Unset):
        is_onshape_support (bool | Unset):
        last_login_time (datetime.datetime | Unset):
        last_name (str | Unset):
        name (str | Unset): Name of the resource.
        personal_message_allowed (bool | Unset):
        source (int | Unset):
        state (int | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    acted: bool | Unset = UNSET
    company: BTCompanySummaryInfo | Unset = UNSET
    documentation_name: str | Unset = UNSET
    documentation_name_override: str | Unset = UNSET
    email: str | Unset = UNSET
    first_name: str | Unset = UNSET
    global_permissions: GlobalPermissionInfo | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    image: str | Unset = UNSET
    invitation_state: int | Unset = UNSET
    is_external: bool | Unset = UNSET
    is_guest: bool | Unset = UNSET
    is_light: bool | Unset = UNSET
    is_onshape_support: bool | Unset = UNSET
    last_login_time: datetime.datetime | Unset = UNSET
    last_name: str | Unset = UNSET
    name: str | Unset = UNSET
    personal_message_allowed: bool | Unset = UNSET
    source: int | Unset = UNSET
    state: int | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acted = self.acted

        company: dict[str, Any] | Unset = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()

        documentation_name = self.documentation_name

        documentation_name_override = self.documentation_name_override

        email = self.email

        first_name = self.first_name

        global_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.global_permissions, Unset):
            global_permissions = self.global_permissions.to_dict()

        href = self.href

        id = self.id

        image = self.image

        invitation_state = self.invitation_state

        is_external = self.is_external

        is_guest = self.is_guest

        is_light = self.is_light

        is_onshape_support = self.is_onshape_support

        last_login_time: str | Unset = UNSET
        if not isinstance(self.last_login_time, Unset):
            last_login_time = self.last_login_time.isoformat()

        last_name = self.last_name

        name = self.name

        personal_message_allowed = self.personal_message_allowed

        source = self.source

        state = self.state

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acted is not UNSET:
            field_dict["acted"] = acted
        if company is not UNSET:
            field_dict["company"] = company
        if documentation_name is not UNSET:
            field_dict["documentationName"] = documentation_name
        if documentation_name_override is not UNSET:
            field_dict["documentationNameOverride"] = documentation_name_override
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if global_permissions is not UNSET:
            field_dict["globalPermissions"] = global_permissions
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if invitation_state is not UNSET:
            field_dict["invitationState"] = invitation_state
        if is_external is not UNSET:
            field_dict["isExternal"] = is_external
        if is_guest is not UNSET:
            field_dict["isGuest"] = is_guest
        if is_light is not UNSET:
            field_dict["isLight"] = is_light
        if is_onshape_support is not UNSET:
            field_dict["isOnshapeSupport"] = is_onshape_support
        if last_login_time is not UNSET:
            field_dict["lastLoginTime"] = last_login_time
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if name is not UNSET:
            field_dict["name"] = name
        if personal_message_allowed is not UNSET:
            field_dict["personalMessageAllowed"] = personal_message_allowed
        if source is not UNSET:
            field_dict["source"] = source
        if state is not UNSET:
            field_dict["state"] = state
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_company_summary_info import BTCompanySummaryInfo
        from ..models.global_permission_info import GlobalPermissionInfo

        d = dict(src_dict)
        acted = d.pop("acted", UNSET)

        _company = d.pop("company", UNSET)
        company: BTCompanySummaryInfo | Unset
        if isinstance(_company, Unset):
            company = UNSET
        else:
            company = BTCompanySummaryInfo.from_dict(_company)

        documentation_name = d.pop("documentationName", UNSET)

        documentation_name_override = d.pop("documentationNameOverride", UNSET)

        email = d.pop("email", UNSET)

        first_name = d.pop("firstName", UNSET)

        _global_permissions = d.pop("globalPermissions", UNSET)
        global_permissions: GlobalPermissionInfo | Unset
        if isinstance(_global_permissions, Unset):
            global_permissions = UNSET
        else:
            global_permissions = GlobalPermissionInfo.from_dict(_global_permissions)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        image = d.pop("image", UNSET)

        invitation_state = d.pop("invitationState", UNSET)

        is_external = d.pop("isExternal", UNSET)

        is_guest = d.pop("isGuest", UNSET)

        is_light = d.pop("isLight", UNSET)

        is_onshape_support = d.pop("isOnshapeSupport", UNSET)

        _last_login_time = d.pop("lastLoginTime", UNSET)
        last_login_time: datetime.datetime | Unset
        if isinstance(_last_login_time, Unset):
            last_login_time = UNSET
        else:
            last_login_time = isoparse(_last_login_time)

        last_name = d.pop("lastName", UNSET)

        name = d.pop("name", UNSET)

        personal_message_allowed = d.pop("personalMessageAllowed", UNSET)

        source = d.pop("source", UNSET)

        state = d.pop("state", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_task_user_summary_info = cls(
            acted=acted,
            company=company,
            documentation_name=documentation_name,
            documentation_name_override=documentation_name_override,
            email=email,
            first_name=first_name,
            global_permissions=global_permissions,
            href=href,
            id=id,
            image=image,
            invitation_state=invitation_state,
            is_external=is_external,
            is_guest=is_guest,
            is_light=is_light,
            is_onshape_support=is_onshape_support,
            last_login_time=last_login_time,
            last_name=last_name,
            name=name,
            personal_message_allowed=personal_message_allowed,
            source=source,
            state=state,
            view_ref=view_ref,
        )

        bt_task_user_summary_info.additional_properties = d
        return bt_task_user_summary_info

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
