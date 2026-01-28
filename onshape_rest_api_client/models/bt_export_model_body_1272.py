from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_body_type import GBTBodyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_export_body_properties_3559 import BTExportBodyProperties3559
    from ..models.bt_export_model_edge_1782 import BTExportModelEdge1782
    from ..models.bt_export_model_face_1363 import BTExportModelFace1363
    from ..models.bt_export_model_vertex_858 import BTExportModelVertex858


T = TypeVar("T", bound="BTExportModelBody1272")


@_attrs_define
class BTExportModelBody1272:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        closed (bool | Unset): If type == COMPOSITE, indicates whether it is open or closed.
        constituent_body_ids (list[str] | Unset):
        consumed_by_composite (bool | Unset): Indicates if there is a closed composite that consumes this body.
        edges (list[BTExportModelEdge1782] | Unset):
        faces (list[BTExportModelFace1363] | Unset):
        id (str | Unset):
        properties (BTExportBodyProperties3559 | Unset):
        type_ (GBTBodyType | Unset):
        vertices (list[BTExportModelVertex858] | Unset):
    """

    bt_type: str | Unset = UNSET
    closed: bool | Unset = UNSET
    constituent_body_ids: list[str] | Unset = UNSET
    consumed_by_composite: bool | Unset = UNSET
    edges: list[BTExportModelEdge1782] | Unset = UNSET
    faces: list[BTExportModelFace1363] | Unset = UNSET
    id: str | Unset = UNSET
    properties: BTExportBodyProperties3559 | Unset = UNSET
    type_: GBTBodyType | Unset = UNSET
    vertices: list[BTExportModelVertex858] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        closed = self.closed

        constituent_body_ids: list[str] | Unset = UNSET
        if not isinstance(self.constituent_body_ids, Unset):
            constituent_body_ids = self.constituent_body_ids

        consumed_by_composite = self.consumed_by_composite

        edges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.edges, Unset):
            edges = []
            for edges_item_data in self.edges:
                edges_item = edges_item_data.to_dict()
                edges.append(edges_item)

        faces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.faces, Unset):
            faces = []
            for faces_item_data in self.faces:
                faces_item = faces_item_data.to_dict()
                faces.append(faces_item)

        id = self.id

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

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
        if closed is not UNSET:
            field_dict["closed"] = closed
        if constituent_body_ids is not UNSET:
            field_dict["constituentBodyIds"] = constituent_body_ids
        if consumed_by_composite is not UNSET:
            field_dict["consumedByComposite"] = consumed_by_composite
        if edges is not UNSET:
            field_dict["edges"] = edges
        if faces is not UNSET:
            field_dict["faces"] = faces
        if id is not UNSET:
            field_dict["id"] = id
        if properties is not UNSET:
            field_dict["properties"] = properties
        if type_ is not UNSET:
            field_dict["type"] = type_
        if vertices is not UNSET:
            field_dict["vertices"] = vertices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_export_body_properties_3559 import BTExportBodyProperties3559
        from ..models.bt_export_model_edge_1782 import BTExportModelEdge1782
        from ..models.bt_export_model_face_1363 import BTExportModelFace1363
        from ..models.bt_export_model_vertex_858 import BTExportModelVertex858

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        closed = d.pop("closed", UNSET)

        constituent_body_ids = cast(list[str], d.pop("constituentBodyIds", UNSET))

        consumed_by_composite = d.pop("consumedByComposite", UNSET)

        _edges = d.pop("edges", UNSET)
        edges: list[BTExportModelEdge1782] | Unset = UNSET
        if _edges is not UNSET:
            edges = []
            for edges_item_data in _edges:
                edges_item = BTExportModelEdge1782.from_dict(edges_item_data)

                edges.append(edges_item)

        _faces = d.pop("faces", UNSET)
        faces: list[BTExportModelFace1363] | Unset = UNSET
        if _faces is not UNSET:
            faces = []
            for faces_item_data in _faces:
                faces_item = BTExportModelFace1363.from_dict(faces_item_data)

                faces.append(faces_item)

        id = d.pop("id", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: BTExportBodyProperties3559 | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = BTExportBodyProperties3559.from_dict(_properties)

        _type_ = d.pop("type", UNSET)
        type_: GBTBodyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GBTBodyType(_type_)

        _vertices = d.pop("vertices", UNSET)
        vertices: list[BTExportModelVertex858] | Unset = UNSET
        if _vertices is not UNSET:
            vertices = []
            for vertices_item_data in _vertices:
                vertices_item = BTExportModelVertex858.from_dict(vertices_item_data)

                vertices.append(vertices_item)

        bt_export_model_body_1272 = cls(
            bt_type=bt_type,
            closed=closed,
            constituent_body_ids=constituent_body_ids,
            consumed_by_composite=consumed_by_composite,
            edges=edges,
            faces=faces,
            id=id,
            properties=properties,
            type_=type_,
            vertices=vertices,
        )

        bt_export_model_body_1272.additional_properties = d
        return bt_export_model_body_1272

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
