from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_coordinate_system_387 import BTCoordinateSystem387
    from ..models.bt_vector_2d1812 import BTVector2D1812


T = TypeVar("T", bound="BTDatumDisplayData3408")


@_attrs_define
class BTDatumDisplayData3408:
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
        name (str | Unset):
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
    name: str | Unset = UNSET
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

        name = self.name

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
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_coordinate_system_387 import BTCoordinateSystem387
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

        name = d.pop("name", UNSET)

        bt_datum_display_data_3408 = cls(
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
            name=name,
        )

        bt_datum_display_data_3408.additional_properties = d
        return bt_datum_display_data_3408

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
