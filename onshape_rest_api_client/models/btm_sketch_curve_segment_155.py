from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_sketch_entity_type import GBTSketchEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btm_parameter_1 import BTMParameter1
    from ..models.combined_sketch_entity_type import CombinedSketchEntityType


T = TypeVar("T", bound="BTMSketchCurveSegment155")


@_attrs_define
class BTMSketchCurveSegment155:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Element microversion that is being imported.
        node_id (str | Unset):
        combined_sketch_entity_type (CombinedSketchEntityType | Unset):
        entity_id (str | Unset):
        entity_id_and_replace_in_dependent_fields (str | Unset):
        index (int | Unset):
        name (str | Unset):
        namespace (str | Unset):
        parameters (list[BTMParameter1] | Unset):
        control_box_ids (list[str] | Unset):
        entity_type (GBTSketchEntityType | Unset):
        function_name (str | Unset):
        is_construction (bool | Unset):
        is_from_endpoint_spline_handle (bool | Unset):
        is_from_spline_control_polygon (bool | Unset):
        is_from_spline_handle (bool | Unset):
        center_id (str | Unset):
        curved_text_ids (list[str] | Unset):
        internal_ids (list[str] | Unset):
        end_param (float | Unset):
        end_point_id (str | Unset):
        offset_curve_extensions (list[float] | Unset):
        start_param (float | Unset):
        start_point_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    node_id: str | Unset = UNSET
    combined_sketch_entity_type: CombinedSketchEntityType | Unset = UNSET
    entity_id: str | Unset = UNSET
    entity_id_and_replace_in_dependent_fields: str | Unset = UNSET
    index: int | Unset = UNSET
    name: str | Unset = UNSET
    namespace: str | Unset = UNSET
    parameters: list[BTMParameter1] | Unset = UNSET
    control_box_ids: list[str] | Unset = UNSET
    entity_type: GBTSketchEntityType | Unset = UNSET
    function_name: str | Unset = UNSET
    is_construction: bool | Unset = UNSET
    is_from_endpoint_spline_handle: bool | Unset = UNSET
    is_from_spline_control_polygon: bool | Unset = UNSET
    is_from_spline_handle: bool | Unset = UNSET
    center_id: str | Unset = UNSET
    curved_text_ids: list[str] | Unset = UNSET
    internal_ids: list[str] | Unset = UNSET
    end_param: float | Unset = UNSET
    end_point_id: str | Unset = UNSET
    offset_curve_extensions: list[float] | Unset = UNSET
    start_param: float | Unset = UNSET
    start_point_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        node_id = self.node_id

        combined_sketch_entity_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.combined_sketch_entity_type, Unset):
            combined_sketch_entity_type = self.combined_sketch_entity_type.to_dict()

        entity_id = self.entity_id

        entity_id_and_replace_in_dependent_fields = self.entity_id_and_replace_in_dependent_fields

        index = self.index

        name = self.name

        namespace = self.namespace

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        control_box_ids: list[str] | Unset = UNSET
        if not isinstance(self.control_box_ids, Unset):
            control_box_ids = self.control_box_ids

        entity_type: str | Unset = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        function_name = self.function_name

        is_construction = self.is_construction

        is_from_endpoint_spline_handle = self.is_from_endpoint_spline_handle

        is_from_spline_control_polygon = self.is_from_spline_control_polygon

        is_from_spline_handle = self.is_from_spline_handle

        center_id = self.center_id

        curved_text_ids: list[str] | Unset = UNSET
        if not isinstance(self.curved_text_ids, Unset):
            curved_text_ids = self.curved_text_ids

        internal_ids: list[str] | Unset = UNSET
        if not isinstance(self.internal_ids, Unset):
            internal_ids = self.internal_ids

        end_param = self.end_param

        end_point_id = self.end_point_id

        offset_curve_extensions: list[float] | Unset = UNSET
        if not isinstance(self.offset_curve_extensions, Unset):
            offset_curve_extensions = self.offset_curve_extensions

        start_param = self.start_param

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
        if combined_sketch_entity_type is not UNSET:
            field_dict["combinedSketchEntityType"] = combined_sketch_entity_type
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity_id_and_replace_in_dependent_fields is not UNSET:
            field_dict["entityIdAndReplaceInDependentFields"] = entity_id_and_replace_in_dependent_fields
        if index is not UNSET:
            field_dict["index"] = index
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if control_box_ids is not UNSET:
            field_dict["controlBoxIds"] = control_box_ids
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if function_name is not UNSET:
            field_dict["functionName"] = function_name
        if is_construction is not UNSET:
            field_dict["isConstruction"] = is_construction
        if is_from_endpoint_spline_handle is not UNSET:
            field_dict["isFromEndpointSplineHandle"] = is_from_endpoint_spline_handle
        if is_from_spline_control_polygon is not UNSET:
            field_dict["isFromSplineControlPolygon"] = is_from_spline_control_polygon
        if is_from_spline_handle is not UNSET:
            field_dict["isFromSplineHandle"] = is_from_spline_handle
        if center_id is not UNSET:
            field_dict["centerId"] = center_id
        if curved_text_ids is not UNSET:
            field_dict["curvedTextIds"] = curved_text_ids
        if internal_ids is not UNSET:
            field_dict["internalIds"] = internal_ids
        if end_param is not UNSET:
            field_dict["endParam"] = end_param
        if end_point_id is not UNSET:
            field_dict["endPointId"] = end_point_id
        if offset_curve_extensions is not UNSET:
            field_dict["offsetCurveExtensions"] = offset_curve_extensions
        if start_param is not UNSET:
            field_dict["startParam"] = start_param
        if start_point_id is not UNSET:
            field_dict["startPointId"] = start_point_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btm_parameter_1 import BTMParameter1
        from ..models.combined_sketch_entity_type import CombinedSketchEntityType

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _combined_sketch_entity_type = d.pop("combinedSketchEntityType", UNSET)
        combined_sketch_entity_type: CombinedSketchEntityType | Unset
        if isinstance(_combined_sketch_entity_type, Unset):
            combined_sketch_entity_type = UNSET
        else:
            combined_sketch_entity_type = CombinedSketchEntityType.from_dict(_combined_sketch_entity_type)

        entity_id = d.pop("entityId", UNSET)

        entity_id_and_replace_in_dependent_fields = d.pop("entityIdAndReplaceInDependentFields", UNSET)

        index = d.pop("index", UNSET)

        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: list[BTMParameter1] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = BTMParameter1.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        control_box_ids = cast(list[str], d.pop("controlBoxIds", UNSET))

        _entity_type = d.pop("entityType", UNSET)
        entity_type: GBTSketchEntityType | Unset
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = GBTSketchEntityType(_entity_type)

        function_name = d.pop("functionName", UNSET)

        is_construction = d.pop("isConstruction", UNSET)

        is_from_endpoint_spline_handle = d.pop("isFromEndpointSplineHandle", UNSET)

        is_from_spline_control_polygon = d.pop("isFromSplineControlPolygon", UNSET)

        is_from_spline_handle = d.pop("isFromSplineHandle", UNSET)

        center_id = d.pop("centerId", UNSET)

        curved_text_ids = cast(list[str], d.pop("curvedTextIds", UNSET))

        internal_ids = cast(list[str], d.pop("internalIds", UNSET))

        end_param = d.pop("endParam", UNSET)

        end_point_id = d.pop("endPointId", UNSET)

        offset_curve_extensions = cast(list[float], d.pop("offsetCurveExtensions", UNSET))

        start_param = d.pop("startParam", UNSET)

        start_point_id = d.pop("startPointId", UNSET)

        btm_sketch_curve_segment_155 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            node_id=node_id,
            combined_sketch_entity_type=combined_sketch_entity_type,
            entity_id=entity_id,
            entity_id_and_replace_in_dependent_fields=entity_id_and_replace_in_dependent_fields,
            index=index,
            name=name,
            namespace=namespace,
            parameters=parameters,
            control_box_ids=control_box_ids,
            entity_type=entity_type,
            function_name=function_name,
            is_construction=is_construction,
            is_from_endpoint_spline_handle=is_from_endpoint_spline_handle,
            is_from_spline_control_polygon=is_from_spline_control_polygon,
            is_from_spline_handle=is_from_spline_handle,
            center_id=center_id,
            curved_text_ids=curved_text_ids,
            internal_ids=internal_ids,
            end_param=end_param,
            end_point_id=end_point_id,
            offset_curve_extensions=offset_curve_extensions,
            start_param=start_param,
            start_point_id=start_point_id,
        )

        btm_sketch_curve_segment_155.additional_properties = d
        return btm_sketch_curve_segment_155

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
