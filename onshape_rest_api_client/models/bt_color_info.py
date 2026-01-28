from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTColorInfo")


@_attrs_define
class BTColorInfo:
    """
    Attributes:
        blue (int | Unset):
        green (int | Unset):
        red (int | Unset):
    """

    blue: int | Unset = UNSET
    green: int | Unset = UNSET
    red: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blue = self.blue

        green = self.green

        red = self.red

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blue is not UNSET:
            field_dict["blue"] = blue
        if green is not UNSET:
            field_dict["green"] = green
        if red is not UNSET:
            field_dict["red"] = red

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        blue = d.pop("blue", UNSET)

        green = d.pop("green", UNSET)

        red = d.pop("red", UNSET)

        bt_color_info = cls(
            blue=blue,
            green=green,
            red=red,
        )

        bt_color_info.additional_properties = d
        return bt_color_info

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
