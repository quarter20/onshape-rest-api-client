from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTMatrix3X3340")


@_attrs_define
class BTMatrix3X3340:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        m00 (float | Unset):
        m01 (float | Unset):
        m02 (float | Unset):
        m10 (float | Unset):
        m11 (float | Unset):
        m12 (float | Unset):
        m20 (float | Unset):
        m21 (float | Unset):
        m22 (float | Unset):
    """

    bt_type: str | Unset = UNSET
    m00: float | Unset = UNSET
    m01: float | Unset = UNSET
    m02: float | Unset = UNSET
    m10: float | Unset = UNSET
    m11: float | Unset = UNSET
    m12: float | Unset = UNSET
    m20: float | Unset = UNSET
    m21: float | Unset = UNSET
    m22: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        m00 = self.m00

        m01 = self.m01

        m02 = self.m02

        m10 = self.m10

        m11 = self.m11

        m12 = self.m12

        m20 = self.m20

        m21 = self.m21

        m22 = self.m22

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if m00 is not UNSET:
            field_dict["m00"] = m00
        if m01 is not UNSET:
            field_dict["m01"] = m01
        if m02 is not UNSET:
            field_dict["m02"] = m02
        if m10 is not UNSET:
            field_dict["m10"] = m10
        if m11 is not UNSET:
            field_dict["m11"] = m11
        if m12 is not UNSET:
            field_dict["m12"] = m12
        if m20 is not UNSET:
            field_dict["m20"] = m20
        if m21 is not UNSET:
            field_dict["m21"] = m21
        if m22 is not UNSET:
            field_dict["m22"] = m22

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        m00 = d.pop("m00", UNSET)

        m01 = d.pop("m01", UNSET)

        m02 = d.pop("m02", UNSET)

        m10 = d.pop("m10", UNSET)

        m11 = d.pop("m11", UNSET)

        m12 = d.pop("m12", UNSET)

        m20 = d.pop("m20", UNSET)

        m21 = d.pop("m21", UNSET)

        m22 = d.pop("m22", UNSET)

        bt_matrix_3x3340 = cls(
            bt_type=bt_type,
            m00=m00,
            m01=m01,
            m02=m02,
            m10=m10,
            m11=m11,
            m12=m12,
            m20=m20,
            m21=m21,
            m22=m22,
        )

        bt_matrix_3x3340.additional_properties = d
        return bt_matrix_3x3340

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
