from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_units_maximum_display_precision_info_units_display_precision import (
        BTUnitsMaximumDisplayPrecisionInfoUnitsDisplayPrecision,
    )


T = TypeVar("T", bound="BTUnitsMaximumDisplayPrecisionInfo")


@_attrs_define
class BTUnitsMaximumDisplayPrecisionInfo:
    """
    Attributes:
        units_display_precision (BTUnitsMaximumDisplayPrecisionInfoUnitsDisplayPrecision | Unset):
    """

    units_display_precision: BTUnitsMaximumDisplayPrecisionInfoUnitsDisplayPrecision | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        units_display_precision: dict[str, Any] | Unset = UNSET
        if not isinstance(self.units_display_precision, Unset):
            units_display_precision = self.units_display_precision.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if units_display_precision is not UNSET:
            field_dict["unitsDisplayPrecision"] = units_display_precision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_units_maximum_display_precision_info_units_display_precision import (
            BTUnitsMaximumDisplayPrecisionInfoUnitsDisplayPrecision,
        )

        d = dict(src_dict)
        _units_display_precision = d.pop("unitsDisplayPrecision", UNSET)
        units_display_precision: BTUnitsMaximumDisplayPrecisionInfoUnitsDisplayPrecision | Unset
        if isinstance(_units_display_precision, Unset):
            units_display_precision = UNSET
        else:
            units_display_precision = BTUnitsMaximumDisplayPrecisionInfoUnitsDisplayPrecision.from_dict(
                _units_display_precision
            )

        bt_units_maximum_display_precision_info = cls(
            units_display_precision=units_display_precision,
        )

        bt_units_maximum_display_precision_info.additional_properties = d
        return bt_units_maximum_display_precision_info

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
