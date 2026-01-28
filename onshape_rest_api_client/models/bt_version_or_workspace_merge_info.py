from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_merge_strategy import BTMergeStrategy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_version_or_workspace_merge_info_merge_strategy_element_overrides import (
        BTVersionOrWorkspaceMergeInfoMergeStrategyElementOverrides,
    )


T = TypeVar("T", bound="BTVersionOrWorkspaceMergeInfo")


@_attrs_define
class BTVersionOrWorkspaceMergeInfo:
    """
    Attributes:
        default_merge_strategy (BTMergeStrategy | Unset):
        id (str | Unset):
        merge_strategy_element_overrides (BTVersionOrWorkspaceMergeInfoMergeStrategyElementOverrides | Unset):
        type_ (str | Unset):
    """

    default_merge_strategy: BTMergeStrategy | Unset = UNSET
    id: str | Unset = UNSET
    merge_strategy_element_overrides: BTVersionOrWorkspaceMergeInfoMergeStrategyElementOverrides | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_merge_strategy: str | Unset = UNSET
        if not isinstance(self.default_merge_strategy, Unset):
            default_merge_strategy = self.default_merge_strategy.value

        id = self.id

        merge_strategy_element_overrides: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merge_strategy_element_overrides, Unset):
            merge_strategy_element_overrides = self.merge_strategy_element_overrides.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_merge_strategy is not UNSET:
            field_dict["defaultMergeStrategy"] = default_merge_strategy
        if id is not UNSET:
            field_dict["id"] = id
        if merge_strategy_element_overrides is not UNSET:
            field_dict["mergeStrategyElementOverrides"] = merge_strategy_element_overrides
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_version_or_workspace_merge_info_merge_strategy_element_overrides import (
            BTVersionOrWorkspaceMergeInfoMergeStrategyElementOverrides,
        )

        d = dict(src_dict)
        _default_merge_strategy = d.pop("defaultMergeStrategy", UNSET)
        default_merge_strategy: BTMergeStrategy | Unset
        if isinstance(_default_merge_strategy, Unset):
            default_merge_strategy = UNSET
        else:
            default_merge_strategy = BTMergeStrategy(_default_merge_strategy)

        id = d.pop("id", UNSET)

        _merge_strategy_element_overrides = d.pop("mergeStrategyElementOverrides", UNSET)
        merge_strategy_element_overrides: BTVersionOrWorkspaceMergeInfoMergeStrategyElementOverrides | Unset
        if isinstance(_merge_strategy_element_overrides, Unset):
            merge_strategy_element_overrides = UNSET
        else:
            merge_strategy_element_overrides = BTVersionOrWorkspaceMergeInfoMergeStrategyElementOverrides.from_dict(
                _merge_strategy_element_overrides
            )

        type_ = d.pop("type", UNSET)

        bt_version_or_workspace_merge_info = cls(
            default_merge_strategy=default_merge_strategy,
            id=id,
            merge_strategy_element_overrides=merge_strategy_element_overrides,
            type_=type_,
        )

        bt_version_or_workspace_merge_info.additional_properties = d
        return bt_version_or_workspace_merge_info

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
