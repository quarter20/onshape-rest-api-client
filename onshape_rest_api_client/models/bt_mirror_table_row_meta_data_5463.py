from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_occurrence_74 import BTOccurrence74
    from ..models.bt_table_assembly_cross_highlight_data_2675 import BTTableAssemblyCrossHighlightData2675
    from ..models.bt_table_base_cross_highlight_data_2609 import BTTableBaseCrossHighlightData2609


T = TypeVar("T", bound="BTMirrorTableRowMetaData5463")


@_attrs_define
class BTMirrorTableRowMetaData5463:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        cross_highlight_data_if_any (BTTableBaseCrossHighlightData2609 | Unset):
        cross_highlight_data (BTTableAssemblyCrossHighlightData2675 | Unset):
        occurrences (list[BTOccurrence74] | Unset):
    """

    bt_type: str | Unset = UNSET
    cross_highlight_data_if_any: BTTableBaseCrossHighlightData2609 | Unset = UNSET
    cross_highlight_data: BTTableAssemblyCrossHighlightData2675 | Unset = UNSET
    occurrences: list[BTOccurrence74] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        cross_highlight_data_if_any: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cross_highlight_data_if_any, Unset):
            cross_highlight_data_if_any = self.cross_highlight_data_if_any.to_dict()

        cross_highlight_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cross_highlight_data, Unset):
            cross_highlight_data = self.cross_highlight_data.to_dict()

        occurrences: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.occurrences, Unset):
            occurrences = []
            for occurrences_item_data in self.occurrences:
                occurrences_item = occurrences_item_data.to_dict()
                occurrences.append(occurrences_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if cross_highlight_data_if_any is not UNSET:
            field_dict["crossHighlightDataIfAny"] = cross_highlight_data_if_any
        if cross_highlight_data is not UNSET:
            field_dict["crossHighlightData"] = cross_highlight_data
        if occurrences is not UNSET:
            field_dict["occurrences"] = occurrences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_occurrence_74 import BTOccurrence74
        from ..models.bt_table_assembly_cross_highlight_data_2675 import BTTableAssemblyCrossHighlightData2675
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
        cross_highlight_data: BTTableAssemblyCrossHighlightData2675 | Unset
        if isinstance(_cross_highlight_data, Unset):
            cross_highlight_data = UNSET
        else:
            cross_highlight_data = BTTableAssemblyCrossHighlightData2675.from_dict(_cross_highlight_data)

        _occurrences = d.pop("occurrences", UNSET)
        occurrences: list[BTOccurrence74] | Unset = UNSET
        if _occurrences is not UNSET:
            occurrences = []
            for occurrences_item_data in _occurrences:
                occurrences_item = BTOccurrence74.from_dict(occurrences_item_data)

                occurrences.append(occurrences_item)

        bt_mirror_table_row_meta_data_5463 = cls(
            bt_type=bt_type,
            cross_highlight_data_if_any=cross_highlight_data_if_any,
            cross_highlight_data=cross_highlight_data,
            occurrences=occurrences,
        )

        bt_mirror_table_row_meta_data_5463.additional_properties = d
        return bt_mirror_table_row_meta_data_5463

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
