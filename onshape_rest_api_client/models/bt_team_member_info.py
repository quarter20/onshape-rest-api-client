from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_team_summary_info import BTTeamSummaryInfo
    from ..models.bt_user_summary_info import BTUserSummaryInfo


T = TypeVar("T", bound="BTTeamMemberInfo")


@_attrs_define
class BTTeamMemberInfo:
    """
    Attributes:
        admin (bool | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        member (BTUserSummaryInfo | Unset):
        name (str | Unset): Name of the resource.
        team (BTTeamSummaryInfo | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    admin: bool | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    member: BTUserSummaryInfo | Unset = UNSET
    name: str | Unset = UNSET
    team: BTTeamSummaryInfo | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        admin = self.admin

        href = self.href

        id = self.id

        member: dict[str, Any] | Unset = UNSET
        if not isinstance(self.member, Unset):
            member = self.member.to_dict()

        name = self.name

        team: dict[str, Any] | Unset = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if admin is not UNSET:
            field_dict["admin"] = admin
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if member is not UNSET:
            field_dict["member"] = member
        if name is not UNSET:
            field_dict["name"] = name
        if team is not UNSET:
            field_dict["team"] = team
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_team_summary_info import BTTeamSummaryInfo
        from ..models.bt_user_summary_info import BTUserSummaryInfo

        d = dict(src_dict)
        admin = d.pop("admin", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _member = d.pop("member", UNSET)
        member: BTUserSummaryInfo | Unset
        if isinstance(_member, Unset):
            member = UNSET
        else:
            member = BTUserSummaryInfo.from_dict(_member)

        name = d.pop("name", UNSET)

        _team = d.pop("team", UNSET)
        team: BTTeamSummaryInfo | Unset
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = BTTeamSummaryInfo.from_dict(_team)

        view_ref = d.pop("viewRef", UNSET)

        bt_team_member_info = cls(
            admin=admin,
            href=href,
            id=id,
            member=member,
            name=name,
            team=team,
            view_ref=view_ref,
        )

        bt_team_member_info.additional_properties = d
        return bt_team_member_info

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
