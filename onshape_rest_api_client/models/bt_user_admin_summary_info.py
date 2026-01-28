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
    from ..models.company_role import CompanyRole
    from ..models.global_permission_info import GlobalPermissionInfo


T = TypeVar("T", bound="BTUserAdminSummaryInfo")


@_attrs_define
class BTUserAdminSummaryInfo:
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
        active_plan_id (str | Unset):
        billing_update_required (bool | Unset):
        company_roles (list[CompanyRole] | Unset):
        created_at (datetime.datetime | Unset):
        forum_id (str | Unset):
        system_user (bool | Unset):
        totp_enabled (bool | Unset):
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
    active_plan_id: str | Unset = UNSET
    billing_update_required: bool | Unset = UNSET
    company_roles: list[CompanyRole] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    forum_id: str | Unset = UNSET
    system_user: bool | Unset = UNSET
    totp_enabled: bool | Unset = UNSET
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

        active_plan_id = self.active_plan_id

        billing_update_required = self.billing_update_required

        company_roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.company_roles, Unset):
            company_roles = []
            for company_roles_item_data in self.company_roles:
                company_roles_item = company_roles_item_data.to_dict()
                company_roles.append(company_roles_item)

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        forum_id = self.forum_id

        system_user = self.system_user

        totp_enabled = self.totp_enabled

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
        if active_plan_id is not UNSET:
            field_dict["activePlanId"] = active_plan_id
        if billing_update_required is not UNSET:
            field_dict["billingUpdateRequired"] = billing_update_required
        if company_roles is not UNSET:
            field_dict["companyRoles"] = company_roles
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if forum_id is not UNSET:
            field_dict["forumId"] = forum_id
        if system_user is not UNSET:
            field_dict["systemUser"] = system_user
        if totp_enabled is not UNSET:
            field_dict["totpEnabled"] = totp_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_company_summary_info import BTCompanySummaryInfo
        from ..models.company_role import CompanyRole
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

        active_plan_id = d.pop("activePlanId", UNSET)

        billing_update_required = d.pop("billingUpdateRequired", UNSET)

        _company_roles = d.pop("companyRoles", UNSET)
        company_roles: list[CompanyRole] | Unset = UNSET
        if _company_roles is not UNSET:
            company_roles = []
            for company_roles_item_data in _company_roles:
                company_roles_item = CompanyRole.from_dict(company_roles_item_data)

                company_roles.append(company_roles_item)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        forum_id = d.pop("forumId", UNSET)

        system_user = d.pop("systemUser", UNSET)

        totp_enabled = d.pop("totpEnabled", UNSET)

        bt_user_admin_summary_info = cls(
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
            active_plan_id=active_plan_id,
            billing_update_required=billing_update_required,
            company_roles=company_roles,
            created_at=created_at,
            forum_id=forum_id,
            system_user=system_user,
            totp_enabled=totp_enabled,
        )

        bt_user_admin_summary_info.additional_properties = d
        return bt_user_admin_summary_info

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
