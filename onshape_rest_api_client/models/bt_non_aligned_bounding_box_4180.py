from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_coordinate_system_387 import BTCoordinateSystem387
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTNonAlignedBoundingBox4180")


@_attrs_define
class BTNonAlignedBoundingBox4180:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        max_corner (BTVector3D389 | Unset):
        min_corner (BTVector3D389 | Unset):
        valid (bool | Unset):
        coordinate_system (BTCoordinateSystem387 | Unset):
    """

    bt_type: str | Unset = UNSET
    max_corner: BTVector3D389 | Unset = UNSET
    min_corner: BTVector3D389 | Unset = UNSET
    valid: bool | Unset = UNSET
    coordinate_system: BTCoordinateSystem387 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        max_corner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.max_corner, Unset):
            max_corner = self.max_corner.to_dict()

        min_corner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.min_corner, Unset):
            min_corner = self.min_corner.to_dict()

        valid = self.valid

        coordinate_system: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coordinate_system, Unset):
            coordinate_system = self.coordinate_system.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if max_corner is not UNSET:
            field_dict["maxCorner"] = max_corner
        if min_corner is not UNSET:
            field_dict["minCorner"] = min_corner
        if valid is not UNSET:
            field_dict["valid"] = valid
        if coordinate_system is not UNSET:
            field_dict["coordinateSystem"] = coordinate_system

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_coordinate_system_387 import BTCoordinateSystem387
        from ..models.bt_vector_3d389 import BTVector3D389

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _max_corner = d.pop("maxCorner", UNSET)
        max_corner: BTVector3D389 | Unset
        if isinstance(_max_corner, Unset):
            max_corner = UNSET
        else:
            max_corner = BTVector3D389.from_dict(_max_corner)

        _min_corner = d.pop("minCorner", UNSET)
        min_corner: BTVector3D389 | Unset
        if isinstance(_min_corner, Unset):
            min_corner = UNSET
        else:
            min_corner = BTVector3D389.from_dict(_min_corner)

        valid = d.pop("valid", UNSET)

        _coordinate_system = d.pop("coordinateSystem", UNSET)
        coordinate_system: BTCoordinateSystem387 | Unset
        if isinstance(_coordinate_system, Unset):
            coordinate_system = UNSET
        else:
            coordinate_system = BTCoordinateSystem387.from_dict(_coordinate_system)

        bt_non_aligned_bounding_box_4180 = cls(
            bt_type=bt_type,
            max_corner=max_corner,
            min_corner=min_corner,
            valid=valid,
            coordinate_system=coordinate_system,
        )

        bt_non_aligned_bounding_box_4180.additional_properties = d
        return bt_non_aligned_bounding_box_4180

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
