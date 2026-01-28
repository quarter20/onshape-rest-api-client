from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_appearance_type import GBTAppearanceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTGeneratedGraphicsAppearance4159")


@_attrs_define
class BTGeneratedGraphicsAppearance4159:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        color (list[str] | Unset):
        non_trivial (bool | Unset):
        opacity (int | Unset):
        reset (bool | Unset):
        rgba_color (list[str] | Unset):
        type_ (GBTAppearanceType | Unset):
        usable_appearance (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    color: list[str] | Unset = UNSET
    non_trivial: bool | Unset = UNSET
    opacity: int | Unset = UNSET
    reset: bool | Unset = UNSET
    rgba_color: list[str] | Unset = UNSET
    type_: GBTAppearanceType | Unset = UNSET
    usable_appearance: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        color: list[str] | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color

        non_trivial = self.non_trivial

        opacity = self.opacity

        reset = self.reset

        rgba_color: list[str] | Unset = UNSET
        if not isinstance(self.rgba_color, Unset):
            rgba_color = self.rgba_color

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        usable_appearance = self.usable_appearance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if color is not UNSET:
            field_dict["color"] = color
        if non_trivial is not UNSET:
            field_dict["nonTrivial"] = non_trivial
        if opacity is not UNSET:
            field_dict["opacity"] = opacity
        if reset is not UNSET:
            field_dict["reset"] = reset
        if rgba_color is not UNSET:
            field_dict["rgbaColor"] = rgba_color
        if type_ is not UNSET:
            field_dict["type"] = type_
        if usable_appearance is not UNSET:
            field_dict["usableAppearance"] = usable_appearance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        color = cast(list[str], d.pop("color", UNSET))

        non_trivial = d.pop("nonTrivial", UNSET)

        opacity = d.pop("opacity", UNSET)

        reset = d.pop("reset", UNSET)

        rgba_color = cast(list[str], d.pop("rgbaColor", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: GBTAppearanceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GBTAppearanceType(_type_)

        usable_appearance = d.pop("usableAppearance", UNSET)

        bt_generated_graphics_appearance_4159 = cls(
            bt_type=bt_type,
            color=color,
            non_trivial=non_trivial,
            opacity=opacity,
            reset=reset,
            rgba_color=rgba_color,
            type_=type_,
            usable_appearance=usable_appearance,
        )

        bt_generated_graphics_appearance_4159.additional_properties = d
        return bt_generated_graphics_appearance_4159

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
