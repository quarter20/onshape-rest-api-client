from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTExportTessellatedEdgesEdge1364")


@_attrs_define
class BTExportTessellatedEdgesEdge1364:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        id (str | Unset):
        vertices (list[BTVector3D389] | Unset):
    """

    bt_type: str | Unset = UNSET
    id: str | Unset = UNSET
    vertices: list[BTVector3D389] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        id = self.id

        vertices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vertices, Unset):
            vertices = []
            for vertices_item_data in self.vertices:
                vertices_item = vertices_item_data.to_dict()
                vertices.append(vertices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if id is not UNSET:
            field_dict["id"] = id
        if vertices is not UNSET:
            field_dict["vertices"] = vertices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_vector_3d389 import BTVector3D389

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        id = d.pop("id", UNSET)

        _vertices = d.pop("vertices", UNSET)
        vertices: list[BTVector3D389] | Unset = UNSET
        if _vertices is not UNSET:
            vertices = []
            for vertices_item_data in _vertices:
                vertices_item = BTVector3D389.from_dict(vertices_item_data)

                vertices.append(vertices_item)

        bt_export_tessellated_edges_edge_1364 = cls(
            bt_type=bt_type,
            id=id,
            vertices=vertices,
        )

        bt_export_tessellated_edges_edge_1364.additional_properties = d
        return bt_export_tessellated_edges_edge_1364

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
