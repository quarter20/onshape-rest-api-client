from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_metadata_property_info import BTMetadataPropertyInfo
    from ..models.bt_thumbnail_info import BTThumbnailInfo


T = TypeVar("T", bound="BTMetadataPartInfo")


@_attrs_define
class BTMetadataPartInfo:
    """
    Attributes:
        json_type (str):
        href (str | Unset):
        properties (list[BTMetadataPropertyInfo] | Unset): Properties associated with this metadata object
        thumbnail (BTThumbnailInfo | Unset):
        is_flattened_body (bool | Unset):
        is_public_part_overridable (bool | Unset):
        mesh_state (int | Unset):
        part_id (str | Unset):
        part_identity (str | Unset):
        part_type (str | Unset):
    """

    json_type: str
    href: str | Unset = UNSET
    properties: list[BTMetadataPropertyInfo] | Unset = UNSET
    thumbnail: BTThumbnailInfo | Unset = UNSET
    is_flattened_body: bool | Unset = UNSET
    is_public_part_overridable: bool | Unset = UNSET
    mesh_state: int | Unset = UNSET
    part_id: str | Unset = UNSET
    part_identity: str | Unset = UNSET
    part_type: str | Unset = UNSET
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

        is_flattened_body = self.is_flattened_body

        is_public_part_overridable = self.is_public_part_overridable

        mesh_state = self.mesh_state

        part_id = self.part_id

        part_identity = self.part_identity

        part_type = self.part_type

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
        if is_flattened_body is not UNSET:
            field_dict["isFlattenedBody"] = is_flattened_body
        if is_public_part_overridable is not UNSET:
            field_dict["isPublicPartOverridable"] = is_public_part_overridable
        if mesh_state is not UNSET:
            field_dict["meshState"] = mesh_state
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_identity is not UNSET:
            field_dict["partIdentity"] = part_identity
        if part_type is not UNSET:
            field_dict["partType"] = part_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        is_flattened_body = d.pop("isFlattenedBody", UNSET)

        is_public_part_overridable = d.pop("isPublicPartOverridable", UNSET)

        mesh_state = d.pop("meshState", UNSET)

        part_id = d.pop("partId", UNSET)

        part_identity = d.pop("partIdentity", UNSET)

        part_type = d.pop("partType", UNSET)

        bt_metadata_part_info = cls(
            json_type=json_type,
            href=href,
            properties=properties,
            thumbnail=thumbnail,
            is_flattened_body=is_flattened_body,
            is_public_part_overridable=is_public_part_overridable,
            mesh_state=mesh_state,
            part_id=part_id,
            part_identity=part_identity,
            part_type=part_type,
        )

        bt_metadata_part_info.additional_properties = d
        return bt_metadata_part_info

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
