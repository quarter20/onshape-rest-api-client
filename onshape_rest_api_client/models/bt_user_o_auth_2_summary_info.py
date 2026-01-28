from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.bt_role import BTRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_company_summary_info import BTCompanySummaryInfo
    from ..models.global_permission_info import GlobalPermissionInfo


T = TypeVar("T", bound="BTUserOAuth2SummaryInfo")


@_attrs_define
class BTUserOAuth2SummaryInfo:
    """
    Attributes:
        json_type (str):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        image (str | Unset):
        is_onshape_support (bool | Unset):
        state (int | Unset):
        documentation_name (str | Unset):
        email (str | Unset):
        first_name (str | Unset):
        last_name (str | Unset):
        company (BTCompanySummaryInfo | Unset):
        documentation_name_override (str | Unset):
        global_permissions (GlobalPermissionInfo | Unset):
        invitation_state (int | Unset):
        is_external (bool | Unset):
        is_guest (bool | Unset):
        is_light (bool | Unset):
        last_login_time (datetime.datetime | Unset):
        personal_message_allowed (bool | Unset):
        source (int | Unset):
        client_id (str | Unset):
        company_plan (bool | Unset):
        oauth_2_scopes (int | Unset):
        plan_group (str | Unset):
        role (int | Unset):
        roles (list[BTRole] | Unset):
    """

    json_type: str
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    image: str | Unset = UNSET
    is_onshape_support: bool | Unset = UNSET
    state: int | Unset = UNSET
    documentation_name: str | Unset = UNSET
    email: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    company: BTCompanySummaryInfo | Unset = UNSET
    documentation_name_override: str | Unset = UNSET
    global_permissions: GlobalPermissionInfo | Unset = UNSET
    invitation_state: int | Unset = UNSET
    is_external: bool | Unset = UNSET
    is_guest: bool | Unset = UNSET
    is_light: bool | Unset = UNSET
    last_login_time: datetime.datetime | Unset = UNSET
    personal_message_allowed: bool | Unset = UNSET
    source: int | Unset = UNSET
    client_id: str | Unset = UNSET
    company_plan: bool | Unset = UNSET
    oauth_2_scopes: int | Unset = UNSET
    plan_group: str | Unset = UNSET
    role: int | Unset = UNSET
    roles: list[BTRole] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        json_type = self.json_type

        href = self.href

        id = self.id

        name = self.name

        view_ref = self.view_ref

        image = self.image

        is_onshape_support = self.is_onshape_support

        state = self.state

        documentation_name = self.documentation_name

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        company: dict[str, Any] | Unset = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()

        documentation_name_override = self.documentation_name_override

        global_permissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.global_permissions, Unset):
            global_permissions = self.global_permissions.to_dict()

        invitation_state = self.invitation_state

        is_external = self.is_external

        is_guest = self.is_guest

        is_light = self.is_light

        last_login_time: str | Unset = UNSET
        if not isinstance(self.last_login_time, Unset):
            last_login_time = self.last_login_time.isoformat()

        personal_message_allowed = self.personal_message_allowed

        source = self.source

        client_id = self.client_id

        company_plan = self.company_plan

        oauth_2_scopes = self.oauth_2_scopes

        plan_group = self.plan_group

        role = self.role

        roles: list[str] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.value
                roles.append(roles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jsonType": json_type,
            }
        )
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if image is not UNSET:
            field_dict["image"] = image
        if is_onshape_support is not UNSET:
            field_dict["isOnshapeSupport"] = is_onshape_support
        if state is not UNSET:
            field_dict["state"] = state
        if documentation_name is not UNSET:
            field_dict["documentationName"] = documentation_name
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if company is not UNSET:
            field_dict["company"] = company
        if documentation_name_override is not UNSET:
            field_dict["documentationNameOverride"] = documentation_name_override
        if global_permissions is not UNSET:
            field_dict["globalPermissions"] = global_permissions
        if invitation_state is not UNSET:
            field_dict["invitationState"] = invitation_state
        if is_external is not UNSET:
            field_dict["isExternal"] = is_external
        if is_guest is not UNSET:
            field_dict["isGuest"] = is_guest
        if is_light is not UNSET:
            field_dict["isLight"] = is_light
        if last_login_time is not UNSET:
            field_dict["lastLoginTime"] = last_login_time
        if personal_message_allowed is not UNSET:
            field_dict["personalMessageAllowed"] = personal_message_allowed
        if source is not UNSET:
            field_dict["source"] = source
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if company_plan is not UNSET:
            field_dict["companyPlan"] = company_plan
        if oauth_2_scopes is not UNSET:
            field_dict["oauth2Scopes"] = oauth_2_scopes
        if plan_group is not UNSET:
            field_dict["planGroup"] = plan_group
        if role is not UNSET:
            field_dict["role"] = role
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_company_summary_info import BTCompanySummaryInfo
        from ..models.global_permission_info import GlobalPermissionInfo

        d = dict(src_dict)
        json_type = d.pop("jsonType")

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        image = d.pop("image", UNSET)

        is_onshape_support = d.pop("isOnshapeSupport", UNSET)

        state = d.pop("state", UNSET)

        documentation_name = d.pop("documentationName", UNSET)

        email = d.pop("email", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        _company = d.pop("company", UNSET)
        company: BTCompanySummaryInfo | Unset
        if isinstance(_company, Unset):
            company = UNSET
        else:
            company = BTCompanySummaryInfo.from_dict(_company)

        documentation_name_override = d.pop("documentationNameOverride", UNSET)

        _global_permissions = d.pop("globalPermissions", UNSET)
        global_permissions: GlobalPermissionInfo | Unset
        if isinstance(_global_permissions, Unset):
            global_permissions = UNSET
        else:
            global_permissions = GlobalPermissionInfo.from_dict(_global_permissions)

        invitation_state = d.pop("invitationState", UNSET)

        is_external = d.pop("isExternal", UNSET)

        is_guest = d.pop("isGuest", UNSET)

        is_light = d.pop("isLight", UNSET)

        _last_login_time = d.pop("lastLoginTime", UNSET)
        last_login_time: datetime.datetime | Unset
        if isinstance(_last_login_time, Unset):
            last_login_time = UNSET
        else:
            last_login_time = isoparse(_last_login_time)

        personal_message_allowed = d.pop("personalMessageAllowed", UNSET)

        source = d.pop("source", UNSET)

        client_id = d.pop("clientId", UNSET)

        company_plan = d.pop("companyPlan", UNSET)

        oauth_2_scopes = d.pop("oauth2Scopes", UNSET)

        plan_group = d.pop("planGroup", UNSET)

        role = d.pop("role", UNSET)

        _roles = d.pop("roles", UNSET)
        roles: list[BTRole] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = BTRole(roles_item_data)

                roles.append(roles_item)

        bt_user_o_auth_2_summary_info = cls(
            json_type=json_type,
            href=href,
            id=id,
            name=name,
            view_ref=view_ref,
            image=image,
            is_onshape_support=is_onshape_support,
            state=state,
            documentation_name=documentation_name,
            email=email,
            first_name=first_name,
            last_name=last_name,
            company=company,
            documentation_name_override=documentation_name_override,
            global_permissions=global_permissions,
            invitation_state=invitation_state,
            is_external=is_external,
            is_guest=is_guest,
            is_light=is_light,
            last_login_time=last_login_time,
            personal_message_allowed=personal_message_allowed,
            source=source,
            client_id=client_id,
            company_plan=company_plan,
            oauth_2_scopes=oauth_2_scopes,
            plan_group=plan_group,
            role=role,
            roles=roles,
        )

        bt_user_o_auth_2_summary_info.additional_properties = d
        return bt_user_o_auth_2_summary_info

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
