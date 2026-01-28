from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_default_units_info import BTDefaultUnitsInfo
    from ..models.bt_unit_info_units_display_precision import BTUnitInfoUnitsDisplayPrecision


T = TypeVar("T", bound="BTUnitInfo")


@_attrs_define
class BTUnitInfo:
    """
    Attributes:
        default_units (BTDefaultUnitsInfo | Unset):
        units_display_precision (BTUnitInfoUnitsDisplayPrecision | Unset): Specifies the display precision for every
            supported unit.
    """

    default_units: BTDefaultUnitsInfo | Unset = UNSET
    units_display_precision: BTUnitInfoUnitsDisplayPrecision | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_units: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_units, Unset):
            default_units = self.default_units.to_dict()

        units_display_precision: dict[str, Any] | Unset = UNSET
        if not isinstance(self.units_display_precision, Unset):
            units_display_precision = self.units_display_precision.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_units is not UNSET:
            field_dict["defaultUnits"] = default_units
        if units_display_precision is not UNSET:
            field_dict["unitsDisplayPrecision"] = units_display_precision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_default_units_info import BTDefaultUnitsInfo
        from ..models.bt_unit_info_units_display_precision import BTUnitInfoUnitsDisplayPrecision

        d = dict(src_dict)
        _default_units = d.pop("defaultUnits", UNSET)
        default_units: BTDefaultUnitsInfo | Unset
        if isinstance(_default_units, Unset):
            default_units = UNSET
        else:
            default_units = BTDefaultUnitsInfo.from_dict(_default_units)

        _units_display_precision = d.pop("unitsDisplayPrecision", UNSET)
        units_display_precision: BTUnitInfoUnitsDisplayPrecision | Unset
        if isinstance(_units_display_precision, Unset):
            units_display_precision = UNSET
        else:
            units_display_precision = BTUnitInfoUnitsDisplayPrecision.from_dict(_units_display_precision)

        bt_unit_info = cls(
            default_units=default_units,
            units_display_precision=units_display_precision,
        )

        bt_unit_info.additional_properties = d
        return bt_unit_info

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
