from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_workflow_action_info import BTWorkflowActionInfo
    from ..models.bt_workflow_state_info import BTWorkflowStateInfo


T = TypeVar("T", bound="BTWorkflowSnapshotInfo")


@_attrs_define
class BTWorkflowSnapshotInfo:
    """
    Attributes:
        actions (list[BTWorkflowActionInfo] | Unset):
        approver_ids (list[str] | Unset):
        can_be_discarded (bool | Unset):
        current_state_display_name (str | Unset):
        debug_microversion_id (str | Unset):
        error_message (str | Unset):
        is_creator (bool | Unset):
        is_discarded (bool | Unset):
        is_frozen (bool | Unset):
        is_setup (bool | Unset):
        metadata_state (str | Unset):
        notifier_ids (list[str] | Unset):
        state (BTWorkflowStateInfo | Unset):
        uses_external_plm (bool | Unset):
    """

    actions: list[BTWorkflowActionInfo] | Unset = UNSET
    approver_ids: list[str] | Unset = UNSET
    can_be_discarded: bool | Unset = UNSET
    current_state_display_name: str | Unset = UNSET
    debug_microversion_id: str | Unset = UNSET
    error_message: str | Unset = UNSET
    is_creator: bool | Unset = UNSET
    is_discarded: bool | Unset = UNSET
    is_frozen: bool | Unset = UNSET
    is_setup: bool | Unset = UNSET
    metadata_state: str | Unset = UNSET
    notifier_ids: list[str] | Unset = UNSET
    state: BTWorkflowStateInfo | Unset = UNSET
    uses_external_plm: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        approver_ids: list[str] | Unset = UNSET
        if not isinstance(self.approver_ids, Unset):
            approver_ids = self.approver_ids

        can_be_discarded = self.can_be_discarded

        current_state_display_name = self.current_state_display_name

        debug_microversion_id = self.debug_microversion_id

        error_message = self.error_message

        is_creator = self.is_creator

        is_discarded = self.is_discarded

        is_frozen = self.is_frozen

        is_setup = self.is_setup

        metadata_state = self.metadata_state

        notifier_ids: list[str] | Unset = UNSET
        if not isinstance(self.notifier_ids, Unset):
            notifier_ids = self.notifier_ids

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        uses_external_plm = self.uses_external_plm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actions is not UNSET:
            field_dict["actions"] = actions
        if approver_ids is not UNSET:
            field_dict["approverIds"] = approver_ids
        if can_be_discarded is not UNSET:
            field_dict["canBeDiscarded"] = can_be_discarded
        if current_state_display_name is not UNSET:
            field_dict["currentStateDisplayName"] = current_state_display_name
        if debug_microversion_id is not UNSET:
            field_dict["debugMicroversionId"] = debug_microversion_id
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if is_creator is not UNSET:
            field_dict["isCreator"] = is_creator
        if is_discarded is not UNSET:
            field_dict["isDiscarded"] = is_discarded
        if is_frozen is not UNSET:
            field_dict["isFrozen"] = is_frozen
        if is_setup is not UNSET:
            field_dict["isSetup"] = is_setup
        if metadata_state is not UNSET:
            field_dict["metadataState"] = metadata_state
        if notifier_ids is not UNSET:
            field_dict["notifierIds"] = notifier_ids
        if state is not UNSET:
            field_dict["state"] = state
        if uses_external_plm is not UNSET:
            field_dict["usesExternalPlm"] = uses_external_plm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_workflow_action_info import BTWorkflowActionInfo
        from ..models.bt_workflow_state_info import BTWorkflowStateInfo

        d = dict(src_dict)
        _actions = d.pop("actions", UNSET)
        actions: list[BTWorkflowActionInfo] | Unset = UNSET
        if _actions is not UNSET:
            actions = []
            for actions_item_data in _actions:
                actions_item = BTWorkflowActionInfo.from_dict(actions_item_data)

                actions.append(actions_item)

        approver_ids = cast(list[str], d.pop("approverIds", UNSET))

        can_be_discarded = d.pop("canBeDiscarded", UNSET)

        current_state_display_name = d.pop("currentStateDisplayName", UNSET)

        debug_microversion_id = d.pop("debugMicroversionId", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        is_creator = d.pop("isCreator", UNSET)

        is_discarded = d.pop("isDiscarded", UNSET)

        is_frozen = d.pop("isFrozen", UNSET)

        is_setup = d.pop("isSetup", UNSET)

        metadata_state = d.pop("metadataState", UNSET)

        notifier_ids = cast(list[str], d.pop("notifierIds", UNSET))

        _state = d.pop("state", UNSET)
        state: BTWorkflowStateInfo | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = BTWorkflowStateInfo.from_dict(_state)

        uses_external_plm = d.pop("usesExternalPlm", UNSET)

        bt_workflow_snapshot_info = cls(
            actions=actions,
            approver_ids=approver_ids,
            can_be_discarded=can_be_discarded,
            current_state_display_name=current_state_display_name,
            debug_microversion_id=debug_microversion_id,
            error_message=error_message,
            is_creator=is_creator,
            is_discarded=is_discarded,
            is_frozen=is_frozen,
            is_setup=is_setup,
            metadata_state=metadata_state,
            notifier_ids=notifier_ids,
            state=state,
            uses_external_plm=uses_external_plm,
        )

        bt_workflow_snapshot_info.additional_properties = d
        return bt_workflow_snapshot_info

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
