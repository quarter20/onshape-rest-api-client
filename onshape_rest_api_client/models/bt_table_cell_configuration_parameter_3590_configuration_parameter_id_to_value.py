from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.btfs_value_1888 import BTFSValue1888


T = TypeVar("T", bound="BTTableCellConfigurationParameter3590ConfigurationParameterIdToValue")


@_attrs_define
class BTTableCellConfigurationParameter3590ConfigurationParameterIdToValue:
    """ """

    additional_properties: dict[str, BTFSValue1888] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btfs_value_1888 import BTFSValue1888

        d = dict(src_dict)
        bt_table_cell_configuration_parameter_3590_configuration_parameter_id_to_value = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = BTFSValue1888.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        bt_table_cell_configuration_parameter_3590_configuration_parameter_id_to_value.additional_properties = (
            additional_properties
        )
        return bt_table_cell_configuration_parameter_3590_configuration_parameter_id_to_value

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> BTFSValue1888:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: BTFSValue1888) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
