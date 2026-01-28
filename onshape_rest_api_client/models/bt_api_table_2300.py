from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_api_table_column_3141 import BTApiTableColumn3141
    from ..models.bt_api_table_row_2915 import BTApiTableRow2915


T = TypeVar("T", bound="BTApiTable2300")


@_attrs_define
class BTApiTable2300:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        columns (list[BTApiTableColumn3141] | Unset):
        entity_ids (list[str] | Unset):
        id (str | Unset):
        rows (list[BTApiTableRow2915] | Unset):
        title (str | Unset):
    """

    bt_type: str | Unset = UNSET
    columns: list[BTApiTableColumn3141] | Unset = UNSET
    entity_ids: list[str] | Unset = UNSET
    id: str | Unset = UNSET
    rows: list[BTApiTableRow2915] | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        columns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()
                columns.append(columns_item)

        entity_ids: list[str] | Unset = UNSET
        if not isinstance(self.entity_ids, Unset):
            entity_ids = self.entity_ids

        id = self.id

        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if columns is not UNSET:
            field_dict["columns"] = columns
        if entity_ids is not UNSET:
            field_dict["entityIds"] = entity_ids
        if id is not UNSET:
            field_dict["id"] = id
        if rows is not UNSET:
            field_dict["rows"] = rows
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_api_table_column_3141 import BTApiTableColumn3141
        from ..models.bt_api_table_row_2915 import BTApiTableRow2915

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _columns = d.pop("columns", UNSET)
        columns: list[BTApiTableColumn3141] | Unset = UNSET
        if _columns is not UNSET:
            columns = []
            for columns_item_data in _columns:
                columns_item = BTApiTableColumn3141.from_dict(columns_item_data)

                columns.append(columns_item)

        entity_ids = cast(list[str], d.pop("entityIds", UNSET))

        id = d.pop("id", UNSET)

        _rows = d.pop("rows", UNSET)
        rows: list[BTApiTableRow2915] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = BTApiTableRow2915.from_dict(rows_item_data)

                rows.append(rows_item)

        title = d.pop("title", UNSET)

        bt_api_table_2300 = cls(
            bt_type=bt_type,
            columns=columns,
            entity_ids=entity_ids,
            id=id,
            rows=rows,
            title=title,
        )

        bt_api_table_2300.additional_properties = d
        return bt_api_table_2300

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
