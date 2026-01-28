from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btfs_value_map_entry_2077 import BTFSValueMapEntry2077


T = TypeVar("T", bound="BTFSValueMap2062")


@_attrs_define
class BTFSValueMap2062:
    """
    Attributes:
        bt_type (str): Type of JSON object.
        type_tag (str | Unset):
        value (list[BTFSValueMapEntry2077] | Unset):
    """

    bt_type: str
    type_tag: str | Unset = UNSET
    value: list[BTFSValueMapEntry2077] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        type_tag = self.type_tag

        value: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = []
            for value_item_data in self.value:
                value_item = value_item_data.to_dict()
                value.append(value_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "btType": bt_type,
            }
        )
        if type_tag is not UNSET:
            field_dict["typeTag"] = type_tag
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btfs_value_map_entry_2077 import BTFSValueMapEntry2077

        d = dict(src_dict)
        bt_type = d.pop("btType")

        type_tag = d.pop("typeTag", UNSET)

        _value = d.pop("value", UNSET)
        value: list[BTFSValueMapEntry2077] | Unset = UNSET
        if _value is not UNSET:
            value = []
            for value_item_data in _value:
                value_item = BTFSValueMapEntry2077.from_dict(value_item_data)

                value.append(value_item)

        btfs_value_map_2062 = cls(
            bt_type=bt_type,
            type_tag=type_tag,
            value=value,
        )

        btfs_value_map_2062.additional_properties = d
        return btfs_value_map_2062

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
