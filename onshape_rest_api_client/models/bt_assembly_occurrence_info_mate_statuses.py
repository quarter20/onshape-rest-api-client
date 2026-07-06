from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_node_status_type import GBTNodeStatusType

T = TypeVar("T", bound="BTAssemblyOccurrenceInfoMateStatuses")


@_attrs_define
class BTAssemblyOccurrenceInfoMateStatuses:
    """ """

    additional_properties: dict[str, GBTNodeStatusType] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_assembly_occurrence_info_mate_statuses = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = GBTNodeStatusType(prop_dict)

            additional_properties[prop_name] = additional_property

        bt_assembly_occurrence_info_mate_statuses.additional_properties = additional_properties
        return bt_assembly_occurrence_info_mate_statuses

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> GBTNodeStatusType:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: GBTNodeStatusType) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
