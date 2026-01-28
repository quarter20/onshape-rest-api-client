from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTExportModelEdgeGeometry1125")


@_attrs_define
class BTExportModelEdgeGeometry1125:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        end_point (BTVector3D389 | Unset):
        end_vector (BTVector3D389 | Unset):
        length (float | Unset):
        mid_point (BTVector3D389 | Unset):
        quarter_point (BTVector3D389 | Unset):
        start_point (BTVector3D389 | Unset):
        start_vector (BTVector3D389 | Unset):
    """

    bt_type: str | Unset = UNSET
    end_point: BTVector3D389 | Unset = UNSET
    end_vector: BTVector3D389 | Unset = UNSET
    length: float | Unset = UNSET
    mid_point: BTVector3D389 | Unset = UNSET
    quarter_point: BTVector3D389 | Unset = UNSET
    start_point: BTVector3D389 | Unset = UNSET
    start_vector: BTVector3D389 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        end_point: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end_point, Unset):
            end_point = self.end_point.to_dict()

        end_vector: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end_vector, Unset):
            end_vector = self.end_vector.to_dict()

        length = self.length

        mid_point: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mid_point, Unset):
            mid_point = self.mid_point.to_dict()

        quarter_point: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quarter_point, Unset):
            quarter_point = self.quarter_point.to_dict()

        start_point: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start_point, Unset):
            start_point = self.start_point.to_dict()

        start_vector: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start_vector, Unset):
            start_vector = self.start_vector.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if end_point is not UNSET:
            field_dict["endPoint"] = end_point
        if end_vector is not UNSET:
            field_dict["endVector"] = end_vector
        if length is not UNSET:
            field_dict["length"] = length
        if mid_point is not UNSET:
            field_dict["midPoint"] = mid_point
        if quarter_point is not UNSET:
            field_dict["quarterPoint"] = quarter_point
        if start_point is not UNSET:
            field_dict["startPoint"] = start_point
        if start_vector is not UNSET:
            field_dict["startVector"] = start_vector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_vector_3d389 import BTVector3D389

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _end_point = d.pop("endPoint", UNSET)
        end_point: BTVector3D389 | Unset
        if isinstance(_end_point, Unset):
            end_point = UNSET
        else:
            end_point = BTVector3D389.from_dict(_end_point)

        _end_vector = d.pop("endVector", UNSET)
        end_vector: BTVector3D389 | Unset
        if isinstance(_end_vector, Unset):
            end_vector = UNSET
        else:
            end_vector = BTVector3D389.from_dict(_end_vector)

        length = d.pop("length", UNSET)

        _mid_point = d.pop("midPoint", UNSET)
        mid_point: BTVector3D389 | Unset
        if isinstance(_mid_point, Unset):
            mid_point = UNSET
        else:
            mid_point = BTVector3D389.from_dict(_mid_point)

        _quarter_point = d.pop("quarterPoint", UNSET)
        quarter_point: BTVector3D389 | Unset
        if isinstance(_quarter_point, Unset):
            quarter_point = UNSET
        else:
            quarter_point = BTVector3D389.from_dict(_quarter_point)

        _start_point = d.pop("startPoint", UNSET)
        start_point: BTVector3D389 | Unset
        if isinstance(_start_point, Unset):
            start_point = UNSET
        else:
            start_point = BTVector3D389.from_dict(_start_point)

        _start_vector = d.pop("startVector", UNSET)
        start_vector: BTVector3D389 | Unset
        if isinstance(_start_vector, Unset):
            start_vector = UNSET
        else:
            start_vector = BTVector3D389.from_dict(_start_vector)

        bt_export_model_edge_geometry_1125 = cls(
            bt_type=bt_type,
            end_point=end_point,
            end_vector=end_vector,
            length=length,
            mid_point=mid_point,
            quarter_point=quarter_point,
            start_point=start_point,
            start_vector=start_vector,
        )

        bt_export_model_edge_geometry_1125.additional_properties = d
        return bt_export_model_edge_geometry_1125

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
