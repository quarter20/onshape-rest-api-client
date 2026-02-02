from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_sketch_entity_type import GBTSketchEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTCurveGeometrySpline118")


@_attrs_define
class BTCurveGeometrySpline118:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        entity_type (GBTSketchEntityType | Unset):
        control_point_count (int | Unset):
        control_points (list[float] | Unset):
        degree (int | Unset):
        is_periodic (bool | Unset):
        is_rational (bool | Unset):
        knots (list[float] | Unset):
    """

    bt_type: str | Unset = UNSET
    entity_type: GBTSketchEntityType | Unset = UNSET
    control_point_count: int | Unset = UNSET
    control_points: list[float] | Unset = UNSET
    degree: int | Unset = UNSET
    is_periodic: bool | Unset = UNSET
    is_rational: bool | Unset = UNSET
    knots: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        entity_type: str | Unset = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        control_point_count = self.control_point_count

        control_points: list[float] | Unset = UNSET
        if not isinstance(self.control_points, Unset):
            control_points = self.control_points

        degree = self.degree

        is_periodic = self.is_periodic

        is_rational = self.is_rational

        knots: list[float] | Unset = UNSET
        if not isinstance(self.knots, Unset):
            knots = self.knots

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if control_point_count is not UNSET:
            field_dict["controlPointCount"] = control_point_count
        if control_points is not UNSET:
            field_dict["controlPoints"] = control_points
        if degree is not UNSET:
            field_dict["degree"] = degree
        if is_periodic is not UNSET:
            field_dict["isPeriodic"] = is_periodic
        if is_rational is not UNSET:
            field_dict["isRational"] = is_rational
        if knots is not UNSET:
            field_dict["knots"] = knots

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: GBTSketchEntityType | Unset
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = GBTSketchEntityType(_entity_type)

        control_point_count = d.pop("controlPointCount", UNSET)

        control_points = cast(list[float], d.pop("controlPoints", UNSET))

        degree = d.pop("degree", UNSET)

        is_periodic = d.pop("isPeriodic", UNSET)

        is_rational = d.pop("isRational", UNSET)

        knots = cast(list[float], d.pop("knots", UNSET))

        bt_curve_geometry_spline_118 = cls(
            bt_type=bt_type,
            entity_type=entity_type,
            control_point_count=control_point_count,
            control_points=control_points,
            degree=degree,
            is_periodic=is_periodic,
            is_rational=is_rational,
            knots=knots,
        )

        bt_curve_geometry_spline_118.additional_properties = d
        return bt_curve_geometry_spline_118

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
