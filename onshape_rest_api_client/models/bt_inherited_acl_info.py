from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_acl_entry_info import BTAclEntryInfo
    from ..models.bt_owner_info import BTOwnerInfo


T = TypeVar("T", bound="BTInheritedAclInfo")


@_attrs_define
class BTInheritedAclInfo:
    """
    Attributes:
        entries (list[BTAclEntryInfo] | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        object_id (str | Unset):
        object_name (str | Unset):
        object_type (int | Unset):
        owner (BTOwnerInfo | Unset):
        public (bool | Unset):
        shared_with_support (bool | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        visibility (str | Unset):
    """

    entries: list[BTAclEntryInfo] | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    object_id: str | Unset = UNSET
    object_name: str | Unset = UNSET
    object_type: int | Unset = UNSET
    owner: BTOwnerInfo | Unset = UNSET
    public: bool | Unset = UNSET
    shared_with_support: bool | Unset = UNSET
    view_ref: str | Unset = UNSET
    visibility: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        href = self.href

        id = self.id

        name = self.name

        object_id = self.object_id

        object_name = self.object_name

        object_type = self.object_type

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        public = self.public

        shared_with_support = self.shared_with_support

        view_ref = self.view_ref

        visibility = self.visibility

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entries is not UNSET:
            field_dict["entries"] = entries
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if object_name is not UNSET:
            field_dict["objectName"] = object_name
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if owner is not UNSET:
            field_dict["owner"] = owner
        if public is not UNSET:
            field_dict["public"] = public
        if shared_with_support is not UNSET:
            field_dict["sharedWithSupport"] = shared_with_support
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_acl_entry_info import BTAclEntryInfo
        from ..models.bt_owner_info import BTOwnerInfo

        d = dict(src_dict)
        _entries = d.pop("entries", UNSET)
        entries: list[BTAclEntryInfo] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = BTAclEntryInfo.from_dict(entries_item_data)

                entries.append(entries_item)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        object_id = d.pop("objectId", UNSET)

        object_name = d.pop("objectName", UNSET)

        object_type = d.pop("objectType", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: BTOwnerInfo | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = BTOwnerInfo.from_dict(_owner)

        public = d.pop("public", UNSET)

        shared_with_support = d.pop("sharedWithSupport", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        visibility = d.pop("visibility", UNSET)

        bt_inherited_acl_info = cls(
            entries=entries,
            href=href,
            id=id,
            name=name,
            object_id=object_id,
            object_name=object_name,
            object_type=object_type,
            owner=owner,
            public=public,
            shared_with_support=shared_with_support,
            view_ref=view_ref,
            visibility=visibility,
        )

        bt_inherited_acl_info.additional_properties = d
        return bt_inherited_acl_info

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
