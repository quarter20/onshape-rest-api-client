from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTKeyMouseValuesInfo")


@_attrs_define
class BTKeyMouseValuesInfo:
    """
    Attributes:
        keys (list[str] | Unset):
        mouse_buttons (list[str] | Unset):
    """

    keys: list[str] | Unset = UNSET
    mouse_buttons: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        keys: list[str] | Unset = UNSET
        if not isinstance(self.keys, Unset):
            keys = self.keys

        mouse_buttons: list[str] | Unset = UNSET
        if not isinstance(self.mouse_buttons, Unset):
            mouse_buttons = self.mouse_buttons

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keys is not UNSET:
            field_dict["keys"] = keys
        if mouse_buttons is not UNSET:
            field_dict["mouseButtons"] = mouse_buttons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keys = cast(list[str], d.pop("keys", UNSET))

        mouse_buttons = cast(list[str], d.pop("mouseButtons", UNSET))

        bt_key_mouse_values_info = cls(
            keys=keys,
            mouse_buttons=mouse_buttons,
        )

        bt_key_mouse_values_info.additional_properties = d
        return bt_key_mouse_values_info

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
