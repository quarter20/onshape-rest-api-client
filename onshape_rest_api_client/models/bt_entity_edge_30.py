from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_edge_type import GBTEdgeType
from ..models.gbt_entity_edge_smoothness_status import GBTEntityEdgeSmoothnessStatus
from ..models.gbt_mesh_state import GBTMeshState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_entity_geometry_35 import BTEntityGeometry35
    from ..models.bt_immutable_byte_array import BTImmutableByteArray
    from ..models.bt_immutable_float_array import BTImmutableFloatArray


T = TypeVar("T", bound="BTEntityEdge30")


@_attrs_define
class BTEntityEdge30:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        compressed (bool | Unset):
        decompressed (BTEntityGeometry35 | Unset):
        error_code (int | Unset):
        estimated_memory_usage_in_bytes (int | Unset):
        has_tessellation_error (bool | Unset):
        setting_index (int | Unset):
        compressed_points (BTImmutableByteArray | Unset):
        edge_smoothness_status (GBTEntityEdgeSmoothnessStatus | Unset):
        edge_type (GBTEdgeType | Unset):
        is_closed (bool | Unset):
        is_internal_edge (bool | Unset):
        mesh_state (GBTMeshState | Unset):
        points (BTImmutableFloatArray | Unset):
    """

    bt_type: str | Unset = UNSET
    compressed: bool | Unset = UNSET
    decompressed: BTEntityGeometry35 | Unset = UNSET
    error_code: int | Unset = UNSET
    estimated_memory_usage_in_bytes: int | Unset = UNSET
    has_tessellation_error: bool | Unset = UNSET
    setting_index: int | Unset = UNSET
    compressed_points: BTImmutableByteArray | Unset = UNSET
    edge_smoothness_status: GBTEntityEdgeSmoothnessStatus | Unset = UNSET
    edge_type: GBTEdgeType | Unset = UNSET
    is_closed: bool | Unset = UNSET
    is_internal_edge: bool | Unset = UNSET
    mesh_state: GBTMeshState | Unset = UNSET
    points: BTImmutableFloatArray | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        compressed = self.compressed

        decompressed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.decompressed, Unset):
            decompressed = self.decompressed.to_dict()

        error_code = self.error_code

        estimated_memory_usage_in_bytes = self.estimated_memory_usage_in_bytes

        has_tessellation_error = self.has_tessellation_error

        setting_index = self.setting_index

        compressed_points: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compressed_points, Unset):
            compressed_points = self.compressed_points.to_dict()

        edge_smoothness_status: str | Unset = UNSET
        if not isinstance(self.edge_smoothness_status, Unset):
            edge_smoothness_status = self.edge_smoothness_status.value

        edge_type: str | Unset = UNSET
        if not isinstance(self.edge_type, Unset):
            edge_type = self.edge_type.value

        is_closed = self.is_closed

        is_internal_edge = self.is_internal_edge

        mesh_state: str | Unset = UNSET
        if not isinstance(self.mesh_state, Unset):
            mesh_state = self.mesh_state.value

        points: dict[str, Any] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = self.points.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if compressed is not UNSET:
            field_dict["compressed"] = compressed
        if decompressed is not UNSET:
            field_dict["decompressed"] = decompressed
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if estimated_memory_usage_in_bytes is not UNSET:
            field_dict["estimatedMemoryUsageInBytes"] = estimated_memory_usage_in_bytes
        if has_tessellation_error is not UNSET:
            field_dict["hasTessellationError"] = has_tessellation_error
        if setting_index is not UNSET:
            field_dict["settingIndex"] = setting_index
        if compressed_points is not UNSET:
            field_dict["compressedPoints"] = compressed_points
        if edge_smoothness_status is not UNSET:
            field_dict["edgeSmoothnessStatus"] = edge_smoothness_status
        if edge_type is not UNSET:
            field_dict["edgeType"] = edge_type
        if is_closed is not UNSET:
            field_dict["isClosed"] = is_closed
        if is_internal_edge is not UNSET:
            field_dict["isInternalEdge"] = is_internal_edge
        if mesh_state is not UNSET:
            field_dict["meshState"] = mesh_state
        if points is not UNSET:
            field_dict["points"] = points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_entity_geometry_35 import BTEntityGeometry35
        from ..models.bt_immutable_byte_array import BTImmutableByteArray
        from ..models.bt_immutable_float_array import BTImmutableFloatArray

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        compressed = d.pop("compressed", UNSET)

        _decompressed = d.pop("decompressed", UNSET)
        decompressed: BTEntityGeometry35 | Unset
        if isinstance(_decompressed, Unset):
            decompressed = UNSET
        else:
            decompressed = BTEntityGeometry35.from_dict(_decompressed)

        error_code = d.pop("errorCode", UNSET)

        estimated_memory_usage_in_bytes = d.pop("estimatedMemoryUsageInBytes", UNSET)

        has_tessellation_error = d.pop("hasTessellationError", UNSET)

        setting_index = d.pop("settingIndex", UNSET)

        _compressed_points = d.pop("compressedPoints", UNSET)
        compressed_points: BTImmutableByteArray | Unset
        if isinstance(_compressed_points, Unset):
            compressed_points = UNSET
        else:
            compressed_points = BTImmutableByteArray.from_dict(_compressed_points)

        _edge_smoothness_status = d.pop("edgeSmoothnessStatus", UNSET)
        edge_smoothness_status: GBTEntityEdgeSmoothnessStatus | Unset
        if isinstance(_edge_smoothness_status, Unset):
            edge_smoothness_status = UNSET
        else:
            edge_smoothness_status = GBTEntityEdgeSmoothnessStatus(_edge_smoothness_status)

        _edge_type = d.pop("edgeType", UNSET)
        edge_type: GBTEdgeType | Unset
        if isinstance(_edge_type, Unset):
            edge_type = UNSET
        else:
            edge_type = GBTEdgeType(_edge_type)

        is_closed = d.pop("isClosed", UNSET)

        is_internal_edge = d.pop("isInternalEdge", UNSET)

        _mesh_state = d.pop("meshState", UNSET)
        mesh_state: GBTMeshState | Unset
        if isinstance(_mesh_state, Unset):
            mesh_state = UNSET
        else:
            mesh_state = GBTMeshState(_mesh_state)

        _points = d.pop("points", UNSET)
        points: BTImmutableFloatArray | Unset
        if isinstance(_points, Unset):
            points = UNSET
        else:
            points = BTImmutableFloatArray.from_dict(_points)

        bt_entity_edge_30 = cls(
            bt_type=bt_type,
            compressed=compressed,
            decompressed=decompressed,
            error_code=error_code,
            estimated_memory_usage_in_bytes=estimated_memory_usage_in_bytes,
            has_tessellation_error=has_tessellation_error,
            setting_index=setting_index,
            compressed_points=compressed_points,
            edge_smoothness_status=edge_smoothness_status,
            edge_type=edge_type,
            is_closed=is_closed,
            is_internal_edge=is_internal_edge,
            mesh_state=mesh_state,
            points=points,
        )

        bt_entity_edge_30.additional_properties = d
        return bt_entity_edge_30

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
