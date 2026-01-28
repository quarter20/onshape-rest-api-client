from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTShareEntryParams")


@_attrs_define
class BTShareEntryParams:
    """
    Attributes:
        application_id (str | Unset):
        company_id (str | Unset):
        connection_id (str | Unset):
        email (str | Unset):
        entry_type (int | Unset):
        team_id (str | Unset):
        user_id (str | Unset):
    """

    application_id: str | Unset = UNSET
    company_id: str | Unset = UNSET
    connection_id: str | Unset = UNSET
    email: str | Unset = UNSET
    entry_type: int | Unset = UNSET
    team_id: str | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_id = self.application_id

        company_id = self.company_id

        connection_id = self.connection_id

        email = self.email

        entry_type = self.entry_type

        team_id = self.team_id

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if email is not UNSET:
            field_dict["email"] = email
        if entry_type is not UNSET:
            field_dict["entryType"] = entry_type
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application_id = d.pop("applicationId", UNSET)

        company_id = d.pop("companyId", UNSET)

        connection_id = d.pop("connectionId", UNSET)

        email = d.pop("email", UNSET)

        entry_type = d.pop("entryType", UNSET)

        team_id = d.pop("teamId", UNSET)

        user_id = d.pop("userId", UNSET)

        bt_share_entry_params = cls(
            application_id=application_id,
            company_id=company_id,
            connection_id=connection_id,
            email=email,
            entry_type=entry_type,
            team_id=team_id,
            user_id=user_id,
        )

        bt_share_entry_params.additional_properties = d
        return bt_share_entry_params

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
