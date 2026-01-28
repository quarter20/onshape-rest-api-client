from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTApplicationElementThumbnailParams")


@_attrs_define
class BTApplicationElementThumbnailParams:
    """
    Attributes:
        base_64_encoded_image (str | Unset):
        description (str | Unset):
        image_height (int | Unset):
        image_width (int | Unset):
        is_primary (bool | Unset):
        unique_id (str | Unset):
    """

    base_64_encoded_image: str | Unset = UNSET
    description: str | Unset = UNSET
    image_height: int | Unset = UNSET
    image_width: int | Unset = UNSET
    is_primary: bool | Unset = UNSET
    unique_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_64_encoded_image = self.base_64_encoded_image

        description = self.description

        image_height = self.image_height

        image_width = self.image_width

        is_primary = self.is_primary

        unique_id = self.unique_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_64_encoded_image is not UNSET:
            field_dict["base64EncodedImage"] = base_64_encoded_image
        if description is not UNSET:
            field_dict["description"] = description
        if image_height is not UNSET:
            field_dict["imageHeight"] = image_height
        if image_width is not UNSET:
            field_dict["imageWidth"] = image_width
        if is_primary is not UNSET:
            field_dict["isPrimary"] = is_primary
        if unique_id is not UNSET:
            field_dict["uniqueId"] = unique_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_64_encoded_image = d.pop("base64EncodedImage", UNSET)

        description = d.pop("description", UNSET)

        image_height = d.pop("imageHeight", UNSET)

        image_width = d.pop("imageWidth", UNSET)

        is_primary = d.pop("isPrimary", UNSET)

        unique_id = d.pop("uniqueId", UNSET)

        bt_application_element_thumbnail_params = cls(
            base_64_encoded_image=base_64_encoded_image,
            description=description,
            image_height=image_height,
            image_width=image_width,
            is_primary=is_primary,
            unique_id=unique_id,
        )

        bt_application_element_thumbnail_params.additional_properties = d
        return bt_application_element_thumbnail_params

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
