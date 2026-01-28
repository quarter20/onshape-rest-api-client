from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_api_table_2300 import BTApiTable2300


T = TypeVar("T", bound="BTApiTableList1223")


@_attrs_define
class BTApiTableList1223:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        tables (list[BTApiTable2300] | Unset):
    """

    bt_type: str | Unset = UNSET
    tables: list[BTApiTable2300] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        tables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tables, Unset):
            tables = []
            for tables_item_data in self.tables:
                tables_item = tables_item_data.to_dict()
                tables.append(tables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if tables is not UNSET:
            field_dict["tables"] = tables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_api_table_2300 import BTApiTable2300

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _tables = d.pop("tables", UNSET)
        tables: list[BTApiTable2300] | Unset = UNSET
        if _tables is not UNSET:
            tables = []
            for tables_item_data in _tables:
                tables_item = BTApiTable2300.from_dict(tables_item_data)

                tables.append(tables_item)

        bt_api_table_list_1223 = cls(
            bt_type=bt_type,
            tables=tables,
        )

        bt_api_table_list_1223.additional_properties = d
        return bt_api_table_list_1223

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
