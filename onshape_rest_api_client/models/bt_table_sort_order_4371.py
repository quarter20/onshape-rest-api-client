from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTTableSortOrder4371")


@_attrs_define
class BTTableSortOrder4371:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        is_ascending (bool | Unset):
        node_id (str | Unset):
        sorting_column_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    is_ascending: bool | Unset = UNSET
    node_id: str | Unset = UNSET
    sorting_column_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        is_ascending = self.is_ascending

        node_id = self.node_id

        sorting_column_id = self.sorting_column_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if is_ascending is not UNSET:
            field_dict["isAscending"] = is_ascending
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if sorting_column_id is not UNSET:
            field_dict["sortingColumnId"] = sorting_column_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        is_ascending = d.pop("isAscending", UNSET)

        node_id = d.pop("nodeId", UNSET)

        sorting_column_id = d.pop("sortingColumnId", UNSET)

        bt_table_sort_order_4371 = cls(
            bt_type=bt_type,
            is_ascending=is_ascending,
            node_id=node_id,
            sorting_column_id=sorting_column_id,
        )

        bt_table_sort_order_4371.additional_properties = d
        return bt_table_sort_order_4371

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
