from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_table_1825 import BTTable1825


T = TypeVar("T", bound="BTTableResponse1546")


@_attrs_define
class BTTableResponse1546:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        source_microversion (str | Unset):
        table (BTTable1825 | Unset):
    """

    bt_type: str | Unset = UNSET
    source_microversion: str | Unset = UNSET
    table: BTTable1825 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        source_microversion = self.source_microversion

        table: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table, Unset):
            table = self.table.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if source_microversion is not UNSET:
            field_dict["sourceMicroversion"] = source_microversion
        if table is not UNSET:
            field_dict["table"] = table

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_table_1825 import BTTable1825

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        source_microversion = d.pop("sourceMicroversion", UNSET)

        _table = d.pop("table", UNSET)
        table: BTTable1825 | Unset
        if isinstance(_table, Unset):
            table = UNSET
        else:
            table = BTTable1825.from_dict(_table)

        bt_table_response_1546 = cls(
            bt_type=bt_type,
            source_microversion=source_microversion,
            table=table,
        )

        bt_table_response_1546.additional_properties = d
        return bt_table_response_1546

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
