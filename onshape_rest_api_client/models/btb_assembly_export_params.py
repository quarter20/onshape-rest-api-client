from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTBAssemblyExportParams")


@_attrs_define
class BTBAssemblyExportParams:
    """Options for exporting assemblies.

    Attributes:
        occurrences_to_export (str | Unset): IDs of the occurrences to retrieve. Use comma-separated IDs for multiple
            instances (example: occurrencesToExport=JHK,JHD).
    """

    occurrences_to_export: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        occurrences_to_export = self.occurrences_to_export

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if occurrences_to_export is not UNSET:
            field_dict["occurrencesToExport"] = occurrences_to_export

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        occurrences_to_export = d.pop("occurrencesToExport", UNSET)

        btb_assembly_export_params = cls(
            occurrences_to_export=occurrences_to_export,
        )

        btb_assembly_export_params.additional_properties = d
        return btb_assembly_export_params

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
