from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTUserBasicSummaryInfo")


@_attrs_define
class BTUserBasicSummaryInfo:
    """
    Attributes:
        json_type (str):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        image (str | Unset):
        is_onshape_support (bool | Unset):
        state (int | Unset):
    """

    json_type: str
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    image: str | Unset = UNSET
    is_onshape_support: bool | Unset = UNSET
    state: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        json_type = self.json_type

        href = self.href

        id = self.id

        name = self.name

        view_ref = self.view_ref

        image = self.image

        is_onshape_support = self.is_onshape_support

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jsonType": json_type,
            }
        )
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if image is not UNSET:
            field_dict["image"] = image
        if is_onshape_support is not UNSET:
            field_dict["isOnshapeSupport"] = is_onshape_support
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        json_type = d.pop("jsonType")

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        image = d.pop("image", UNSET)

        is_onshape_support = d.pop("isOnshapeSupport", UNSET)

        state = d.pop("state", UNSET)

        bt_user_basic_summary_info = cls(
            json_type=json_type,
            href=href,
            id=id,
            name=name,
            view_ref=view_ref,
            image=image,
            is_onshape_support=is_onshape_support,
            state=state,
        )

        bt_user_basic_summary_info.additional_properties = d
        return bt_user_basic_summary_info

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
