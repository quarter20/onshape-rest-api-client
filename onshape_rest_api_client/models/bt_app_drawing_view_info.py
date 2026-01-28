from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_app_element_error_code import BTAppElementErrorCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_app_drawing_view_info_broken_out_b_boxes import BTAppDrawingViewInfoBrokenOutBBoxes
    from ..models.bt_app_drawing_view_info_broken_out_end_conditions import BTAppDrawingViewInfoBrokenOutEndConditions
    from ..models.bt_app_drawing_view_info_occurrence_or_query_to_geometry_properties import (
        BTAppDrawingViewInfoOccurrenceOrQueryToGeometryProperties,
    )
    from ..models.bt_broken_out_end_condition_1107 import BTBrokenOutEndCondition1107


T = TypeVar("T", bound="BTAppDrawingViewInfo")


@_attrs_define
class BTAppDrawingViewInfo:
    """
    Attributes:
        associativity_change_id (str | Unset):
        bom_reference_id (str | Unset):
        broken_out_b_boxes (BTAppDrawingViewInfoBrokenOutBBoxes | Unset):
        broken_out_end_conditions (BTAppDrawingViewInfoBrokenOutEndConditions | Unset):
        broken_out_point_numbers (list[int] | Unset):
        change_id (str | Unset):
        compute_intersection (bool | Unset):
        cut_point (list[float] | Unset):
        depth_section_end_condition (BTBrokenOutEndCondition1107 | Unset):
        display_state_id (str | Unset):
        error_code (int | Unset): `0: OK (healthy) | 1: INFO | 2: WARNING | 3: ERROR (dangling or view generation call
            failed) | 4: UNKNOWN`
        error_description (str | Unset): A human-readable value for the error that occurred, if one occurred.
        error_value (BTAppElementErrorCode | Unset):
        exploded_view_id (str | Unset):
        has_secondary_view_definition (bool | Unset):
        hidden_lines (str | Unset):
        ignore_faulty_parts (bool | Unset):
        include_hidden_instances (bool | Unset):
        include_surfaces (bool | Unset):
        include_wires (bool | Unset):
        is_aligned_section (bool | Unset):
        is_broken_out_section (bool | Unset):
        is_copied_view (bool | Unset):
        is_crop_view (bool | Unset):
        is_partial_section (bool | Unset):
        is_section_of_aligned_section (bool | Unset):
        is_section_of_section_on_base (bool | Unset):
        is_surface (bool | Unset):
        model_reference_id (str | Unset):
        modification_id (str | Unset):
        named_position_id (str | Unset):
        occurrence_or_query_to_geometry_properties (BTAppDrawingViewInfoOccurrenceOrQueryToGeometryProperties | Unset):
        offset_section_points (list[float] | Unset):
        parent_change_id (str | Unset):
        parent_view_id (str | Unset):
        perspective (bool | Unset):
        projection_angle (str | Unset):
        quality_option (int | Unset):
        render_sketches (bool | Unset):
        section_id (str | Unset):
        section_planes (list[float] | Unset):
        show_auto_centerlines (bool | Unset):
        show_auto_centermarks (bool | Unset):
        show_cut_geom_only (bool | Unset):
        show_tangent_lines (bool | Unset):
        show_threads (bool | Unset):
        show_viewing_plane (bool | Unset):
        simplification_option (int | Unset):
        simplification_threshold (float | Unset):
        use_parent_view_section_data (bool | Unset):
        view_direction (list[float] | Unset):
        view_id (str | Unset):
        view_matrix (list[float] | Unset):
        view_version (int | Unset):
    """

    associativity_change_id: str | Unset = UNSET
    bom_reference_id: str | Unset = UNSET
    broken_out_b_boxes: BTAppDrawingViewInfoBrokenOutBBoxes | Unset = UNSET
    broken_out_end_conditions: BTAppDrawingViewInfoBrokenOutEndConditions | Unset = UNSET
    broken_out_point_numbers: list[int] | Unset = UNSET
    change_id: str | Unset = UNSET
    compute_intersection: bool | Unset = UNSET
    cut_point: list[float] | Unset = UNSET
    depth_section_end_condition: BTBrokenOutEndCondition1107 | Unset = UNSET
    display_state_id: str | Unset = UNSET
    error_code: int | Unset = UNSET
    error_description: str | Unset = UNSET
    error_value: BTAppElementErrorCode | Unset = UNSET
    exploded_view_id: str | Unset = UNSET
    has_secondary_view_definition: bool | Unset = UNSET
    hidden_lines: str | Unset = UNSET
    ignore_faulty_parts: bool | Unset = UNSET
    include_hidden_instances: bool | Unset = UNSET
    include_surfaces: bool | Unset = UNSET
    include_wires: bool | Unset = UNSET
    is_aligned_section: bool | Unset = UNSET
    is_broken_out_section: bool | Unset = UNSET
    is_copied_view: bool | Unset = UNSET
    is_crop_view: bool | Unset = UNSET
    is_partial_section: bool | Unset = UNSET
    is_section_of_aligned_section: bool | Unset = UNSET
    is_section_of_section_on_base: bool | Unset = UNSET
    is_surface: bool | Unset = UNSET
    model_reference_id: str | Unset = UNSET
    modification_id: str | Unset = UNSET
    named_position_id: str | Unset = UNSET
    occurrence_or_query_to_geometry_properties: BTAppDrawingViewInfoOccurrenceOrQueryToGeometryProperties | Unset = (
        UNSET
    )
    offset_section_points: list[float] | Unset = UNSET
    parent_change_id: str | Unset = UNSET
    parent_view_id: str | Unset = UNSET
    perspective: bool | Unset = UNSET
    projection_angle: str | Unset = UNSET
    quality_option: int | Unset = UNSET
    render_sketches: bool | Unset = UNSET
    section_id: str | Unset = UNSET
    section_planes: list[float] | Unset = UNSET
    show_auto_centerlines: bool | Unset = UNSET
    show_auto_centermarks: bool | Unset = UNSET
    show_cut_geom_only: bool | Unset = UNSET
    show_tangent_lines: bool | Unset = UNSET
    show_threads: bool | Unset = UNSET
    show_viewing_plane: bool | Unset = UNSET
    simplification_option: int | Unset = UNSET
    simplification_threshold: float | Unset = UNSET
    use_parent_view_section_data: bool | Unset = UNSET
    view_direction: list[float] | Unset = UNSET
    view_id: str | Unset = UNSET
    view_matrix: list[float] | Unset = UNSET
    view_version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        associativity_change_id = self.associativity_change_id

        bom_reference_id = self.bom_reference_id

        broken_out_b_boxes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.broken_out_b_boxes, Unset):
            broken_out_b_boxes = self.broken_out_b_boxes.to_dict()

        broken_out_end_conditions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.broken_out_end_conditions, Unset):
            broken_out_end_conditions = self.broken_out_end_conditions.to_dict()

        broken_out_point_numbers: list[int] | Unset = UNSET
        if not isinstance(self.broken_out_point_numbers, Unset):
            broken_out_point_numbers = self.broken_out_point_numbers

        change_id = self.change_id

        compute_intersection = self.compute_intersection

        cut_point: list[float] | Unset = UNSET
        if not isinstance(self.cut_point, Unset):
            cut_point = self.cut_point

        depth_section_end_condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.depth_section_end_condition, Unset):
            depth_section_end_condition = self.depth_section_end_condition.to_dict()

        display_state_id = self.display_state_id

        error_code = self.error_code

        error_description = self.error_description

        error_value: str | Unset = UNSET
        if not isinstance(self.error_value, Unset):
            error_value = self.error_value.value

        exploded_view_id = self.exploded_view_id

        has_secondary_view_definition = self.has_secondary_view_definition

        hidden_lines = self.hidden_lines

        ignore_faulty_parts = self.ignore_faulty_parts

        include_hidden_instances = self.include_hidden_instances

        include_surfaces = self.include_surfaces

        include_wires = self.include_wires

        is_aligned_section = self.is_aligned_section

        is_broken_out_section = self.is_broken_out_section

        is_copied_view = self.is_copied_view

        is_crop_view = self.is_crop_view

        is_partial_section = self.is_partial_section

        is_section_of_aligned_section = self.is_section_of_aligned_section

        is_section_of_section_on_base = self.is_section_of_section_on_base

        is_surface = self.is_surface

        model_reference_id = self.model_reference_id

        modification_id = self.modification_id

        named_position_id = self.named_position_id

        occurrence_or_query_to_geometry_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.occurrence_or_query_to_geometry_properties, Unset):
            occurrence_or_query_to_geometry_properties = self.occurrence_or_query_to_geometry_properties.to_dict()

        offset_section_points: list[float] | Unset = UNSET
        if not isinstance(self.offset_section_points, Unset):
            offset_section_points = self.offset_section_points

        parent_change_id = self.parent_change_id

        parent_view_id = self.parent_view_id

        perspective = self.perspective

        projection_angle = self.projection_angle

        quality_option = self.quality_option

        render_sketches = self.render_sketches

        section_id = self.section_id

        section_planes: list[float] | Unset = UNSET
        if not isinstance(self.section_planes, Unset):
            section_planes = self.section_planes

        show_auto_centerlines = self.show_auto_centerlines

        show_auto_centermarks = self.show_auto_centermarks

        show_cut_geom_only = self.show_cut_geom_only

        show_tangent_lines = self.show_tangent_lines

        show_threads = self.show_threads

        show_viewing_plane = self.show_viewing_plane

        simplification_option = self.simplification_option

        simplification_threshold = self.simplification_threshold

        use_parent_view_section_data = self.use_parent_view_section_data

        view_direction: list[float] | Unset = UNSET
        if not isinstance(self.view_direction, Unset):
            view_direction = self.view_direction

        view_id = self.view_id

        view_matrix: list[float] | Unset = UNSET
        if not isinstance(self.view_matrix, Unset):
            view_matrix = self.view_matrix

        view_version = self.view_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if associativity_change_id is not UNSET:
            field_dict["associativityChangeId"] = associativity_change_id
        if bom_reference_id is not UNSET:
            field_dict["bomReferenceId"] = bom_reference_id
        if broken_out_b_boxes is not UNSET:
            field_dict["brokenOutBBoxes"] = broken_out_b_boxes
        if broken_out_end_conditions is not UNSET:
            field_dict["brokenOutEndConditions"] = broken_out_end_conditions
        if broken_out_point_numbers is not UNSET:
            field_dict["brokenOutPointNumbers"] = broken_out_point_numbers
        if change_id is not UNSET:
            field_dict["changeId"] = change_id
        if compute_intersection is not UNSET:
            field_dict["computeIntersection"] = compute_intersection
        if cut_point is not UNSET:
            field_dict["cutPoint"] = cut_point
        if depth_section_end_condition is not UNSET:
            field_dict["depthSectionEndCondition"] = depth_section_end_condition
        if display_state_id is not UNSET:
            field_dict["displayStateId"] = display_state_id
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_description is not UNSET:
            field_dict["errorDescription"] = error_description
        if error_value is not UNSET:
            field_dict["errorValue"] = error_value
        if exploded_view_id is not UNSET:
            field_dict["explodedViewId"] = exploded_view_id
        if has_secondary_view_definition is not UNSET:
            field_dict["hasSecondaryViewDefinition"] = has_secondary_view_definition
        if hidden_lines is not UNSET:
            field_dict["hiddenLines"] = hidden_lines
        if ignore_faulty_parts is not UNSET:
            field_dict["ignoreFaultyParts"] = ignore_faulty_parts
        if include_hidden_instances is not UNSET:
            field_dict["includeHiddenInstances"] = include_hidden_instances
        if include_surfaces is not UNSET:
            field_dict["includeSurfaces"] = include_surfaces
        if include_wires is not UNSET:
            field_dict["includeWires"] = include_wires
        if is_aligned_section is not UNSET:
            field_dict["isAlignedSection"] = is_aligned_section
        if is_broken_out_section is not UNSET:
            field_dict["isBrokenOutSection"] = is_broken_out_section
        if is_copied_view is not UNSET:
            field_dict["isCopiedView"] = is_copied_view
        if is_crop_view is not UNSET:
            field_dict["isCropView"] = is_crop_view
        if is_partial_section is not UNSET:
            field_dict["isPartialSection"] = is_partial_section
        if is_section_of_aligned_section is not UNSET:
            field_dict["isSectionOfAlignedSection"] = is_section_of_aligned_section
        if is_section_of_section_on_base is not UNSET:
            field_dict["isSectionOfSectionOnBase"] = is_section_of_section_on_base
        if is_surface is not UNSET:
            field_dict["isSurface"] = is_surface
        if model_reference_id is not UNSET:
            field_dict["modelReferenceId"] = model_reference_id
        if modification_id is not UNSET:
            field_dict["modificationId"] = modification_id
        if named_position_id is not UNSET:
            field_dict["namedPositionId"] = named_position_id
        if occurrence_or_query_to_geometry_properties is not UNSET:
            field_dict["occurrenceOrQueryToGeometryProperties"] = occurrence_or_query_to_geometry_properties
        if offset_section_points is not UNSET:
            field_dict["offsetSectionPoints"] = offset_section_points
        if parent_change_id is not UNSET:
            field_dict["parentChangeId"] = parent_change_id
        if parent_view_id is not UNSET:
            field_dict["parentViewId"] = parent_view_id
        if perspective is not UNSET:
            field_dict["perspective"] = perspective
        if projection_angle is not UNSET:
            field_dict["projectionAngle"] = projection_angle
        if quality_option is not UNSET:
            field_dict["qualityOption"] = quality_option
        if render_sketches is not UNSET:
            field_dict["renderSketches"] = render_sketches
        if section_id is not UNSET:
            field_dict["sectionId"] = section_id
        if section_planes is not UNSET:
            field_dict["sectionPlanes"] = section_planes
        if show_auto_centerlines is not UNSET:
            field_dict["showAutoCenterlines"] = show_auto_centerlines
        if show_auto_centermarks is not UNSET:
            field_dict["showAutoCentermarks"] = show_auto_centermarks
        if show_cut_geom_only is not UNSET:
            field_dict["showCutGeomOnly"] = show_cut_geom_only
        if show_tangent_lines is not UNSET:
            field_dict["showTangentLines"] = show_tangent_lines
        if show_threads is not UNSET:
            field_dict["showThreads"] = show_threads
        if show_viewing_plane is not UNSET:
            field_dict["showViewingPlane"] = show_viewing_plane
        if simplification_option is not UNSET:
            field_dict["simplificationOption"] = simplification_option
        if simplification_threshold is not UNSET:
            field_dict["simplificationThreshold"] = simplification_threshold
        if use_parent_view_section_data is not UNSET:
            field_dict["useParentViewSectionData"] = use_parent_view_section_data
        if view_direction is not UNSET:
            field_dict["viewDirection"] = view_direction
        if view_id is not UNSET:
            field_dict["viewId"] = view_id
        if view_matrix is not UNSET:
            field_dict["viewMatrix"] = view_matrix
        if view_version is not UNSET:
            field_dict["viewVersion"] = view_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_app_drawing_view_info_broken_out_b_boxes import BTAppDrawingViewInfoBrokenOutBBoxes
        from ..models.bt_app_drawing_view_info_broken_out_end_conditions import (
            BTAppDrawingViewInfoBrokenOutEndConditions,
        )
        from ..models.bt_app_drawing_view_info_occurrence_or_query_to_geometry_properties import (
            BTAppDrawingViewInfoOccurrenceOrQueryToGeometryProperties,
        )
        from ..models.bt_broken_out_end_condition_1107 import BTBrokenOutEndCondition1107

        d = dict(src_dict)
        associativity_change_id = d.pop("associativityChangeId", UNSET)

        bom_reference_id = d.pop("bomReferenceId", UNSET)

        _broken_out_b_boxes = d.pop("brokenOutBBoxes", UNSET)
        broken_out_b_boxes: BTAppDrawingViewInfoBrokenOutBBoxes | Unset
        if isinstance(_broken_out_b_boxes, Unset):
            broken_out_b_boxes = UNSET
        else:
            broken_out_b_boxes = BTAppDrawingViewInfoBrokenOutBBoxes.from_dict(_broken_out_b_boxes)

        _broken_out_end_conditions = d.pop("brokenOutEndConditions", UNSET)
        broken_out_end_conditions: BTAppDrawingViewInfoBrokenOutEndConditions | Unset
        if isinstance(_broken_out_end_conditions, Unset):
            broken_out_end_conditions = UNSET
        else:
            broken_out_end_conditions = BTAppDrawingViewInfoBrokenOutEndConditions.from_dict(_broken_out_end_conditions)

        broken_out_point_numbers = cast(list[int], d.pop("brokenOutPointNumbers", UNSET))

        change_id = d.pop("changeId", UNSET)

        compute_intersection = d.pop("computeIntersection", UNSET)

        cut_point = cast(list[float], d.pop("cutPoint", UNSET))

        _depth_section_end_condition = d.pop("depthSectionEndCondition", UNSET)
        depth_section_end_condition: BTBrokenOutEndCondition1107 | Unset
        if isinstance(_depth_section_end_condition, Unset):
            depth_section_end_condition = UNSET
        else:
            depth_section_end_condition = BTBrokenOutEndCondition1107.from_dict(_depth_section_end_condition)

        display_state_id = d.pop("displayStateId", UNSET)

        error_code = d.pop("errorCode", UNSET)

        error_description = d.pop("errorDescription", UNSET)

        _error_value = d.pop("errorValue", UNSET)
        error_value: BTAppElementErrorCode | Unset
        if isinstance(_error_value, Unset):
            error_value = UNSET
        else:
            error_value = BTAppElementErrorCode(_error_value)

        exploded_view_id = d.pop("explodedViewId", UNSET)

        has_secondary_view_definition = d.pop("hasSecondaryViewDefinition", UNSET)

        hidden_lines = d.pop("hiddenLines", UNSET)

        ignore_faulty_parts = d.pop("ignoreFaultyParts", UNSET)

        include_hidden_instances = d.pop("includeHiddenInstances", UNSET)

        include_surfaces = d.pop("includeSurfaces", UNSET)

        include_wires = d.pop("includeWires", UNSET)

        is_aligned_section = d.pop("isAlignedSection", UNSET)

        is_broken_out_section = d.pop("isBrokenOutSection", UNSET)

        is_copied_view = d.pop("isCopiedView", UNSET)

        is_crop_view = d.pop("isCropView", UNSET)

        is_partial_section = d.pop("isPartialSection", UNSET)

        is_section_of_aligned_section = d.pop("isSectionOfAlignedSection", UNSET)

        is_section_of_section_on_base = d.pop("isSectionOfSectionOnBase", UNSET)

        is_surface = d.pop("isSurface", UNSET)

        model_reference_id = d.pop("modelReferenceId", UNSET)

        modification_id = d.pop("modificationId", UNSET)

        named_position_id = d.pop("namedPositionId", UNSET)

        _occurrence_or_query_to_geometry_properties = d.pop("occurrenceOrQueryToGeometryProperties", UNSET)
        occurrence_or_query_to_geometry_properties: BTAppDrawingViewInfoOccurrenceOrQueryToGeometryProperties | Unset
        if isinstance(_occurrence_or_query_to_geometry_properties, Unset):
            occurrence_or_query_to_geometry_properties = UNSET
        else:
            occurrence_or_query_to_geometry_properties = (
                BTAppDrawingViewInfoOccurrenceOrQueryToGeometryProperties.from_dict(
                    _occurrence_or_query_to_geometry_properties
                )
            )

        offset_section_points = cast(list[float], d.pop("offsetSectionPoints", UNSET))

        parent_change_id = d.pop("parentChangeId", UNSET)

        parent_view_id = d.pop("parentViewId", UNSET)

        perspective = d.pop("perspective", UNSET)

        projection_angle = d.pop("projectionAngle", UNSET)

        quality_option = d.pop("qualityOption", UNSET)

        render_sketches = d.pop("renderSketches", UNSET)

        section_id = d.pop("sectionId", UNSET)

        section_planes = cast(list[float], d.pop("sectionPlanes", UNSET))

        show_auto_centerlines = d.pop("showAutoCenterlines", UNSET)

        show_auto_centermarks = d.pop("showAutoCentermarks", UNSET)

        show_cut_geom_only = d.pop("showCutGeomOnly", UNSET)

        show_tangent_lines = d.pop("showTangentLines", UNSET)

        show_threads = d.pop("showThreads", UNSET)

        show_viewing_plane = d.pop("showViewingPlane", UNSET)

        simplification_option = d.pop("simplificationOption", UNSET)

        simplification_threshold = d.pop("simplificationThreshold", UNSET)

        use_parent_view_section_data = d.pop("useParentViewSectionData", UNSET)

        view_direction = cast(list[float], d.pop("viewDirection", UNSET))

        view_id = d.pop("viewId", UNSET)

        view_matrix = cast(list[float], d.pop("viewMatrix", UNSET))

        view_version = d.pop("viewVersion", UNSET)

        bt_app_drawing_view_info = cls(
            associativity_change_id=associativity_change_id,
            bom_reference_id=bom_reference_id,
            broken_out_b_boxes=broken_out_b_boxes,
            broken_out_end_conditions=broken_out_end_conditions,
            broken_out_point_numbers=broken_out_point_numbers,
            change_id=change_id,
            compute_intersection=compute_intersection,
            cut_point=cut_point,
            depth_section_end_condition=depth_section_end_condition,
            display_state_id=display_state_id,
            error_code=error_code,
            error_description=error_description,
            error_value=error_value,
            exploded_view_id=exploded_view_id,
            has_secondary_view_definition=has_secondary_view_definition,
            hidden_lines=hidden_lines,
            ignore_faulty_parts=ignore_faulty_parts,
            include_hidden_instances=include_hidden_instances,
            include_surfaces=include_surfaces,
            include_wires=include_wires,
            is_aligned_section=is_aligned_section,
            is_broken_out_section=is_broken_out_section,
            is_copied_view=is_copied_view,
            is_crop_view=is_crop_view,
            is_partial_section=is_partial_section,
            is_section_of_aligned_section=is_section_of_aligned_section,
            is_section_of_section_on_base=is_section_of_section_on_base,
            is_surface=is_surface,
            model_reference_id=model_reference_id,
            modification_id=modification_id,
            named_position_id=named_position_id,
            occurrence_or_query_to_geometry_properties=occurrence_or_query_to_geometry_properties,
            offset_section_points=offset_section_points,
            parent_change_id=parent_change_id,
            parent_view_id=parent_view_id,
            perspective=perspective,
            projection_angle=projection_angle,
            quality_option=quality_option,
            render_sketches=render_sketches,
            section_id=section_id,
            section_planes=section_planes,
            show_auto_centerlines=show_auto_centerlines,
            show_auto_centermarks=show_auto_centermarks,
            show_cut_geom_only=show_cut_geom_only,
            show_tangent_lines=show_tangent_lines,
            show_threads=show_threads,
            show_viewing_plane=show_viewing_plane,
            simplification_option=simplification_option,
            simplification_threshold=simplification_threshold,
            use_parent_view_section_data=use_parent_view_section_data,
            view_direction=view_direction,
            view_id=view_id,
            view_matrix=view_matrix,
            view_version=view_version,
        )

        bt_app_drawing_view_info.additional_properties = d
        return bt_app_drawing_view_info

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
