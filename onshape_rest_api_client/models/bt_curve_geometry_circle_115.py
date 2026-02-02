from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_sketch_entity_type import GBTSketchEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTCurveGeometryCircle115")


@_attrs_define
class BTCurveGeometryCircle115:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        entity_type (GBTSketchEntityType | Unset):
        clockwise (bool | Unset):
        radius (float | Unset):
        x_center (float | Unset):
        x_dir (float | Unset):
        y_center (float | Unset):
        y_dir (float | Unset):
    """

    bt_type: str | Unset = UNSET
    entity_type: GBTSketchEntityType | Unset = UNSET
    clockwise: bool | Unset = UNSET
    radius: float | Unset = UNSET
    x_center: float | Unset = UNSET
    x_dir: float | Unset = UNSET
    y_center: float | Unset = UNSET
    y_dir: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        entity_type: str | Unset = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        clockwise = self.clockwise

        radius = self.radius

        x_center = self.x_center

        x_dir = self.x_dir

        y_center = self.y_center

        y_dir = self.y_dir

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if clockwise is not UNSET:
            field_dict["clockwise"] = clockwise
        if radius is not UNSET:
            field_dict["radius"] = radius
        if x_center is not UNSET:
            field_dict["xCenter"] = x_center
        if x_dir is not UNSET:
            field_dict["xDir"] = x_dir
        if y_center is not UNSET:
            field_dict["yCenter"] = y_center
        if y_dir is not UNSET:
            field_dict["yDir"] = y_dir

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

        clockwise = d.pop("clockwise", UNSET)

        radius = d.pop("radius", UNSET)

        x_center = d.pop("xCenter", UNSET)

        x_dir = d.pop("xDir", UNSET)

        y_center = d.pop("yCenter", UNSET)

        y_dir = d.pop("yDir", UNSET)

        bt_curve_geometry_circle_115 = cls(
            bt_type=bt_type,
            entity_type=entity_type,
            clockwise=clockwise,
            radius=radius,
            x_center=x_center,
            x_dir=x_dir,
            y_center=y_center,
            y_dir=y_dir,
        )

        bt_curve_geometry_circle_115.additional_properties = d
        return bt_curve_geometry_circle_115

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
