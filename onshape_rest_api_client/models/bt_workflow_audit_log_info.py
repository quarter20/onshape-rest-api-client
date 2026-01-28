from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_published_workflow_id import BTPublishedWorkflowId
    from ..models.bt_workflow_audit_log_entry_info import BTWorkflowAuditLogEntryInfo


T = TypeVar("T", bound="BTWorkflowAuditLogInfo")


@_attrs_define
class BTWorkflowAuditLogInfo:
    """
    Attributes:
        company_id (str | Unset):
        debug_microversion_id (str | Unset):
        entries (list[BTWorkflowAuditLogEntryInfo] | Unset):
        object_id (str | Unset):
        object_type (int | Unset):
        published_workflow_id (BTPublishedWorkflowId | Unset):
    """

    company_id: str | Unset = UNSET
    debug_microversion_id: str | Unset = UNSET
    entries: list[BTWorkflowAuditLogEntryInfo] | Unset = UNSET
    object_id: str | Unset = UNSET
    object_type: int | Unset = UNSET
    published_workflow_id: BTPublishedWorkflowId | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        debug_microversion_id = self.debug_microversion_id

        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        object_id = self.object_id

        object_type = self.object_type

        published_workflow_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.published_workflow_id, Unset):
            published_workflow_id = self.published_workflow_id.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if debug_microversion_id is not UNSET:
            field_dict["debugMicroversionId"] = debug_microversion_id
        if entries is not UNSET:
            field_dict["entries"] = entries
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if published_workflow_id is not UNSET:
            field_dict["publishedWorkflowId"] = published_workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_published_workflow_id import BTPublishedWorkflowId
        from ..models.bt_workflow_audit_log_entry_info import BTWorkflowAuditLogEntryInfo

        d = dict(src_dict)
        company_id = d.pop("companyId", UNSET)

        debug_microversion_id = d.pop("debugMicroversionId", UNSET)

        _entries = d.pop("entries", UNSET)
        entries: list[BTWorkflowAuditLogEntryInfo] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = BTWorkflowAuditLogEntryInfo.from_dict(entries_item_data)

                entries.append(entries_item)

        object_id = d.pop("objectId", UNSET)

        object_type = d.pop("objectType", UNSET)

        _published_workflow_id = d.pop("publishedWorkflowId", UNSET)
        published_workflow_id: BTPublishedWorkflowId | Unset
        if isinstance(_published_workflow_id, Unset):
            published_workflow_id = UNSET
        else:
            published_workflow_id = BTPublishedWorkflowId.from_dict(_published_workflow_id)

        bt_workflow_audit_log_info = cls(
            company_id=company_id,
            debug_microversion_id=debug_microversion_id,
            entries=entries,
            object_id=object_id,
            object_type=object_type,
            published_workflow_id=published_workflow_id,
        )

        bt_workflow_audit_log_info.additional_properties = d
        return bt_workflow_audit_log_info

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
