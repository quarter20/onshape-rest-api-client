from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTActiveSheetMetalFilter2944")


@_attrs_define
class BTActiveSheetMetalFilter2944:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        is_from_active_sheet_metal (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    is_from_active_sheet_metal: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        is_from_active_sheet_metal = self.is_from_active_sheet_metal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if is_from_active_sheet_metal is not UNSET:
            field_dict["isFromActiveSheetMetal"] = is_from_active_sheet_metal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        is_from_active_sheet_metal = d.pop("isFromActiveSheetMetal", UNSET)

        bt_active_sheet_metal_filter_2944 = cls(
            bt_type=bt_type,
            is_from_active_sheet_metal=is_from_active_sheet_metal,
        )

        bt_active_sheet_metal_filter_2944.additional_properties = d
        return bt_active_sheet_metal_filter_2944

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
