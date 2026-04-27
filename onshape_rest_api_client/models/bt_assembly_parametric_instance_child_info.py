from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAssemblyParametricInstanceChildInfo")


@_attrs_define
class BTAssemblyParametricInstanceChildInfo:
    """Children instance description of parametric instance.

    Attributes:
        instance_ids (list[str] | Unset): Children instance ids.
        seed_occurrence (str | Unset): Seed occurrence id. Unspecified if there is no seed.
    """

    instance_ids: list[str] | Unset = UNSET
    seed_occurrence: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        instance_ids: list[str] | Unset = UNSET
        if not isinstance(self.instance_ids, Unset):
            instance_ids = self.instance_ids

        seed_occurrence = self.seed_occurrence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_ids is not UNSET:
            field_dict["instanceIds"] = instance_ids
        if seed_occurrence is not UNSET:
            field_dict["seedOccurrence"] = seed_occurrence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        instance_ids = cast(list[str], d.pop("instanceIds", UNSET))

        seed_occurrence = d.pop("seedOccurrence", UNSET)

        bt_assembly_parametric_instance_child_info = cls(
            instance_ids=instance_ids,
            seed_occurrence=seed_occurrence,
        )

        bt_assembly_parametric_instance_child_info.additional_properties = d
        return bt_assembly_parametric_instance_child_info

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
