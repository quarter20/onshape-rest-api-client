from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_annotation_attachment_location import GBTAnnotationAttachmentLocation
from ..models.gbt_annotation_type import GBTAnnotationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_coordinate_system_387 import BTCoordinateSystem387
    from ..models.bt_vector_2d1812 import BTVector2D1812


T = TypeVar("T", bound="BTAnnotationDeleteDisplayData1815")


@_attrs_define
class BTAnnotationDeleteDisplayData1815:
    """
    Attributes:
        all_references (list[str] | Unset):
        all_references_populated (bool | Unset):
        annotation_id (str | Unset):
        annotation_plane (BTCoordinateSystem387 | Unset):
        annotation_type (GBTAnnotationType | Unset):
        attachment_location (GBTAnnotationAttachmentLocation | Unset):
        base_plane (BTCoordinateSystem387 | Unset):
        bt_type (str | Unset): Type of JSON object.
        characteristic_id (str | Unset):
        deterministic_id (str | Unset):
        dxdy_segments (list[BTVector2D1812] | Unset):
        is_constrained_to_plane (bool | Unset):
        is_deletion (bool | Unset):
        is_derived (bool | Unset):
        is_plane_reference_missing (bool | Unset):
        main_annotation_id (str | Unset):
        main_constraint_id (str | Unset):
        main_feature_id (str | Unset):
        main_parameter_id (str | Unset):
        main_part_id (str | Unset):
        parent_characteristic_id (str | Unset):
    """

    all_references: list[str] | Unset = UNSET
    all_references_populated: bool | Unset = UNSET
    annotation_id: str | Unset = UNSET
    annotation_plane: BTCoordinateSystem387 | Unset = UNSET
    annotation_type: GBTAnnotationType | Unset = UNSET
    attachment_location: GBTAnnotationAttachmentLocation | Unset = UNSET
    base_plane: BTCoordinateSystem387 | Unset = UNSET
    bt_type: str | Unset = UNSET
    characteristic_id: str | Unset = UNSET
    deterministic_id: str | Unset = UNSET
    dxdy_segments: list[BTVector2D1812] | Unset = UNSET
    is_constrained_to_plane: bool | Unset = UNSET
    is_deletion: bool | Unset = UNSET
    is_derived: bool | Unset = UNSET
    is_plane_reference_missing: bool | Unset = UNSET
    main_annotation_id: str | Unset = UNSET
    main_constraint_id: str | Unset = UNSET
    main_feature_id: str | Unset = UNSET
    main_parameter_id: str | Unset = UNSET
    main_part_id: str | Unset = UNSET
    parent_characteristic_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_references: list[str] | Unset = UNSET
        if not isinstance(self.all_references, Unset):
            all_references = self.all_references

        all_references_populated = self.all_references_populated

        annotation_id = self.annotation_id

        annotation_plane: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotation_plane, Unset):
            annotation_plane = self.annotation_plane.to_dict()

        annotation_type: str | Unset = UNSET
        if not isinstance(self.annotation_type, Unset):
            annotation_type = self.annotation_type.value

        attachment_location: str | Unset = UNSET
        if not isinstance(self.attachment_location, Unset):
            attachment_location = self.attachment_location.value

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

        is_plane_reference_missing = self.is_plane_reference_missing

        main_annotation_id = self.main_annotation_id

        main_constraint_id = self.main_constraint_id

        main_feature_id = self.main_feature_id

        main_parameter_id = self.main_parameter_id

        main_part_id = self.main_part_id

        parent_characteristic_id = self.parent_characteristic_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_references is not UNSET:
            field_dict["allReferences"] = all_references
        if all_references_populated is not UNSET:
            field_dict["allReferencesPopulated"] = all_references_populated
        if annotation_id is not UNSET:
            field_dict["annotationId"] = annotation_id
        if annotation_plane is not UNSET:
            field_dict["annotationPlane"] = annotation_plane
        if annotation_type is not UNSET:
            field_dict["annotationType"] = annotation_type
        if attachment_location is not UNSET:
            field_dict["attachmentLocation"] = attachment_location
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
        if is_plane_reference_missing is not UNSET:
            field_dict["isPlaneReferenceMissing"] = is_plane_reference_missing
        if main_annotation_id is not UNSET:
            field_dict["mainAnnotationId"] = main_annotation_id
        if main_constraint_id is not UNSET:
            field_dict["mainConstraintId"] = main_constraint_id
        if main_feature_id is not UNSET:
            field_dict["mainFeatureId"] = main_feature_id
        if main_parameter_id is not UNSET:
            field_dict["mainParameterId"] = main_parameter_id
        if main_part_id is not UNSET:
            field_dict["mainPartId"] = main_part_id
        if parent_characteristic_id is not UNSET:
            field_dict["parentCharacteristicId"] = parent_characteristic_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_coordinate_system_387 import BTCoordinateSystem387
        from ..models.bt_vector_2d1812 import BTVector2D1812

        d = dict(src_dict)
        all_references = cast(list[str], d.pop("allReferences", UNSET))

        all_references_populated = d.pop("allReferencesPopulated", UNSET)

        annotation_id = d.pop("annotationId", UNSET)

        _annotation_plane = d.pop("annotationPlane", UNSET)
        annotation_plane: BTCoordinateSystem387 | Unset
        if isinstance(_annotation_plane, Unset):
            annotation_plane = UNSET
        else:
            annotation_plane = BTCoordinateSystem387.from_dict(_annotation_plane)

        _annotation_type = d.pop("annotationType", UNSET)
        annotation_type: GBTAnnotationType | Unset
        if isinstance(_annotation_type, Unset):
            annotation_type = UNSET
        else:
            annotation_type = GBTAnnotationType(_annotation_type)

        _attachment_location = d.pop("attachmentLocation", UNSET)
        attachment_location: GBTAnnotationAttachmentLocation | Unset
        if isinstance(_attachment_location, Unset):
            attachment_location = UNSET
        else:
            attachment_location = GBTAnnotationAttachmentLocation(_attachment_location)

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

        is_plane_reference_missing = d.pop("isPlaneReferenceMissing", UNSET)

        main_annotation_id = d.pop("mainAnnotationId", UNSET)

        main_constraint_id = d.pop("mainConstraintId", UNSET)

        main_feature_id = d.pop("mainFeatureId", UNSET)

        main_parameter_id = d.pop("mainParameterId", UNSET)

        main_part_id = d.pop("mainPartId", UNSET)

        parent_characteristic_id = d.pop("parentCharacteristicId", UNSET)

        bt_annotation_delete_display_data_1815 = cls(
            all_references=all_references,
            all_references_populated=all_references_populated,
            annotation_id=annotation_id,
            annotation_plane=annotation_plane,
            annotation_type=annotation_type,
            attachment_location=attachment_location,
            base_plane=base_plane,
            bt_type=bt_type,
            characteristic_id=characteristic_id,
            deterministic_id=deterministic_id,
            dxdy_segments=dxdy_segments,
            is_constrained_to_plane=is_constrained_to_plane,
            is_deletion=is_deletion,
            is_derived=is_derived,
            is_plane_reference_missing=is_plane_reference_missing,
            main_annotation_id=main_annotation_id,
            main_constraint_id=main_constraint_id,
            main_feature_id=main_feature_id,
            main_parameter_id=main_parameter_id,
            main_part_id=main_part_id,
            parent_characteristic_id=parent_characteristic_id,
        )

        bt_annotation_delete_display_data_1815.additional_properties = d
        return bt_annotation_delete_display_data_1815

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
