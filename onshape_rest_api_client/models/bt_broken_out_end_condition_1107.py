from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTBrokenOutEndCondition1107")


@_attrs_define
class BTBrokenOutEndCondition1107:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        has_offset (bool | Unset):
        has_upto_point (bool | Unset):
        offset_distance (float | Unset):
        offset_opposite_direction (bool | Unset):
        upto_point (list[float] | Unset):
        upto_point_3_d (BTVector3D389 | Unset):
    """

    bt_type: str | Unset = UNSET
    has_offset: bool | Unset = UNSET
    has_upto_point: bool | Unset = UNSET
    offset_distance: float | Unset = UNSET
    offset_opposite_direction: bool | Unset = UNSET
    upto_point: list[float] | Unset = UNSET
    upto_point_3_d: BTVector3D389 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        has_offset = self.has_offset

        has_upto_point = self.has_upto_point

        offset_distance = self.offset_distance

        offset_opposite_direction = self.offset_opposite_direction

        upto_point: list[float] | Unset = UNSET
        if not isinstance(self.upto_point, Unset):
            upto_point = self.upto_point

        upto_point_3_d: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upto_point_3_d, Unset):
            upto_point_3_d = self.upto_point_3_d.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if has_offset is not UNSET:
            field_dict["hasOffset"] = has_offset
        if has_upto_point is not UNSET:
            field_dict["hasUptoPoint"] = has_upto_point
        if offset_distance is not UNSET:
            field_dict["offsetDistance"] = offset_distance
        if offset_opposite_direction is not UNSET:
            field_dict["offsetOppositeDirection"] = offset_opposite_direction
        if upto_point is not UNSET:
            field_dict["uptoPoint"] = upto_point
        if upto_point_3_d is not UNSET:
            field_dict["uptoPoint3d"] = upto_point_3_d

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_vector_3d389 import BTVector3D389

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        has_offset = d.pop("hasOffset", UNSET)

        has_upto_point = d.pop("hasUptoPoint", UNSET)

        offset_distance = d.pop("offsetDistance", UNSET)

        offset_opposite_direction = d.pop("offsetOppositeDirection", UNSET)

        upto_point = cast(list[float], d.pop("uptoPoint", UNSET))

        _upto_point_3_d = d.pop("uptoPoint3d", UNSET)
        upto_point_3_d: BTVector3D389 | Unset
        if isinstance(_upto_point_3_d, Unset):
            upto_point_3_d = UNSET
        else:
            upto_point_3_d = BTVector3D389.from_dict(_upto_point_3_d)

        bt_broken_out_end_condition_1107 = cls(
            bt_type=bt_type,
            has_offset=has_offset,
            has_upto_point=has_upto_point,
            offset_distance=offset_distance,
            offset_opposite_direction=offset_opposite_direction,
            upto_point=upto_point,
            upto_point_3_d=upto_point_3_d,
        )

        bt_broken_out_end_condition_1107.additional_properties = d
        return bt_broken_out_end_condition_1107

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
