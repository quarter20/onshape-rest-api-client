from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTTableTestCellString2112")


@_attrs_define
class BTTableTestCellString2112:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        is_ever_visible (bool | Unset):
        is_read_only (bool | Unset):
        cell_value (str | Unset):
    """

    bt_type: str | Unset = UNSET
    is_ever_visible: bool | Unset = UNSET
    is_read_only: bool | Unset = UNSET
    cell_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        is_ever_visible = self.is_ever_visible

        is_read_only = self.is_read_only

        cell_value = self.cell_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if is_ever_visible is not UNSET:
            field_dict["isEverVisible"] = is_ever_visible
        if is_read_only is not UNSET:
            field_dict["isReadOnly"] = is_read_only
        if cell_value is not UNSET:
            field_dict["cellValue"] = cell_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        is_ever_visible = d.pop("isEverVisible", UNSET)

        is_read_only = d.pop("isReadOnly", UNSET)

        cell_value = d.pop("cellValue", UNSET)

        bt_table_test_cell_string_2112 = cls(
            bt_type=bt_type,
            is_ever_visible=is_ever_visible,
            is_read_only=is_read_only,
            cell_value=cell_value,
        )

        bt_table_test_cell_string_2112.additional_properties = d
        return bt_table_test_cell_string_2112

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
