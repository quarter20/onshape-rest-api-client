from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_annotation_element_display_data_894 import BTAnnotationElementDisplayData894
    from ..models.bt_assembly_feature_display_data_1783 import BTAssemblyFeatureDisplayData1783
    from ..models.bt_element_display_data_326 import BTElementDisplayData326
    from ..models.bt_full_element_id_756 import BTFullElementId756
    from ..models.bt_geometry_mate_display_data_1050 import BTGeometryMateDisplayData1050
    from ..models.bt_load_display_data_837 import BTLoadDisplayData837
    from ..models.bt_mate_connector_display_data_94 import BTMateConnectorDisplayData94
    from ..models.bt_mate_display_data_1358 import BTMateDisplayData1358
    from ..models.bt_mate_group_display_data_1990 import BTMateGroupDisplayData1990
    from ..models.bt_microversion_id_366 import BTMicroversionId366
    from ..models.bt_microversion_id_and_configuration_interval_2364 import BTMicroversionIdAndConfigurationInterval2364
    from ..models.bt_microversion_id_interval_367 import BTMicroversionIdInterval367
    from ..models.bt_occurrence_74 import BTOccurrence74
    from ..models.bt_occurrence_display_data_95 import BTOccurrenceDisplayData95
    from ..models.bt_origin_display_data_934 import BTOriginDisplayData934
    from ..models.bt_part_studio_display_data_base_2751 import BTPartStudioDisplayDataBase2751
    from ..models.bt_root_assembly_display_data_96_full_element_id_to_referenced_sketch_ids import (
        BTRootAssemblyDisplayData96FullElementIdToReferencedSketchIds,
    )


T = TypeVar("T", bound="BTRootAssemblyDisplayData96")


