from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_table_cell_modifier_4883 import BTTableCellModifier4883


T = TypeVar("T", bound="BTTableTestCellString2112")


@_attrs_define
class BTTableTestCellString2112:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        is_ever_visible (bool | Unset):
        is_read_only (bool | Unset):
        modifiers (list[BTTableCellModifier4883] | Unset):
        cell_value (str | Unset):
    """

    bt_type: str | Unset = UNSET
    is_ever_visible: bool | Unset = UNSET
    is_read_only: bool | Unset = UNSET
    modifiers: list[BTTableCellModifier4883] | Unset = UNSET
    cell_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        is_ever_visible = self.is_ever_visible

        is_read_only = self.is_read_only

        modifiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.modifiers, Unset):
            modifiers = []
            for modifiers_item_data in self.modifiers:
                modifiers_item = modifiers_item_data.to_dict()
                modifiers.append(modifiers_item)

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
        if modifiers is not UNSET:
            field_dict["modifiers"] = modifiers
        if cell_value is not UNSET:
            field_dict["cellValue"] = cell_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_table_cell_modifier_4883 import BTTableCellModifier4883

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        is_ever_visible = d.pop("isEverVisible", UNSET)

        is_read_only = d.pop("isReadOnly", UNSET)

        _modifiers = d.pop("modifiers", UNSET)
        modifiers: list[BTTableCellModifier4883] | Unset = UNSET
        if _modifiers is not UNSET:
            modifiers = []
            for modifiers_item_data in _modifiers:
                modifiers_item = BTTableCellModifier4883.from_dict(modifiers_item_data)

                modifiers.append(modifiers_item)

        cell_value = d.pop("cellValue", UNSET)

        bt_table_test_cell_string_2112 = cls(
            bt_type=bt_type,
            is_ever_visible=is_ever_visible,
            is_read_only=is_read_only,
            modifiers=modifiers,
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
