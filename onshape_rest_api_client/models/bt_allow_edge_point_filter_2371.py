from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAllowEdgePointFilter2371")


@_attrs_define
class BTAllowEdgePointFilter2371:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        allows_edge_point (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    allows_edge_point: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        allows_edge_point = self.allows_edge_point

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if allows_edge_point is not UNSET:
            field_dict["allowsEdgePoint"] = allows_edge_point

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        allows_edge_point = d.pop("allowsEdgePoint", UNSET)

        bt_allow_edge_point_filter_2371 = cls(
            bt_type=bt_type,
            allows_edge_point=allows_edge_point,
        )

        bt_allow_edge_point_filter_2371.additional_properties = d
        return bt_allow_edge_point_filter_2371

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
