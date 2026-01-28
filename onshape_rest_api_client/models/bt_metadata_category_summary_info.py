from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTMetadataCategorySummaryInfo")


@_attrs_define
class BTMetadataCategorySummaryInfo:
    """
    Attributes:
        default_object_type (int | Unset):
        description (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        object_types (list[int] | Unset):
        owner_id (str | Unset):
        owner_type (int | Unset):
        publish_state (int | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    default_object_type: int | Unset = UNSET
    description: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    object_types: list[int] | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: int | Unset = UNSET
    publish_state: int | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_object_type = self.default_object_type

        description = self.description

        href = self.href

        id = self.id

        name = self.name

        object_types: list[int] | Unset = UNSET
        if not isinstance(self.object_types, Unset):
            object_types = self.object_types

        owner_id = self.owner_id

        owner_type = self.owner_type

        publish_state = self.publish_state

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_object_type is not UNSET:
            field_dict["defaultObjectType"] = default_object_type
        if description is not UNSET:
            field_dict["description"] = description
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if object_types is not UNSET:
            field_dict["objectTypes"] = object_types
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if owner_type is not UNSET:
            field_dict["ownerType"] = owner_type
        if publish_state is not UNSET:
            field_dict["publishState"] = publish_state
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_object_type = d.pop("defaultObjectType", UNSET)

        description = d.pop("description", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        object_types = cast(list[int], d.pop("objectTypes", UNSET))

        owner_id = d.pop("ownerId", UNSET)

        owner_type = d.pop("ownerType", UNSET)

        publish_state = d.pop("publishState", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_metadata_category_summary_info = cls(
            default_object_type=default_object_type,
            description=description,
            href=href,
            id=id,
            name=name,
            object_types=object_types,
            owner_id=owner_id,
            owner_type=owner_type,
            publish_state=publish_state,
            view_ref=view_ref,
        )

        bt_metadata_category_summary_info.additional_properties = d
        return bt_metadata_category_summary_info

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
