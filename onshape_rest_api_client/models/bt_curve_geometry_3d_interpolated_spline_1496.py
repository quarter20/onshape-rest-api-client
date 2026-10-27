from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_sketch_entity_type import GBTSketchEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTCurveGeometry3DInterpolatedSpline1496")


@_attrs_define
class BTCurveGeometry3DInterpolatedSpline1496:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        entity_type (GBTSketchEntityType | Unset):
        interpolation_points (list[BTVector3D389] | Unset):
        is_periodic (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    entity_type: GBTSketchEntityType | Unset = UNSET
    interpolation_points: list[BTVector3D389] | Unset = UNSET
    is_periodic: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        entity_type: str | Unset = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        interpolation_points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interpolation_points, Unset):
            interpolation_points = []
            for interpolation_points_item_data in self.interpolation_points:
                interpolation_points_item = interpolation_points_item_data.to_dict()
                interpolation_points.append(interpolation_points_item)

        is_periodic = self.is_periodic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if interpolation_points is not UNSET:
            field_dict["interpolationPoints"] = interpolation_points
        if is_periodic is not UNSET:
            field_dict["isPeriodic"] = is_periodic

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

        _interpolation_points = d.pop("interpolationPoints", UNSET)
        interpolation_points: list[BTVector3D389] | Unset = UNSET
        if _interpolation_points is not UNSET:
            interpolation_points = []
            for interpolation_points_item_data in _interpolation_points:
                interpolation_points_item = BTVector3D389.from_dict(interpolation_points_item_data)

                interpolation_points.append(interpolation_points_item)

        is_periodic = d.pop("isPeriodic", UNSET)

        bt_curve_geometry_3d_interpolated_spline_1496 = cls(
            bt_type=bt_type,
            entity_type=entity_type,
            interpolation_points=interpolation_points,
            is_periodic=is_periodic,
        )

        bt_curve_geometry_3d_interpolated_spline_1496.additional_properties = d
        return bt_curve_geometry_3d_interpolated_spline_1496

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
