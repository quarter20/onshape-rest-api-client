from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_field_weld_flag import GBTFieldWeldFlag
from ..models.gbt_weld_contour_type import GBTWeldContourType
from ..models.gbt_weld_finishing import GBTWeldFinishing
from ..models.gbt_weld_joint_type import GBTWeldJointType
from ..models.gbt_weld_standard import GBTWeldStandard
from ..models.gbt_weld_type import GBTWeldType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_coordinate_system_387 import BTCoordinateSystem387
    from ..models.bt_vector_2d1812 import BTVector2D1812


T = TypeVar("T", bound="BTAnnotationWeldDisplayData4919")


@_attrs_define
class BTAnnotationWeldDisplayData4919:
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
        main_constraint_id (str | Unset):
        main_feature_id (str | Unset):
        main_parameter_id (str | Unset):
        main_part_id (str | Unset):
        all_around (bool | Unset):
        flag (GBTFieldWeldFlag | Unset):
        iso_flip (bool | Unset):
        joint_type (GBTWeldJointType | Unset):
        lower_contour_type (GBTWeldContourType | Unset):
        lower_finishing (GBTWeldFinishing | Unset):
        lower_flag (bool | Unset):
        lower_groove (float | Unset):
        lower_root_opening (float | Unset):
        lower_value_four (float | Unset):
        lower_value_one (float | Unset):
        lower_value_three (float | Unset):
        lower_value_two (float | Unset):
        lower_weld_type (GBTWeldType | Unset):
        reference (str | Unset):
        standard (GBTWeldStandard | Unset):
        upper_contour_type (GBTWeldContourType | Unset):
        upper_finishing (GBTWeldFinishing | Unset):
        upper_flag (bool | Unset):
        upper_groove (float | Unset):
        upper_root_opening (float | Unset):
        upper_value_four (float | Unset):
        upper_value_one (float | Unset):
        upper_value_three (float | Unset):
        upper_value_two (float | Unset):
        upper_weld_type (GBTWeldType | Unset):
    """

    annotation_plane: BTCoordinateSystem387 | Unset = UNSET
    base_plane: BTCoordinateSystem387 | Unset = UNSET
    bt_type: str | Unset = UNSET
    characteristic_id: str | Unset = UNSET
    deterministic_id: str | Unset = UNSET
    dxdy_segments: list[BTVector2D1812] | Unset = UNSET
    is_constrained_to_plane: bool | Unset = UNSET
    is_deletion: bool | Unset = UNSET
    main_constraint_id: str | Unset = UNSET
    main_feature_id: str | Unset = UNSET
    main_parameter_id: str | Unset = UNSET
    main_part_id: str | Unset = UNSET
    all_around: bool | Unset = UNSET
    flag: GBTFieldWeldFlag | Unset = UNSET
    iso_flip: bool | Unset = UNSET
    joint_type: GBTWeldJointType | Unset = UNSET
    lower_contour_type: GBTWeldContourType | Unset = UNSET
    lower_finishing: GBTWeldFinishing | Unset = UNSET
    lower_flag: bool | Unset = UNSET
    lower_groove: float | Unset = UNSET
    lower_root_opening: float | Unset = UNSET
    lower_value_four: float | Unset = UNSET
    lower_value_one: float | Unset = UNSET
    lower_value_three: float | Unset = UNSET
    lower_value_two: float | Unset = UNSET
    lower_weld_type: GBTWeldType | Unset = UNSET
    reference: str | Unset = UNSET
    standard: GBTWeldStandard | Unset = UNSET
    upper_contour_type: GBTWeldContourType | Unset = UNSET
    upper_finishing: GBTWeldFinishing | Unset = UNSET
    upper_flag: bool | Unset = UNSET
    upper_groove: float | Unset = UNSET
    upper_root_opening: float | Unset = UNSET
    upper_value_four: float | Unset = UNSET
    upper_value_one: float | Unset = UNSET
    upper_value_three: float | Unset = UNSET
    upper_value_two: float | Unset = UNSET
    upper_weld_type: GBTWeldType | Unset = UNSET
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

        main_constraint_id = self.main_constraint_id

        main_feature_id = self.main_feature_id

        main_parameter_id = self.main_parameter_id

        main_part_id = self.main_part_id

        all_around = self.all_around

        flag: str | Unset = UNSET
        if not isinstance(self.flag, Unset):
            flag = self.flag.value

        iso_flip = self.iso_flip

        joint_type: str | Unset = UNSET
        if not isinstance(self.joint_type, Unset):
            joint_type = self.joint_type.value

        lower_contour_type: str | Unset = UNSET
        if not isinstance(self.lower_contour_type, Unset):
            lower_contour_type = self.lower_contour_type.value

        lower_finishing: str | Unset = UNSET
        if not isinstance(self.lower_finishing, Unset):
            lower_finishing = self.lower_finishing.value

        lower_flag = self.lower_flag

        lower_groove = self.lower_groove

        lower_root_opening = self.lower_root_opening

        lower_value_four = self.lower_value_four

        lower_value_one = self.lower_value_one

        lower_value_three = self.lower_value_three

        lower_value_two = self.lower_value_two

        lower_weld_type: str | Unset = UNSET
        if not isinstance(self.lower_weld_type, Unset):
            lower_weld_type = self.lower_weld_type.value

        reference = self.reference

        standard: str | Unset = UNSET
        if not isinstance(self.standard, Unset):
            standard = self.standard.value

        upper_contour_type: str | Unset = UNSET
        if not isinstance(self.upper_contour_type, Unset):
            upper_contour_type = self.upper_contour_type.value

        upper_finishing: str | Unset = UNSET
        if not isinstance(self.upper_finishing, Unset):
            upper_finishing = self.upper_finishing.value

        upper_flag = self.upper_flag

        upper_groove = self.upper_groove

        upper_root_opening = self.upper_root_opening

        upper_value_four = self.upper_value_four

        upper_value_one = self.upper_value_one

        upper_value_three = self.upper_value_three

        upper_value_two = self.upper_value_two

        upper_weld_type: str | Unset = UNSET
        if not isinstance(self.upper_weld_type, Unset):
            upper_weld_type = self.upper_weld_type.value

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
        if main_constraint_id is not UNSET:
            field_dict["mainConstraintId"] = main_constraint_id
        if main_feature_id is not UNSET:
            field_dict["mainFeatureId"] = main_feature_id
        if main_parameter_id is not UNSET:
            field_dict["mainParameterId"] = main_parameter_id
        if main_part_id is not UNSET:
            field_dict["mainPartId"] = main_part_id
        if all_around is not UNSET:
            field_dict["allAround"] = all_around
        if flag is not UNSET:
            field_dict["flag"] = flag
        if iso_flip is not UNSET:
            field_dict["isoFlip"] = iso_flip
        if joint_type is not UNSET:
            field_dict["jointType"] = joint_type
        if lower_contour_type is not UNSET:
            field_dict["lowerContourType"] = lower_contour_type
        if lower_finishing is not UNSET:
            field_dict["lowerFinishing"] = lower_finishing
        if lower_flag is not UNSET:
            field_dict["lowerFlag"] = lower_flag
        if lower_groove is not UNSET:
            field_dict["lowerGroove"] = lower_groove
        if lower_root_opening is not UNSET:
            field_dict["lowerRootOpening"] = lower_root_opening
        if lower_value_four is not UNSET:
            field_dict["lowerValueFour"] = lower_value_four
        if lower_value_one is not UNSET:
            field_dict["lowerValueOne"] = lower_value_one
        if lower_value_three is not UNSET:
            field_dict["lowerValueThree"] = lower_value_three
        if lower_value_two is not UNSET:
            field_dict["lowerValueTwo"] = lower_value_two
        if lower_weld_type is not UNSET:
            field_dict["lowerWeldType"] = lower_weld_type
        if reference is not UNSET:
            field_dict["reference"] = reference
        if standard is not UNSET:
            field_dict["standard"] = standard
        if upper_contour_type is not UNSET:
            field_dict["upperContourType"] = upper_contour_type
        if upper_finishing is not UNSET:
            field_dict["upperFinishing"] = upper_finishing
        if upper_flag is not UNSET:
            field_dict["upperFlag"] = upper_flag
        if upper_groove is not UNSET:
            field_dict["upperGroove"] = upper_groove
        if upper_root_opening is not UNSET:
            field_dict["upperRootOpening"] = upper_root_opening
        if upper_value_four is not UNSET:
            field_dict["upperValueFour"] = upper_value_four
        if upper_value_one is not UNSET:
            field_dict["upperValueOne"] = upper_value_one
        if upper_value_three is not UNSET:
            field_dict["upperValueThree"] = upper_value_three
        if upper_value_two is not UNSET:
            field_dict["upperValueTwo"] = upper_value_two
        if upper_weld_type is not UNSET:
            field_dict["upperWeldType"] = upper_weld_type

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

        main_constraint_id = d.pop("mainConstraintId", UNSET)

        main_feature_id = d.pop("mainFeatureId", UNSET)

        main_parameter_id = d.pop("mainParameterId", UNSET)

        main_part_id = d.pop("mainPartId", UNSET)

        all_around = d.pop("allAround", UNSET)

        _flag = d.pop("flag", UNSET)
        flag: GBTFieldWeldFlag | Unset
        if isinstance(_flag, Unset):
            flag = UNSET
        else:
            flag = GBTFieldWeldFlag(_flag)

        iso_flip = d.pop("isoFlip", UNSET)

        _joint_type = d.pop("jointType", UNSET)
        joint_type: GBTWeldJointType | Unset
        if isinstance(_joint_type, Unset):
            joint_type = UNSET
        else:
            joint_type = GBTWeldJointType(_joint_type)

        _lower_contour_type = d.pop("lowerContourType", UNSET)
        lower_contour_type: GBTWeldContourType | Unset
        if isinstance(_lower_contour_type, Unset):
            lower_contour_type = UNSET
        else:
            lower_contour_type = GBTWeldContourType(_lower_contour_type)

        _lower_finishing = d.pop("lowerFinishing", UNSET)
        lower_finishing: GBTWeldFinishing | Unset
        if isinstance(_lower_finishing, Unset):
            lower_finishing = UNSET
        else:
            lower_finishing = GBTWeldFinishing(_lower_finishing)

        lower_flag = d.pop("lowerFlag", UNSET)

        lower_groove = d.pop("lowerGroove", UNSET)

        lower_root_opening = d.pop("lowerRootOpening", UNSET)

        lower_value_four = d.pop("lowerValueFour", UNSET)

        lower_value_one = d.pop("lowerValueOne", UNSET)

        lower_value_three = d.pop("lowerValueThree", UNSET)

        lower_value_two = d.pop("lowerValueTwo", UNSET)

        _lower_weld_type = d.pop("lowerWeldType", UNSET)
        lower_weld_type: GBTWeldType | Unset
        if isinstance(_lower_weld_type, Unset):
            lower_weld_type = UNSET
        else:
            lower_weld_type = GBTWeldType(_lower_weld_type)

        reference = d.pop("reference", UNSET)

        _standard = d.pop("standard", UNSET)
        standard: GBTWeldStandard | Unset
        if isinstance(_standard, Unset):
            standard = UNSET
        else:
            standard = GBTWeldStandard(_standard)

        _upper_contour_type = d.pop("upperContourType", UNSET)
        upper_contour_type: GBTWeldContourType | Unset
        if isinstance(_upper_contour_type, Unset):
            upper_contour_type = UNSET
        else:
            upper_contour_type = GBTWeldContourType(_upper_contour_type)

        _upper_finishing = d.pop("upperFinishing", UNSET)
        upper_finishing: GBTWeldFinishing | Unset
        if isinstance(_upper_finishing, Unset):
            upper_finishing = UNSET
        else:
            upper_finishing = GBTWeldFinishing(_upper_finishing)

        upper_flag = d.pop("upperFlag", UNSET)

        upper_groove = d.pop("upperGroove", UNSET)

        upper_root_opening = d.pop("upperRootOpening", UNSET)

        upper_value_four = d.pop("upperValueFour", UNSET)

        upper_value_one = d.pop("upperValueOne", UNSET)

        upper_value_three = d.pop("upperValueThree", UNSET)

        upper_value_two = d.pop("upperValueTwo", UNSET)

        _upper_weld_type = d.pop("upperWeldType", UNSET)
        upper_weld_type: GBTWeldType | Unset
        if isinstance(_upper_weld_type, Unset):
            upper_weld_type = UNSET
        else:
            upper_weld_type = GBTWeldType(_upper_weld_type)

        bt_annotation_weld_display_data_4919 = cls(
            annotation_plane=annotation_plane,
            base_plane=base_plane,
            bt_type=bt_type,
            characteristic_id=characteristic_id,
            deterministic_id=deterministic_id,
            dxdy_segments=dxdy_segments,
            is_constrained_to_plane=is_constrained_to_plane,
            is_deletion=is_deletion,
            main_constraint_id=main_constraint_id,
            main_feature_id=main_feature_id,
            main_parameter_id=main_parameter_id,
            main_part_id=main_part_id,
            all_around=all_around,
            flag=flag,
            iso_flip=iso_flip,
            joint_type=joint_type,
            lower_contour_type=lower_contour_type,
            lower_finishing=lower_finishing,
            lower_flag=lower_flag,
            lower_groove=lower_groove,
            lower_root_opening=lower_root_opening,
            lower_value_four=lower_value_four,
            lower_value_one=lower_value_one,
            lower_value_three=lower_value_three,
            lower_value_two=lower_value_two,
            lower_weld_type=lower_weld_type,
            reference=reference,
            standard=standard,
            upper_contour_type=upper_contour_type,
            upper_finishing=upper_finishing,
            upper_flag=upper_flag,
            upper_groove=upper_groove,
            upper_root_opening=upper_root_opening,
            upper_value_four=upper_value_four,
            upper_value_one=upper_value_one,
            upper_value_three=upper_value_three,
            upper_value_two=upper_value_two,
            upper_weld_type=upper_weld_type,
        )

        bt_annotation_weld_display_data_4919.additional_properties = d
        return bt_annotation_weld_display_data_4919

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
