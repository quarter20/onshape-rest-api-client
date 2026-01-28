from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_table_assembly_cross_highlight_data_2675 import BTTableAssemblyCrossHighlightData2675
    from ..models.bt_table_column_spec_1967 import BTTableColumnSpec1967


T = TypeVar("T", bound="BTSimulationTableColumnInfo1785")


@_attrs_define
class BTSimulationTableColumnInfo1785:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        id (str | Unset):
        node_id (str | Unset):
        specification (BTTableColumnSpec1967 | Unset):
        cross_highlight_data (BTTableAssemblyCrossHighlightData2675 | Unset):
    """

    bt_type: str | Unset = UNSET
    id: str | Unset = UNSET
    node_id: str | Unset = UNSET
    specification: BTTableColumnSpec1967 | Unset = UNSET
    cross_highlight_data: BTTableAssemblyCrossHighlightData2675 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        id = self.id

        node_id = self.node_id

        specification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.specification, Unset):
            specification = self.specification.to_dict()

        cross_highlight_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cross_highlight_data, Unset):
            cross_highlight_data = self.cross_highlight_data.to_dict()

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
        if cross_highlight_data is not UNSET:
            field_dict["crossHighlightData"] = cross_highlight_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_table_assembly_cross_highlight_data_2675 import BTTableAssemblyCrossHighlightData2675
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

        _cross_highlight_data = d.pop("crossHighlightData", UNSET)
        cross_highlight_data: BTTableAssemblyCrossHighlightData2675 | Unset
        if isinstance(_cross_highlight_data, Unset):
            cross_highlight_data = UNSET
        else:
            cross_highlight_data = BTTableAssemblyCrossHighlightData2675.from_dict(_cross_highlight_data)

        bt_simulation_table_column_info_1785 = cls(
            bt_type=bt_type,
            id=id,
            node_id=node_id,
            specification=specification,
            cross_highlight_data=cross_highlight_data,
        )

        bt_simulation_table_column_info_1785.additional_properties = d
        return bt_simulation_table_column_info_1785

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
