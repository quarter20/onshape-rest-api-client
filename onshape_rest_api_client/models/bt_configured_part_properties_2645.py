from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_configured_part_properties_2645_property_id_to_configured_table import (
        BTConfiguredPartProperties2645PropertyIdToConfiguredTable,
    )
    from ..models.bt_part_with_configured_properties_2163 import BTPartWithConfiguredProperties2163


T = TypeVar("T", bound="BTConfiguredPartProperties2645")


@_attrs_define
class BTConfiguredPartProperties2645:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        node_id (str | Unset):
        parts (list[BTPartWithConfiguredProperties2163] | Unset):
        property_id_to_configured_table (BTConfiguredPartProperties2645PropertyIdToConfiguredTable | Unset):
        synchronize_to_single_enum_input (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    node_id: str | Unset = UNSET
    parts: list[BTPartWithConfiguredProperties2163] | Unset = UNSET
    property_id_to_configured_table: BTConfiguredPartProperties2645PropertyIdToConfiguredTable | Unset = UNSET
    synchronize_to_single_enum_input: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        node_id = self.node_id

        parts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parts, Unset):
            parts = []
            for parts_item_data in self.parts:
                parts_item = parts_item_data.to_dict()
                parts.append(parts_item)

        property_id_to_configured_table: dict[str, Any] | Unset = UNSET
        if not isinstance(self.property_id_to_configured_table, Unset):
            property_id_to_configured_table = self.property_id_to_configured_table.to_dict()

        synchronize_to_single_enum_input = self.synchronize_to_single_enum_input

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if parts is not UNSET:
            field_dict["parts"] = parts
        if property_id_to_configured_table is not UNSET:
            field_dict["propertyIdToConfiguredTable"] = property_id_to_configured_table
        if synchronize_to_single_enum_input is not UNSET:
            field_dict["synchronizeToSingleEnumInput"] = synchronize_to_single_enum_input

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_configured_part_properties_2645_property_id_to_configured_table import (
            BTConfiguredPartProperties2645PropertyIdToConfiguredTable,
        )
        from ..models.bt_part_with_configured_properties_2163 import BTPartWithConfiguredProperties2163

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _parts = d.pop("parts", UNSET)
        parts: list[BTPartWithConfiguredProperties2163] | Unset = UNSET
        if _parts is not UNSET:
            parts = []
            for parts_item_data in _parts:
                parts_item = BTPartWithConfiguredProperties2163.from_dict(parts_item_data)

                parts.append(parts_item)

        _property_id_to_configured_table = d.pop("propertyIdToConfiguredTable", UNSET)
        property_id_to_configured_table: BTConfiguredPartProperties2645PropertyIdToConfiguredTable | Unset
        if isinstance(_property_id_to_configured_table, Unset):
            property_id_to_configured_table = UNSET
        else:
            property_id_to_configured_table = BTConfiguredPartProperties2645PropertyIdToConfiguredTable.from_dict(
                _property_id_to_configured_table
            )

        synchronize_to_single_enum_input = d.pop("synchronizeToSingleEnumInput", UNSET)

        bt_configured_part_properties_2645 = cls(
            bt_type=bt_type,
            node_id=node_id,
            parts=parts,
            property_id_to_configured_table=property_id_to_configured_table,
            synchronize_to_single_enum_input=synchronize_to_single_enum_input,
        )

        bt_configured_part_properties_2645.additional_properties = d
        return bt_configured_part_properties_2645

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
