from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_metadata_part_info import BTMetadataPartInfo


T = TypeVar("T", bound="BTMetadataObjectListInfoBTMetadataPartInfo")


@_attrs_define
class BTMetadataObjectListInfoBTMetadataPartInfo:
    """
    Attributes:
        href (str | Unset):
        items (list[BTMetadataPartInfo] | Unset):
        next_ (str | Unset):
        prev (str | Unset):
    """

    href: str | Unset = UNSET
    items: list[BTMetadataPartInfo] | Unset = UNSET
    next_: str | Unset = UNSET
    prev: str | Unset = UNSET
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

        prev = self.prev

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if items is not UNSET:
            field_dict["items"] = items
        if next_ is not UNSET:
            field_dict["next"] = next_
        if prev is not UNSET:
            field_dict["prev"] = prev

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_metadata_part_info import BTMetadataPartInfo

        d = dict(src_dict)
        href = d.pop("href", UNSET)

        _items = d.pop("items", UNSET)
        items: list[BTMetadataPartInfo] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = BTMetadataPartInfo.from_dict(items_item_data)

                items.append(items_item)

        next_ = d.pop("next", UNSET)

        prev = d.pop("prev", UNSET)

        bt_metadata_object_list_info_bt_metadata_part_info = cls(
            href=href,
            items=items,
            next_=next_,
            prev=prev,
        )

        bt_metadata_object_list_info_bt_metadata_part_info.additional_properties = d
        return bt_metadata_object_list_info_bt_metadata_part_info

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
