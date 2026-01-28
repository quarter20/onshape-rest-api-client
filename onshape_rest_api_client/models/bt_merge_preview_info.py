from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_element_merge_info import BTElementMergeInfo
    from ..models.bt_merge_upgrade_info import BTMergeUpgradeInfo


T = TypeVar("T", bound="BTMergePreviewInfo")


@_attrs_define
class BTMergePreviewInfo:
    """
    Attributes:
        branch_point_microversion_id (str | Unset):
        branch_point_version_id (str | Unset):
        branch_point_workspace_id (str | Unset):
        changes (list[BTElementMergeInfo] | Unset):
        is_branch_point_at_start (bool | Unset):
        source_microversion_id (str | Unset):
        target_microversion_id (str | Unset):
        upgrade_info (BTMergeUpgradeInfo | Unset):
    """

    branch_point_microversion_id: str | Unset = UNSET
    branch_point_version_id: str | Unset = UNSET
    branch_point_workspace_id: str | Unset = UNSET
    changes: list[BTElementMergeInfo] | Unset = UNSET
    is_branch_point_at_start: bool | Unset = UNSET
    source_microversion_id: str | Unset = UNSET
    target_microversion_id: str | Unset = UNSET
    upgrade_info: BTMergeUpgradeInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch_point_microversion_id = self.branch_point_microversion_id

        branch_point_version_id = self.branch_point_version_id

        branch_point_workspace_id = self.branch_point_workspace_id

        changes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.changes, Unset):
            changes = []
            for changes_item_data in self.changes:
                changes_item = changes_item_data.to_dict()
                changes.append(changes_item)

        is_branch_point_at_start = self.is_branch_point_at_start

        source_microversion_id = self.source_microversion_id

        target_microversion_id = self.target_microversion_id

        upgrade_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upgrade_info, Unset):
            upgrade_info = self.upgrade_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branch_point_microversion_id is not UNSET:
            field_dict["branchPointMicroversionId"] = branch_point_microversion_id
        if branch_point_version_id is not UNSET:
            field_dict["branchPointVersionId"] = branch_point_version_id
        if branch_point_workspace_id is not UNSET:
            field_dict["branchPointWorkspaceId"] = branch_point_workspace_id
        if changes is not UNSET:
            field_dict["changes"] = changes
        if is_branch_point_at_start is not UNSET:
            field_dict["isBranchPointAtStart"] = is_branch_point_at_start
        if source_microversion_id is not UNSET:
            field_dict["sourceMicroversionId"] = source_microversion_id
        if target_microversion_id is not UNSET:
            field_dict["targetMicroversionId"] = target_microversion_id
        if upgrade_info is not UNSET:
            field_dict["upgradeInfo"] = upgrade_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_element_merge_info import BTElementMergeInfo
        from ..models.bt_merge_upgrade_info import BTMergeUpgradeInfo

        d = dict(src_dict)
        branch_point_microversion_id = d.pop("branchPointMicroversionId", UNSET)

        branch_point_version_id = d.pop("branchPointVersionId", UNSET)

        branch_point_workspace_id = d.pop("branchPointWorkspaceId", UNSET)

        _changes = d.pop("changes", UNSET)
        changes: list[BTElementMergeInfo] | Unset = UNSET
        if _changes is not UNSET:
            changes = []
            for changes_item_data in _changes:
                changes_item = BTElementMergeInfo.from_dict(changes_item_data)

                changes.append(changes_item)

        is_branch_point_at_start = d.pop("isBranchPointAtStart", UNSET)

        source_microversion_id = d.pop("sourceMicroversionId", UNSET)

        target_microversion_id = d.pop("targetMicroversionId", UNSET)

        _upgrade_info = d.pop("upgradeInfo", UNSET)
        upgrade_info: BTMergeUpgradeInfo | Unset
        if isinstance(_upgrade_info, Unset):
            upgrade_info = UNSET
        else:
            upgrade_info = BTMergeUpgradeInfo.from_dict(_upgrade_info)

        bt_merge_preview_info = cls(
            branch_point_microversion_id=branch_point_microversion_id,
            branch_point_version_id=branch_point_version_id,
            branch_point_workspace_id=branch_point_workspace_id,
            changes=changes,
            is_branch_point_at_start=is_branch_point_at_start,
            source_microversion_id=source_microversion_id,
            target_microversion_id=target_microversion_id,
            upgrade_info=upgrade_info,
        )

        bt_merge_preview_info.additional_properties = d
        return bt_merge_preview_info

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
