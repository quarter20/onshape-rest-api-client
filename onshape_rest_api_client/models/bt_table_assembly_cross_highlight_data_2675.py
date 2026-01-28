from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_table_assembly_cross_highlight_data_item_2659 import BTTableAssemblyCrossHighlightDataItem2659


T = TypeVar("T", bound="BTTableAssemblyCrossHighlightData2675")


@_attrs_define
class BTTableAssemblyCrossHighlightData2675:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        assembly_cross_highlight_items (list[BTTableAssemblyCrossHighlightDataItem2659] | Unset):
    """

    bt_type: str | Unset = UNSET
    assembly_cross_highlight_items: list[BTTableAssemblyCrossHighlightDataItem2659] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        assembly_cross_highlight_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assembly_cross_highlight_items, Unset):
            assembly_cross_highlight_items = []
            for assembly_cross_highlight_items_item_data in self.assembly_cross_highlight_items:
                assembly_cross_highlight_items_item = assembly_cross_highlight_items_item_data.to_dict()
                assembly_cross_highlight_items.append(assembly_cross_highlight_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if assembly_cross_highlight_items is not UNSET:
            field_dict["assemblyCrossHighlightItems"] = assembly_cross_highlight_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_table_assembly_cross_highlight_data_item_2659 import BTTableAssemblyCrossHighlightDataItem2659

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _assembly_cross_highlight_items = d.pop("assemblyCrossHighlightItems", UNSET)
        assembly_cross_highlight_items: list[BTTableAssemblyCrossHighlightDataItem2659] | Unset = UNSET
        if _assembly_cross_highlight_items is not UNSET:
            assembly_cross_highlight_items = []
            for assembly_cross_highlight_items_item_data in _assembly_cross_highlight_items:
                assembly_cross_highlight_items_item = BTTableAssemblyCrossHighlightDataItem2659.from_dict(
                    assembly_cross_highlight_items_item_data
                )

                assembly_cross_highlight_items.append(assembly_cross_highlight_items_item)

        bt_table_assembly_cross_highlight_data_2675 = cls(
            bt_type=bt_type,
            assembly_cross_highlight_items=assembly_cross_highlight_items,
        )

        bt_table_assembly_cross_highlight_data_2675.additional_properties = d
        return bt_table_assembly_cross_highlight_data_2675

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
