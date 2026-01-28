from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbtbs_feature_visibility import GBTBSFeatureVisibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_mate_occurrence_data_1671_value_map import BTMateOccurrenceData1671ValueMap


T = TypeVar("T", bound="BTMateOccurrenceData1671")


@_attrs_define
class BTMateOccurrenceData1671:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        visibility (GBTBSFeatureVisibility | Unset):
        value_map (BTMateOccurrenceData1671ValueMap | Unset):
        values (list[float] | Unset):
    """

    bt_type: str | Unset = UNSET
    visibility: GBTBSFeatureVisibility | Unset = UNSET
    value_map: BTMateOccurrenceData1671ValueMap | Unset = UNSET
    values: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        value_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value_map, Unset):
            value_map = self.value_map.to_dict()

        values: list[float] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if visibility is not UNSET:
            field_dict["visibility"] = visibility
        if value_map is not UNSET:
            field_dict["valueMap"] = value_map
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_mate_occurrence_data_1671_value_map import BTMateOccurrenceData1671ValueMap

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: GBTBSFeatureVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = GBTBSFeatureVisibility(_visibility)

        _value_map = d.pop("valueMap", UNSET)
        value_map: BTMateOccurrenceData1671ValueMap | Unset
        if isinstance(_value_map, Unset):
            value_map = UNSET
        else:
            value_map = BTMateOccurrenceData1671ValueMap.from_dict(_value_map)

        values = cast(list[float], d.pop("values", UNSET))

        bt_mate_occurrence_data_1671 = cls(
            bt_type=bt_type,
            visibility=visibility,
            value_map=value_map,
            values=values,
        )

        bt_mate_occurrence_data_1671.additional_properties = d
        return bt_mate_occurrence_data_1671

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
