from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_transition_type import BTTransitionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTWorkflowActionInfo")


@_attrs_define
class BTWorkflowActionInfo:
    """
    Attributes:
        action (str | Unset):
        allow_if_approvers (bool | Unset):
        allow_if_no_approvers (bool | Unset):
        always_allow (bool | Unset):
        is_admin_override (bool | Unset):
        is_approver_action (bool | Unset):
        is_creator_override (bool | Unset):
        label (str | Unset):
        required_properties (list[str] | Unset):
        tooltip (str | Unset):
        type_ (BTTransitionType | Unset): Transition types(SUBMIT, APPROVE, REJECT)
        ui_hint (str | Unset):
    """

    action: str | Unset = UNSET
    allow_if_approvers: bool | Unset = UNSET
    allow_if_no_approvers: bool | Unset = UNSET
    always_allow: bool | Unset = UNSET
    is_admin_override: bool | Unset = UNSET
    is_approver_action: bool | Unset = UNSET
    is_creator_override: bool | Unset = UNSET
    label: str | Unset = UNSET
    required_properties: list[str] | Unset = UNSET
    tooltip: str | Unset = UNSET
    type_: BTTransitionType | Unset = UNSET
    ui_hint: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        allow_if_approvers = self.allow_if_approvers

        allow_if_no_approvers = self.allow_if_no_approvers

        always_allow = self.always_allow

        is_admin_override = self.is_admin_override

        is_approver_action = self.is_approver_action

        is_creator_override = self.is_creator_override

        label = self.label

        required_properties: list[str] | Unset = UNSET
        if not isinstance(self.required_properties, Unset):
            required_properties = self.required_properties

        tooltip = self.tooltip

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        ui_hint = self.ui_hint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if allow_if_approvers is not UNSET:
            field_dict["allowIfApprovers"] = allow_if_approvers
        if allow_if_no_approvers is not UNSET:
            field_dict["allowIfNoApprovers"] = allow_if_no_approvers
        if always_allow is not UNSET:
            field_dict["alwaysAllow"] = always_allow
        if is_admin_override is not UNSET:
            field_dict["isAdminOverride"] = is_admin_override
        if is_approver_action is not UNSET:
            field_dict["isApproverAction"] = is_approver_action
        if is_creator_override is not UNSET:
            field_dict["isCreatorOverride"] = is_creator_override
        if label is not UNSET:
            field_dict["label"] = label
        if required_properties is not UNSET:
            field_dict["requiredProperties"] = required_properties
        if tooltip is not UNSET:
            field_dict["tooltip"] = tooltip
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ui_hint is not UNSET:
            field_dict["uiHint"] = ui_hint

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        allow_if_approvers = d.pop("allowIfApprovers", UNSET)

        allow_if_no_approvers = d.pop("allowIfNoApprovers", UNSET)

        always_allow = d.pop("alwaysAllow", UNSET)

        is_admin_override = d.pop("isAdminOverride", UNSET)

        is_approver_action = d.pop("isApproverAction", UNSET)

        is_creator_override = d.pop("isCreatorOverride", UNSET)

        label = d.pop("label", UNSET)

        required_properties = cast(list[str], d.pop("requiredProperties", UNSET))

        tooltip = d.pop("tooltip", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: BTTransitionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BTTransitionType(_type_)

        ui_hint = d.pop("uiHint", UNSET)

        bt_workflow_action_info = cls(
            action=action,
            allow_if_approvers=allow_if_approvers,
            allow_if_no_approvers=allow_if_no_approvers,
            always_allow=always_allow,
            is_admin_override=is_admin_override,
            is_approver_action=is_approver_action,
            is_creator_override=is_creator_override,
            label=label,
            required_properties=required_properties,
            tooltip=tooltip,
            type_=type_,
            ui_hint=ui_hint,
        )

        bt_workflow_action_info.additional_properties = d
        return bt_workflow_action_info

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
