from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_comment_info import BTCommentInfo
    from ..models.bt_published_workflow_id import BTPublishedWorkflowId
    from ..models.bt_release_comment_list_info import BTReleaseCommentListInfo
    from ..models.bt_release_package_info_column_names import BTReleasePackageInfoColumnNames
    from ..models.bt_release_package_item_info import BTReleasePackageItemInfo
    from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo
    from ..models.bt_workflow_property_info import BTWorkflowPropertyInfo
    from ..models.bt_workflow_snapshot_info import BTWorkflowSnapshotInfo


T = TypeVar("T", bound="BTReleasePackageInfo")


@_attrs_define
class BTReleasePackageInfo:
    """
    Attributes:
        add_all_drawings_active (bool | Unset):
        change_order_id (str | Unset):
        column_names (BTReleasePackageInfoColumnNames | Unset):
        comments (list[BTCommentInfo] | Unset):
        company_id (str | Unset):
        created_at (datetime.datetime | Unset):
        created_by (BTUserBasicSummaryInfo | Unset):
        description (str | Unset):
        detailed (bool | Unset):
        document_id (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        is_obsoletion (bool | Unset):
        items (list[BTReleasePackageItemInfo] | Unset):
        linked_version_ids (list[str] | Unset):
        modified_at (datetime.datetime | Unset):
        modified_by (BTUserBasicSummaryInfo | Unset):
        name (str | Unset): Name of the resource.
        original_workspace_id (str | Unset):
        package_thumbnail (str | Unset):
        parent_comments (list[BTReleaseCommentListInfo] | Unset):
        parent_packages (list[str] | Unset):
        properties (list[BTWorkflowPropertyInfo] | Unset):
        retained_as_draft (bool | Unset): Indicates whether the release is still in setup state and saved as a draft.
        revision_rule_id (str | Unset):
        root_items_to_rebuild (list[str] | Unset):
        updated_item_ids (list[str] | Unset):
        version_id (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        workflow (BTWorkflowSnapshotInfo | Unset):
        workflow_error (str | Unset):
        workflow_id (BTPublishedWorkflowId | Unset):
        workspace_id (str | Unset):
    """

    add_all_drawings_active: bool | Unset = UNSET
    change_order_id: str | Unset = UNSET
    column_names: BTReleasePackageInfoColumnNames | Unset = UNSET
    comments: list[BTCommentInfo] | Unset = UNSET
    company_id: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by: BTUserBasicSummaryInfo | Unset = UNSET
    description: str | Unset = UNSET
    detailed: bool | Unset = UNSET
    document_id: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    is_obsoletion: bool | Unset = UNSET
    items: list[BTReleasePackageItemInfo] | Unset = UNSET
    linked_version_ids: list[str] | Unset = UNSET
    modified_at: datetime.datetime | Unset = UNSET
    modified_by: BTUserBasicSummaryInfo | Unset = UNSET
    name: str | Unset = UNSET
    original_workspace_id: str | Unset = UNSET
    package_thumbnail: str | Unset = UNSET
    parent_comments: list[BTReleaseCommentListInfo] | Unset = UNSET
    parent_packages: list[str] | Unset = UNSET
    properties: list[BTWorkflowPropertyInfo] | Unset = UNSET
    retained_as_draft: bool | Unset = UNSET
    revision_rule_id: str | Unset = UNSET
    root_items_to_rebuild: list[str] | Unset = UNSET
    updated_item_ids: list[str] | Unset = UNSET
    version_id: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    workflow: BTWorkflowSnapshotInfo | Unset = UNSET
    workflow_error: str | Unset = UNSET
    workflow_id: BTPublishedWorkflowId | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        add_all_drawings_active = self.add_all_drawings_active

        change_order_id = self.change_order_id

        column_names: dict[str, Any] | Unset = UNSET
        if not isinstance(self.column_names, Unset):
            column_names = self.column_names.to_dict()

        comments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()
                comments.append(comments_item)

        company_id = self.company_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        description = self.description

        detailed = self.detailed

        document_id = self.document_id

        href = self.href

        id = self.id

        is_obsoletion = self.is_obsoletion

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        linked_version_ids: list[str] | Unset = UNSET
        if not isinstance(self.linked_version_ids, Unset):
            linked_version_ids = self.linked_version_ids

        modified_at: str | Unset = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        modified_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.modified_by, Unset):
            modified_by = self.modified_by.to_dict()

        name = self.name

        original_workspace_id = self.original_workspace_id

        package_thumbnail = self.package_thumbnail

        parent_comments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parent_comments, Unset):
            parent_comments = []
            for parent_comments_item_data in self.parent_comments:
                parent_comments_item = parent_comments_item_data.to_dict()
                parent_comments.append(parent_comments_item)

        parent_packages: list[str] | Unset = UNSET
        if not isinstance(self.parent_packages, Unset):
            parent_packages = self.parent_packages

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        retained_as_draft = self.retained_as_draft

        revision_rule_id = self.revision_rule_id

        root_items_to_rebuild: list[str] | Unset = UNSET
        if not isinstance(self.root_items_to_rebuild, Unset):
            root_items_to_rebuild = self.root_items_to_rebuild

        updated_item_ids: list[str] | Unset = UNSET
        if not isinstance(self.updated_item_ids, Unset):
            updated_item_ids = self.updated_item_ids

        version_id = self.version_id

        view_ref = self.view_ref

        workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        workflow_error = self.workflow_error

        workflow_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow_id, Unset):
            workflow_id = self.workflow_id.to_dict()

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_all_drawings_active is not UNSET:
            field_dict["addAllDrawingsActive"] = add_all_drawings_active
        if change_order_id is not UNSET:
            field_dict["changeOrderId"] = change_order_id
        if column_names is not UNSET:
            field_dict["columnNames"] = column_names
        if comments is not UNSET:
            field_dict["comments"] = comments
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if detailed is not UNSET:
            field_dict["detailed"] = detailed
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if is_obsoletion is not UNSET:
            field_dict["isObsoletion"] = is_obsoletion
        if items is not UNSET:
            field_dict["items"] = items
        if linked_version_ids is not UNSET:
            field_dict["linkedVersionIds"] = linked_version_ids
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if name is not UNSET:
            field_dict["name"] = name
        if original_workspace_id is not UNSET:
            field_dict["originalWorkspaceId"] = original_workspace_id
        if package_thumbnail is not UNSET:
            field_dict["packageThumbnail"] = package_thumbnail
        if parent_comments is not UNSET:
            field_dict["parentComments"] = parent_comments
        if parent_packages is not UNSET:
            field_dict["parentPackages"] = parent_packages
        if properties is not UNSET:
            field_dict["properties"] = properties
        if retained_as_draft is not UNSET:
            field_dict["retainedAsDraft"] = retained_as_draft
        if revision_rule_id is not UNSET:
            field_dict["revisionRuleId"] = revision_rule_id
        if root_items_to_rebuild is not UNSET:
            field_dict["rootItemsToRebuild"] = root_items_to_rebuild
        if updated_item_ids is not UNSET:
            field_dict["updatedItemIds"] = updated_item_ids
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if workflow_error is not UNSET:
            field_dict["workflowError"] = workflow_error
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_comment_info import BTCommentInfo
        from ..models.bt_published_workflow_id import BTPublishedWorkflowId
        from ..models.bt_release_comment_list_info import BTReleaseCommentListInfo
        from ..models.bt_release_package_info_column_names import BTReleasePackageInfoColumnNames
        from ..models.bt_release_package_item_info import BTReleasePackageItemInfo
        from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo
        from ..models.bt_workflow_property_info import BTWorkflowPropertyInfo
        from ..models.bt_workflow_snapshot_info import BTWorkflowSnapshotInfo

        d = dict(src_dict)
        add_all_drawings_active = d.pop("addAllDrawingsActive", UNSET)

        change_order_id = d.pop("changeOrderId", UNSET)

        _column_names = d.pop("columnNames", UNSET)
        column_names: BTReleasePackageInfoColumnNames | Unset
        if isinstance(_column_names, Unset):
            column_names = UNSET
        else:
            column_names = BTReleasePackageInfoColumnNames.from_dict(_column_names)

        _comments = d.pop("comments", UNSET)
        comments: list[BTCommentInfo] | Unset = UNSET
        if _comments is not UNSET:
            comments = []
            for comments_item_data in _comments:
                comments_item = BTCommentInfo.from_dict(comments_item_data)

                comments.append(comments_item)

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

        detailed = d.pop("detailed", UNSET)

        document_id = d.pop("documentId", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        is_obsoletion = d.pop("isObsoletion", UNSET)

        _items = d.pop("items", UNSET)
        items: list[BTReleasePackageItemInfo] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = BTReleasePackageItemInfo.from_dict(items_item_data)

                items.append(items_item)

        linked_version_ids = cast(list[str], d.pop("linkedVersionIds", UNSET))

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

        original_workspace_id = d.pop("originalWorkspaceId", UNSET)

        package_thumbnail = d.pop("packageThumbnail", UNSET)

        _parent_comments = d.pop("parentComments", UNSET)
        parent_comments: list[BTReleaseCommentListInfo] | Unset = UNSET
        if _parent_comments is not UNSET:
            parent_comments = []
            for parent_comments_item_data in _parent_comments:
                parent_comments_item = BTReleaseCommentListInfo.from_dict(parent_comments_item_data)

                parent_comments.append(parent_comments_item)

        parent_packages = cast(list[str], d.pop("parentPackages", UNSET))

        _properties = d.pop("properties", UNSET)
        properties: list[BTWorkflowPropertyInfo] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = BTWorkflowPropertyInfo.from_dict(properties_item_data)

                properties.append(properties_item)

        retained_as_draft = d.pop("retainedAsDraft", UNSET)

        revision_rule_id = d.pop("revisionRuleId", UNSET)

        root_items_to_rebuild = cast(list[str], d.pop("rootItemsToRebuild", UNSET))

        updated_item_ids = cast(list[str], d.pop("updatedItemIds", UNSET))

        version_id = d.pop("versionId", UNSET)

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

        workspace_id = d.pop("workspaceId", UNSET)

        bt_release_package_info = cls(
            add_all_drawings_active=add_all_drawings_active,
            change_order_id=change_order_id,
            column_names=column_names,
            comments=comments,
            company_id=company_id,
            created_at=created_at,
            created_by=created_by,
            description=description,
            detailed=detailed,
            document_id=document_id,
            href=href,
            id=id,
            is_obsoletion=is_obsoletion,
            items=items,
            linked_version_ids=linked_version_ids,
            modified_at=modified_at,
            modified_by=modified_by,
            name=name,
            original_workspace_id=original_workspace_id,
            package_thumbnail=package_thumbnail,
            parent_comments=parent_comments,
            parent_packages=parent_packages,
            properties=properties,
            retained_as_draft=retained_as_draft,
            revision_rule_id=revision_rule_id,
            root_items_to_rebuild=root_items_to_rebuild,
            updated_item_ids=updated_item_ids,
            version_id=version_id,
            view_ref=view_ref,
            workflow=workflow,
            workflow_error=workflow_error,
            workflow_id=workflow_id,
            workspace_id=workspace_id,
        )

        bt_release_package_info.additional_properties = d
        return bt_release_package_info

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
