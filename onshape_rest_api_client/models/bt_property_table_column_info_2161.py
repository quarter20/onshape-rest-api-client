from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_table_column_spec_1967 import BTTableColumnSpec1967


T = TypeVar("T", bound="BTPropertyTableColumnInfo2161")


@_attrs_define
class BTPropertyTableColumnInfo2161:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        id (str | Unset):
        node_id (str | Unset):
        specification (BTTableColumnSpec1967 | Unset):
        is_computed_assembly_property (bool | Unset):
        is_computed_property (bool | Unset):
        property_value_type (int | Unset):
    """

    bt_type: str | Unset = UNSET
    id: str | Unset = UNSET
    node_id: str | Unset = UNSET
    specification: BTTableColumnSpec1967 | Unset = UNSET
    is_computed_assembly_property: bool | Unset = UNSET
    is_computed_property: bool | Unset = UNSET
    property_value_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        id = self.id

        node_id = self.node_id

        specification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.specification, Unset):
            specification = self.specification.to_dict()

        is_computed_assembly_property = self.is_computed_assembly_property

        is_computed_property = self.is_computed_property

        property_value_type = self.property_value_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if id is not UNSET:
            field_dict["id"] = id
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if specification is not UNSET:
            field_dict["specification"] = specification
        if is_computed_assembly_property is not UNSET:
            field_dict["isComputedAssemblyProperty"] = is_computed_assembly_property
        if is_computed_property is not UNSET:
            field_dict["isComputedProperty"] = is_computed_property
        if property_value_type is not UNSET:
            field_dict["propertyValueType"] = property_value_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_table_column_spec_1967 import BTTableColumnSpec1967

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        id = d.pop("id", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _specification = d.pop("specification", UNSET)
        specification: BTTableColumnSpec1967 | Unset
        if isinstance(_specification, Unset):
            specification = UNSET
        else:
            specification = BTTableColumnSpec1967.from_dict(_specification)

        is_computed_assembly_property = d.pop("isComputedAssemblyProperty", UNSET)

        is_computed_property = d.pop("isComputedProperty", UNSET)

        property_value_type = d.pop("propertyValueType", UNSET)

        bt_property_table_column_info_2161 = cls(
            bt_type=bt_type,
            id=id,
            node_id=node_id,
            specification=specification,
            is_computed_assembly_property=is_computed_assembly_property,
            is_computed_property=is_computed_property,
            property_value_type=property_value_type,
        )

        bt_property_table_column_info_2161.additional_properties = d
        return bt_property_table_column_info_2161

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
