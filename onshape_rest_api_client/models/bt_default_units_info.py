from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_default_unit_info import BTDefaultUnitInfo


T = TypeVar("T", bound="BTDefaultUnitsInfo")


@_attrs_define
class BTDefaultUnitsInfo:
    """
    Attributes:
        node_id (str | Unset):
        units (list[BTDefaultUnitInfo] | Unset):
    """

    node_id: str | Unset = UNSET
    units: list[BTDefaultUnitInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_id = self.node_id

        units: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.units, Unset):
            units = []
            for units_item_data in self.units:
                units_item = units_item_data.to_dict()
                units.append(units_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if units is not UNSET:
            field_dict["units"] = units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_default_unit_info import BTDefaultUnitInfo

        d = dict(src_dict)
        node_id = d.pop("nodeId", UNSET)

        _units = d.pop("units", UNSET)
        units: list[BTDefaultUnitInfo] | Unset = UNSET
        if _units is not UNSET:
            units = []
            for units_item_data in _units:
                units_item = BTDefaultUnitInfo.from_dict(units_item_data)

                units.append(units_item)

        bt_default_units_info = cls(
            node_id=node_id,
            units=units,
        )

        bt_default_units_info.additional_properties = d
        return bt_default_units_info

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
