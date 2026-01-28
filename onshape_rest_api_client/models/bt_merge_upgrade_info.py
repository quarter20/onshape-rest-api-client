from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_merge_upgrade_type import BTMergeUpgradeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_pending_upgrade_info import BTPendingUpgradeInfo


T = TypeVar("T", bound="BTMergeUpgradeInfo")


@_attrs_define
class BTMergeUpgradeInfo:
    """
    Attributes:
        pending_source_upgrade (BTPendingUpgradeInfo | Unset):
        pending_target_upgrade (BTPendingUpgradeInfo | Unset):
        recommended_version (int | Unset):
        type_ (BTMergeUpgradeType | Unset):
    """

    pending_source_upgrade: BTPendingUpgradeInfo | Unset = UNSET
    pending_target_upgrade: BTPendingUpgradeInfo | Unset = UNSET
    recommended_version: int | Unset = UNSET
    type_: BTMergeUpgradeType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pending_source_upgrade: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pending_source_upgrade, Unset):
            pending_source_upgrade = self.pending_source_upgrade.to_dict()

        pending_target_upgrade: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pending_target_upgrade, Unset):
            pending_target_upgrade = self.pending_target_upgrade.to_dict()

        recommended_version = self.recommended_version

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pending_source_upgrade is not UNSET:
            field_dict["pendingSourceUpgrade"] = pending_source_upgrade
        if pending_target_upgrade is not UNSET:
            field_dict["pendingTargetUpgrade"] = pending_target_upgrade
        if recommended_version is not UNSET:
            field_dict["recommendedVersion"] = recommended_version
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_pending_upgrade_info import BTPendingUpgradeInfo

        d = dict(src_dict)
        _pending_source_upgrade = d.pop("pendingSourceUpgrade", UNSET)
        pending_source_upgrade: BTPendingUpgradeInfo | Unset
        if isinstance(_pending_source_upgrade, Unset):
            pending_source_upgrade = UNSET
        else:
            pending_source_upgrade = BTPendingUpgradeInfo.from_dict(_pending_source_upgrade)

        _pending_target_upgrade = d.pop("pendingTargetUpgrade", UNSET)
        pending_target_upgrade: BTPendingUpgradeInfo | Unset
        if isinstance(_pending_target_upgrade, Unset):
            pending_target_upgrade = UNSET
        else:
            pending_target_upgrade = BTPendingUpgradeInfo.from_dict(_pending_target_upgrade)

        recommended_version = d.pop("recommendedVersion", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: BTMergeUpgradeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BTMergeUpgradeType(_type_)

        bt_merge_upgrade_info = cls(
            pending_source_upgrade=pending_source_upgrade,
            pending_target_upgrade=pending_target_upgrade,
            recommended_version=recommended_version,
            type_=type_,
        )

        bt_merge_upgrade_info.additional_properties = d
        return bt_merge_upgrade_info

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
