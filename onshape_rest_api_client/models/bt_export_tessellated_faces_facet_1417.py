from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_vector_2d1812 import BTVector2D1812
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTExportTessellatedFacesFacet1417")


@_attrs_define
class BTExportTessellatedFacesFacet1417:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        indices (list[int] | Unset):
        normal (BTVector3D389 | Unset):
        normals (list[BTVector3D389] | Unset):
        texture_coordinates (list[BTVector2D1812] | Unset):
        vertices (list[BTVector3D389] | Unset):
    """

    bt_type: str | Unset = UNSET
    indices: list[int] | Unset = UNSET
    normal: BTVector3D389 | Unset = UNSET
    normals: list[BTVector3D389] | Unset = UNSET
    texture_coordinates: list[BTVector2D1812] | Unset = UNSET
    vertices: list[BTVector3D389] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        indices: list[int] | Unset = UNSET
        if not isinstance(self.indices, Unset):
            indices = self.indices

        normal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.normal, Unset):
            normal = self.normal.to_dict()

        normals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.normals, Unset):
            normals = []
            for normals_item_data in self.normals:
                normals_item = normals_item_data.to_dict()
                normals.append(normals_item)

        texture_coordinates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.texture_coordinates, Unset):
            texture_coordinates = []
            for texture_coordinates_item_data in self.texture_coordinates:
                texture_coordinates_item = texture_coordinates_item_data.to_dict()
                texture_coordinates.append(texture_coordinates_item)

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
        if indices is not UNSET:
            field_dict["indices"] = indices
        if normal is not UNSET:
            field_dict["normal"] = normal
        if normals is not UNSET:
            field_dict["normals"] = normals
        if texture_coordinates is not UNSET:
            field_dict["textureCoordinates"] = texture_coordinates
        if vertices is not UNSET:
            field_dict["vertices"] = vertices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_vector_2d1812 import BTVector2D1812
        from ..models.bt_vector_3d389 import BTVector3D389

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        indices = cast(list[int], d.pop("indices", UNSET))

        _normal = d.pop("normal", UNSET)
        normal: BTVector3D389 | Unset
        if isinstance(_normal, Unset):
            normal = UNSET
        else:
            normal = BTVector3D389.from_dict(_normal)

        _normals = d.pop("normals", UNSET)
        normals: list[BTVector3D389] | Unset = UNSET
        if _normals is not UNSET:
            normals = []
            for normals_item_data in _normals:
                normals_item = BTVector3D389.from_dict(normals_item_data)

                normals.append(normals_item)

        _texture_coordinates = d.pop("textureCoordinates", UNSET)
        texture_coordinates: list[BTVector2D1812] | Unset = UNSET
        if _texture_coordinates is not UNSET:
            texture_coordinates = []
            for texture_coordinates_item_data in _texture_coordinates:
                texture_coordinates_item = BTVector2D1812.from_dict(texture_coordinates_item_data)

                texture_coordinates.append(texture_coordinates_item)

        _vertices = d.pop("vertices", UNSET)
        vertices: list[BTVector3D389] | Unset = UNSET
        if _vertices is not UNSET:
            vertices = []
            for vertices_item_data in _vertices:
                vertices_item = BTVector3D389.from_dict(vertices_item_data)

                vertices.append(vertices_item)

        bt_export_tessellated_faces_facet_1417 = cls(
            bt_type=bt_type,
            indices=indices,
            normal=normal,
            normals=normals,
            texture_coordinates=texture_coordinates,
            vertices=vertices,
        )

        bt_export_tessellated_faces_facet_1417.additional_properties = d
        return bt_export_tessellated_faces_facet_1417

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
