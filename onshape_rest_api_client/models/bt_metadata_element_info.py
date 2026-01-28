from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_metadata_object_list_info_bt_metadata_part_info import BTMetadataObjectListInfoBTMetadataPartInfo
    from ..models.bt_metadata_property_info import BTMetadataPropertyInfo
    from ..models.bt_thumbnail_info import BTThumbnailInfo


T = TypeVar("T", bound="BTMetadataElementInfo")


@_attrs_define
class BTMetadataElementInfo:
    """
    Attributes:
        json_type (str):
        href (str | Unset):
        properties (list[BTMetadataPropertyInfo] | Unset): Properties associated with this metadata object
        thumbnail (BTThumbnailInfo | Unset):
        element_id (str | Unset):
        element_type (int | Unset):
        mime_type (str | Unset):
        parts (BTMetadataObjectListInfoBTMetadataPartInfo | Unset):
    """

    json_type: str
    href: str | Unset = UNSET
    properties: list[BTMetadataPropertyInfo] | Unset = UNSET
    thumbnail: BTThumbnailInfo | Unset = UNSET
    element_id: str | Unset = UNSET
    element_type: int | Unset = UNSET
    mime_type: str | Unset = UNSET
    parts: BTMetadataObjectListInfoBTMetadataPartInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        json_type = self.json_type

        href = self.href

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        thumbnail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail, Unset):
            thumbnail = self.thumbnail.to_dict()

        element_id = self.element_id

        element_type = self.element_type

        mime_type = self.mime_type

        parts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parts, Unset):
            parts = self.parts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jsonType": json_type,
            }
        )
        if href is not UNSET:
            field_dict["href"] = href
        if properties is not UNSET:
            field_dict["properties"] = properties
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_type is not UNSET:
            field_dict["elementType"] = element_type
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if parts is not UNSET:
            field_dict["parts"] = parts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_metadata_object_list_info_bt_metadata_part_info import (
            BTMetadataObjectListInfoBTMetadataPartInfo,
        )
        from ..models.bt_metadata_property_info import BTMetadataPropertyInfo
        from ..models.bt_thumbnail_info import BTThumbnailInfo

        d = dict(src_dict)
        json_type = d.pop("jsonType")

        href = d.pop("href", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: list[BTMetadataPropertyInfo] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = BTMetadataPropertyInfo.from_dict(properties_item_data)

                properties.append(properties_item)

        _thumbnail = d.pop("thumbnail", UNSET)
        thumbnail: BTThumbnailInfo | Unset
        if isinstance(_thumbnail, Unset):
            thumbnail = UNSET
        else:
            thumbnail = BTThumbnailInfo.from_dict(_thumbnail)

        element_id = d.pop("elementId", UNSET)

        element_type = d.pop("elementType", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        _parts = d.pop("parts", UNSET)
        parts: BTMetadataObjectListInfoBTMetadataPartInfo | Unset
        if isinstance(_parts, Unset):
            parts = UNSET
        else:
            parts = BTMetadataObjectListInfoBTMetadataPartInfo.from_dict(_parts)

        bt_metadata_element_info = cls(
            json_type=json_type,
            href=href,
            properties=properties,
            thumbnail=thumbnail,
            element_id=element_id,
            element_type=element_type,
            mime_type=mime_type,
            parts=parts,
        )

        bt_metadata_element_info.additional_properties = d
        return bt_metadata_element_info

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
