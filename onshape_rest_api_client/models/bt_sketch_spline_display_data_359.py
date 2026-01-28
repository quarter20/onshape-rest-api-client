from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTSketchSplineDisplayData359")


@_attrs_define
class BTSketchSplineDisplayData359:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        points (list[float] | Unset):
        closed (bool | Unset):
        control_point_count (int | Unset):
        degree (int | Unset):
        has_handles_in_sketch (bool | Unset):
        maximum_parameter (float | Unset):
        minimum_parameter (float | Unset):
        rational (bool | Unset):
        segment (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    points: list[float] | Unset = UNSET
    closed: bool | Unset = UNSET
    control_point_count: int | Unset = UNSET
    degree: int | Unset = UNSET
    has_handles_in_sketch: bool | Unset = UNSET
    maximum_parameter: float | Unset = UNSET
    minimum_parameter: float | Unset = UNSET
    rational: bool | Unset = UNSET
    segment: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        points: list[float] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = self.points

        closed = self.closed

        control_point_count = self.control_point_count

        degree = self.degree

        has_handles_in_sketch = self.has_handles_in_sketch

        maximum_parameter = self.maximum_parameter

        minimum_parameter = self.minimum_parameter

        rational = self.rational

        segment = self.segment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if points is not UNSET:
            field_dict["points"] = points
        if closed is not UNSET:
            field_dict["closed"] = closed
        if control_point_count is not UNSET:
            field_dict["controlPointCount"] = control_point_count
        if degree is not UNSET:
            field_dict["degree"] = degree
        if has_handles_in_sketch is not UNSET:
            field_dict["hasHandlesInSketch"] = has_handles_in_sketch
        if maximum_parameter is not UNSET:
            field_dict["maximumParameter"] = maximum_parameter
        if minimum_parameter is not UNSET:
            field_dict["minimumParameter"] = minimum_parameter
        if rational is not UNSET:
            field_dict["rational"] = rational
        if segment is not UNSET:
            field_dict["segment"] = segment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        points = cast(list[float], d.pop("points", UNSET))

        closed = d.pop("closed", UNSET)

        control_point_count = d.pop("controlPointCount", UNSET)

        degree = d.pop("degree", UNSET)

        has_handles_in_sketch = d.pop("hasHandlesInSketch", UNSET)

        maximum_parameter = d.pop("maximumParameter", UNSET)

        minimum_parameter = d.pop("minimumParameter", UNSET)

        rational = d.pop("rational", UNSET)

        segment = d.pop("segment", UNSET)

        bt_sketch_spline_display_data_359 = cls(
            bt_type=bt_type,
            points=points,
            closed=closed,
            control_point_count=control_point_count,
            degree=degree,
            has_handles_in_sketch=has_handles_in_sketch,
            maximum_parameter=maximum_parameter,
            minimum_parameter=minimum_parameter,
            rational=rational,
            segment=segment,
        )

        bt_sketch_spline_display_data_359.additional_properties = d
        return bt_sketch_spline_display_data_359

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
