from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_company_summary_info import BTCompanySummaryInfo
    from ..models.bt_team_summary_info import BTTeamSummaryInfo
    from ..models.bt_user_summary_info import BTUserSummaryInfo


T = TypeVar("T", bound="BTIdentityInfo")


@_attrs_define
class BTIdentityInfo:
    """
    Attributes:
        company (BTCompanySummaryInfo | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        identity_type (int | Unset):
        team (BTTeamSummaryInfo | Unset):
        user (BTUserSummaryInfo | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    company: BTCompanySummaryInfo | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    identity_type: int | Unset = UNSET
    team: BTTeamSummaryInfo | Unset = UNSET
    user: BTUserSummaryInfo | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company: dict[str, Any] | Unset = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()

        href = self.href

        id = self.id

        identity_type = self.identity_type

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
        if company is not UNSET:
            field_dict["company"] = company
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if identity_type is not UNSET:
            field_dict["identityType"] = identity_type
        if team is not UNSET:
            field_dict["team"] = team
        if user is not UNSET:
            field_dict["user"] = user
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_company_summary_info import BTCompanySummaryInfo
        from ..models.bt_team_summary_info import BTTeamSummaryInfo
        from ..models.bt_user_summary_info import BTUserSummaryInfo

        d = dict(src_dict)
        _company = d.pop("company", UNSET)
        company: BTCompanySummaryInfo | Unset
        if isinstance(_company, Unset):
            company = UNSET
        else:
            company = BTCompanySummaryInfo.from_dict(_company)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        identity_type = d.pop("identityType", UNSET)

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

        bt_identity_info = cls(
            company=company,
            href=href,
            id=id,
            identity_type=identity_type,
            team=team,
            user=user,
            view_ref=view_ref,
        )

        bt_identity_info.additional_properties = d
        return bt_identity_info

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
