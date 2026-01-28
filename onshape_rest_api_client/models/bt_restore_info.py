from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_restore_strategy import BTRestoreStrategy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_restore_info_element_id_to_strategy_override import BTRestoreInfoElementIdToStrategyOverride


T = TypeVar("T", bound="BTRestoreInfo")


@_attrs_define
class BTRestoreInfo:
    """
    Attributes:
        default_restore_strategy (BTRestoreStrategy | Unset):
        element_id_to_strategy_override (BTRestoreInfoElementIdToStrategyOverride | Unset):
    """

    default_restore_strategy: BTRestoreStrategy | Unset = UNSET
    element_id_to_strategy_override: BTRestoreInfoElementIdToStrategyOverride | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_restore_strategy: str | Unset = UNSET
        if not isinstance(self.default_restore_strategy, Unset):
            default_restore_strategy = self.default_restore_strategy.value

        element_id_to_strategy_override: dict[str, Any] | Unset = UNSET
        if not isinstance(self.element_id_to_strategy_override, Unset):
            element_id_to_strategy_override = self.element_id_to_strategy_override.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_restore_strategy is not UNSET:
            field_dict["defaultRestoreStrategy"] = default_restore_strategy
        if element_id_to_strategy_override is not UNSET:
            field_dict["elementIdToStrategyOverride"] = element_id_to_strategy_override

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_restore_info_element_id_to_strategy_override import BTRestoreInfoElementIdToStrategyOverride

        d = dict(src_dict)
        _default_restore_strategy = d.pop("defaultRestoreStrategy", UNSET)
        default_restore_strategy: BTRestoreStrategy | Unset
        if isinstance(_default_restore_strategy, Unset):
            default_restore_strategy = UNSET
        else:
            default_restore_strategy = BTRestoreStrategy(_default_restore_strategy)

        _element_id_to_strategy_override = d.pop("elementIdToStrategyOverride", UNSET)
        element_id_to_strategy_override: BTRestoreInfoElementIdToStrategyOverride | Unset
        if isinstance(_element_id_to_strategy_override, Unset):
            element_id_to_strategy_override = UNSET
        else:
            element_id_to_strategy_override = BTRestoreInfoElementIdToStrategyOverride.from_dict(
                _element_id_to_strategy_override
            )

        bt_restore_info = cls(
            default_restore_strategy=default_restore_strategy,
            element_id_to_strategy_override=element_id_to_strategy_override,
        )

        bt_restore_info.additional_properties = d
        return bt_restore_info

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
