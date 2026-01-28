from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_comment_info import BTCommentInfo
    from ..models.bt_metadata_property_info import BTMetadataPropertyInfo
    from ..models.bt_published_workflow_info import BTPublishedWorkflowInfo
    from ..models.bt_task_item_info import BTTaskItemInfo
    from ..models.bt_task_rbac_role_info import BTTaskRbacRoleInfo
    from ..models.bt_task_team_summary_info import BTTaskTeamSummaryInfo
    from ..models.bt_task_user_summary_info import BTTaskUserSummaryInfo
    from ..models.bt_thumbnail_info import BTThumbnailInfo
    from ..models.bt_user_summary_info import BTUserSummaryInfo
    from ..models.bt_workflowable_object_info import BTWorkflowableObjectInfo


T = TypeVar("T", bound="BTTaskInfo")


@_attrs_define
class BTTaskInfo:
    """
    Attributes:
        action (str | Unset):
        approver_role (str | Unset):
        comments (list[BTCommentInfo] | Unset):
        company_id (str | Unset):
        created_at (datetime.datetime | Unset):
        creator (BTUserSummaryInfo | Unset):
        deletable (bool | Unset):
        description (str | Unset):
        document_id (str | Unset):
        document_name (str | Unset):
        document_type (int | Unset):
        editable (bool | Unset):
        element_id (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        object_id (str | Unset):
        properties (list[BTMetadataPropertyInfo] | Unset):
        published_workflow (BTPublishedWorkflowInfo | Unset): Captures information about a published workflow
        resolved_at (datetime.datetime | Unset):
        resolved_by (BTUserSummaryInfo | Unset):
        roles (list[BTTaskRbacRoleInfo] | Unset):
        simple_name (str | Unset):
        source_workspace_or_version_name (str | Unset):
        state (str | Unset):
        status (int | Unset):
        task_items (list[BTTaskItemInfo] | Unset):
        task_type (str | Unset):
        teams (list[BTTaskTeamSummaryInfo] | Unset):
        thumbnail (BTThumbnailInfo | Unset):
        transition (str | Unset):
        users (list[BTTaskUserSummaryInfo] | Unset):
        version_id (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        workflow_info (BTWorkflowableObjectInfo | Unset):
        workflowable_object_type (int | Unset):
        workspace_id (str | Unset):
    """

    action: str | Unset = UNSET
    approver_role: str | Unset = UNSET
    comments: list[BTCommentInfo] | Unset = UNSET
    company_id: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    creator: BTUserSummaryInfo | Unset = UNSET
    deletable: bool | Unset = UNSET
    description: str | Unset = UNSET
    document_id: str | Unset = UNSET
    document_name: str | Unset = UNSET
    document_type: int | Unset = UNSET
    editable: bool | Unset = UNSET
    element_id: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    object_id: str | Unset = UNSET
    properties: list[BTMetadataPropertyInfo] | Unset = UNSET
    published_workflow: BTPublishedWorkflowInfo | Unset = UNSET
    resolved_at: datetime.datetime | Unset = UNSET
    resolved_by: BTUserSummaryInfo | Unset = UNSET
    roles: list[BTTaskRbacRoleInfo] | Unset = UNSET
    simple_name: str | Unset = UNSET
    source_workspace_or_version_name: str | Unset = UNSET
    state: str | Unset = UNSET
    status: int | Unset = UNSET
    task_items: list[BTTaskItemInfo] | Unset = UNSET
    task_type: str | Unset = UNSET
    teams: list[BTTaskTeamSummaryInfo] | Unset = UNSET
    thumbnail: BTThumbnailInfo | Unset = UNSET
    transition: str | Unset = UNSET
    users: list[BTTaskUserSummaryInfo] | Unset = UNSET
    version_id: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    workflow_info: BTWorkflowableObjectInfo | Unset = UNSET
    workflowable_object_type: int | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        approver_role = self.approver_role

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

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        deletable = self.deletable

        description = self.description

        document_id = self.document_id

        document_name = self.document_name

        document_type = self.document_type

        editable = self.editable

        element_id = self.element_id

        href = self.href

        id = self.id

        name = self.name

        object_id = self.object_id

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        published_workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.published_workflow, Unset):
            published_workflow = self.published_workflow.to_dict()

        resolved_at: str | Unset = UNSET
        if not isinstance(self.resolved_at, Unset):
            resolved_at = self.resolved_at.isoformat()

        resolved_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resolved_by, Unset):
            resolved_by = self.resolved_by.to_dict()

        roles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        simple_name = self.simple_name

        source_workspace_or_version_name = self.source_workspace_or_version_name

        state = self.state

        status = self.status

        task_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.task_items, Unset):
            task_items = []
            for task_items_item_data in self.task_items:
                task_items_item = task_items_item_data.to_dict()
                task_items.append(task_items_item)

        task_type = self.task_type

        teams: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)

        thumbnail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail, Unset):
            thumbnail = self.thumbnail.to_dict()

        transition = self.transition

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        version_id = self.version_id

        view_ref = self.view_ref

        workflow_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow_info, Unset):
            workflow_info = self.workflow_info.to_dict()

        workflowable_object_type = self.workflowable_object_type

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if approver_role is not UNSET:
            field_dict["approverRole"] = approver_role
        if comments is not UNSET:
            field_dict["comments"] = comments
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if creator is not UNSET:
            field_dict["creator"] = creator
        if deletable is not UNSET:
            field_dict["deletable"] = deletable
        if description is not UNSET:
            field_dict["description"] = description
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if document_name is not UNSET:
            field_dict["documentName"] = document_name
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if editable is not UNSET:
            field_dict["editable"] = editable
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if properties is not UNSET:
            field_dict["properties"] = properties
        if published_workflow is not UNSET:
            field_dict["publishedWorkflow"] = published_workflow
        if resolved_at is not UNSET:
            field_dict["resolvedAt"] = resolved_at
        if resolved_by is not UNSET:
            field_dict["resolvedBy"] = resolved_by
        if roles is not UNSET:
            field_dict["roles"] = roles
        if simple_name is not UNSET:
            field_dict["simpleName"] = simple_name
        if source_workspace_or_version_name is not UNSET:
            field_dict["sourceWorkspaceOrVersionName"] = source_workspace_or_version_name
        if state is not UNSET:
            field_dict["state"] = state
        if status is not UNSET:
            field_dict["status"] = status
        if task_items is not UNSET:
            field_dict["taskItems"] = task_items
        if task_type is not UNSET:
            field_dict["taskType"] = task_type
        if teams is not UNSET:
            field_dict["teams"] = teams
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if transition is not UNSET:
            field_dict["transition"] = transition
        if users is not UNSET:
            field_dict["users"] = users
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if workflow_info is not UNSET:
            field_dict["workflowInfo"] = workflow_info
        if workflowable_object_type is not UNSET:
            field_dict["workflowableObjectType"] = workflowable_object_type
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_comment_info import BTCommentInfo
        from ..models.bt_metadata_property_info import BTMetadataPropertyInfo
        from ..models.bt_published_workflow_info import BTPublishedWorkflowInfo
        from ..models.bt_task_item_info import BTTaskItemInfo
        from ..models.bt_task_rbac_role_info import BTTaskRbacRoleInfo
        from ..models.bt_task_team_summary_info import BTTaskTeamSummaryInfo
        from ..models.bt_task_user_summary_info import BTTaskUserSummaryInfo
        from ..models.bt_thumbnail_info import BTThumbnailInfo
        from ..models.bt_user_summary_info import BTUserSummaryInfo
        from ..models.bt_workflowable_object_info import BTWorkflowableObjectInfo

        d = dict(src_dict)
        action = d.pop("action", UNSET)

        approver_role = d.pop("approverRole", UNSET)

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

        _creator = d.pop("creator", UNSET)
        creator: BTUserSummaryInfo | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = BTUserSummaryInfo.from_dict(_creator)

        deletable = d.pop("deletable", UNSET)

        description = d.pop("description", UNSET)

        document_id = d.pop("documentId", UNSET)

        document_name = d.pop("documentName", UNSET)

        document_type = d.pop("documentType", UNSET)

        editable = d.pop("editable", UNSET)

        element_id = d.pop("elementId", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        object_id = d.pop("objectId", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: list[BTMetadataPropertyInfo] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = BTMetadataPropertyInfo.from_dict(properties_item_data)

                properties.append(properties_item)

        _published_workflow = d.pop("publishedWorkflow", UNSET)
        published_workflow: BTPublishedWorkflowInfo | Unset
        if isinstance(_published_workflow, Unset):
            published_workflow = UNSET
        else:
            published_workflow = BTPublishedWorkflowInfo.from_dict(_published_workflow)

        _resolved_at = d.pop("resolvedAt", UNSET)
        resolved_at: datetime.datetime | Unset
        if isinstance(_resolved_at, Unset):
            resolved_at = UNSET
        else:
            resolved_at = isoparse(_resolved_at)

        _resolved_by = d.pop("resolvedBy", UNSET)
        resolved_by: BTUserSummaryInfo | Unset
        if isinstance(_resolved_by, Unset):
            resolved_by = UNSET
        else:
            resolved_by = BTUserSummaryInfo.from_dict(_resolved_by)

        _roles = d.pop("roles", UNSET)
        roles: list[BTTaskRbacRoleInfo] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = BTTaskRbacRoleInfo.from_dict(roles_item_data)

                roles.append(roles_item)

        simple_name = d.pop("simpleName", UNSET)

        source_workspace_or_version_name = d.pop("sourceWorkspaceOrVersionName", UNSET)

        state = d.pop("state", UNSET)

        status = d.pop("status", UNSET)

        _task_items = d.pop("taskItems", UNSET)
        task_items: list[BTTaskItemInfo] | Unset = UNSET
        if _task_items is not UNSET:
            task_items = []
            for task_items_item_data in _task_items:
                task_items_item = BTTaskItemInfo.from_dict(task_items_item_data)

                task_items.append(task_items_item)

        task_type = d.pop("taskType", UNSET)

        _teams = d.pop("teams", UNSET)
        teams: list[BTTaskTeamSummaryInfo] | Unset = UNSET
        if _teams is not UNSET:
            teams = []
            for teams_item_data in _teams:
                teams_item = BTTaskTeamSummaryInfo.from_dict(teams_item_data)

                teams.append(teams_item)

        _thumbnail = d.pop("thumbnail", UNSET)
        thumbnail: BTThumbnailInfo | Unset
        if isinstance(_thumbnail, Unset):
            thumbnail = UNSET
        else:
            thumbnail = BTThumbnailInfo.from_dict(_thumbnail)

        transition = d.pop("transition", UNSET)

        _users = d.pop("users", UNSET)
        users: list[BTTaskUserSummaryInfo] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = BTTaskUserSummaryInfo.from_dict(users_item_data)

                users.append(users_item)

        version_id = d.pop("versionId", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        _workflow_info = d.pop("workflowInfo", UNSET)
        workflow_info: BTWorkflowableObjectInfo | Unset
        if isinstance(_workflow_info, Unset):
            workflow_info = UNSET
        else:
            workflow_info = BTWorkflowableObjectInfo.from_dict(_workflow_info)

        workflowable_object_type = d.pop("workflowableObjectType", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_task_info = cls(
            action=action,
            approver_role=approver_role,
            comments=comments,
            company_id=company_id,
            created_at=created_at,
            creator=creator,
            deletable=deletable,
            description=description,
            document_id=document_id,
            document_name=document_name,
            document_type=document_type,
            editable=editable,
            element_id=element_id,
            href=href,
            id=id,
            name=name,
            object_id=object_id,
            properties=properties,
            published_workflow=published_workflow,
            resolved_at=resolved_at,
            resolved_by=resolved_by,
            roles=roles,
            simple_name=simple_name,
            source_workspace_or_version_name=source_workspace_or_version_name,
            state=state,
            status=status,
            task_items=task_items,
            task_type=task_type,
            teams=teams,
            thumbnail=thumbnail,
            transition=transition,
            users=users,
            version_id=version_id,
            view_ref=view_ref,
            workflow_info=workflow_info,
            workflowable_object_type=workflowable_object_type,
            workspace_id=workspace_id,
        )

        bt_task_info.additional_properties = d
        return bt_task_info

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
