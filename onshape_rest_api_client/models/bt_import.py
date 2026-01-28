from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTImport")


@_attrs_define
class BTImport:
    """
    Attributes:
        for_export (bool | Unset):
        import_microversion (str | Unset): Element microversion that is being imported.
    """

    for_export: bool | Unset = UNSET
    import_microversion: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        for_export = self.for_export

        import_microversion = self.import_microversion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if for_export is not UNSET:
            field_dict["forExport"] = for_export
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        for_export = d.pop("forExport", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        bt_import = cls(
            for_export=for_export,
            import_microversion=import_microversion,
        )

        bt_import.additional_properties = d
        return bt_import

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
