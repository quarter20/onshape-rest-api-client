from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_common_unit_info import BTCommonUnitInfo
    from ..models.bt_common_units_info_quantity_type_to_base_units import BTCommonUnitsInfoQuantityTypeToBaseUnits


T = TypeVar("T", bound="BTCommonUnitsInfo")


@_attrs_define
class BTCommonUnitsInfo:
    """
    Attributes:
        quantity_type_to_base_units (BTCommonUnitsInfoQuantityTypeToBaseUnits | Unset):
        units (list[BTCommonUnitInfo] | Unset):
    """

    quantity_type_to_base_units: BTCommonUnitsInfoQuantityTypeToBaseUnits | Unset = UNSET
    units: list[BTCommonUnitInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quantity_type_to_base_units: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quantity_type_to_base_units, Unset):
            quantity_type_to_base_units = self.quantity_type_to_base_units.to_dict()

        units: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.units, Unset):
            units = []
            for units_item_data in self.units:
                units_item = units_item_data.to_dict()
                units.append(units_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quantity_type_to_base_units is not UNSET:
            field_dict["quantityTypeToBaseUnits"] = quantity_type_to_base_units
        if units is not UNSET:
            field_dict["units"] = units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_common_unit_info import BTCommonUnitInfo
        from ..models.bt_common_units_info_quantity_type_to_base_units import BTCommonUnitsInfoQuantityTypeToBaseUnits

        d = dict(src_dict)
        _quantity_type_to_base_units = d.pop("quantityTypeToBaseUnits", UNSET)
        quantity_type_to_base_units: BTCommonUnitsInfoQuantityTypeToBaseUnits | Unset
        if isinstance(_quantity_type_to_base_units, Unset):
            quantity_type_to_base_units = UNSET
        else:
            quantity_type_to_base_units = BTCommonUnitsInfoQuantityTypeToBaseUnits.from_dict(
                _quantity_type_to_base_units
            )

        _units = d.pop("units", UNSET)
        units: list[BTCommonUnitInfo] | Unset = UNSET
        if _units is not UNSET:
            units = []
            for units_item_data in _units:
                units_item = BTCommonUnitInfo.from_dict(units_item_data)

                units.append(units_item)

        bt_common_units_info = cls(
            quantity_type_to_base_units=quantity_type_to_base_units,
            units=units,
        )

        bt_common_units_info.additional_properties = d
        return bt_common_units_info

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
