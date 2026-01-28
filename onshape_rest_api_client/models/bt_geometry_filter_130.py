from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_geometry_type import GBTGeometryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTGeometryFilter130")


@_attrs_define
class BTGeometryFilter130:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        geometry_type (GBTGeometryType | Unset):
    """

    bt_type: str | Unset = UNSET
    geometry_type: GBTGeometryType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        geometry_type: str | Unset = UNSET
        if not isinstance(self.geometry_type, Unset):
            geometry_type = self.geometry_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if geometry_type is not UNSET:
            field_dict["geometryType"] = geometry_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _geometry_type = d.pop("geometryType", UNSET)
        geometry_type: GBTGeometryType | Unset
        if isinstance(_geometry_type, Unset):
            geometry_type = UNSET
        else:
            geometry_type = GBTGeometryType(_geometry_type)

        bt_geometry_filter_130 = cls(
            bt_type=bt_type,
            geometry_type=geometry_type,
        )

        bt_geometry_filter_130.additional_properties = d
        return bt_geometry_filter_130

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
