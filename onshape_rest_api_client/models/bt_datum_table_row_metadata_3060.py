from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_table_base_cross_highlight_data_2609 import BTTableBaseCrossHighlightData2609
    from ..models.bt_table_cross_highlight_data_1753 import BTTableCrossHighlightData1753


T = TypeVar("T", bound="BTDatumTableRowMetadata3060")


@_attrs_define
class BTDatumTableRowMetadata3060:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        cross_highlight_data_if_any (BTTableBaseCrossHighlightData2609 | Unset):
        annotation_id (str | Unset):
        cross_highlight_data (BTTableCrossHighlightData1753 | Unset):
        is_derived (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    cross_highlight_data_if_any: BTTableBaseCrossHighlightData2609 | Unset = UNSET
    annotation_id: str | Unset = UNSET
    cross_highlight_data: BTTableCrossHighlightData1753 | Unset = UNSET
    is_derived: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        cross_highlight_data_if_any: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cross_highlight_data_if_any, Unset):
            cross_highlight_data_if_any = self.cross_highlight_data_if_any.to_dict()

        annotation_id = self.annotation_id

        cross_highlight_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cross_highlight_data, Unset):
            cross_highlight_data = self.cross_highlight_data.to_dict()

        is_derived = self.is_derived

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if cross_highlight_data_if_any is not UNSET:
            field_dict["crossHighlightDataIfAny"] = cross_highlight_data_if_any
        if annotation_id is not UNSET:
            field_dict["annotationId"] = annotation_id
        if cross_highlight_data is not UNSET:
            field_dict["crossHighlightData"] = cross_highlight_data
        if is_derived is not UNSET:
            field_dict["isDerived"] = is_derived

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_table_base_cross_highlight_data_2609 import BTTableBaseCrossHighlightData2609
        from ..models.bt_table_cross_highlight_data_1753 import BTTableCrossHighlightData1753

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _cross_highlight_data_if_any = d.pop("crossHighlightDataIfAny", UNSET)
        cross_highlight_data_if_any: BTTableBaseCrossHighlightData2609 | Unset
        if isinstance(_cross_highlight_data_if_any, Unset):
            cross_highlight_data_if_any = UNSET
        else:
            cross_highlight_data_if_any = BTTableBaseCrossHighlightData2609.from_dict(_cross_highlight_data_if_any)

        annotation_id = d.pop("annotationId", UNSET)

        _cross_highlight_data = d.pop("crossHighlightData", UNSET)
        cross_highlight_data: BTTableCrossHighlightData1753 | Unset
        if isinstance(_cross_highlight_data, Unset):
            cross_highlight_data = UNSET
        else:
            cross_highlight_data = BTTableCrossHighlightData1753.from_dict(_cross_highlight_data)

        is_derived = d.pop("isDerived", UNSET)

        bt_datum_table_row_metadata_3060 = cls(
            bt_type=bt_type,
            cross_highlight_data_if_any=cross_highlight_data_if_any,
            annotation_id=annotation_id,
            cross_highlight_data=cross_highlight_data,
            is_derived=is_derived,
        )

        bt_datum_table_row_metadata_3060.additional_properties = d
        return bt_datum_table_row_metadata_3060

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
