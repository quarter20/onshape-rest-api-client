from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_sketch_entity_type import GBTSketchEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_curve_geometry_interpolated_spline_116_derivatives import (
        BTCurveGeometryInterpolatedSpline116Derivatives,
    )


T = TypeVar("T", bound="BTCurveGeometryInterpolatedSpline116")


@_attrs_define
class BTCurveGeometryInterpolatedSpline116:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        entity_type (GBTSketchEntityType | Unset):
        derivatives (BTCurveGeometryInterpolatedSpline116Derivatives | Unset):
        end_derivative_x (float | Unset):
        end_derivative_y (float | Unset):
        end_handle_x (float | Unset):
        end_handle_y (float | Unset):
        interpolation_points (list[float] | Unset):
        is_periodic (bool | Unset):
        start_derivative_x (float | Unset):
        start_derivative_y (float | Unset):
        start_handle_x (float | Unset):
        start_handle_y (float | Unset):
    """

    bt_type: str | Unset = UNSET
    entity_type: GBTSketchEntityType | Unset = UNSET
    derivatives: BTCurveGeometryInterpolatedSpline116Derivatives | Unset = UNSET
    end_derivative_x: float | Unset = UNSET
    end_derivative_y: float | Unset = UNSET
    end_handle_x: float | Unset = UNSET
    end_handle_y: float | Unset = UNSET
    interpolation_points: list[float] | Unset = UNSET
    is_periodic: bool | Unset = UNSET
    start_derivative_x: float | Unset = UNSET
    start_derivative_y: float | Unset = UNSET
    start_handle_x: float | Unset = UNSET
    start_handle_y: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        entity_type: str | Unset = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        derivatives: dict[str, Any] | Unset = UNSET
        if not isinstance(self.derivatives, Unset):
            derivatives = self.derivatives.to_dict()

        end_derivative_x = self.end_derivative_x

        end_derivative_y = self.end_derivative_y

        end_handle_x = self.end_handle_x

        end_handle_y = self.end_handle_y

        interpolation_points: list[float] | Unset = UNSET
        if not isinstance(self.interpolation_points, Unset):
            interpolation_points = self.interpolation_points

        is_periodic = self.is_periodic

        start_derivative_x = self.start_derivative_x

        start_derivative_y = self.start_derivative_y

        start_handle_x = self.start_handle_x

        start_handle_y = self.start_handle_y

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if derivatives is not UNSET:
            field_dict["derivatives"] = derivatives
        if end_derivative_x is not UNSET:
            field_dict["endDerivativeX"] = end_derivative_x
        if end_derivative_y is not UNSET:
            field_dict["endDerivativeY"] = end_derivative_y
        if end_handle_x is not UNSET:
            field_dict["endHandleX"] = end_handle_x
        if end_handle_y is not UNSET:
            field_dict["endHandleY"] = end_handle_y
        if interpolation_points is not UNSET:
            field_dict["interpolationPoints"] = interpolation_points
        if is_periodic is not UNSET:
            field_dict["isPeriodic"] = is_periodic
        if start_derivative_x is not UNSET:
            field_dict["startDerivativeX"] = start_derivative_x
        if start_derivative_y is not UNSET:
            field_dict["startDerivativeY"] = start_derivative_y
        if start_handle_x is not UNSET:
            field_dict["startHandleX"] = start_handle_x
        if start_handle_y is not UNSET:
            field_dict["startHandleY"] = start_handle_y

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_curve_geometry_interpolated_spline_116_derivatives import (
            BTCurveGeometryInterpolatedSpline116Derivatives,
        )

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: GBTSketchEntityType | Unset
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = GBTSketchEntityType(_entity_type)

        _derivatives = d.pop("derivatives", UNSET)
        derivatives: BTCurveGeometryInterpolatedSpline116Derivatives | Unset
        if isinstance(_derivatives, Unset):
            derivatives = UNSET
        else:
            derivatives = BTCurveGeometryInterpolatedSpline116Derivatives.from_dict(_derivatives)

        end_derivative_x = d.pop("endDerivativeX", UNSET)

        end_derivative_y = d.pop("endDerivativeY", UNSET)

        end_handle_x = d.pop("endHandleX", UNSET)

        end_handle_y = d.pop("endHandleY", UNSET)

        interpolation_points = cast(list[float], d.pop("interpolationPoints", UNSET))

        is_periodic = d.pop("isPeriodic", UNSET)

        start_derivative_x = d.pop("startDerivativeX", UNSET)

        start_derivative_y = d.pop("startDerivativeY", UNSET)

        start_handle_x = d.pop("startHandleX", UNSET)

        start_handle_y = d.pop("startHandleY", UNSET)

        bt_curve_geometry_interpolated_spline_116 = cls(
            bt_type=bt_type,
            entity_type=entity_type,
            derivatives=derivatives,
            end_derivative_x=end_derivative_x,
            end_derivative_y=end_derivative_y,
            end_handle_x=end_handle_x,
            end_handle_y=end_handle_y,
            interpolation_points=interpolation_points,
            is_periodic=is_periodic,
            start_derivative_x=start_derivative_x,
            start_derivative_y=start_derivative_y,
            start_handle_x=start_handle_x,
            start_handle_y=start_handle_y,
        )

        bt_curve_geometry_interpolated_spline_116.additional_properties = d
        return bt_curve_geometry_interpolated_spline_116

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
