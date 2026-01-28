from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_edge_topology import GBTEdgeTopology
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTEdgeTopologyFilter122")


@_attrs_define
class BTEdgeTopologyFilter122:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        edge_topology (GBTEdgeTopology | Unset):
        is_internal_edge (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    edge_topology: GBTEdgeTopology | Unset = UNSET
    is_internal_edge: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        edge_topology: str | Unset = UNSET
        if not isinstance(self.edge_topology, Unset):
            edge_topology = self.edge_topology.value

        is_internal_edge = self.is_internal_edge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if edge_topology is not UNSET:
            field_dict["edgeTopology"] = edge_topology
        if is_internal_edge is not UNSET:
            field_dict["isInternalEdge"] = is_internal_edge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _edge_topology = d.pop("edgeTopology", UNSET)
        edge_topology: GBTEdgeTopology | Unset
        if isinstance(_edge_topology, Unset):
            edge_topology = UNSET
        else:
            edge_topology = GBTEdgeTopology(_edge_topology)

        is_internal_edge = d.pop("isInternalEdge", UNSET)

        bt_edge_topology_filter_122 = cls(
            bt_type=bt_type,
            edge_topology=edge_topology,
            is_internal_edge=is_internal_edge,
        )

        bt_edge_topology_filter_122.additional_properties = d
        return bt_edge_topology_filter_122

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
