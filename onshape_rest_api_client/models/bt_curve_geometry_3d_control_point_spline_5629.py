from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_sketch_entity_type import GBTSketchEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTCurveGeometry3DControlPointSpline5629")


@_attrs_define
class BTCurveGeometry3DControlPointSpline5629:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        entity_type (GBTSketchEntityType | Unset):
        control_points (list[BTVector3D389] | Unset):
        degree (int | Unset):
        is_periodic (bool | Unset):
        is_rational (bool | Unset):
        knots (list[float] | Unset):
        weights (list[float] | Unset):
        is_bezier (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    entity_type: GBTSketchEntityType | Unset = UNSET
    control_points: list[BTVector3D389] | Unset = UNSET
    degree: int | Unset = UNSET
    is_periodic: bool | Unset = UNSET
    is_rational: bool | Unset = UNSET
    knots: list[float] | Unset = UNSET
    weights: list[float] | Unset = UNSET
    is_bezier: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        entity_type: str | Unset = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        control_points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.control_points, Unset):
            control_points = []
            for control_points_item_data in self.control_points:
                control_points_item = control_points_item_data.to_dict()
                control_points.append(control_points_item)

        degree = self.degree

        is_periodic = self.is_periodic

        is_rational = self.is_rational

        knots: list[float] | Unset = UNSET
        if not isinstance(self.knots, Unset):
            knots = self.knots

        weights: list[float] | Unset = UNSET
        if not isinstance(self.weights, Unset):
            weights = self.weights

        is_bezier = self.is_bezier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
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
        if weights is not UNSET:
            field_dict["weights"] = weights
        if is_bezier is not UNSET:
            field_dict["isBezier"] = is_bezier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_vector_3d389 import BTVector3D389  # noqa: PLC0415

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: GBTSketchEntityType | Unset
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = GBTSketchEntityType(_entity_type)

        _control_points = d.pop("controlPoints", UNSET)
        control_points: list[BTVector3D389] | Unset = UNSET
        if _control_points is not UNSET:
            control_points = []
            for control_points_item_data in _control_points:
                control_points_item = BTVector3D389.from_dict(control_points_item_data)

                control_points.append(control_points_item)

        degree = d.pop("degree", UNSET)

        is_periodic = d.pop("isPeriodic", UNSET)

        is_rational = d.pop("isRational", UNSET)

        knots = cast(list[float], d.pop("knots", UNSET))

        weights = cast(list[float], d.pop("weights", UNSET))

        is_bezier = d.pop("isBezier", UNSET)

        bt_curve_geometry_3d_control_point_spline_5629 = cls(
            bt_type=bt_type,
            entity_type=entity_type,
            control_points=control_points,
            degree=degree,
            is_periodic=is_periodic,
            is_rational=is_rational,
            knots=knots,
            weights=weights,
            is_bezier=is_bezier,
        )

        bt_curve_geometry_3d_control_point_spline_5629.additional_properties = d
        return bt_curve_geometry_3d_control_point_spline_5629

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
