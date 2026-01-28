from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTCommonUnitInfo")


@_attrs_define
class BTCommonUnitInfo:
    """
    Attributes:
        abbreviation (str | Unset):
        unit (str | Unset):
        unit_name (str | Unset):
        unit_type (str | Unset):
        value_in_base_units (float | Unset):
    """

    abbreviation: str | Unset = UNSET
    unit: str | Unset = UNSET
    unit_name: str | Unset = UNSET
    unit_type: str | Unset = UNSET
    value_in_base_units: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        abbreviation = self.abbreviation

        unit = self.unit

        unit_name = self.unit_name

        unit_type = self.unit_type

        value_in_base_units = self.value_in_base_units

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if unit is not UNSET:
            field_dict["unit"] = unit
        if unit_name is not UNSET:
            field_dict["unitName"] = unit_name
        if unit_type is not UNSET:
            field_dict["unitType"] = unit_type
        if value_in_base_units is not UNSET:
            field_dict["valueInBaseUnits"] = value_in_base_units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        abbreviation = d.pop("abbreviation", UNSET)

        unit = d.pop("unit", UNSET)

        unit_name = d.pop("unitName", UNSET)

        unit_type = d.pop("unitType", UNSET)

        value_in_base_units = d.pop("valueInBaseUnits", UNSET)

        bt_common_unit_info = cls(
            abbreviation=abbreviation,
            unit=unit,
            unit_name=unit_name,
            unit_type=unit_type,
            value_in_base_units=value_in_base_units,
        )

        bt_common_unit_info.additional_properties = d
        return bt_common_unit_info

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
