from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTBSMatrix386")


@_attrs_define
class BTBSMatrix386:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        full_transformation (list[float] | Unset):
        is_normalized (bool | Unset):
        m00 (float | Unset):
        m01 (float | Unset):
        m02 (float | Unset):
        m03 (float | Unset):
        m10 (float | Unset):
        m11 (float | Unset):
        m12 (float | Unset):
        m13 (float | Unset):
        m20 (float | Unset):
        m21 (float | Unset):
        m22 (float | Unset):
        m23 (float | Unset):
        rigid (bool | Unset):
        rigid_within_transform_tolerance (bool | Unset):
        translation (BTVector3D389 | Unset):
    """

    bt_type: str | Unset = UNSET
    full_transformation: list[float] | Unset = UNSET
    is_normalized: bool | Unset = UNSET
    m00: float | Unset = UNSET
    m01: float | Unset = UNSET
    m02: float | Unset = UNSET
    m03: float | Unset = UNSET
    m10: float | Unset = UNSET
    m11: float | Unset = UNSET
    m12: float | Unset = UNSET
    m13: float | Unset = UNSET
    m20: float | Unset = UNSET
    m21: float | Unset = UNSET
    m22: float | Unset = UNSET
    m23: float | Unset = UNSET
    rigid: bool | Unset = UNSET
    rigid_within_transform_tolerance: bool | Unset = UNSET
    translation: BTVector3D389 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        full_transformation: list[float] | Unset = UNSET
        if not isinstance(self.full_transformation, Unset):
            full_transformation = self.full_transformation

        is_normalized = self.is_normalized

        m00 = self.m00

        m01 = self.m01

        m02 = self.m02

        m03 = self.m03

        m10 = self.m10

        m11 = self.m11

        m12 = self.m12

        m13 = self.m13

        m20 = self.m20

        m21 = self.m21

        m22 = self.m22

        m23 = self.m23

        rigid = self.rigid

        rigid_within_transform_tolerance = self.rigid_within_transform_tolerance

        translation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.translation, Unset):
            translation = self.translation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if full_transformation is not UNSET:
            field_dict["fullTransformation"] = full_transformation
        if is_normalized is not UNSET:
            field_dict["isNormalized"] = is_normalized
        if m00 is not UNSET:
            field_dict["m00"] = m00
        if m01 is not UNSET:
            field_dict["m01"] = m01
        if m02 is not UNSET:
            field_dict["m02"] = m02
        if m03 is not UNSET:
            field_dict["m03"] = m03
        if m10 is not UNSET:
            field_dict["m10"] = m10
        if m11 is not UNSET:
            field_dict["m11"] = m11
        if m12 is not UNSET:
            field_dict["m12"] = m12
        if m13 is not UNSET:
            field_dict["m13"] = m13
        if m20 is not UNSET:
            field_dict["m20"] = m20
        if m21 is not UNSET:
            field_dict["m21"] = m21
        if m22 is not UNSET:
            field_dict["m22"] = m22
        if m23 is not UNSET:
            field_dict["m23"] = m23
        if rigid is not UNSET:
            field_dict["rigid"] = rigid
        if rigid_within_transform_tolerance is not UNSET:
            field_dict["rigidWithinTransformTolerance"] = rigid_within_transform_tolerance
        if translation is not UNSET:
            field_dict["translation"] = translation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_vector_3d389 import BTVector3D389

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        full_transformation = cast(list[float], d.pop("fullTransformation", UNSET))

        is_normalized = d.pop("isNormalized", UNSET)

        m00 = d.pop("m00", UNSET)

        m01 = d.pop("m01", UNSET)

        m02 = d.pop("m02", UNSET)

        m03 = d.pop("m03", UNSET)

        m10 = d.pop("m10", UNSET)

        m11 = d.pop("m11", UNSET)

        m12 = d.pop("m12", UNSET)

        m13 = d.pop("m13", UNSET)

        m20 = d.pop("m20", UNSET)

        m21 = d.pop("m21", UNSET)

        m22 = d.pop("m22", UNSET)

        m23 = d.pop("m23", UNSET)

        rigid = d.pop("rigid", UNSET)

        rigid_within_transform_tolerance = d.pop("rigidWithinTransformTolerance", UNSET)

        _translation = d.pop("translation", UNSET)
        translation: BTVector3D389 | Unset
        if isinstance(_translation, Unset):
            translation = UNSET
        else:
            translation = BTVector3D389.from_dict(_translation)

        btbs_matrix_386 = cls(
            bt_type=bt_type,
            full_transformation=full_transformation,
            is_normalized=is_normalized,
            m00=m00,
            m01=m01,
            m02=m02,
            m03=m03,
            m10=m10,
            m11=m11,
            m12=m12,
            m13=m13,
            m20=m20,
            m21=m21,
            m22=m22,
            m23=m23,
            rigid=rigid,
            rigid_within_transform_tolerance=rigid_within_transform_tolerance,
            translation=translation,
        )

        btbs_matrix_386.additional_properties = d
        return btbs_matrix_386

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
