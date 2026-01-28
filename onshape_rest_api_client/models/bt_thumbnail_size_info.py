from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTThumbnailSizeInfo")


@_attrs_define
class BTThumbnailSizeInfo:
    """
    Attributes:
        href (str | Unset):
        media_type (str | Unset):
        render_mode (str | Unset):
        sheet_name (str | Unset):
        size (str | Unset):
        unique_id (str | Unset):
        view_orientation (str | Unset):
    """

    href: str | Unset = UNSET
    media_type: str | Unset = UNSET
    render_mode: str | Unset = UNSET
    sheet_name: str | Unset = UNSET
    size: str | Unset = UNSET
    unique_id: str | Unset = UNSET
    view_orientation: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        href = self.href

        media_type = self.media_type

        render_mode = self.render_mode

        sheet_name = self.sheet_name

        size = self.size

        unique_id = self.unique_id

        view_orientation = self.view_orientation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
        if render_mode is not UNSET:
            field_dict["renderMode"] = render_mode
        if sheet_name is not UNSET:
            field_dict["sheetName"] = sheet_name
        if size is not UNSET:
            field_dict["size"] = size
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id
        if view_orientation is not UNSET:
            field_dict["viewOrientation"] = view_orientation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        href = d.pop("href", UNSET)

        media_type = d.pop("mediaType", UNSET)

        render_mode = d.pop("renderMode", UNSET)

        sheet_name = d.pop("sheetName", UNSET)

        size = d.pop("size", UNSET)

        unique_id = d.pop("uniqueId", UNSET)

        view_orientation = d.pop("viewOrientation", UNSET)

        bt_thumbnail_size_info = cls(
            href=href,
            media_type=media_type,
            render_mode=render_mode,
            sheet_name=sheet_name,
            size=size,
            unique_id=unique_id,
            view_orientation=view_orientation,
        )

        bt_thumbnail_size_info.additional_properties = d
        return bt_thumbnail_size_info

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
