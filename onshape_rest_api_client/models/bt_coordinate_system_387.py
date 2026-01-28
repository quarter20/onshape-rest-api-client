from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_vector_3d389 import BTVector3D389
    from ..models.btbs_matrix_386 import BTBSMatrix386


T = TypeVar("T", bound="BTCoordinateSystem387")


@_attrs_define
class BTCoordinateSystem387:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        matrix (BTBSMatrix386 | Unset):
        origin (BTVector3D389 | Unset):
        x_axis (BTVector3D389 | Unset):
        y_axis (BTVector3D389 | Unset):
        z_axis (BTVector3D389 | Unset):
    """

    bt_type: str | Unset = UNSET
    matrix: BTBSMatrix386 | Unset = UNSET
    origin: BTVector3D389 | Unset = UNSET
    x_axis: BTVector3D389 | Unset = UNSET
    y_axis: BTVector3D389 | Unset = UNSET
    z_axis: BTVector3D389 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        matrix: dict[str, Any] | Unset = UNSET
        if not isinstance(self.matrix, Unset):
            matrix = self.matrix.to_dict()

        origin: dict[str, Any] | Unset = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin.to_dict()

        x_axis: dict[str, Any] | Unset = UNSET
        if not isinstance(self.x_axis, Unset):
            x_axis = self.x_axis.to_dict()

        y_axis: dict[str, Any] | Unset = UNSET
        if not isinstance(self.y_axis, Unset):
            y_axis = self.y_axis.to_dict()

        z_axis: dict[str, Any] | Unset = UNSET
        if not isinstance(self.z_axis, Unset):
            z_axis = self.z_axis.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if matrix is not UNSET:
            field_dict["matrix"] = matrix
        if origin is not UNSET:
            field_dict["origin"] = origin
        if x_axis is not UNSET:
            field_dict["xAxis"] = x_axis
        if y_axis is not UNSET:
            field_dict["yAxis"] = y_axis
        if z_axis is not UNSET:
            field_dict["zAxis"] = z_axis

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_vector_3d389 import BTVector3D389
        from ..models.btbs_matrix_386 import BTBSMatrix386

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _matrix = d.pop("matrix", UNSET)
        matrix: BTBSMatrix386 | Unset
        if isinstance(_matrix, Unset):
            matrix = UNSET
        else:
            matrix = BTBSMatrix386.from_dict(_matrix)

        _origin = d.pop("origin", UNSET)
        origin: BTVector3D389 | Unset
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = BTVector3D389.from_dict(_origin)

        _x_axis = d.pop("xAxis", UNSET)
        x_axis: BTVector3D389 | Unset
        if isinstance(_x_axis, Unset):
            x_axis = UNSET
        else:
            x_axis = BTVector3D389.from_dict(_x_axis)

        _y_axis = d.pop("yAxis", UNSET)
        y_axis: BTVector3D389 | Unset
        if isinstance(_y_axis, Unset):
            y_axis = UNSET
        else:
            y_axis = BTVector3D389.from_dict(_y_axis)

        _z_axis = d.pop("zAxis", UNSET)
        z_axis: BTVector3D389 | Unset
        if isinstance(_z_axis, Unset):
            z_axis = UNSET
        else:
            z_axis = BTVector3D389.from_dict(_z_axis)

        bt_coordinate_system_387 = cls(
            bt_type=bt_type,
            matrix=matrix,
            origin=origin,
            x_axis=x_axis,
            y_axis=y_axis,
            z_axis=z_axis,
        )

        bt_coordinate_system_387.additional_properties = d
        return bt_coordinate_system_387

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
