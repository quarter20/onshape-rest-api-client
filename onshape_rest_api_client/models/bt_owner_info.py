from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTOwnerInfo")


@_attrs_define
class BTOwnerInfo:
    """
    Attributes:
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        image (str | Unset):
        is_enterprise_owned_resource (bool | Unset):
        name (str | Unset): Name of the resource.
        type_ (int | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    href: str | Unset = UNSET
    id: str | Unset = UNSET
    image: str | Unset = UNSET
    is_enterprise_owned_resource: bool | Unset = UNSET
    name: str | Unset = UNSET
    type_: int | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        href = self.href

        id = self.id

        image = self.image

        is_enterprise_owned_resource = self.is_enterprise_owned_resource

        name = self.name

        type_ = self.type_

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if is_enterprise_owned_resource is not UNSET:
            field_dict["isEnterpriseOwnedResource"] = is_enterprise_owned_resource
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        image = d.pop("image", UNSET)

        is_enterprise_owned_resource = d.pop("isEnterpriseOwnedResource", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_owner_info = cls(
            href=href,
            id=id,
            image=image,
            is_enterprise_owned_resource=is_enterprise_owned_resource,
            name=name,
            type_=type_,
            view_ref=view_ref,
        )

        bt_owner_info.additional_properties = d
        return bt_owner_info

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
