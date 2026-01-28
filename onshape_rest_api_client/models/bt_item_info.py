from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_item_info_properties import BTItemInfoProperties


T = TypeVar("T", bound="BTItemInfo")


@_attrs_define
class BTItemInfo:
    """Information for non-geometric items.

    Attributes:
        company_id (str | Unset): ID of the company, classroom, or enterprise that owns this item.
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        properties (BTItemInfoProperties | Unset): Map of the item's properties and their values.
        publish_state (int | Unset): `0: PENDING | 1: ACTIVE | 2: INACTIVE`
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    company_id: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    properties: BTItemInfoProperties | Unset = UNSET
    publish_state: int | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        href = self.href

        id = self.id

        name = self.name

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        publish_state = self.publish_state

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if properties is not UNSET:
            field_dict["properties"] = properties
        if publish_state is not UNSET:
            field_dict["publishState"] = publish_state
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_item_info_properties import BTItemInfoProperties

        d = dict(src_dict)
        company_id = d.pop("companyId", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: BTItemInfoProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = BTItemInfoProperties.from_dict(_properties)

        publish_state = d.pop("publishState", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_item_info = cls(
            company_id=company_id,
            href=href,
            id=id,
            name=name,
            properties=properties,
            publish_state=publish_state,
            view_ref=view_ref,
        )

        bt_item_info.additional_properties = d
        return bt_item_info

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
