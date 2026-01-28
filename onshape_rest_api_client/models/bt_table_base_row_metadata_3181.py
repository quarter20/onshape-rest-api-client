from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_table_base_cross_highlight_data_2609 import BTTableBaseCrossHighlightData2609


T = TypeVar("T", bound="BTTableBaseRowMetadata3181")


@_attrs_define
class BTTableBaseRowMetadata3181:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        cross_highlight_data_if_any (BTTableBaseCrossHighlightData2609 | Unset):
    """

    bt_type: str | Unset = UNSET
    cross_highlight_data_if_any: BTTableBaseCrossHighlightData2609 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        cross_highlight_data_if_any: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cross_highlight_data_if_any, Unset):
            cross_highlight_data_if_any = self.cross_highlight_data_if_any.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if cross_highlight_data_if_any is not UNSET:
            field_dict["crossHighlightDataIfAny"] = cross_highlight_data_if_any

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_table_base_cross_highlight_data_2609 import BTTableBaseCrossHighlightData2609

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _cross_highlight_data_if_any = d.pop("crossHighlightDataIfAny", UNSET)
        cross_highlight_data_if_any: BTTableBaseCrossHighlightData2609 | Unset
        if isinstance(_cross_highlight_data_if_any, Unset):
            cross_highlight_data_if_any = UNSET
        else:
            cross_highlight_data_if_any = BTTableBaseCrossHighlightData2609.from_dict(_cross_highlight_data_if_any)

        bt_table_base_row_metadata_3181 = cls(
            bt_type=bt_type,
            cross_highlight_data_if_any=cross_highlight_data_if_any,
        )

        bt_table_base_row_metadata_3181.additional_properties = d
        return bt_table_base_row_metadata_3181

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
