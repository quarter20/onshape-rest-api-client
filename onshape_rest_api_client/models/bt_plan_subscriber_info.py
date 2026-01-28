from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTPlanSubscriberInfo")


@_attrs_define
class BTPlanSubscriberInfo:
    """
    Attributes:
        email (str | Unset):
        first_name (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        image (str | Unset):
        last_name (str | Unset):
        name (str | Unset): Name of the resource.
        state (int | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    email: str | Unset = UNSET
    first_name: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    image: str | Unset = UNSET
    last_name: str | Unset = UNSET
    name: str | Unset = UNSET
    state: int | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        first_name = self.first_name

        href = self.href

        id = self.id

        image = self.image

        last_name = self.last_name

        name = self.name

        state = self.state

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if image is not UNSET:
            field_dict["image"] = image
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if name is not UNSET:
            field_dict["name"] = name
        if state is not UNSET:
            field_dict["state"] = state
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        first_name = d.pop("firstName", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        image = d.pop("image", UNSET)

        last_name = d.pop("lastName", UNSET)

        name = d.pop("name", UNSET)

        state = d.pop("state", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_plan_subscriber_info = cls(
            email=email,
            first_name=first_name,
            href=href,
            id=id,
            image=image,
            last_name=last_name,
            name=name,
            state=state,
            view_ref=view_ref,
        )

        bt_plan_subscriber_info.additional_properties = d
        return bt_plan_subscriber_info

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
