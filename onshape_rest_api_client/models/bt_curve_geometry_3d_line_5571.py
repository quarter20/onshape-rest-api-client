from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_sketch_entity_type import GBTSketchEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTCurveGeometry3DLine5571")


@_attrs_define
class BTCurveGeometry3DLine5571:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        entity_type (GBTSketchEntityType | Unset):
        direction (BTVector3D389 | Unset):
        point (BTVector3D389 | Unset):
    """

    bt_type: str | Unset = UNSET
    entity_type: GBTSketchEntityType | Unset = UNSET
    direction: BTVector3D389 | Unset = UNSET
    point: BTVector3D389 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        entity_type: str | Unset = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        direction: dict[str, Any] | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.to_dict()

        point: dict[str, Any] | Unset = UNSET
        if not isinstance(self.point, Unset):
            point = self.point.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if direction is not UNSET:
            field_dict["direction"] = direction
        if point is not UNSET:
            field_dict["point"] = point

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

        _direction = d.pop("direction", UNSET)
        direction: BTVector3D389 | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = BTVector3D389.from_dict(_direction)

        _point = d.pop("point", UNSET)
        point: BTVector3D389 | Unset
        if isinstance(_point, Unset):
            point = UNSET
        else:
            point = BTVector3D389.from_dict(_point)

        bt_curve_geometry_3d_line_5571 = cls(
            bt_type=bt_type,
            entity_type=entity_type,
            direction=direction,
            point=point,
        )

        bt_curve_geometry_3d_line_5571.additional_properties = d
        return bt_curve_geometry_3d_line_5571

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
