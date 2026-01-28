from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_node_status_type import GBTNodeStatusType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_table_column_info_1222 import BTTableColumnInfo1222
    from ..models.bt_table_row_1054 import BTTableRow1054
    from ..models.bt_table_sort_order_4371 import BTTableSortOrder4371


T = TypeVar("T", bound="BTConfiguredPartPropertiesTable2740")


@_attrs_define
class BTConfiguredPartPropertiesTable2740:
    """
    Attributes:
        all_row_values (list[list[str]] | Unset):
        bt_type (str | Unset): Type of JSON object.
        column_count (int | Unset):
        frozen_columns (int | Unset):
        is_failed (bool | Unset):
        node_id (str | Unset):
        read_only (bool | Unset):
        row_count (int | Unset):
        sort_order (BTTableSortOrder4371 | Unset):
        status_message (str | Unset):
        status_type (GBTNodeStatusType | Unset):
        table_columns (list[BTTableColumnInfo1222] | Unset):
        table_id (str | Unset):
        table_rows (list[BTTableRow1054] | Unset):
        title (str | Unset):
        part_deterministic_id (str | Unset):
        part_deterministic_ids (list[str] | Unset):
        property_node_id (str | Unset):
    """

    all_row_values: list[list[str]] | Unset = UNSET
    bt_type: str | Unset = UNSET
    column_count: int | Unset = UNSET
    frozen_columns: int | Unset = UNSET
    is_failed: bool | Unset = UNSET
    node_id: str | Unset = UNSET
    read_only: bool | Unset = UNSET
    row_count: int | Unset = UNSET
    sort_order: BTTableSortOrder4371 | Unset = UNSET
    status_message: str | Unset = UNSET
    status_type: GBTNodeStatusType | Unset = UNSET
    table_columns: list[BTTableColumnInfo1222] | Unset = UNSET
    table_id: str | Unset = UNSET
    table_rows: list[BTTableRow1054] | Unset = UNSET
    title: str | Unset = UNSET
    part_deterministic_id: str | Unset = UNSET
    part_deterministic_ids: list[str] | Unset = UNSET
    property_node_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_row_values: list[list[str]] | Unset = UNSET
        if not isinstance(self.all_row_values, Unset):
            all_row_values = []
            for all_row_values_item_data in self.all_row_values:
                all_row_values_item = all_row_values_item_data

                all_row_values.append(all_row_values_item)

        bt_type = self.bt_type

        column_count = self.column_count

        frozen_columns = self.frozen_columns

        is_failed = self.is_failed

        node_id = self.node_id

        read_only = self.read_only

        row_count = self.row_count

        sort_order: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.to_dict()

        status_message = self.status_message

        status_type: str | Unset = UNSET
        if not isinstance(self.status_type, Unset):
            status_type = self.status_type.value

        table_columns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.table_columns, Unset):
            table_columns = []
            for table_columns_item_data in self.table_columns:
                table_columns_item = table_columns_item_data.to_dict()
                table_columns.append(table_columns_item)

        table_id = self.table_id

        table_rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.table_rows, Unset):
            table_rows = []
            for table_rows_item_data in self.table_rows:
                table_rows_item = table_rows_item_data.to_dict()
                table_rows.append(table_rows_item)

        title = self.title

        part_deterministic_id = self.part_deterministic_id

        part_deterministic_ids: list[str] | Unset = UNSET
        if not isinstance(self.part_deterministic_ids, Unset):
            part_deterministic_ids = self.part_deterministic_ids

        property_node_id = self.property_node_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_row_values is not UNSET:
            field_dict["allRowValues"] = all_row_values
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if column_count is not UNSET:
            field_dict["columnCount"] = column_count
        if frozen_columns is not UNSET:
            field_dict["frozenColumns"] = frozen_columns
        if is_failed is not UNSET:
            field_dict["isFailed"] = is_failed
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if row_count is not UNSET:
            field_dict["rowCount"] = row_count
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message
        if status_type is not UNSET:
            field_dict["statusType"] = status_type
        if table_columns is not UNSET:
            field_dict["tableColumns"] = table_columns
        if table_id is not UNSET:
            field_dict["tableId"] = table_id
        if table_rows is not UNSET:
            field_dict["tableRows"] = table_rows
        if title is not UNSET:
            field_dict["title"] = title
        if part_deterministic_id is not UNSET:
            field_dict["partDeterministicId"] = part_deterministic_id
        if part_deterministic_ids is not UNSET:
            field_dict["partDeterministicIds"] = part_deterministic_ids
        if property_node_id is not UNSET:
            field_dict["propertyNodeId"] = property_node_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_table_column_info_1222 import BTTableColumnInfo1222
        from ..models.bt_table_row_1054 import BTTableRow1054
        from ..models.bt_table_sort_order_4371 import BTTableSortOrder4371

        d = dict(src_dict)
        _all_row_values = d.pop("allRowValues", UNSET)
        all_row_values: list[list[str]] | Unset = UNSET
        if _all_row_values is not UNSET:
            all_row_values = []
            for all_row_values_item_data in _all_row_values:
                all_row_values_item = cast(list[str], all_row_values_item_data)

                all_row_values.append(all_row_values_item)

        bt_type = d.pop("btType", UNSET)

        column_count = d.pop("columnCount", UNSET)

        frozen_columns = d.pop("frozenColumns", UNSET)

        is_failed = d.pop("isFailed", UNSET)

        node_id = d.pop("nodeId", UNSET)

        read_only = d.pop("readOnly", UNSET)

        row_count = d.pop("rowCount", UNSET)

        _sort_order = d.pop("sortOrder", UNSET)
        sort_order: BTTableSortOrder4371 | Unset
        if isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = BTTableSortOrder4371.from_dict(_sort_order)

        status_message = d.pop("statusMessage", UNSET)

        _status_type = d.pop("statusType", UNSET)
        status_type: GBTNodeStatusType | Unset
        if isinstance(_status_type, Unset):
            status_type = UNSET
        else:
            status_type = GBTNodeStatusType(_status_type)

        _table_columns = d.pop("tableColumns", UNSET)
        table_columns: list[BTTableColumnInfo1222] | Unset = UNSET
        if _table_columns is not UNSET:
            table_columns = []
            for table_columns_item_data in _table_columns:
                table_columns_item = BTTableColumnInfo1222.from_dict(table_columns_item_data)

                table_columns.append(table_columns_item)

        table_id = d.pop("tableId", UNSET)

        _table_rows = d.pop("tableRows", UNSET)
        table_rows: list[BTTableRow1054] | Unset = UNSET
        if _table_rows is not UNSET:
            table_rows = []
            for table_rows_item_data in _table_rows:
                table_rows_item = BTTableRow1054.from_dict(table_rows_item_data)

                table_rows.append(table_rows_item)

        title = d.pop("title", UNSET)

        part_deterministic_id = d.pop("partDeterministicId", UNSET)

        part_deterministic_ids = cast(list[str], d.pop("partDeterministicIds", UNSET))

        property_node_id = d.pop("propertyNodeId", UNSET)

        bt_configured_part_properties_table_2740 = cls(
            all_row_values=all_row_values,
            bt_type=bt_type,
            column_count=column_count,
            frozen_columns=frozen_columns,
            is_failed=is_failed,
            node_id=node_id,
            read_only=read_only,
            row_count=row_count,
            sort_order=sort_order,
            status_message=status_message,
            status_type=status_type,
            table_columns=table_columns,
            table_id=table_id,
            table_rows=table_rows,
            title=title,
            part_deterministic_id=part_deterministic_id,
            part_deterministic_ids=part_deterministic_ids,
            property_node_id=property_node_id,
        )

        bt_configured_part_properties_table_2740.additional_properties = d
        return bt_configured_part_properties_table_2740

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
