from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_curve_type_enum import GBTCurveTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTLineDescription1559")


@_attrs_define
class BTLineDescription1559:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        direction (BTVector3D389 | Unset):
        direction_oriented_with_face (BTVector3D389 | Unset):
        origin (BTVector3D389 | Unset):
        type_ (GBTCurveTypeEnum | Unset):
    """

    bt_type: str | Unset = UNSET
    direction: BTVector3D389 | Unset = UNSET
    direction_oriented_with_face: BTVector3D389 | Unset = UNSET
    origin: BTVector3D389 | Unset = UNSET
    type_: GBTCurveTypeEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        direction: dict[str, Any] | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.to_dict()

        direction_oriented_with_face: dict[str, Any] | Unset = UNSET
        if not isinstance(self.direction_oriented_with_face, Unset):
            direction_oriented_with_face = self.direction_oriented_with_face.to_dict()

        origin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if direction is not UNSET:
            field_dict["direction"] = direction
        if direction_oriented_with_face is not UNSET:
            field_dict["directionOrientedWithFace"] = direction_oriented_with_face
        if origin is not UNSET:
            field_dict["origin"] = origin
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_vector_3d389 import BTVector3D389

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: BTVector3D389 | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = BTVector3D389.from_dict(_direction)

        _direction_oriented_with_face = d.pop("directionOrientedWithFace", UNSET)
        direction_oriented_with_face: BTVector3D389 | Unset
        if isinstance(_direction_oriented_with_face, Unset):
            direction_oriented_with_face = UNSET
        else:
            direction_oriented_with_face = BTVector3D389.from_dict(_direction_oriented_with_face)

        _origin = d.pop("origin", UNSET)
        origin: BTVector3D389 | Unset
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = BTVector3D389.from_dict(_origin)

        _type_ = d.pop("type", UNSET)
        type_: GBTCurveTypeEnum | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GBTCurveTypeEnum(_type_)

        bt_line_description_1559 = cls(
            bt_type=bt_type,
            direction=direction,
            direction_oriented_with_face=direction_oriented_with_face,
            origin=origin,
            type_=type_,
        )

        bt_line_description_1559.additional_properties = d
        return bt_line_description_1559

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
