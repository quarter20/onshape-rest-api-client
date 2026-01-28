from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entry import Entry


T = TypeVar("T", bound="BTRbacPermissionSchemeInfo")


@_attrs_define
class BTRbacPermissionSchemeInfo:
    """
    Attributes:
        active (bool | Unset):
        description (str | Unset):
        entries (list[Entry] | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        predefined_permission_scheme (int | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    active: bool | Unset = UNSET
    description: str | Unset = UNSET
    entries: list[Entry] | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    predefined_permission_scheme: int | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        description = self.description

        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        href = self.href

        id = self.id

        name = self.name

        predefined_permission_scheme = self.predefined_permission_scheme

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if description is not UNSET:
            field_dict["description"] = description
        if entries is not UNSET:
            field_dict["entries"] = entries
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if predefined_permission_scheme is not UNSET:
            field_dict["predefinedPermissionScheme"] = predefined_permission_scheme
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entry import Entry

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        description = d.pop("description", UNSET)

        _entries = d.pop("entries", UNSET)
        entries: list[Entry] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = Entry.from_dict(entries_item_data)

                entries.append(entries_item)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        predefined_permission_scheme = d.pop("predefinedPermissionScheme", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_rbac_permission_scheme_info = cls(
            active=active,
            description=description,
            entries=entries,
            href=href,
            id=id,
            name=name,
            predefined_permission_scheme=predefined_permission_scheme,
            view_ref=view_ref,
        )

        bt_rbac_permission_scheme_info.additional_properties = d
        return bt_rbac_permission_scheme_info

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
