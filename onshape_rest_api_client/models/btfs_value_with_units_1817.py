from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btfs_value_with_units_1817_unit_to_power import BTFSValueWithUnits1817UnitToPower


T = TypeVar("T", bound="BTFSValueWithUnits1817")


@_attrs_define
class BTFSValueWithUnits1817:
    """
    Attributes:
        bt_type (str): Type of JSON object.
        type_tag (str | Unset):
        unit_to_power (BTFSValueWithUnits1817UnitToPower | Unset):
        value (float | Unset):
    """

    bt_type: str
    type_tag: str | Unset = UNSET
    unit_to_power: BTFSValueWithUnits1817UnitToPower | Unset = UNSET
    value: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        type_tag = self.type_tag

        unit_to_power: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unit_to_power, Unset):
            unit_to_power = self.unit_to_power.to_dict()

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "btType": bt_type,
            }
        )
        if type_tag is not UNSET:
            field_dict["typeTag"] = type_tag
        if unit_to_power is not UNSET:
            field_dict["unitToPower"] = unit_to_power
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btfs_value_with_units_1817_unit_to_power import BTFSValueWithUnits1817UnitToPower

        d = dict(src_dict)
        bt_type = d.pop("btType")

        type_tag = d.pop("typeTag", UNSET)

        _unit_to_power = d.pop("unitToPower", UNSET)
        unit_to_power: BTFSValueWithUnits1817UnitToPower | Unset
        if isinstance(_unit_to_power, Unset):
            unit_to_power = UNSET
        else:
            unit_to_power = BTFSValueWithUnits1817UnitToPower.from_dict(_unit_to_power)

        value = d.pop("value", UNSET)

        btfs_value_with_units_1817 = cls(
            bt_type=bt_type,
            type_tag=type_tag,
            unit_to_power=unit_to_power,
            value=value,
        )

        btfs_value_with_units_1817.additional_properties = d
        return btfs_value_with_units_1817

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
