from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_table_base_row_metadata_3181 import BTTableBaseRowMetadata3181
    from ..models.bt_table_row_1054_column_id_to_cell import BTTableRow1054ColumnIdToCell
    from ..models.bt_tree_node_20 import BTTreeNode20


T = TypeVar("T", bound="BTTableRow1054")


@_attrs_define
class BTTableRow1054:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        column_id_to_cell (BTTableRow1054ColumnIdToCell | Unset):
        id (str | Unset):
        meta_data (BTTreeNode20 | Unset):
        node_id (str | Unset):
        row_metadata (BTTableBaseRowMetadata3181 | Unset):
    """

    bt_type: str | Unset = UNSET
    column_id_to_cell: BTTableRow1054ColumnIdToCell | Unset = UNSET
    id: str | Unset = UNSET
    meta_data: BTTreeNode20 | Unset = UNSET
    node_id: str | Unset = UNSET
    row_metadata: BTTableBaseRowMetadata3181 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        column_id_to_cell: dict[str, Any] | Unset = UNSET
        if not isinstance(self.column_id_to_cell, Unset):
            column_id_to_cell = self.column_id_to_cell.to_dict()

        id = self.id

        meta_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta_data, Unset):
            meta_data = self.meta_data.to_dict()

        node_id = self.node_id

        row_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.row_metadata, Unset):
            row_metadata = self.row_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if column_id_to_cell is not UNSET:
            field_dict["columnIdToCell"] = column_id_to_cell
        if id is not UNSET:
            field_dict["id"] = id
        if meta_data is not UNSET:
            field_dict["metaData"] = meta_data
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if row_metadata is not UNSET:
            field_dict["rowMetadata"] = row_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_table_base_row_metadata_3181 import BTTableBaseRowMetadata3181
        from ..models.bt_table_row_1054_column_id_to_cell import BTTableRow1054ColumnIdToCell
        from ..models.bt_tree_node_20 import BTTreeNode20

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _column_id_to_cell = d.pop("columnIdToCell", UNSET)
        column_id_to_cell: BTTableRow1054ColumnIdToCell | Unset
        if isinstance(_column_id_to_cell, Unset):
            column_id_to_cell = UNSET
        else:
            column_id_to_cell = BTTableRow1054ColumnIdToCell.from_dict(_column_id_to_cell)

        id = d.pop("id", UNSET)

        _meta_data = d.pop("metaData", UNSET)
        meta_data: BTTreeNode20 | Unset
        if isinstance(_meta_data, Unset):
            meta_data = UNSET
        else:
            meta_data = BTTreeNode20.from_dict(_meta_data)

        node_id = d.pop("nodeId", UNSET)

        _row_metadata = d.pop("rowMetadata", UNSET)
        row_metadata: BTTableBaseRowMetadata3181 | Unset
        if isinstance(_row_metadata, Unset):
            row_metadata = UNSET
        else:
            row_metadata = BTTableBaseRowMetadata3181.from_dict(_row_metadata)

        bt_table_row_1054 = cls(
            bt_type=bt_type,
            column_id_to_cell=column_id_to_cell,
            id=id,
            meta_data=meta_data,
            node_id=node_id,
            row_metadata=row_metadata,
        )

        bt_table_row_1054.additional_properties = d
        return bt_table_row_1054

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
