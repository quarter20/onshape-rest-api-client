from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTSketchArcDisplayData349")


@_attrs_define
class BTSketchArcDisplayData349:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        points (list[float] | Unset):
    """

    bt_type: str | Unset = UNSET
    points: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        points: list[float] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = self.points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if points is not UNSET:
            field_dict["points"] = points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        points = cast(list[float], d.pop("points", UNSET))

        bt_sketch_arc_display_data_349 = cls(
            bt_type=bt_type,
            points=points,
        )

        bt_sketch_arc_display_data_349.additional_properties = d
        return bt_sketch_arc_display_data_349

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
