from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_assembly_mate_value_info import BTAssemblyMateValueInfo


T = TypeVar("T", bound="BTAssemblyMateValuesInfo")


@_attrs_define
class BTAssemblyMateValuesInfo:
    """Get a list of mate values for all the mates of a specified assembly.

    Attributes:
        mate_values (list[BTAssemblyMateValueInfo] | Unset): Describes the relative position of the first mate connector
            with respect to the second along the designated degrees of freedom (DOF) for mates in the specified assembly.
    """

    mate_values: list[BTAssemblyMateValueInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mate_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mate_values, Unset):
            mate_values = []
            for mate_values_item_data in self.mate_values:
                mate_values_item = mate_values_item_data.to_dict()
                mate_values.append(mate_values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mate_values is not UNSET:
            field_dict["mateValues"] = mate_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_assembly_mate_value_info import BTAssemblyMateValueInfo

        d = dict(src_dict)
        _mate_values = d.pop("mateValues", UNSET)
        mate_values: list[BTAssemblyMateValueInfo] | Unset = UNSET
        if _mate_values is not UNSET:
            mate_values = []
            for mate_values_item_data in _mate_values:
                mate_values_item = BTAssemblyMateValueInfo.from_dict(mate_values_item_data)

                mate_values.append(mate_values_item)

        bt_assembly_mate_values_info = cls(
            mate_values=mate_values,
        )

        bt_assembly_mate_values_info.additional_properties = d
        return bt_assembly_mate_values_info

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
