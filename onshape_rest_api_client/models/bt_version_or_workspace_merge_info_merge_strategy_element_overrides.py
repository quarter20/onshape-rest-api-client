from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_merge_strategy import BTMergeStrategy

T = TypeVar("T", bound="BTVersionOrWorkspaceMergeInfoMergeStrategyElementOverrides")


@_attrs_define
class BTVersionOrWorkspaceMergeInfoMergeStrategyElementOverrides:
    """ """

    additional_properties: dict[str, BTMergeStrategy] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_version_or_workspace_merge_info_merge_strategy_element_overrides = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = BTMergeStrategy(prop_dict)

            additional_properties[prop_name] = additional_property

        bt_version_or_workspace_merge_info_merge_strategy_element_overrides.additional_properties = (
            additional_properties
        )
        return bt_version_or_workspace_merge_info_merge_strategy_element_overrides

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> BTMergeStrategy:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: BTMergeStrategy) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
