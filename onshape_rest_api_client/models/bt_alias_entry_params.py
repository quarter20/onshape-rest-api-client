from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAliasEntryParams")


@_attrs_define
class BTAliasEntryParams:
    """
    Attributes:
        email (str | Unset):
        team_id (str | Unset):
        user_id (str | Unset):
    """

    email: str | Unset = UNSET
    team_id: str | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        team_id = self.team_id

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        team_id = d.pop("teamId", UNSET)

        user_id = d.pop("userId", UNSET)

        bt_alias_entry_params = cls(
            email=email,
            team_id=team_id,
            user_id=user_id,
        )

        bt_alias_entry_params.additional_properties = d
        return bt_alias_entry_params

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
