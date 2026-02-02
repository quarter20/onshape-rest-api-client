from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_hole_type import GBTHoleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_coordinate_system_387 import BTCoordinateSystem387
    from ..models.bt_tolerant_value_display_data_3483 import BTTolerantValueDisplayData3483
    from ..models.bt_vector_2d1812 import BTVector2D1812


T = TypeVar("T", bound="BTHoleCalloutDisplayData3452")


@_attrs_define
class BTHoleCalloutDisplayData3452:
    """
    Attributes:
        annotation_plane (BTCoordinateSystem387 | Unset):
        base_plane (BTCoordinateSystem387 | Unset):
        bt_type (str | Unset): Type of JSON object.
        characteristic_id (str | Unset):
        deterministic_id (str | Unset):
        dxdy_segments (list[BTVector2D1812] | Unset):
        is_constrained_to_plane (bool | Unset):
        is_deletion (bool | Unset):
        is_derived (bool | Unset):
        main_constraint_id (str | Unset):
        main_feature_id (str | Unset):
        main_parameter_id (str | Unset):
        main_part_id (str | Unset):
        all_hole_faces (list[str] | Unset):
        counterbore_depth (BTTolerantValueDisplayData3483 | Unset):
        counterbore_diameter (BTTolerantValueDisplayData3483 | Unset):
        countersink_angle (BTTolerantValueDisplayData3483 | Unset):
        countersink_diameter (BTTolerantValueDisplayData3483 | Unset):
        depth (BTTolerantValueDisplayData3483 | Unset):
        diameter (BTTolerantValueDisplayData3483 | Unset):
        feature_id (str | Unset):
        hole_type (GBTHoleType | Unset):
        is_pipe_tap (bool | Unset):
        is_tapered_pipe_tap (bool | Unset):
        is_tapped (bool | Unset):
        label_location (BTVector2D1812 | Unset):
        part_id (str | Unset):
        reference_radius (float | Unset):
        tap_size (str | Unset):
        tapped_depth (BTTolerantValueDisplayData3483 | Unset):
    """

    annotation_plane: BTCoordinateSystem387 | Unset = UNSET
    base_plane: BTCoordinateSystem387 | Unset = UNSET
    bt_type: str | Unset = UNSET
    characteristic_id: str | Unset = UNSET
    deterministic_id: str | Unset = UNSET
    dxdy_segments: list[BTVector2D1812] | Unset = UNSET
    is_constrained_to_plane: bool | Unset = UNSET
    is_deletion: bool | Unset = UNSET
    is_derived: bool | Unset = UNSET
    main_constraint_id: str | Unset = UNSET
    main_feature_id: str | Unset = UNSET
    main_parameter_id: str | Unset = UNSET
    main_part_id: str | Unset = UNSET
    all_hole_faces: list[str] | Unset = UNSET
    counterbore_depth: BTTolerantValueDisplayData3483 | Unset = UNSET
    counterbore_diameter: BTTolerantValueDisplayData3483 | Unset = UNSET
    countersink_angle: BTTolerantValueDisplayData3483 | Unset = UNSET
    countersink_diameter: BTTolerantValueDisplayData3483 | Unset = UNSET
    depth: BTTolerantValueDisplayData3483 | Unset = UNSET
    diameter: BTTolerantValueDisplayData3483 | Unset = UNSET
    feature_id: str | Unset = UNSET
    hole_type: GBTHoleType | Unset = UNSET
    is_pipe_tap: bool | Unset = UNSET
    is_tapered_pipe_tap: bool | Unset = UNSET
    is_tapped: bool | Unset = UNSET
    label_location: BTVector2D1812 | Unset = UNSET
    part_id: str | Unset = UNSET
    reference_radius: float | Unset = UNSET
    tap_size: str | Unset = UNSET
    tapped_depth: BTTolerantValueDisplayData3483 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotation_plane: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotation_plane, Unset):
            annotation_plane = self.annotation_plane.to_dict()

        base_plane: dict[str, Any] | Unset = UNSET
        if not isinstance(self.base_plane, Unset):
            base_plane = self.base_plane.to_dict()

        bt_type = self.bt_type

        characteristic_id = self.characteristic_id

        deterministic_id = self.deterministic_id

        dxdy_segments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dxdy_segments, Unset):
            dxdy_segments = []
            for dxdy_segments_item_data in self.dxdy_segments:
                dxdy_segments_item = dxdy_segments_item_data.to_dict()
                dxdy_segments.append(dxdy_segments_item)

        is_constrained_to_plane = self.is_constrained_to_plane

        is_deletion = self.is_deletion

        is_derived = self.is_derived

        main_constraint_id = self.main_constraint_id

        main_feature_id = self.main_feature_id

        main_parameter_id = self.main_parameter_id

        main_part_id = self.main_part_id

        all_hole_faces: list[str] | Unset = UNSET
        if not isinstance(self.all_hole_faces, Unset):
            all_hole_faces = self.all_hole_faces

        counterbore_depth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.counterbore_depth, Unset):
            counterbore_depth = self.counterbore_depth.to_dict()

        counterbore_diameter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.counterbore_diameter, Unset):
            counterbore_diameter = self.counterbore_diameter.to_dict()

        countersink_angle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.countersink_angle, Unset):
            countersink_angle = self.countersink_angle.to_dict()

        countersink_diameter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.countersink_diameter, Unset):
            countersink_diameter = self.countersink_diameter.to_dict()

        depth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.depth, Unset):
            depth = self.depth.to_dict()

        diameter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.diameter, Unset):
            diameter = self.diameter.to_dict()

        feature_id = self.feature_id

        hole_type: str | Unset = UNSET
        if not isinstance(self.hole_type, Unset):
            hole_type = self.hole_type.value

        is_pipe_tap = self.is_pipe_tap

        is_tapered_pipe_tap = self.is_tapered_pipe_tap

        is_tapped = self.is_tapped

        label_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.label_location, Unset):
            label_location = self.label_location.to_dict()

        part_id = self.part_id

        reference_radius = self.reference_radius

        tap_size = self.tap_size

        tapped_depth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tapped_depth, Unset):
            tapped_depth = self.tapped_depth.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotation_plane is not UNSET:
            field_dict["annotationPlane"] = annotation_plane
        if base_plane is not UNSET:
            field_dict["basePlane"] = base_plane
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if characteristic_id is not UNSET:
            field_dict["characteristicId"] = characteristic_id
        if deterministic_id is not UNSET:
            field_dict["deterministicId"] = deterministic_id
        if dxdy_segments is not UNSET:
            field_dict["dxdySegments"] = dxdy_segments
        if is_constrained_to_plane is not UNSET:
            field_dict["isConstrainedToPlane"] = is_constrained_to_plane
        if is_deletion is not UNSET:
            field_dict["isDeletion"] = is_deletion
        if is_derived is not UNSET:
            field_dict["isDerived"] = is_derived
        if main_constraint_id is not UNSET:
            field_dict["mainConstraintId"] = main_constraint_id
        if main_feature_id is not UNSET:
            field_dict["mainFeatureId"] = main_feature_id
        if main_parameter_id is not UNSET:
            field_dict["mainParameterId"] = main_parameter_id
        if main_part_id is not UNSET:
            field_dict["mainPartId"] = main_part_id
        if all_hole_faces is not UNSET:
            field_dict["allHoleFaces"] = all_hole_faces
        if counterbore_depth is not UNSET:
            field_dict["counterboreDepth"] = counterbore_depth
        if counterbore_diameter is not UNSET:
            field_dict["counterboreDiameter"] = counterbore_diameter
        if countersink_angle is not UNSET:
            field_dict["countersinkAngle"] = countersink_angle
        if countersink_diameter is not UNSET:
            field_dict["countersinkDiameter"] = countersink_diameter
        if depth is not UNSET:
            field_dict["depth"] = depth
        if diameter is not UNSET:
            field_dict["diameter"] = diameter
        if feature_id is not UNSET:
            field_dict["featureId"] = feature_id
        if hole_type is not UNSET:
            field_dict["holeType"] = hole_type
        if is_pipe_tap is not UNSET:
            field_dict["isPipeTap"] = is_pipe_tap
        if is_tapered_pipe_tap is not UNSET:
            field_dict["isTaperedPipeTap"] = is_tapered_pipe_tap
        if is_tapped is not UNSET:
            field_dict["isTapped"] = is_tapped
        if label_location is not UNSET:
            field_dict["labelLocation"] = label_location
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if reference_radius is not UNSET:
            field_dict["referenceRadius"] = reference_radius
        if tap_size is not UNSET:
            field_dict["tapSize"] = tap_size
        if tapped_depth is not UNSET:
            field_dict["tappedDepth"] = tapped_depth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_coordinate_system_387 import BTCoordinateSystem387
        from ..models.bt_tolerant_value_display_data_3483 import BTTolerantValueDisplayData3483
        from ..models.bt_vector_2d1812 import BTVector2D1812

        d = dict(src_dict)
        _annotation_plane = d.pop("annotationPlane", UNSET)
        annotation_plane: BTCoordinateSystem387 | Unset
        if isinstance(_annotation_plane, Unset):
            annotation_plane = UNSET
        else:
            annotation_plane = BTCoordinateSystem387.from_dict(_annotation_plane)

        _base_plane = d.pop("basePlane", UNSET)
        base_plane: BTCoordinateSystem387 | Unset
        if isinstance(_base_plane, Unset):
            base_plane = UNSET
        else:
            base_plane = BTCoordinateSystem387.from_dict(_base_plane)

        bt_type = d.pop("btType", UNSET)

        characteristic_id = d.pop("characteristicId", UNSET)

        deterministic_id = d.pop("deterministicId", UNSET)

        _dxdy_segments = d.pop("dxdySegments", UNSET)
        dxdy_segments: list[BTVector2D1812] | Unset = UNSET
        if _dxdy_segments is not UNSET:
            dxdy_segments = []
            for dxdy_segments_item_data in _dxdy_segments:
                dxdy_segments_item = BTVector2D1812.from_dict(dxdy_segments_item_data)

                dxdy_segments.append(dxdy_segments_item)

        is_constrained_to_plane = d.pop("isConstrainedToPlane", UNSET)

        is_deletion = d.pop("isDeletion", UNSET)

        is_derived = d.pop("isDerived", UNSET)

        main_constraint_id = d.pop("mainConstraintId", UNSET)

        main_feature_id = d.pop("mainFeatureId", UNSET)

        main_parameter_id = d.pop("mainParameterId", UNSET)

        main_part_id = d.pop("mainPartId", UNSET)

        all_hole_faces = cast(list[str], d.pop("allHoleFaces", UNSET))

        _counterbore_depth = d.pop("counterboreDepth", UNSET)
        counterbore_depth: BTTolerantValueDisplayData3483 | Unset
        if isinstance(_counterbore_depth, Unset):
            counterbore_depth = UNSET
        else:
            counterbore_depth = BTTolerantValueDisplayData3483.from_dict(_counterbore_depth)

        _counterbore_diameter = d.pop("counterboreDiameter", UNSET)
        counterbore_diameter: BTTolerantValueDisplayData3483 | Unset
        if isinstance(_counterbore_diameter, Unset):
            counterbore_diameter = UNSET
        else:
            counterbore_diameter = BTTolerantValueDisplayData3483.from_dict(_counterbore_diameter)

        _countersink_angle = d.pop("countersinkAngle", UNSET)
        countersink_angle: BTTolerantValueDisplayData3483 | Unset
        if isinstance(_countersink_angle, Unset):
            countersink_angle = UNSET
        else:
            countersink_angle = BTTolerantValueDisplayData3483.from_dict(_countersink_angle)

        _countersink_diameter = d.pop("countersinkDiameter", UNSET)
        countersink_diameter: BTTolerantValueDisplayData3483 | Unset
        if isinstance(_countersink_diameter, Unset):
            countersink_diameter = UNSET
        else:
            countersink_diameter = BTTolerantValueDisplayData3483.from_dict(_countersink_diameter)

        _depth = d.pop("depth", UNSET)
        depth: BTTolerantValueDisplayData3483 | Unset
        if isinstance(_depth, Unset):
            depth = UNSET
        else:
            depth = BTTolerantValueDisplayData3483.from_dict(_depth)

        _diameter = d.pop("diameter", UNSET)
        diameter: BTTolerantValueDisplayData3483 | Unset
        if isinstance(_diameter, Unset):
            diameter = UNSET
        else:
            diameter = BTTolerantValueDisplayData3483.from_dict(_diameter)

        feature_id = d.pop("featureId", UNSET)

        _hole_type = d.pop("holeType", UNSET)
        hole_type: GBTHoleType | Unset
        if isinstance(_hole_type, Unset):
            hole_type = UNSET
        else:
            hole_type = GBTHoleType(_hole_type)

        is_pipe_tap = d.pop("isPipeTap", UNSET)

        is_tapered_pipe_tap = d.pop("isTaperedPipeTap", UNSET)

        is_tapped = d.pop("isTapped", UNSET)

        _label_location = d.pop("labelLocation", UNSET)
        label_location: BTVector2D1812 | Unset
        if isinstance(_label_location, Unset):
            label_location = UNSET
        else:
            label_location = BTVector2D1812.from_dict(_label_location)

        part_id = d.pop("partId", UNSET)

        reference_radius = d.pop("referenceRadius", UNSET)

        tap_size = d.pop("tapSize", UNSET)

        _tapped_depth = d.pop("tappedDepth", UNSET)
        tapped_depth: BTTolerantValueDisplayData3483 | Unset
        if isinstance(_tapped_depth, Unset):
            tapped_depth = UNSET
        else:
            tapped_depth = BTTolerantValueDisplayData3483.from_dict(_tapped_depth)

        bt_hole_callout_display_data_3452 = cls(
            annotation_plane=annotation_plane,
            base_plane=base_plane,
            bt_type=bt_type,
            characteristic_id=characteristic_id,
            deterministic_id=deterministic_id,
            dxdy_segments=dxdy_segments,
            is_constrained_to_plane=is_constrained_to_plane,
            is_deletion=is_deletion,
            is_derived=is_derived,
            main_constraint_id=main_constraint_id,
            main_feature_id=main_feature_id,
            main_parameter_id=main_parameter_id,
            main_part_id=main_part_id,
            all_hole_faces=all_hole_faces,
            counterbore_depth=counterbore_depth,
            counterbore_diameter=counterbore_diameter,
            countersink_angle=countersink_angle,
            countersink_diameter=countersink_diameter,
            depth=depth,
            diameter=diameter,
            feature_id=feature_id,
            hole_type=hole_type,
            is_pipe_tap=is_pipe_tap,
            is_tapered_pipe_tap=is_tapered_pipe_tap,
            is_tapped=is_tapped,
            label_location=label_location,
            part_id=part_id,
            reference_radius=reference_radius,
            tap_size=tap_size,
            tapped_depth=tapped_depth,
        )

        bt_hole_callout_display_data_3452.additional_properties = d
        return bt_hole_callout_display_data_3452

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
