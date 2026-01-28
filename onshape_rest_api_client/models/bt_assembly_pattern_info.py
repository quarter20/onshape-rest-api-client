from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_pattern_type import GBTPatternType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_assembly_pattern_info_seed_to_pattern_instances import BTAssemblyPatternInfoSeedToPatternInstances


T = TypeVar("T", bound="BTAssemblyPatternInfo")


@_attrs_define
class BTAssemblyPatternInfo:
    """Pattern description.

    Attributes:
        id (str | Unset): Id of the pattern.
        name (str | Unset): Name of the pattern.
        seed_to_pattern_instances (BTAssemblyPatternInfoSeedToPatternInstances | Unset): Mapping of seed to pattern
            instance ids.
        suppressed (bool | Unset): If pattern is suppressed.
        type_ (GBTPatternType | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    seed_to_pattern_instances: BTAssemblyPatternInfoSeedToPatternInstances | Unset = UNSET
    suppressed: bool | Unset = UNSET
    type_: GBTPatternType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        seed_to_pattern_instances: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seed_to_pattern_instances, Unset):
            seed_to_pattern_instances = self.seed_to_pattern_instances.to_dict()

        suppressed = self.suppressed

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if seed_to_pattern_instances is not UNSET:
            field_dict["seedToPatternInstances"] = seed_to_pattern_instances
        if suppressed is not UNSET:
            field_dict["suppressed"] = suppressed
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_assembly_pattern_info_seed_to_pattern_instances import (
            BTAssemblyPatternInfoSeedToPatternInstances,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _seed_to_pattern_instances = d.pop("seedToPatternInstances", UNSET)
        seed_to_pattern_instances: BTAssemblyPatternInfoSeedToPatternInstances | Unset
        if isinstance(_seed_to_pattern_instances, Unset):
            seed_to_pattern_instances = UNSET
        else:
            seed_to_pattern_instances = BTAssemblyPatternInfoSeedToPatternInstances.from_dict(
                _seed_to_pattern_instances
            )

        suppressed = d.pop("suppressed", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: GBTPatternType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GBTPatternType(_type_)

        bt_assembly_pattern_info = cls(
            id=id,
            name=name,
            seed_to_pattern_instances=seed_to_pattern_instances,
            suppressed=suppressed,
            type_=type_,
        )

        bt_assembly_pattern_info.additional_properties = d
        return bt_assembly_pattern_info

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
