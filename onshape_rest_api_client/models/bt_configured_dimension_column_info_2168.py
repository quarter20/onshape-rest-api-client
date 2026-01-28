from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_configured_parent_type import GBTConfiguredParentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_table_column_spec_1967 import BTTableColumnSpec1967


T = TypeVar("T", bound="BTConfiguredDimensionColumnInfo2168")


@_attrs_define
class BTConfiguredDimensionColumnInfo2168:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        id (str | Unset):
        node_id (str | Unset):
        specification (BTTableColumnSpec1967 | Unset):
        parent_id (str | Unset):
        parent_name (str | Unset):
        parent_type (GBTConfiguredParentType | Unset):
        dimension_id (str | Unset):
        parameter_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    id: str | Unset = UNSET
    node_id: str | Unset = UNSET
    specification: BTTableColumnSpec1967 | Unset = UNSET
    parent_id: str | Unset = UNSET
    parent_name: str | Unset = UNSET
    parent_type: GBTConfiguredParentType | Unset = UNSET
    dimension_id: str | Unset = UNSET
    parameter_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        id = self.id

        node_id = self.node_id

        specification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.specification, Unset):
            specification = self.specification.to_dict()

        parent_id = self.parent_id

        parent_name = self.parent_name

        parent_type: str | Unset = UNSET
        if not isinstance(self.parent_type, Unset):
            parent_type = self.parent_type.value

        dimension_id = self.dimension_id

        parameter_id = self.parameter_id

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
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if parent_name is not UNSET:
            field_dict["parentName"] = parent_name
        if parent_type is not UNSET:
            field_dict["parentType"] = parent_type
        if dimension_id is not UNSET:
            field_dict["dimensionId"] = dimension_id
        if parameter_id is not UNSET:
            field_dict["parameterId"] = parameter_id

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

        parent_id = d.pop("parentId", UNSET)

        parent_name = d.pop("parentName", UNSET)

        _parent_type = d.pop("parentType", UNSET)
        parent_type: GBTConfiguredParentType | Unset
        if isinstance(_parent_type, Unset):
            parent_type = UNSET
        else:
            parent_type = GBTConfiguredParentType(_parent_type)

        dimension_id = d.pop("dimensionId", UNSET)

        parameter_id = d.pop("parameterId", UNSET)

        bt_configured_dimension_column_info_2168 = cls(
            bt_type=bt_type,
            id=id,
            node_id=node_id,
            specification=specification,
            parent_id=parent_id,
            parent_name=parent_name,
            parent_type=parent_type,
            dimension_id=dimension_id,
            parameter_id=parameter_id,
        )

        bt_configured_dimension_column_info_2168.additional_properties = d
        return bt_configured_dimension_column_info_2168

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
