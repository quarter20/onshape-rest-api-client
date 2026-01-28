from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_alias_entry_info import BTAliasEntryInfo
    from ..models.bt_identity_info import BTIdentityInfo


T = TypeVar("T", bound="BTAliasInfo")


@_attrs_define
class BTAliasInfo:
    """
    Attributes:
        company_id (str | Unset):
        created_at (datetime.datetime | Unset):
        description (str | Unset):
        entries (list[BTAliasEntryInfo] | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        identities (list[BTIdentityInfo] | Unset):
        name (str | Unset): Name of the resource.
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    company_id: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    entries: list[BTAliasEntryInfo] | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    identities: list[BTIdentityInfo] | Unset = UNSET
    name: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        description = self.description

        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        href = self.href

        id = self.id

        identities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identities, Unset):
            identities = []
            for identities_item_data in self.identities:
                identities_item = identities_item_data.to_dict()
                identities.append(identities_item)

        name = self.name

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if entries is not UNSET:
            field_dict["entries"] = entries
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if identities is not UNSET:
            field_dict["identities"] = identities
        if name is not UNSET:
            field_dict["name"] = name
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_alias_entry_info import BTAliasEntryInfo
        from ..models.bt_identity_info import BTIdentityInfo

        d = dict(src_dict)
        company_id = d.pop("companyId", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        description = d.pop("description", UNSET)

        _entries = d.pop("entries", UNSET)
        entries: list[BTAliasEntryInfo] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = BTAliasEntryInfo.from_dict(entries_item_data)

                entries.append(entries_item)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _identities = d.pop("identities", UNSET)
        identities: list[BTIdentityInfo] | Unset = UNSET
        if _identities is not UNSET:
            identities = []
            for identities_item_data in _identities:
                identities_item = BTIdentityInfo.from_dict(identities_item_data)

                identities.append(identities_item)

        name = d.pop("name", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_alias_info = cls(
            company_id=company_id,
            created_at=created_at,
            description=description,
            entries=entries,
            href=href,
            id=id,
            identities=identities,
            name=name,
            view_ref=view_ref,
        )

        bt_alias_info.additional_properties = d
        return bt_alias_info

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
