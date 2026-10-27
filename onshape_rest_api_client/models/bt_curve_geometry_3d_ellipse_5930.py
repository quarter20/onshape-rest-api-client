from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_sketch_entity_type import GBTSketchEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTCurveGeometry3DEllipse5930")


@_attrs_define
class BTCurveGeometry3DEllipse5930:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        entity_type (GBTSketchEntityType | Unset):
        center (BTVector3D389 | Unset):
        major_axis_direction (BTVector3D389 | Unset):
        minor_radius (float | Unset):
        normal (BTVector3D389 | Unset):
        radius (float | Unset):
    """

    bt_type: str | Unset = UNSET
    entity_type: GBTSketchEntityType | Unset = UNSET
    center: BTVector3D389 | Unset = UNSET
    major_axis_direction: BTVector3D389 | Unset = UNSET
    minor_radius: float | Unset = UNSET
    normal: BTVector3D389 | Unset = UNSET
    radius: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        entity_type: str | Unset = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        center: dict[str, Any] | Unset = UNSET
        if not isinstance(self.center, Unset):
            center = self.center.to_dict()

        major_axis_direction: dict[str, Any] | Unset = UNSET
        if not isinstance(self.major_axis_direction, Unset):
            major_axis_direction = self.major_axis_direction.to_dict()

        minor_radius = self.minor_radius

        normal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.normal, Unset):
            normal = self.normal.to_dict()

        radius = self.radius

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if center is not UNSET:
            field_dict["center"] = center
        if major_axis_direction is not UNSET:
            field_dict["majorAxisDirection"] = major_axis_direction
        if minor_radius is not UNSET:
            field_dict["minorRadius"] = minor_radius
        if normal is not UNSET:
            field_dict["normal"] = normal
        if radius is not UNSET:
            field_dict["radius"] = radius

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

        _center = d.pop("center", UNSET)
        center: BTVector3D389 | Unset
        if isinstance(_center, Unset):
            center = UNSET
        else:
            center = BTVector3D389.from_dict(_center)

        _major_axis_direction = d.pop("majorAxisDirection", UNSET)
        major_axis_direction: BTVector3D389 | Unset
        if isinstance(_major_axis_direction, Unset):
            major_axis_direction = UNSET
        else:
            major_axis_direction = BTVector3D389.from_dict(_major_axis_direction)

        minor_radius = d.pop("minorRadius", UNSET)

        _normal = d.pop("normal", UNSET)
        normal: BTVector3D389 | Unset
        if isinstance(_normal, Unset):
            normal = UNSET
        else:
            normal = BTVector3D389.from_dict(_normal)

        radius = d.pop("radius", UNSET)

        bt_curve_geometry_3d_ellipse_5930 = cls(
            bt_type=bt_type,
            entity_type=entity_type,
            center=center,
            major_axis_direction=major_axis_direction,
            minor_radius=minor_radius,
            normal=normal,
            radius=radius,
        )

        bt_curve_geometry_3d_ellipse_5930.additional_properties = d
        return bt_curve_geometry_3d_ellipse_5930

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
