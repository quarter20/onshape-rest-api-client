from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_identity_info import BTIdentityInfo


T = TypeVar("T", bound="BTAliasEntryInfo")


@_attrs_define
class BTAliasEntryInfo:
    """
    Attributes:
        created_at (datetime.datetime | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        identity (BTIdentityInfo | Unset):
        name (str | Unset): Name of the resource.
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    created_at: datetime.datetime | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    identity: BTIdentityInfo | Unset = UNSET
    name: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        href = self.href

        id = self.id

        identity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identity, Unset):
            identity = self.identity.to_dict()

        name = self.name

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if identity is not UNSET:
            field_dict["identity"] = identity
        if name is not UNSET:
            field_dict["name"] = name
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_identity_info import BTIdentityInfo

        d = dict(src_dict)
        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _identity = d.pop("identity", UNSET)
        identity: BTIdentityInfo | Unset
        if isinstance(_identity, Unset):
            identity = UNSET
        else:
            identity = BTIdentityInfo.from_dict(_identity)

        name = d.pop("name", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_alias_entry_info = cls(
            created_at=created_at,
            href=href,
            id=id,
            identity=identity,
            name=name,
            view_ref=view_ref,
        )

        bt_alias_entry_info.additional_properties = d
        return bt_alias_entry_info

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
