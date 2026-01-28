from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_table_base_cross_highlight_data_2609 import BTTableBaseCrossHighlightData2609


T = TypeVar("T", bound="BTVariableTableRowMetadata3912")


@_attrs_define
class BTVariableTableRowMetadata3912:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        cross_highlight_data_if_any (BTTableBaseCrossHighlightData2609 | Unset):
        cross_highlight_data (BTTableBaseCrossHighlightData2609 | Unset):
        info (str | Unset):
        is_fully_editable (bool | Unset):
        is_recursive_import (bool | Unset):
        last_writing_feature_node_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    cross_highlight_data_if_any: BTTableBaseCrossHighlightData2609 | Unset = UNSET
    cross_highlight_data: BTTableBaseCrossHighlightData2609 | Unset = UNSET
    info: str | Unset = UNSET
    is_fully_editable: bool | Unset = UNSET
    is_recursive_import: bool | Unset = UNSET
    last_writing_feature_node_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        cross_highlight_data_if_any: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cross_highlight_data_if_any, Unset):
            cross_highlight_data_if_any = self.cross_highlight_data_if_any.to_dict()

        cross_highlight_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cross_highlight_data, Unset):
            cross_highlight_data = self.cross_highlight_data.to_dict()

        info = self.info

        is_fully_editable = self.is_fully_editable

        is_recursive_import = self.is_recursive_import

        last_writing_feature_node_id = self.last_writing_feature_node_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if cross_highlight_data_if_any is not UNSET:
            field_dict["crossHighlightDataIfAny"] = cross_highlight_data_if_any
        if cross_highlight_data is not UNSET:
            field_dict["crossHighlightData"] = cross_highlight_data
        if info is not UNSET:
            field_dict["info"] = info
        if is_fully_editable is not UNSET:
            field_dict["isFullyEditable"] = is_fully_editable
        if is_recursive_import is not UNSET:
            field_dict["isRecursiveImport"] = is_recursive_import
        if last_writing_feature_node_id is not UNSET:
            field_dict["lastWritingFeatureNodeId"] = last_writing_feature_node_id

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

        _cross_highlight_data = d.pop("crossHighlightData", UNSET)
        cross_highlight_data: BTTableBaseCrossHighlightData2609 | Unset
        if isinstance(_cross_highlight_data, Unset):
            cross_highlight_data = UNSET
        else:
            cross_highlight_data = BTTableBaseCrossHighlightData2609.from_dict(_cross_highlight_data)

        info = d.pop("info", UNSET)

        is_fully_editable = d.pop("isFullyEditable", UNSET)

        is_recursive_import = d.pop("isRecursiveImport", UNSET)

        last_writing_feature_node_id = d.pop("lastWritingFeatureNodeId", UNSET)

        bt_variable_table_row_metadata_3912 = cls(
            bt_type=bt_type,
            cross_highlight_data_if_any=cross_highlight_data_if_any,
            cross_highlight_data=cross_highlight_data,
            info=info,
            is_fully_editable=is_fully_editable,
            is_recursive_import=is_recursive_import,
            last_writing_feature_node_id=last_writing_feature_node_id,
        )

        bt_variable_table_row_metadata_3912.additional_properties = d
        return bt_variable_table_row_metadata_3912

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
