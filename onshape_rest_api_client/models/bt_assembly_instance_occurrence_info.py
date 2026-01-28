from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_assembly_occurrence_info import BTAssemblyOccurrenceInfo


T = TypeVar("T", bound="BTAssemblyInstanceOccurrenceInfo")


@_attrs_define
class BTAssemblyInstanceOccurrenceInfo:
    """
    Attributes:
        occurrences (list[BTAssemblyOccurrenceInfo] | Unset):
    """

    occurrences: list[BTAssemblyOccurrenceInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        occurrences: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.occurrences, Unset):
            occurrences = []
            for occurrences_item_data in self.occurrences:
                occurrences_item = occurrences_item_data.to_dict()
                occurrences.append(occurrences_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if occurrences is not UNSET:
            field_dict["occurrences"] = occurrences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_assembly_occurrence_info import BTAssemblyOccurrenceInfo

        d = dict(src_dict)
        _occurrences = d.pop("occurrences", UNSET)
        occurrences: list[BTAssemblyOccurrenceInfo] | Unset = UNSET
        if _occurrences is not UNSET:
            occurrences = []
            for occurrences_item_data in _occurrences:
                occurrences_item = BTAssemblyOccurrenceInfo.from_dict(occurrences_item_data)

                occurrences.append(occurrences_item)

        bt_assembly_instance_occurrence_info = cls(
            occurrences=occurrences,
        )

        bt_assembly_instance_occurrence_info.additional_properties = d
        return bt_assembly_instance_occurrence_info

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
