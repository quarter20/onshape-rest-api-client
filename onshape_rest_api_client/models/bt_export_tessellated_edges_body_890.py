from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_export_tessellated_edges_edge_1364 import BTExportTessellatedEdgesEdge1364


T = TypeVar("T", bound="BTExportTessellatedEdgesBody890")


@_attrs_define
class BTExportTessellatedEdgesBody890:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        constituents (list[str] | Unset):
        id (str | Unset):
        name (str | Unset):
        edges (list[BTExportTessellatedEdgesEdge1364] | Unset):
    """

    bt_type: str | Unset = UNSET
    constituents: list[str] | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    edges: list[BTExportTessellatedEdgesEdge1364] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        constituents: list[str] | Unset = UNSET
        if not isinstance(self.constituents, Unset):
            constituents = self.constituents

        id = self.id

        name = self.name

        edges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.edges, Unset):
            edges = []
            for edges_item_data in self.edges:
                edges_item = edges_item_data.to_dict()
                edges.append(edges_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if constituents is not UNSET:
            field_dict["constituents"] = constituents
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if edges is not UNSET:
            field_dict["edges"] = edges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_export_tessellated_edges_edge_1364 import BTExportTessellatedEdgesEdge1364

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        constituents = cast(list[str], d.pop("constituents", UNSET))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _edges = d.pop("edges", UNSET)
        edges: list[BTExportTessellatedEdgesEdge1364] | Unset = UNSET
        if _edges is not UNSET:
            edges = []
            for edges_item_data in _edges:
                edges_item = BTExportTessellatedEdgesEdge1364.from_dict(edges_item_data)

                edges.append(edges_item)

        bt_export_tessellated_edges_body_890 = cls(
            bt_type=bt_type,
            constituents=constituents,
            id=id,
            name=name,
            edges=edges,
        )

        bt_export_tessellated_edges_body_890.additional_properties = d
        return bt_export_tessellated_edges_body_890

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
