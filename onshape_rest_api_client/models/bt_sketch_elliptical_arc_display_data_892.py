from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTSketchEllipticalArcDisplayData892")


@_attrs_define
class BTSketchEllipticalArcDisplayData892:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        points (list[float] | Unset):
        end_param (float | Unset):
        minor_radius (float | Unset):
        offset (float | Unset):
        radius (float | Unset):
        start_param (float | Unset):
    """

    bt_type: str | Unset = UNSET
    points: list[float] | Unset = UNSET
    end_param: float | Unset = UNSET
    minor_radius: float | Unset = UNSET
    offset: float | Unset = UNSET
    radius: float | Unset = UNSET
    start_param: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        points: list[float] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = self.points

        end_param = self.end_param

        minor_radius = self.minor_radius

        offset = self.offset

        radius = self.radius

        start_param = self.start_param

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if points is not UNSET:
            field_dict["points"] = points
        if end_param is not UNSET:
            field_dict["endParam"] = end_param
        if minor_radius is not UNSET:
            field_dict["minorRadius"] = minor_radius
        if offset is not UNSET:
            field_dict["offset"] = offset
        if radius is not UNSET:
            field_dict["radius"] = radius
        if start_param is not UNSET:
            field_dict["startParam"] = start_param

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        points = cast(list[float], d.pop("points", UNSET))

        end_param = d.pop("endParam", UNSET)

        minor_radius = d.pop("minorRadius", UNSET)

        offset = d.pop("offset", UNSET)

        radius = d.pop("radius", UNSET)

        start_param = d.pop("startParam", UNSET)

        bt_sketch_elliptical_arc_display_data_892 = cls(
            bt_type=bt_type,
            points=points,
            end_param=end_param,
            minor_radius=minor_radius,
            offset=offset,
            radius=radius,
            start_param=start_param,
        )

        bt_sketch_elliptical_arc_display_data_892.additional_properties = d
        return bt_sketch_elliptical_arc_display_data_892

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
