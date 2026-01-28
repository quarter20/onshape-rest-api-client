from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_thumbnail_size_info import BTThumbnailSizeInfo


T = TypeVar("T", bound="BTThumbnailInfo")


@_attrs_define
class BTThumbnailInfo:
    """
    Attributes:
        href (str | Unset):
        id (str | Unset):
        secondary_sizes (list[list[BTThumbnailSizeInfo]] | Unset):
        sizes (list[BTThumbnailSizeInfo] | Unset):
    """

    href: str | Unset = UNSET
    id: str | Unset = UNSET
    secondary_sizes: list[list[BTThumbnailSizeInfo]] | Unset = UNSET
    sizes: list[BTThumbnailSizeInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        href = self.href

        id = self.id

        secondary_sizes: list[list[dict[str, Any]]] | Unset = UNSET
        if not isinstance(self.secondary_sizes, Unset):
            secondary_sizes = []
            for secondary_sizes_item_data in self.secondary_sizes:
                secondary_sizes_item = []
                for secondary_sizes_item_item_data in secondary_sizes_item_data:
                    secondary_sizes_item_item = secondary_sizes_item_item_data.to_dict()
                    secondary_sizes_item.append(secondary_sizes_item_item)

                secondary_sizes.append(secondary_sizes_item)

        sizes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sizes, Unset):
            sizes = []
            for sizes_item_data in self.sizes:
                sizes_item = sizes_item_data.to_dict()
                sizes.append(sizes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if secondary_sizes is not UNSET:
            field_dict["secondarySizes"] = secondary_sizes
        if sizes is not UNSET:
            field_dict["sizes"] = sizes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_thumbnail_size_info import BTThumbnailSizeInfo

        d = dict(src_dict)
        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _secondary_sizes = d.pop("secondarySizes", UNSET)
        secondary_sizes: list[list[BTThumbnailSizeInfo]] | Unset = UNSET
        if _secondary_sizes is not UNSET:
            secondary_sizes = []
            for secondary_sizes_item_data in _secondary_sizes:
                secondary_sizes_item = []
                _secondary_sizes_item = secondary_sizes_item_data
                for secondary_sizes_item_item_data in _secondary_sizes_item:
                    secondary_sizes_item_item = BTThumbnailSizeInfo.from_dict(secondary_sizes_item_item_data)

                    secondary_sizes_item.append(secondary_sizes_item_item)

                secondary_sizes.append(secondary_sizes_item)

        _sizes = d.pop("sizes", UNSET)
        sizes: list[BTThumbnailSizeInfo] | Unset = UNSET
        if _sizes is not UNSET:
            sizes = []
            for sizes_item_data in _sizes:
                sizes_item = BTThumbnailSizeInfo.from_dict(sizes_item_data)

                sizes.append(sizes_item)

        bt_thumbnail_info = cls(
            href=href,
            id=id,
            secondary_sizes=secondary_sizes,
            sizes=sizes,
        )

        bt_thumbnail_info.additional_properties = d
        return bt_thumbnail_info

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
