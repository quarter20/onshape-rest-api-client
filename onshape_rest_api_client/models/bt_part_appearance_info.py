from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_color_info import BTColorInfo


T = TypeVar("T", bound="BTPartAppearanceInfo")


@_attrs_define
class BTPartAppearanceInfo:
    """
    Attributes:
        color (BTColorInfo | Unset):
        is_generated (bool | Unset):
        opacity (int | Unset):
    """

    color: BTColorInfo | Unset = UNSET
    is_generated: bool | Unset = UNSET
    opacity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.to_dict()

        is_generated = self.is_generated

        opacity = self.opacity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if is_generated is not UNSET:
            field_dict["isGenerated"] = is_generated
        if opacity is not UNSET:
            field_dict["opacity"] = opacity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_color_info import BTColorInfo

        d = dict(src_dict)
        _color = d.pop("color", UNSET)
        color: BTColorInfo | Unset
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = BTColorInfo.from_dict(_color)

        is_generated = d.pop("isGenerated", UNSET)

        opacity = d.pop("opacity", UNSET)

        bt_part_appearance_info = cls(
            color=color,
            is_generated=is_generated,
            opacity=opacity,
        )

        bt_part_appearance_info.additional_properties = d
        return bt_part_appearance_info

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
