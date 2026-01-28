from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTFSValueUndefined2003")


@_attrs_define
class BTFSValueUndefined2003:
    """
    Attributes:
        bt_type (str): Type of JSON object.
        type_tag (str | Unset):
    """

    bt_type: str
    type_tag: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        type_tag = self.type_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "btType": bt_type,
            }
        )
        if type_tag is not UNSET:
            field_dict["typeTag"] = type_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType")

        type_tag = d.pop("typeTag", UNSET)

        btfs_value_undefined_2003 = cls(
            bt_type=bt_type,
            type_tag=type_tag,
        )

        btfs_value_undefined_2003.additional_properties = d
        return btfs_value_undefined_2003

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
