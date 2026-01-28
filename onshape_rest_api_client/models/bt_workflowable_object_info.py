from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_published_workflow_id import BTPublishedWorkflowId
    from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo
    from ..models.bt_workflow_property_info import BTWorkflowPropertyInfo
    from ..models.bt_workflow_snapshot_info import BTWorkflowSnapshotInfo


T = TypeVar("T", bound="BTWorkflowableObjectInfo")


@_attrs_define
class BTWorkflowableObjectInfo:
    """
    Attributes:
        company_id (str | Unset):
        created_at (datetime.datetime | Unset):
        created_by (BTUserBasicSummaryInfo | Unset):
        description (str | Unset):
        document_id (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        modified_at (datetime.datetime | Unset):
        modified_by (BTUserBasicSummaryInfo | Unset):
        name (str | Unset): Name of the resource.
        properties (list[BTWorkflowPropertyInfo] | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        workflow (BTWorkflowSnapshotInfo | Unset):
        workflow_error (str | Unset):
        workflow_id (BTPublishedWorkflowId | Unset):
    """

    company_id: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by: BTUserBasicSummaryInfo | Unset = UNSET
    description: str | Unset = UNSET
    document_id: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    modified_at: datetime.datetime | Unset = UNSET
    modified_by: BTUserBasicSummaryInfo | Unset = UNSET
    name: str | Unset = UNSET
    properties: list[BTWorkflowPropertyInfo] | Unset = UNSET
    view_ref: str | Unset = UNSET
    workflow: BTWorkflowSnapshotInfo | Unset = UNSET
    workflow_error: str | Unset = UNSET
    workflow_id: BTPublishedWorkflowId | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        description = self.description

        document_id = self.document_id

        href = self.href

        id = self.id

        modified_at: str | Unset = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        modified_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.modified_by, Unset):
            modified_by = self.modified_by.to_dict()

        name = self.name

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        view_ref = self.view_ref

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        workflow_error = self.workflow_error

        workflow_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow_id, Unset):
            workflow_id = self.workflow_id.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if name is not UNSET:
            field_dict["name"] = name
        if properties is not UNSET:
            field_dict["properties"] = properties
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if workflow_error is not UNSET:
            field_dict["workflowError"] = workflow_error
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_published_workflow_id import BTPublishedWorkflowId
        from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo
        from ..models.bt_workflow_property_info import BTWorkflowPropertyInfo
        from ..models.bt_workflow_snapshot_info import BTWorkflowSnapshotInfo

        d = dict(src_dict)
        company_id = d.pop("companyId", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _created_by = d.pop("createdBy", UNSET)
        created_by: BTUserBasicSummaryInfo | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = BTUserBasicSummaryInfo.from_dict(_created_by)

        description = d.pop("description", UNSET)

        document_id = d.pop("documentId", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _modified_at = d.pop("modifiedAt", UNSET)
        modified_at: datetime.datetime | Unset
        if isinstance(_modified_at, Unset):
            modified_at = UNSET
        else:
            modified_at = isoparse(_modified_at)

        _modified_by = d.pop("modifiedBy", UNSET)
        modified_by: BTUserBasicSummaryInfo | Unset
        if isinstance(_modified_by, Unset):
            modified_by = UNSET
        else:
            modified_by = BTUserBasicSummaryInfo.from_dict(_modified_by)

        name = d.pop("name", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: list[BTWorkflowPropertyInfo] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = BTWorkflowPropertyInfo.from_dict(properties_item_data)

                properties.append(properties_item)

        view_ref = d.pop("viewRef", UNSET)

        _workflow = d.pop("workflow", UNSET)
        workflow: BTWorkflowSnapshotInfo | Unset
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = BTWorkflowSnapshotInfo.from_dict(_workflow)

        workflow_error = d.pop("workflowError", UNSET)

        _workflow_id = d.pop("workflowId", UNSET)
        workflow_id: BTPublishedWorkflowId | Unset
        if isinstance(_workflow_id, Unset):
            workflow_id = UNSET
        else:
            workflow_id = BTPublishedWorkflowId.from_dict(_workflow_id)

        bt_workflowable_object_info = cls(
            company_id=company_id,
            created_at=created_at,
            created_by=created_by,
            description=description,
            document_id=document_id,
            href=href,
            id=id,
            modified_at=modified_at,
            modified_by=modified_by,
            name=name,
            properties=properties,
            view_ref=view_ref,
            workflow=workflow,
            workflow_error=workflow_error,
            workflow_id=workflow_id,
        )

        bt_workflowable_object_info.additional_properties = d
        return bt_workflowable_object_info

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
