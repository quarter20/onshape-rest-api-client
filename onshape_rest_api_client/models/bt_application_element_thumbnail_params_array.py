from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_application_element_thumbnail_params import BTApplicationElementThumbnailParams


T = TypeVar("T", bound="BTApplicationElementThumbnailParamsArray")


@_attrs_define
class BTApplicationElementThumbnailParamsArray:
    """
    Attributes:
        thumbnails (list[BTApplicationElementThumbnailParams] | Unset):
    """

    thumbnails: list[BTApplicationElementThumbnailParams] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        thumbnails: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.thumbnails, Unset):
            thumbnails = []
            for thumbnails_item_data in self.thumbnails:
                thumbnails_item = thumbnails_item_data.to_dict()
                thumbnails.append(thumbnails_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if thumbnails is not UNSET:
            field_dict["thumbnails"] = thumbnails

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_application_element_thumbnail_params import BTApplicationElementThumbnailParams

        d = dict(src_dict)
        _thumbnails = d.pop("thumbnails", UNSET)
        thumbnails: list[BTApplicationElementThumbnailParams] | Unset = UNSET
        if _thumbnails is not UNSET:
            thumbnails = []
            for thumbnails_item_data in _thumbnails:
                thumbnails_item = BTApplicationElementThumbnailParams.from_dict(thumbnails_item_data)

                thumbnails.append(thumbnails_item)

        bt_application_element_thumbnail_params_array = cls(
            thumbnails=thumbnails,
        )

        bt_application_element_thumbnail_params_array.additional_properties = d
        return bt_application_element_thumbnail_params_array

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
