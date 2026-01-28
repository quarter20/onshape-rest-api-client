from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAssemblyOccurrenceInfo")


@_attrs_define
class BTAssemblyOccurrenceInfo:
    """
    Attributes:
        fixed (bool | Unset):
        hidden (bool | Unset):
        path (list[str] | Unset):
        transform (list[float] | Unset):
    """

    fixed: bool | Unset = UNSET
    hidden: bool | Unset = UNSET
    path: list[str] | Unset = UNSET
    transform: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fixed = self.fixed

        hidden = self.hidden

        path: list[str] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = self.path

        transform: list[float] | Unset = UNSET
        if not isinstance(self.transform, Unset):
            transform = self.transform

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fixed is not UNSET:
            field_dict["fixed"] = fixed
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if path is not UNSET:
            field_dict["path"] = path
        if transform is not UNSET:
            field_dict["transform"] = transform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fixed = d.pop("fixed", UNSET)

        hidden = d.pop("hidden", UNSET)

        path = cast(list[str], d.pop("path", UNSET))

        transform = cast(list[float], d.pop("transform", UNSET))

        bt_assembly_occurrence_info = cls(
            fixed=fixed,
            hidden=hidden,
            path=path,
            transform=transform,
        )

        bt_assembly_occurrence_info.additional_properties = d
        return bt_assembly_occurrence_info

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
