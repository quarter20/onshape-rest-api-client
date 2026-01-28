from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_curve_description_1583 import BTCurveDescription1583
    from ..models.bt_export_model_edge_geometry_1125 import BTExportModelEdgeGeometry1125


T = TypeVar("T", bound="BTExportModelEdge1782")


@_attrs_define
class BTExportModelEdge1782:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        curve (BTCurveDescription1583 | Unset):
        geometry (BTExportModelEdgeGeometry1125 | Unset):
        id (str | Unset):
        vertices (list[str] | Unset):
    """

    bt_type: str | Unset = UNSET
    curve: BTCurveDescription1583 | Unset = UNSET
    geometry: BTExportModelEdgeGeometry1125 | Unset = UNSET
    id: str | Unset = UNSET
    vertices: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        curve: dict[str, Any] | Unset = UNSET
        if not isinstance(self.curve, Unset):
            curve = self.curve.to_dict()

        geometry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.geometry, Unset):
            geometry = self.geometry.to_dict()

        id = self.id

        vertices: list[str] | Unset = UNSET
        if not isinstance(self.vertices, Unset):
            vertices = self.vertices

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if curve is not UNSET:
            field_dict["curve"] = curve
        if geometry is not UNSET:
            field_dict["geometry"] = geometry
        if id is not UNSET:
            field_dict["id"] = id
        if vertices is not UNSET:
            field_dict["vertices"] = vertices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_curve_description_1583 import BTCurveDescription1583
        from ..models.bt_export_model_edge_geometry_1125 import BTExportModelEdgeGeometry1125

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _curve = d.pop("curve", UNSET)
        curve: BTCurveDescription1583 | Unset
        if isinstance(_curve, Unset):
            curve = UNSET
        else:
            curve = BTCurveDescription1583.from_dict(_curve)

        _geometry = d.pop("geometry", UNSET)
        geometry: BTExportModelEdgeGeometry1125 | Unset
        if isinstance(_geometry, Unset):
            geometry = UNSET
        else:
            geometry = BTExportModelEdgeGeometry1125.from_dict(_geometry)

        id = d.pop("id", UNSET)

        vertices = cast(list[str], d.pop("vertices", UNSET))

        bt_export_model_edge_1782 = cls(
            bt_type=bt_type,
            curve=curve,
            geometry=geometry,
            id=id,
            vertices=vertices,
        )

        bt_export_model_edge_1782.additional_properties = d
        return bt_export_model_edge_1782

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
