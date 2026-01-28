from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_metadata_source_type import GBTMetadataSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTPartMetadataSource2895")


@_attrs_define
class BTPartMetadataSource2895:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        source_id (str | Unset):
        source_type (GBTMetadataSourceType | Unset):
    """

    bt_type: str | Unset = UNSET
    source_id: str | Unset = UNSET
    source_type: GBTMetadataSourceType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        source_id = self.source_id

        source_type: str | Unset = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        source_id = d.pop("sourceId", UNSET)

        _source_type = d.pop("sourceType", UNSET)
        source_type: GBTMetadataSourceType | Unset
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = GBTMetadataSourceType(_source_type)

        bt_part_metadata_source_2895 = cls(
            bt_type=bt_type,
            source_id=source_id,
            source_type=source_type,
        )

        bt_part_metadata_source_2895.additional_properties = d
        return bt_part_metadata_source_2895

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
