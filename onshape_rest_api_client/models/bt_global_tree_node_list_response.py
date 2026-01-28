from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_global_tree_node_info import BTGlobalTreeNodeInfo


T = TypeVar("T", bound="BTGlobalTreeNodeListResponse")


@_attrs_define
class BTGlobalTreeNodeListResponse:
    """
    Attributes:
        href (str | Unset): Requested Document URL
        items (list[BTGlobalTreeNodeInfo] | Unset): Document Items array. Array entries are the same as that returned
            from "/api/documents/{did}".
        next_ (str | Unset): The URL for the next page of items. Responses are limited to 20 items per page.
        previous (str | Unset): The URL for the previous page of items. Responses are limited to 20 items per page.
    """

    href: str | Unset = UNSET
    items: list[BTGlobalTreeNodeInfo] | Unset = UNSET
    next_: str | Unset = UNSET
    previous: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        href = self.href

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        next_ = self.next_

        previous = self.previous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if items is not UNSET:
            field_dict["items"] = items
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_global_tree_node_info import BTGlobalTreeNodeInfo

        d = dict(src_dict)
        href = d.pop("href", UNSET)

        _items = d.pop("items", UNSET)
        items: list[BTGlobalTreeNodeInfo] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = BTGlobalTreeNodeInfo.from_dict(items_item_data)

                items.append(items_item)

        next_ = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        bt_global_tree_node_list_response = cls(
            href=href,
            items=items,
            next_=next_,
            previous=previous,
        )

        bt_global_tree_node_list_response.additional_properties = d
        return bt_global_tree_node_list_response

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
