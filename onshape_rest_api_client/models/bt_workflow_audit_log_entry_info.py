from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_property_update_info import BTPropertyUpdateInfo
    from ..models.bt_workflow_audit_log_entry_info_feature_script_response import (
        BTWorkflowAuditLogEntryInfoFeatureScriptResponse,
    )


T = TypeVar("T", bound="BTWorkflowAuditLogEntryInfo")


@_attrs_define
class BTWorkflowAuditLogEntryInfo:
    """
    Attributes:
        approval_override (bool | Unset):
        approver_ids (list[str] | Unset):
        comment_id (str | Unset):
        date (datetime.datetime | Unset):
        entry_type (int | Unset):
        error_message (str | Unset):
        feature_script_console (str | Unset):
        feature_script_notices (list[str] | Unset):
        feature_script_response (BTWorkflowAuditLogEntryInfoFeatureScriptResponse | Unset):
        id (str | Unset):
        object_id (str | Unset):
        property_updates (list[BTPropertyUpdateInfo] | Unset):
        support_code (str | Unset):
        user_id (str | Unset):
        workflow_action (str | Unset):
        workflow_state (str | Unset):
        workflow_transition (str | Unset):
    """

    approval_override: bool | Unset = UNSET
    approver_ids: list[str] | Unset = UNSET
    comment_id: str | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    entry_type: int | Unset = UNSET
    error_message: str | Unset = UNSET
    feature_script_console: str | Unset = UNSET
    feature_script_notices: list[str] | Unset = UNSET
    feature_script_response: BTWorkflowAuditLogEntryInfoFeatureScriptResponse | Unset = UNSET
    id: str | Unset = UNSET
    object_id: str | Unset = UNSET
    property_updates: list[BTPropertyUpdateInfo] | Unset = UNSET
    support_code: str | Unset = UNSET
    user_id: str | Unset = UNSET
    workflow_action: str | Unset = UNSET
    workflow_state: str | Unset = UNSET
    workflow_transition: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approval_override = self.approval_override

        approver_ids: list[str] | Unset = UNSET
        if not isinstance(self.approver_ids, Unset):
            approver_ids = self.approver_ids

        comment_id = self.comment_id

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        entry_type = self.entry_type

        error_message = self.error_message

        feature_script_console = self.feature_script_console

        feature_script_notices: list[str] | Unset = UNSET
        if not isinstance(self.feature_script_notices, Unset):
            feature_script_notices = self.feature_script_notices

        feature_script_response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_script_response, Unset):
            feature_script_response = self.feature_script_response.to_dict()

        id = self.id

        object_id = self.object_id

        property_updates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.property_updates, Unset):
            property_updates = []
            for property_updates_item_data in self.property_updates:
                property_updates_item = property_updates_item_data.to_dict()
                property_updates.append(property_updates_item)

        support_code = self.support_code

        user_id = self.user_id

        workflow_action = self.workflow_action

        workflow_state = self.workflow_state

        workflow_transition = self.workflow_transition

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approval_override is not UNSET:
            field_dict["approvalOverride"] = approval_override
        if approver_ids is not UNSET:
            field_dict["approverIds"] = approver_ids
        if comment_id is not UNSET:
            field_dict["commentId"] = comment_id
        if date is not UNSET:
            field_dict["date"] = date
        if entry_type is not UNSET:
            field_dict["entryType"] = entry_type
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if feature_script_console is not UNSET:
            field_dict["featureScriptConsole"] = feature_script_console
        if feature_script_notices is not UNSET:
            field_dict["featureScriptNotices"] = feature_script_notices
        if feature_script_response is not UNSET:
            field_dict["featureScriptResponse"] = feature_script_response
        if id is not UNSET:
            field_dict["id"] = id
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if property_updates is not UNSET:
            field_dict["propertyUpdates"] = property_updates
        if support_code is not UNSET:
            field_dict["supportCode"] = support_code
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if workflow_action is not UNSET:
            field_dict["workflowAction"] = workflow_action
        if workflow_state is not UNSET:
            field_dict["workflowState"] = workflow_state
        if workflow_transition is not UNSET:
            field_dict["workflowTransition"] = workflow_transition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_property_update_info import BTPropertyUpdateInfo
        from ..models.bt_workflow_audit_log_entry_info_feature_script_response import (
            BTWorkflowAuditLogEntryInfoFeatureScriptResponse,
        )

        d = dict(src_dict)
        approval_override = d.pop("approvalOverride", UNSET)

        approver_ids = cast(list[str], d.pop("approverIds", UNSET))

        comment_id = d.pop("commentId", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        entry_type = d.pop("entryType", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        feature_script_console = d.pop("featureScriptConsole", UNSET)

        feature_script_notices = cast(list[str], d.pop("featureScriptNotices", UNSET))

        _feature_script_response = d.pop("featureScriptResponse", UNSET)
        feature_script_response: BTWorkflowAuditLogEntryInfoFeatureScriptResponse | Unset
        if isinstance(_feature_script_response, Unset):
            feature_script_response = UNSET
        else:
            feature_script_response = BTWorkflowAuditLogEntryInfoFeatureScriptResponse.from_dict(
                _feature_script_response
            )

        id = d.pop("id", UNSET)

        object_id = d.pop("objectId", UNSET)

        _property_updates = d.pop("propertyUpdates", UNSET)
        property_updates: list[BTPropertyUpdateInfo] | Unset = UNSET
        if _property_updates is not UNSET:
            property_updates = []
            for property_updates_item_data in _property_updates:
                property_updates_item = BTPropertyUpdateInfo.from_dict(property_updates_item_data)

                property_updates.append(property_updates_item)

        support_code = d.pop("supportCode", UNSET)

        user_id = d.pop("userId", UNSET)

        workflow_action = d.pop("workflowAction", UNSET)

        workflow_state = d.pop("workflowState", UNSET)

        workflow_transition = d.pop("workflowTransition", UNSET)

        bt_workflow_audit_log_entry_info = cls(
            approval_override=approval_override,
            approver_ids=approver_ids,
            comment_id=comment_id,
            date=date,
            entry_type=entry_type,
            error_message=error_message,
            feature_script_console=feature_script_console,
            feature_script_notices=feature_script_notices,
            feature_script_response=feature_script_response,
            id=id,
            object_id=object_id,
            property_updates=property_updates,
            support_code=support_code,
            user_id=user_id,
            workflow_action=workflow_action,
            workflow_state=workflow_state,
            workflow_transition=workflow_transition,
        )

        bt_workflow_audit_log_entry_info.additional_properties = d
        return bt_workflow_audit_log_entry_info

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
