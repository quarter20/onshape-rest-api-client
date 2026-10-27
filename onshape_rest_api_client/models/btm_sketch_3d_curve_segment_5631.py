from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_curve_geometry_3d3354 import BTCurveGeometry3D3354
    from ..models.btm_parameter_1 import BTMParameter1


T = TypeVar("T", bound="BTMSketch3DCurveSegment5631")


@_attrs_define
class BTMSketch3DCurveSegment5631:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Microversion that resulted from the import.
        node_id (str | Unset):
        entity_id (str | Unset):
        parameters (list[BTMParameter1] | Unset):
        is_construction (bool | Unset):
        geometry (BTCurveGeometry3D3354 | Unset):
        internal_ids (list[str] | Unset):
        end_point_id (str | Unset):
        start_point_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    node_id: str | Unset = UNSET
    entity_id: str | Unset = UNSET
    parameters: list[BTMParameter1] | Unset = UNSET
    is_construction: bool | Unset = UNSET
    geometry: BTCurveGeometry3D3354 | Unset = UNSET
    internal_ids: list[str] | Unset = UNSET
    end_point_id: str | Unset = UNSET
    start_point_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        node_id = self.node_id

        entity_id = self.entity_id

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        is_construction = self.is_construction

        geometry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.geometry, Unset):
            geometry = self.geometry.to_dict()

        internal_ids: list[str] | Unset = UNSET
        if not isinstance(self.internal_ids, Unset):
            internal_ids = self.internal_ids

        end_point_id = self.end_point_id

        start_point_id = self.start_point_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if is_construction is not UNSET:
            field_dict["isConstruction"] = is_construction
        if geometry is not UNSET:
            field_dict["geometry"] = geometry
        if internal_ids is not UNSET:
            field_dict["internalIds"] = internal_ids
        if end_point_id is not UNSET:
            field_dict["endPointId"] = end_point_id
        if start_point_id is not UNSET:
            field_dict["startPointId"] = start_point_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_curve_geometry_3d3354 import BTCurveGeometry3D3354  # noqa: PLC0415
        from ..models.btm_parameter_1 import BTMParameter1  # noqa: PLC0415

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        node_id = d.pop("nodeId", UNSET)

        entity_id = d.pop("entityId", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: list[BTMParameter1] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = BTMParameter1.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        is_construction = d.pop("isConstruction", UNSET)

        _geometry = d.pop("geometry", UNSET)
        geometry: BTCurveGeometry3D3354 | Unset
        if isinstance(_geometry, Unset):
            geometry = UNSET
        else:
            geometry = BTCurveGeometry3D3354.from_dict(_geometry)

        internal_ids = cast(list[str], d.pop("internalIds", UNSET))

        end_point_id = d.pop("endPointId", UNSET)

        start_point_id = d.pop("startPointId", UNSET)

        btm_sketch_3d_curve_segment_5631 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            node_id=node_id,
            entity_id=entity_id,
            parameters=parameters,
            is_construction=is_construction,
            geometry=geometry,
            internal_ids=internal_ids,
            end_point_id=end_point_id,
            start_point_id=start_point_id,
        )

        btm_sketch_3d_curve_segment_5631.additional_properties = d
        return btm_sketch_3d_curve_segment_5631

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
