from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_sketch_curve_type import GBTSketchCurveType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_base_entity_data_33 import BTBaseEntityData33
    from ..models.bt_domain_specific_metadata_961 import BTDomainSpecificMetadata961
    from ..models.bt_entity_geometry_35 import BTEntityGeometry35


T = TypeVar("T", bound="BTSketchEntity25")


@_attrs_define
class BTSketchEntity25:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        construction_plane (bool | Unset):
        copy_without_geometry (BTBaseEntityData33 | Unset):
        decompressed (BTBaseEntityData33 | Unset):
        default_pane (bool | Unset):
        deletion (bool | Unset):
        feature_ids (list[str] | Unset):
        from_sketch (bool | Unset):
        geometries (list[BTEntityGeometry35] | Unset):
        origin (bool | Unset):
        domain_specific_metadata (list[BTDomainSpecificMetadata961] | Unset):
        first_geometry (BTEntityGeometry35 | Unset):
        is_construction (bool | Unset):
        is_from_spline_control_polygon (bool | Unset):
        is_from_spline_handle (bool | Unset):
        is_text_stroke (bool | Unset):
        is_user_point (bool | Unset):
        sketch_curve_type (GBTSketchCurveType | Unset):
        sketch_entity_id (str | Unset):
        sketch_feature_id (str | Unset):
        solve_status (int | Unset):
    """

    bt_type: str | Unset = UNSET
    construction_plane: bool | Unset = UNSET
    copy_without_geometry: BTBaseEntityData33 | Unset = UNSET
    decompressed: BTBaseEntityData33 | Unset = UNSET
    default_pane: bool | Unset = UNSET
    deletion: bool | Unset = UNSET
    feature_ids: list[str] | Unset = UNSET
    from_sketch: bool | Unset = UNSET
    geometries: list[BTEntityGeometry35] | Unset = UNSET
    origin: bool | Unset = UNSET
    domain_specific_metadata: list[BTDomainSpecificMetadata961] | Unset = UNSET
    first_geometry: BTEntityGeometry35 | Unset = UNSET
    is_construction: bool | Unset = UNSET
    is_from_spline_control_polygon: bool | Unset = UNSET
    is_from_spline_handle: bool | Unset = UNSET
    is_text_stroke: bool | Unset = UNSET
    is_user_point: bool | Unset = UNSET
    sketch_curve_type: GBTSketchCurveType | Unset = UNSET
    sketch_entity_id: str | Unset = UNSET
    sketch_feature_id: str | Unset = UNSET
    solve_status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        construction_plane = self.construction_plane

        copy_without_geometry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.copy_without_geometry, Unset):
            copy_without_geometry = self.copy_without_geometry.to_dict()

        decompressed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.decompressed, Unset):
            decompressed = self.decompressed.to_dict()

        default_pane = self.default_pane

        deletion = self.deletion

        feature_ids: list[str] | Unset = UNSET
        if not isinstance(self.feature_ids, Unset):
            feature_ids = self.feature_ids

        from_sketch = self.from_sketch

        geometries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.geometries, Unset):
            geometries = []
            for geometries_item_data in self.geometries:
                geometries_item = geometries_item_data.to_dict()
                geometries.append(geometries_item)

        origin = self.origin

        domain_specific_metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.domain_specific_metadata, Unset):
            domain_specific_metadata = []
            for domain_specific_metadata_item_data in self.domain_specific_metadata:
                domain_specific_metadata_item = domain_specific_metadata_item_data.to_dict()
                domain_specific_metadata.append(domain_specific_metadata_item)

        first_geometry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.first_geometry, Unset):
            first_geometry = self.first_geometry.to_dict()

        is_construction = self.is_construction

        is_from_spline_control_polygon = self.is_from_spline_control_polygon

        is_from_spline_handle = self.is_from_spline_handle

        is_text_stroke = self.is_text_stroke

        is_user_point = self.is_user_point

        sketch_curve_type: str | Unset = UNSET
        if not isinstance(self.sketch_curve_type, Unset):
            sketch_curve_type = self.sketch_curve_type.value

        sketch_entity_id = self.sketch_entity_id

        sketch_feature_id = self.sketch_feature_id

        solve_status = self.solve_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if construction_plane is not UNSET:
            field_dict["constructionPlane"] = construction_plane
        if copy_without_geometry is not UNSET:
            field_dict["copyWithoutGeometry"] = copy_without_geometry
        if decompressed is not UNSET:
            field_dict["decompressed"] = decompressed
        if default_pane is not UNSET:
            field_dict["defaultPane"] = default_pane
        if deletion is not UNSET:
            field_dict["deletion"] = deletion
        if feature_ids is not UNSET:
            field_dict["featureIds"] = feature_ids
        if from_sketch is not UNSET:
            field_dict["fromSketch"] = from_sketch
        if geometries is not UNSET:
            field_dict["geometries"] = geometries
        if origin is not UNSET:
            field_dict["origin"] = origin
        if domain_specific_metadata is not UNSET:
            field_dict["domainSpecificMetadata"] = domain_specific_metadata
        if first_geometry is not UNSET:
            field_dict["firstGeometry"] = first_geometry
        if is_construction is not UNSET:
            field_dict["isConstruction"] = is_construction
        if is_from_spline_control_polygon is not UNSET:
            field_dict["isFromSplineControlPolygon"] = is_from_spline_control_polygon
        if is_from_spline_handle is not UNSET:
            field_dict["isFromSplineHandle"] = is_from_spline_handle
        if is_text_stroke is not UNSET:
            field_dict["isTextStroke"] = is_text_stroke
        if is_user_point is not UNSET:
            field_dict["isUserPoint"] = is_user_point
        if sketch_curve_type is not UNSET:
            field_dict["sketchCurveType"] = sketch_curve_type
        if sketch_entity_id is not UNSET:
            field_dict["sketchEntityId"] = sketch_entity_id
        if sketch_feature_id is not UNSET:
            field_dict["sketchFeatureId"] = sketch_feature_id
        if solve_status is not UNSET:
            field_dict["solveStatus"] = solve_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_base_entity_data_33 import BTBaseEntityData33
        from ..models.bt_domain_specific_metadata_961 import BTDomainSpecificMetadata961
        from ..models.bt_entity_geometry_35 import BTEntityGeometry35

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        construction_plane = d.pop("constructionPlane", UNSET)

        _copy_without_geometry = d.pop("copyWithoutGeometry", UNSET)
        copy_without_geometry: BTBaseEntityData33 | Unset
        if isinstance(_copy_without_geometry, Unset):
            copy_without_geometry = UNSET
        else:
            copy_without_geometry = BTBaseEntityData33.from_dict(_copy_without_geometry)

        _decompressed = d.pop("decompressed", UNSET)
        decompressed: BTBaseEntityData33 | Unset
        if isinstance(_decompressed, Unset):
            decompressed = UNSET
        else:
            decompressed = BTBaseEntityData33.from_dict(_decompressed)

        default_pane = d.pop("defaultPane", UNSET)

        deletion = d.pop("deletion", UNSET)

        feature_ids = cast(list[str], d.pop("featureIds", UNSET))

        from_sketch = d.pop("fromSketch", UNSET)

        _geometries = d.pop("geometries", UNSET)
        geometries: list[BTEntityGeometry35] | Unset = UNSET
        if _geometries is not UNSET:
            geometries = []
            for geometries_item_data in _geometries:
                geometries_item = BTEntityGeometry35.from_dict(geometries_item_data)

                geometries.append(geometries_item)

        origin = d.pop("origin", UNSET)

        _domain_specific_metadata = d.pop("domainSpecificMetadata", UNSET)
        domain_specific_metadata: list[BTDomainSpecificMetadata961] | Unset = UNSET
        if _domain_specific_metadata is not UNSET:
            domain_specific_metadata = []
            for domain_specific_metadata_item_data in _domain_specific_metadata:
                domain_specific_metadata_item = BTDomainSpecificMetadata961.from_dict(
                    domain_specific_metadata_item_data
                )

                domain_specific_metadata.append(domain_specific_metadata_item)

        _first_geometry = d.pop("firstGeometry", UNSET)
        first_geometry: BTEntityGeometry35 | Unset
        if isinstance(_first_geometry, Unset):
            first_geometry = UNSET
        else:
            first_geometry = BTEntityGeometry35.from_dict(_first_geometry)

        is_construction = d.pop("isConstruction", UNSET)

        is_from_spline_control_polygon = d.pop("isFromSplineControlPolygon", UNSET)

        is_from_spline_handle = d.pop("isFromSplineHandle", UNSET)

        is_text_stroke = d.pop("isTextStroke", UNSET)

        is_user_point = d.pop("isUserPoint", UNSET)

        _sketch_curve_type = d.pop("sketchCurveType", UNSET)
        sketch_curve_type: GBTSketchCurveType | Unset
        if isinstance(_sketch_curve_type, Unset):
            sketch_curve_type = UNSET
        else:
            sketch_curve_type = GBTSketchCurveType(_sketch_curve_type)

        sketch_entity_id = d.pop("sketchEntityId", UNSET)

        sketch_feature_id = d.pop("sketchFeatureId", UNSET)

        solve_status = d.pop("solveStatus", UNSET)

        bt_sketch_entity_25 = cls(
            bt_type=bt_type,
            construction_plane=construction_plane,
            copy_without_geometry=copy_without_geometry,
            decompressed=decompressed,
            default_pane=default_pane,
            deletion=deletion,
            feature_ids=feature_ids,
            from_sketch=from_sketch,
            geometries=geometries,
            origin=origin,
            domain_specific_metadata=domain_specific_metadata,
            first_geometry=first_geometry,
            is_construction=is_construction,
            is_from_spline_control_polygon=is_from_spline_control_polygon,
            is_from_spline_handle=is_from_spline_handle,
            is_text_stroke=is_text_stroke,
            is_user_point=is_user_point,
            sketch_curve_type=sketch_curve_type,
            sketch_entity_id=sketch_entity_id,
            sketch_feature_id=sketch_feature_id,
            solve_status=solve_status,
        )

        bt_sketch_entity_25.additional_properties = d
        return bt_sketch_entity_25

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
