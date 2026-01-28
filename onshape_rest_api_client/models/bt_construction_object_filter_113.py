from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTConstructionObjectFilter113")


@_attrs_define
class BTConstructionObjectFilter113:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        is_construction (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    is_construction: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        is_construction = self.is_construction

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if is_construction is not UNSET:
            field_dict["isConstruction"] = is_construction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        is_construction = d.pop("isConstruction", UNSET)

        bt_construction_object_filter_113 = cls(
            bt_type=bt_type,
            is_construction=is_construction,
        )

        bt_construction_object_filter_113.additional_properties = d
        return bt_construction_object_filter_113

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