@_attrs_define
class BTRootAssemblyDisplayData96:
    """
    Attributes:
        annotations_for_element (BTAnnotationElementDisplayData894 | Unset):
        assembly_features (list[BTAssemblyFeatureDisplayData1783] | Unset):
        bt_type (str | Unset): Type of JSON object.
        build_duration_millis (float | Unset):
        deleted_assembly_features (list[str] | Unset):
        deleted_geometry_mate_ids (list[str] | Unset):
        deleted_loads (list[str] | Unset):
        deleted_mate_connector_ids (list[str] | Unset):
        deleted_mate_group_ids (list[str] | Unset):
        deleted_mate_ids (list[str] | Unset):
        deleted_occurrences (list[BTOccurrence74] | Unset):
        element_id (str | Unset):
        from_full_element_id (BTFullElementId756 | Unset):
        full_element_id (BTFullElementId756 | Unset):
        full_element_id_to_referenced_sketch_ids (BTRootAssemblyDisplayData96FullElementIdToReferencedSketchIds |
            Unset):
        geometry_mates (list[BTGeometryMateDisplayData1050] | Unset):
        incremental (bool | Unset):
        instance_count (int | Unset):
        is_collapsible (bool | Unset):
        is_for_in_context (bool | Unset):
        keep_from_microversion (bool | Unset):
        loads (list[BTLoadDisplayData837] | Unset):
        mate_connectors (list[BTMateConnectorDisplayData94] | Unset):
        mate_groups (list[BTMateGroupDisplayData1990] | Unset):
        mates (list[BTMateDisplayData1358] | Unset):
        microversion_id (BTMicroversionId366 | Unset):
        microversion_id_and_configuration_interval (BTMicroversionIdAndConfigurationInterval2364 | Unset):
        microversion_interval (BTMicroversionIdInterval367 | Unset):
        occurrences (list[BTOccurrenceDisplayData95] | Unset):
        origin_display_data (BTOriginDisplayData934 | Unset):
        part_studio_display_data (list[BTPartStudioDisplayDataBase2751] | Unset):
        quick_summary (str | Unset):
        sent_time_iso (str | Unset):
        version_for_rasterization (BTElementDisplayData326 | Unset):
    """

    annotations_for_element: BTAnnotationElementDisplayData894 | Unset = UNSET
    assembly_features: list[BTAssemblyFeatureDisplayData1783] | Unset = UNSET
    bt_type: str | Unset = UNSET
    build_duration_millis: float | Unset = UNSET
    deleted_assembly_features: list[str] | Unset = UNSET
    deleted_geometry_mate_ids: list[str] | Unset = UNSET
    deleted_loads: list[str] | Unset = UNSET
    deleted_mate_connector_ids: list[str] | Unset = UNSET
    deleted_mate_group_ids: list[str] | Unset = UNSET
    deleted_mate_ids: list[str] | Unset = UNSET
    deleted_occurrences: list[BTOccurrence74] | Unset = UNSET
    element_id: str | Unset = UNSET
    from_full_element_id: BTFullElementId756 | Unset = UNSET
    full_element_id: BTFullElementId756 | Unset = UNSET
    full_element_id_to_referenced_sketch_ids: BTRootAssemblyDisplayData96FullElementIdToReferencedSketchIds | Unset = (
        UNSET
    )
    geometry_mates: list[BTGeometryMateDisplayData1050] | Unset = UNSET
    incremental: bool | Unset = UNSET
    instance_count: int | Unset = UNSET
    is_collapsible: bool | Unset = UNSET
    is_for_in_context: bool | Unset = UNSET
    keep_from_microversion: bool | Unset = UNSET
    loads: list[BTLoadDisplayData837] | Unset = UNSET
    mate_connectors: list[BTMateConnectorDisplayData94] | Unset = UNSET
    mate_groups: list[BTMateGroupDisplayData1990] | Unset = UNSET
    mates: list[BTMateDisplayData1358] | Unset = UNSET
    microversion_id: BTMicroversionId366 | Unset = UNSET
    microversion_id_and_configuration_interval: BTMicroversionIdAndConfigurationInterval2364 | Unset = UNSET
    microversion_interval: BTMicroversionIdInterval367 | Unset = UNSET
    occurrences: list[BTOccurrenceDisplayData95] | Unset = UNSET
    origin_display_data: BTOriginDisplayData934 | Unset = UNSET
    part_studio_display_data: list[BTPartStudioDisplayDataBase2751] | Unset = UNSET
    quick_summary: str | Unset = UNSET
    sent_time_iso: str | Unset = UNSET
    version_for_rasterization: BTElementDisplayData326 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotations_for_element: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotations_for_element, Unset):
            annotations_for_element = self.annotations_for_element.to_dict()

        assembly_features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assembly_features, Unset):
            assembly_features = []
            for assembly_features_item_data in self.assembly_features:
                assembly_features_item = assembly_features_item_data.to_dict()
                assembly_features.append(assembly_features_item)

        bt_type = self.bt_type

        build_duration_millis = self.build_duration_millis

        deleted_assembly_features: list[str] | Unset = UNSET
        if not isinstance(self.deleted_assembly_features, Unset):
            deleted_assembly_features = self.deleted_assembly_features

        deleted_geometry_mate_ids: list[str] | Unset = UNSET
        if not isinstance(self.deleted_geometry_mate_ids, Unset):
            deleted_geometry_mate_ids = self.deleted_geometry_mate_ids

        deleted_loads: list[str] | Unset = UNSET
        if not isinstance(self.deleted_loads, Unset):
            deleted_loads = self.deleted_loads

        deleted_mate_connector_ids: list[str] | Unset = UNSET
        if not isinstance(self.deleted_mate_connector_ids, Unset):
            deleted_mate_connector_ids = self.deleted_mate_connector_ids

        deleted_mate_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.deleted_mate_group_ids, Unset):
            deleted_mate_group_ids = self.deleted_mate_group_ids

        deleted_mate_ids: list[str] | Unset = UNSET
        if not isinstance(self.deleted_mate_ids, Unset):
            deleted_mate_ids = self.deleted_mate_ids

        deleted_occurrences: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.deleted_occurrences, Unset):
            deleted_occurrences = []
            for deleted_occurrences_item_data in self.deleted_occurrences:
                deleted_occurrences_item = deleted_occurrences_item_data.to_dict()
                deleted_occurrences.append(deleted_occurrences_item)

        element_id = self.element_id

        from_full_element_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_full_element_id, Unset):
            from_full_element_id = self.from_full_element_id.to_dict()

        full_element_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.full_element_id, Unset):
            full_element_id = self.full_element_id.to_dict()

        full_element_id_to_referenced_sketch_ids: dict[str, Any] | Unset = UNSET
        if not isinstance(self.full_element_id_to_referenced_sketch_ids, Unset):
            full_element_id_to_referenced_sketch_ids = self.full_element_id_to_referenced_sketch_ids.to_dict()

        geometry_mates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.geometry_mates, Unset):
            geometry_mates = []
            for geometry_mates_item_data in self.geometry_mates:
                geometry_mates_item = geometry_mates_item_data.to_dict()
                geometry_mates.append(geometry_mates_item)

        incremental = self.incremental

        instance_count = self.instance_count

        is_collapsible = self.is_collapsible

        is_for_in_context = self.is_for_in_context

        keep_from_microversion = self.keep_from_microversion

        loads: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.loads, Unset):
            loads = []
            for loads_item_data in self.loads:
                loads_item = loads_item_data.to_dict()
                loads.append(loads_item)

        mate_connectors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mate_connectors, Unset):
            mate_connectors = []
            for mate_connectors_item_data in self.mate_connectors:
                mate_connectors_item = mate_connectors_item_data.to_dict()
                mate_connectors.append(mate_connectors_item)

        mate_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mate_groups, Unset):
            mate_groups = []
            for mate_groups_item_data in self.mate_groups:
                mate_groups_item = mate_groups_item_data.to_dict()
                mate_groups.append(mate_groups_item)

        mates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mates, Unset):
            mates = []
            for mates_item_data in self.mates:
                mates_item = mates_item_data.to_dict()
                mates.append(mates_item)

        microversion_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_id, Unset):
            microversion_id = self.microversion_id.to_dict()

        microversion_id_and_configuration_interval: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_id_and_configuration_interval, Unset):
            microversion_id_and_configuration_interval = self.microversion_id_and_configuration_interval.to_dict()

        microversion_interval: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_interval, Unset):
            microversion_interval = self.microversion_interval.to_dict()

        occurrences: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.occurrences, Unset):
            occurrences = []
            for occurrences_item_data in self.occurrences:
                occurrences_item = occurrences_item_data.to_dict()
                occurrences.append(occurrences_item)

        origin_display_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.origin_display_data, Unset):
            origin_display_data = self.origin_display_data.to_dict()

        part_studio_display_data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.part_studio_display_data, Unset):
            part_studio_display_data = []
            for part_studio_display_data_item_data in self.part_studio_display_data:
                part_studio_display_data_item = part_studio_display_data_item_data.to_dict()
                part_studio_display_data.append(part_studio_display_data_item)

        quick_summary = self.quick_summary

        sent_time_iso = self.sent_time_iso

        version_for_rasterization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version_for_rasterization, Unset):
            version_for_rasterization = self.version_for_rasterization.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotations_for_element is not UNSET:
            field_dict["annotationsForElement"] = annotations_for_element
        if assembly_features is not UNSET:
            field_dict["assemblyFeatures"] = assembly_features
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if build_duration_millis is not UNSET:
            field_dict["buildDurationMillis"] = build_duration_millis
        if deleted_assembly_features is not UNSET:
            field_dict["deletedAssemblyFeatures"] = deleted_assembly_features
        if deleted_geometry_mate_ids is not UNSET:
            field_dict["deletedGeometryMateIds"] = deleted_geometry_mate_ids
        if deleted_loads is not UNSET:
            field_dict["deletedLoads"] = deleted_loads
        if deleted_mate_connector_ids is not UNSET:
            field_dict["deletedMateConnectorIds"] = deleted_mate_connector_ids
        if deleted_mate_group_ids is not UNSET:
            field_dict["deletedMateGroupIds"] = deleted_mate_group_ids
        if deleted_mate_ids is not UNSET:
            field_dict["deletedMateIds"] = deleted_mate_ids
        if deleted_occurrences is not UNSET:
            field_dict["deletedOccurrences"] = deleted_occurrences
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if from_full_element_id is not UNSET:
            field_dict["fromFullElementId"] = from_full_element_id
        if full_element_id is not UNSET:
            field_dict["fullElementId"] = full_element_id
        if full_element_id_to_referenced_sketch_ids is not UNSET:
            field_dict["fullElementIdToReferencedSketchIds"] = full_element_id_to_referenced_sketch_ids
        if geometry_mates is not UNSET:
            field_dict["geometryMates"] = geometry_mates
        if incremental is not UNSET:
            field_dict["incremental"] = incremental
        if instance_count is not UNSET:
            field_dict["instanceCount"] = instance_count
        if is_collapsible is not UNSET:
            field_dict["isCollapsible"] = is_collapsible
        if is_for_in_context is not UNSET:
            field_dict["isForInContext"] = is_for_in_context
        if keep_from_microversion is not UNSET:
            field_dict["keepFromMicroversion"] = keep_from_microversion
        if loads is not UNSET:
            field_dict["loads"] = loads
        if mate_connectors is not UNSET:
            field_dict["mateConnectors"] = mate_connectors
        if mate_groups is not UNSET:
            field_dict["mateGroups"] = mate_groups
        if mates is not UNSET:
            field_dict["mates"] = mates
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id
        if microversion_id_and_configuration_interval is not UNSET:
            field_dict["microversionIdAndConfigurationInterval"] = microversion_id_and_configuration_interval
        if microversion_interval is not UNSET:
            field_dict["microversionInterval"] = microversion_interval
        if occurrences is not UNSET:
            field_dict["occurrences"] = occurrences
        if origin_display_data is not UNSET:
            field_dict["originDisplayData"] = origin_display_data
        if part_studio_display_data is not UNSET:
            field_dict["partStudioDisplayData"] = part_studio_display_data
        if quick_summary is not UNSET:
            field_dict["quickSummary"] = quick_summary
        if sent_time_iso is not UNSET:
            field_dict["sentTimeISO"] = sent_time_iso
        if version_for_rasterization is not UNSET:
            field_dict["versionForRasterization"] = version_for_rasterization

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_annotation_element_display_data_894 import BTAnnotationElementDisplayData894
        from ..models.bt_assembly_feature_display_data_1783 import BTAssemblyFeatureDisplayData1783
        from ..models.bt_element_display_data_326 import BTElementDisplayData326
        from ..models.bt_full_element_id_756 import BTFullElementId756
        from ..models.bt_geometry_mate_display_data_1050 import BTGeometryMateDisplayData1050
        from ..models.bt_load_display_data_837 import BTLoadDisplayData837
        from ..models.bt_mate_connector_display_data_94 import BTMateConnectorDisplayData94
        from ..models.bt_mate_display_data_1358 import BTMateDisplayData1358
        from ..models.bt_mate_group_display_data_1990 import BTMateGroupDisplayData1990
        from ..models.bt_microversion_id_366 import BTMicroversionId366
        from ..models.bt_microversion_id_and_configuration_interval_2364 import (
            BTMicroversionIdAndConfigurationInterval2364,
        )
        from ..models.bt_microversion_id_interval_367 import BTMicroversionIdInterval367
        from ..models.bt_occurrence_74 import BTOccurrence74
        from ..models.bt_occurrence_display_data_95 import BTOccurrenceDisplayData95
        from ..models.bt_origin_display_data_934 import BTOriginDisplayData934
        from ..models.bt_part_studio_display_data_base_2751 import BTPartStudioDisplayDataBase2751
        from ..models.bt_root_assembly_display_data_96_full_element_id_to_referenced_sketch_ids import (
            BTRootAssemblyDisplayData96FullElementIdToReferencedSketchIds,
        )

        d = dict(src_dict)
        _annotations_for_element = d.pop("annotationsForElement", UNSET)
        annotations_for_element: BTAnnotationElementDisplayData894 | Unset
        if isinstance(_annotations_for_element, Unset):
            annotations_for_element = UNSET
        else:
            annotations_for_element = BTAnnotationElementDisplayData894.from_dict(_annotations_for_element)

        _assembly_features = d.pop("assemblyFeatures", UNSET)
        assembly_features: list[BTAssemblyFeatureDisplayData1783] | Unset = UNSET
        if _assembly_features is not UNSET:
            assembly_features = []
            for assembly_features_item_data in _assembly_features:
                assembly_features_item = BTAssemblyFeatureDisplayData1783.from_dict(assembly_features_item_data)

                assembly_features.append(assembly_features_item)

        bt_type = d.pop("btType", UNSET)

        build_duration_millis = d.pop("buildDurationMillis", UNSET)

        deleted_assembly_features = cast(list[str], d.pop("deletedAssemblyFeatures", UNSET))

        deleted_geometry_mate_ids = cast(list[str], d.pop("deletedGeometryMateIds", UNSET))

        deleted_loads = cast(list[str], d.pop("deletedLoads", UNSET))

        deleted_mate_connector_ids = cast(list[str], d.pop("deletedMateConnectorIds", UNSET))

        deleted_mate_group_ids = cast(list[str], d.pop("deletedMateGroupIds", UNSET))

        deleted_mate_ids = cast(list[str], d.pop("deletedMateIds", UNSET))

        _deleted_occurrences = d.pop("deletedOccurrences", UNSET)
        deleted_occurrences: list[BTOccurrence74] | Unset = UNSET
        if _deleted_occurrences is not UNSET:
            deleted_occurrences = []
            for deleted_occurrences_item_data in _deleted_occurrences:
                deleted_occurrences_item = BTOccurrence74.from_dict(deleted_occurrences_item_data)

                deleted_occurrences.append(deleted_occurrences_item)

        element_id = d.pop("elementId", UNSET)

        _from_full_element_id = d.pop("fromFullElementId", UNSET)
        from_full_element_id: BTFullElementId756 | Unset
        if isinstance(_from_full_element_id, Unset):
            from_full_element_id = UNSET
        else:
            from_full_element_id = BTFullElementId756.from_dict(_from_full_element_id)

        _full_element_id = d.pop("fullElementId", UNSET)
        full_element_id: BTFullElementId756 | Unset
        if isinstance(_full_element_id, Unset):
            full_element_id = UNSET
        else:
            full_element_id = BTFullElementId756.from_dict(_full_element_id)

        _full_element_id_to_referenced_sketch_ids = d.pop("fullElementIdToReferencedSketchIds", UNSET)
        full_element_id_to_referenced_sketch_ids: BTRootAssemblyDisplayData96FullElementIdToReferencedSketchIds | Unset
        if isinstance(_full_element_id_to_referenced_sketch_ids, Unset):
            full_element_id_to_referenced_sketch_ids = UNSET
        else:
            full_element_id_to_referenced_sketch_ids = (
                BTRootAssemblyDisplayData96FullElementIdToReferencedSketchIds.from_dict(
                    _full_element_id_to_referenced_sketch_ids
                )
            )

        _geometry_mates = d.pop("geometryMates", UNSET)
        geometry_mates: list[BTGeometryMateDisplayData1050] | Unset = UNSET
        if _geometry_mates is not UNSET:
            geometry_mates = []
            for geometry_mates_item_data in _geometry_mates:
                geometry_mates_item = BTGeometryMateDisplayData1050.from_dict(geometry_mates_item_data)

                geometry_mates.append(geometry_mates_item)

        incremental = d.pop("incremental", UNSET)

        instance_count = d.pop("instanceCount", UNSET)

        is_collapsible = d.pop("isCollapsible", UNSET)

        is_for_in_context = d.pop("isForInContext", UNSET)

        keep_from_microversion = d.pop("keepFromMicroversion", UNSET)

        _loads = d.pop("loads", UNSET)
        loads: list[BTLoadDisplayData837] | Unset = UNSET
        if _loads is not UNSET:
            loads = []
            for loads_item_data in _loads:
                loads_item = BTLoadDisplayData837.from_dict(loads_item_data)

                loads.append(loads_item)

        _mate_connectors = d.pop("mateConnectors", UNSET)
        mate_connectors: list[BTMateConnectorDisplayData94] | Unset = UNSET
        if _mate_connectors is not UNSET:
            mate_connectors = []
            for mate_connectors_item_data in _mate_connectors:
                mate_connectors_item = BTMateConnectorDisplayData94.from_dict(mate_connectors_item_data)

                mate_connectors.append(mate_connectors_item)

        _mate_groups = d.pop("mateGroups", UNSET)
        mate_groups: list[BTMateGroupDisplayData1990] | Unset = UNSET
        if _mate_groups is not UNSET:
            mate_groups = []
            for mate_groups_item_data in _mate_groups:
                mate_groups_item = BTMateGroupDisplayData1990.from_dict(mate_groups_item_data)

                mate_groups.append(mate_groups_item)

        _mates = d.pop("mates", UNSET)
        mates: list[BTMateDisplayData1358] | Unset = UNSET
        if _mates is not UNSET:
            mates = []
            for mates_item_data in _mates:
                mates_item = BTMateDisplayData1358.from_dict(mates_item_data)

                mates.append(mates_item)

        _microversion_id = d.pop("microversionId", UNSET)
        microversion_id: BTMicroversionId366 | Unset
        if isinstance(_microversion_id, Unset):
            microversion_id = UNSET
        else:
            microversion_id = BTMicroversionId366.from_dict(_microversion_id)

        _microversion_id_and_configuration_interval = d.pop("microversionIdAndConfigurationInterval", UNSET)
        microversion_id_and_configuration_interval: BTMicroversionIdAndConfigurationInterval2364 | Unset
        if isinstance(_microversion_id_and_configuration_interval, Unset):
            microversion_id_and_configuration_interval = UNSET
        else:
            microversion_id_and_configuration_interval = BTMicroversionIdAndConfigurationInterval2364.from_dict(
                _microversion_id_and_configuration_interval
            )

        _microversion_interval = d.pop("microversionInterval", UNSET)
        microversion_interval: BTMicroversionIdInterval367 | Unset
        if isinstance(_microversion_interval, Unset):
            microversion_interval = UNSET
        else:
            microversion_interval = BTMicroversionIdInterval367.from_dict(_microversion_interval)

        _occurrences = d.pop("occurrences", UNSET)
        occurrences: list[BTOccurrenceDisplayData95] | Unset = UNSET
        if _occurrences is not UNSET:
            occurrences = []
            for occurrences_item_data in _occurrences:
                occurrences_item = BTOccurrenceDisplayData95.from_dict(occurrences_item_data)

                occurrences.append(occurrences_item)

        _origin_display_data = d.pop("originDisplayData", UNSET)
        origin_display_data: BTOriginDisplayData934 | Unset
        if isinstance(_origin_display_data, Unset):
            origin_display_data = UNSET
        else:
            origin_display_data = BTOriginDisplayData934.from_dict(_origin_display_data)

        _part_studio_display_data = d.pop("partStudioDisplayData", UNSET)
        part_studio_display_data: list[BTPartStudioDisplayDataBase2751] | Unset = UNSET
        if _part_studio_display_data is not UNSET:
            part_studio_display_data = []
            for part_studio_display_data_item_data in _part_studio_display_data:
                part_studio_display_data_item = BTPartStudioDisplayDataBase2751.from_dict(
                    part_studio_display_data_item_data
                )

                part_studio_display_data.append(part_studio_display_data_item)

        quick_summary = d.pop("quickSummary", UNSET)

        sent_time_iso = d.pop("sentTimeISO", UNSET)

        _version_for_rasterization = d.pop("versionForRasterization", UNSET)
        version_for_rasterization: BTElementDisplayData326 | Unset
        if isinstance(_version_for_rasterization, Unset):
            version_for_rasterization = UNSET
        else:
            version_for_rasterization = BTElementDisplayData326.from_dict(_version_for_rasterization)

        bt_root_assembly_display_data_96 = cls(
            annotations_for_element=annotations_for_element,
            assembly_features=assembly_features,
            bt_type=bt_type,
            build_duration_millis=build_duration_millis,
            deleted_assembly_features=deleted_assembly_features,
            deleted_geometry_mate_ids=deleted_geometry_mate_ids,
            deleted_loads=deleted_loads,
            deleted_mate_connector_ids=deleted_mate_connector_ids,
            deleted_mate_group_ids=deleted_mate_group_ids,
            deleted_mate_ids=deleted_mate_ids,
            deleted_occurrences=deleted_occurrences,
            element_id=element_id,
            from_full_element_id=from_full_element_id,
            full_element_id=full_element_id,
            full_element_id_to_referenced_sketch_ids=full_element_id_to_referenced_sketch_ids,
            geometry_mates=geometry_mates,
            incremental=incremental,
            instance_count=instance_count,
            is_collapsible=is_collapsible,
            is_for_in_context=is_for_in_context,
            keep_from_microversion=keep_from_microversion,
            loads=loads,
            mate_connectors=mate_connectors,
            mate_groups=mate_groups,
            mates=mates,
            microversion_id=microversion_id,
            microversion_id_and_configuration_interval=microversion_id_and_configuration_interval,
            microversion_interval=microversion_interval,
            occurrences=occurrences,
            origin_display_data=origin_display_data,
            part_studio_display_data=part_studio_display_data,
            quick_summary=quick_summary,
            sent_time_iso=sent_time_iso,
            version_for_rasterization=version_for_rasterization,
        )

        bt_root_assembly_display_data_96.additional_properties = d
        return bt_root_assembly_display_data_96

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
