from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_image_mapping_3821 import BTImageMapping3821


T = TypeVar("T", bound="BTDecal2404")


@_attrs_define
class BTDecal2404:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        image_source_id (str | Unset):
        mappings (list[BTImageMapping3821] | Unset):
    """

    bt_type: str | Unset = UNSET
    image_source_id: str | Unset = UNSET
    mappings: list[BTImageMapping3821] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        image_source_id = self.image_source_id

        mappings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mappings, Unset):
            mappings = []
            for mappings_item_data in self.mappings:
                mappings_item = mappings_item_data.to_dict()
                mappings.append(mappings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if image_source_id is not UNSET:
            field_dict["imageSourceId"] = image_source_id
        if mappings is not UNSET:
            field_dict["mappings"] = mappings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_image_mapping_3821 import BTImageMapping3821

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        image_source_id = d.pop("imageSourceId", UNSET)

        _mappings = d.pop("mappings", UNSET)
        mappings: list[BTImageMapping3821] | Unset = UNSET
        if _mappings is not UNSET:
            mappings = []
            for mappings_item_data in _mappings:
                mappings_item = BTImageMapping3821.from_dict(mappings_item_data)

                mappings.append(mappings_item)

        bt_decal_2404 = cls(
            bt_type=bt_type,
            image_source_id=image_source_id,
            mappings=mappings,
        )

        bt_decal_2404.additional_properties = d
        return bt_decal_2404

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
