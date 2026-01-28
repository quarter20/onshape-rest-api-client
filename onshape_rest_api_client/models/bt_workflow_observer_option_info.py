from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_alias_info import BTAliasInfo
    from ..models.bt_company_summary_info import BTCompanySummaryInfo
    from ..models.bt_rbac_role_info import BTRbacRoleInfo
    from ..models.bt_team_summary_info import BTTeamSummaryInfo
    from ..models.bt_user_summary_info import BTUserSummaryInfo


T = TypeVar("T", bound="BTWorkflowObserverOptionInfo")


@_attrs_define
class BTWorkflowObserverOptionInfo:
    """Array of items in the current page.

    Attributes:
        alias (BTAliasInfo | Unset):
        company (BTCompanySummaryInfo | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        identity_type (int | Unset):
        role (BTRbacRoleInfo | Unset):
        team (BTTeamSummaryInfo | Unset):
        user (BTUserSummaryInfo | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    alias: BTAliasInfo | Unset = UNSET
    company: BTCompanySummaryInfo | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    identity_type: int | Unset = UNSET
    role: BTRbacRoleInfo | Unset = UNSET
    team: BTTeamSummaryInfo | Unset = UNSET
    user: BTUserSummaryInfo | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alias, Unset):
            alias = self.alias.to_dict()

        company: dict[str, Any] | Unset = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()

        href = self.href

        id = self.id

        identity_type = self.identity_type

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        team: dict[str, Any] | Unset = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias is not UNSET:
            field_dict["alias"] = alias
        if company is not UNSET:
            field_dict["company"] = company
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if identity_type is not UNSET:
            field_dict["identityType"] = identity_type
        if role is not UNSET:
            field_dict["role"] = role
        if team is not UNSET:
            field_dict["team"] = team
        if user is not UNSET:
            field_dict["user"] = user
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_alias_info import BTAliasInfo
        from ..models.bt_company_summary_info import BTCompanySummaryInfo
        from ..models.bt_rbac_role_info import BTRbacRoleInfo
        from ..models.bt_team_summary_info import BTTeamSummaryInfo
        from ..models.bt_user_summary_info import BTUserSummaryInfo

        d = dict(src_dict)
        _alias = d.pop("alias", UNSET)
        alias: BTAliasInfo | Unset
        if isinstance(_alias, Unset):
            alias = UNSET
        else:
            alias = BTAliasInfo.from_dict(_alias)

        _company = d.pop("company", UNSET)
        company: BTCompanySummaryInfo | Unset
        if isinstance(_company, Unset):
            company = UNSET
        else:
            company = BTCompanySummaryInfo.from_dict(_company)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        identity_type = d.pop("identityType", UNSET)

        _role = d.pop("role", UNSET)
        role: BTRbacRoleInfo | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = BTRbacRoleInfo.from_dict(_role)

        _team = d.pop("team", UNSET)
        team: BTTeamSummaryInfo | Unset
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = BTTeamSummaryInfo.from_dict(_team)

        _user = d.pop("user", UNSET)
        user: BTUserSummaryInfo | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = BTUserSummaryInfo.from_dict(_user)

        view_ref = d.pop("viewRef", UNSET)

        bt_workflow_observer_option_info = cls(
            alias=alias,
            company=company,
            href=href,
            id=id,
            identity_type=identity_type,
            role=role,
            team=team,
            user=user,
            view_ref=view_ref,
        )

        bt_workflow_observer_option_info.additional_properties = d
        return bt_workflow_observer_option_info

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
