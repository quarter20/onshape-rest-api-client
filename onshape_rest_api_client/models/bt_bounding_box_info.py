from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTBoundingBoxInfo")


@_attrs_define
class BTBoundingBoxInfo:
    """
    Attributes:
        high_x (float | Unset):
        high_y (float | Unset):
        high_z (float | Unset):
        low_x (float | Unset):
        low_y (float | Unset):
        low_z (float | Unset):
    """

    high_x: float | Unset = UNSET
    high_y: float | Unset = UNSET
    high_z: float | Unset = UNSET
    low_x: float | Unset = UNSET
    low_y: float | Unset = UNSET
    low_z: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        high_x = self.high_x

        high_y = self.high_y

        high_z = self.high_z

        low_x = self.low_x

        low_y = self.low_y

        low_z = self.low_z

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if high_x is not UNSET:
            field_dict["highX"] = high_x
        if high_y is not UNSET:
            field_dict["highY"] = high_y
        if high_z is not UNSET:
            field_dict["highZ"] = high_z
        if low_x is not UNSET:
            field_dict["lowX"] = low_x
        if low_y is not UNSET:
            field_dict["lowY"] = low_y
        if low_z is not UNSET:
            field_dict["lowZ"] = low_z

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        high_x = d.pop("highX", UNSET)

        high_y = d.pop("highY", UNSET)

        high_z = d.pop("highZ", UNSET)

        low_x = d.pop("lowX", UNSET)

        low_y = d.pop("lowY", UNSET)

        low_z = d.pop("lowZ", UNSET)

        bt_bounding_box_info = cls(
            high_x=high_x,
            high_y=high_y,
            high_z=high_z,
            low_x=low_x,
            low_y=low_y,
            low_z=low_z,
        )

        bt_bounding_box_info.additional_properties = d
        return bt_bounding_box_info

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
