from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_api_table_row_2915_column_id_to_value import BTApiTableRow2915ColumnIdToValue


T = TypeVar("T", bound="BTApiTableRow2915")


@_attrs_define
class BTApiTableRow2915:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        callout (str | Unset):
        column_id_to_value (BTApiTableRow2915ColumnIdToValue | Unset):
        entity_ids (list[str] | Unset):
    """

    bt_type: str | Unset = UNSET
    callout: str | Unset = UNSET
    column_id_to_value: BTApiTableRow2915ColumnIdToValue | Unset = UNSET
    entity_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        callout = self.callout

        column_id_to_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.column_id_to_value, Unset):
            column_id_to_value = self.column_id_to_value.to_dict()

        entity_ids: list[str] | Unset = UNSET
        if not isinstance(self.entity_ids, Unset):
            entity_ids = self.entity_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if callout is not UNSET:
            field_dict["callout"] = callout
        if column_id_to_value is not UNSET:
            field_dict["columnIdToValue"] = column_id_to_value
        if entity_ids is not UNSET:
            field_dict["entityIds"] = entity_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_api_table_row_2915_column_id_to_value import BTApiTableRow2915ColumnIdToValue

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        callout = d.pop("callout", UNSET)

        _column_id_to_value = d.pop("columnIdToValue", UNSET)
        column_id_to_value: BTApiTableRow2915ColumnIdToValue | Unset
        if isinstance(_column_id_to_value, Unset):
            column_id_to_value = UNSET
        else:
            column_id_to_value = BTApiTableRow2915ColumnIdToValue.from_dict(_column_id_to_value)

        entity_ids = cast(list[str], d.pop("entityIds", UNSET))

        bt_api_table_row_2915 = cls(
            bt_type=bt_type,
            callout=callout,
            column_id_to_value=column_id_to_value,
            entity_ids=entity_ids,
        )

        bt_api_table_row_2915.additional_properties = d
        return bt_api_table_row_2915

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
