from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.bt_old_permission import BTOldPermission
from ..models.bt_version_graph_mode import BTVersionGraphMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_base_info import BTBaseInfo
    from ..models.bt_document_label_info import BTDocumentLabelInfo
    from ..models.bt_document_search_hit_info import BTDocumentSearchHitInfo
    from ..models.bt_element_library_summary_info import BTElementLibrarySummaryInfo
    from ..models.bt_owner_info import BTOwnerInfo
    from ..models.bt_thumbnail_info import BTThumbnailInfo
    from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo
    from ..models.bt_workspace_info import BTWorkspaceInfo


T = TypeVar("T", bound="BTDocumentSummarySearchInfo")


@_attrs_define
class BTDocumentSummarySearchInfo:
    """
    Attributes:
        json_type (str):
        can_move (bool | Unset):
        connection_name (str | Unset):
        connection_names (list[str] | Unset):
        created_at (datetime.datetime | Unset):
        created_by (BTUserBasicSummaryInfo | Unset):
        description (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        is_container (bool | Unset):
        is_enterprise_owned (bool | Unset):
        is_external_connection_resource (bool | Unset):
        is_mutable (bool | Unset):
        modified_at (datetime.datetime | Unset):
        modified_by (BTUserBasicSummaryInfo | Unset):
        name (str | Unset): Name of the resource.
        owner (BTOwnerInfo | Unset):
        parent_id (str | Unset):
        project_id (str | Unset):
        resource_type (str | Unset):
        tree_href (str | Unset):
        unparent_href (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        anonymous_access_allowed (bool | Unset):
        anonymous_allows_export (bool | Unset):
        can_unshare (bool | Unset):
        created_with_education_plan (bool | Unset):
        default_element_id (str | Unset):
        default_version_graph_mode (BTVersionGraphMode | Unset):
        default_version_graph_show_auto_versions (bool | Unset):
        default_version_graph_show_merges (bool | Unset):
        default_workspace (BTWorkspaceInfo | Unset):
        document_labels (list[BTDocumentLabelInfo] | Unset):
        document_type (int | Unset):
        element_library_summary_info (list[BTElementLibrarySummaryInfo] | Unset):
        force_export_rules (bool | Unset):
        has_release_revisionable_objects (bool | Unset):
        has_relevant_insertables (bool | Unset):
        is_orphaned (bool | Unset):
        is_using_managed_workflow (bool | Unset):
        liked_by_current_user (bool | Unset):
        likes (int | Unset):
        not_revision_managed (bool | Unset):
        notes (str | Unset):
        number_of_times_copied (int | Unset):
        number_of_times_referenced (int | Unset):
        permission (BTOldPermission | Unset):
        permission_set (list[str] | Unset):
        public (bool | Unset):
        published_version_id (str | Unset):
        recent_version (BTBaseInfo | Unset):
        sequence (str | Unset):
        support_team_user_and_shared (bool | Unset):
        tags (list[str] | Unset):
        thumbnail (BTThumbnailInfo | Unset):
        total_workspaces_scheduled_for_update (int | Unset):
        total_workspaces_updating (int | Unset):
        trash (bool | Unset):
        trashed_at (datetime.datetime | Unset):
        user_account_limits_breached (bool | Unset):
        search_hits (list[BTDocumentSearchHitInfo] | Unset):
    """

    json_type: str
    can_move: bool | Unset = UNSET
    connection_name: str | Unset = UNSET
    connection_names: list[str] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by: BTUserBasicSummaryInfo | Unset = UNSET
    description: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    is_container: bool | Unset = UNSET
    is_enterprise_owned: bool | Unset = UNSET
    is_external_connection_resource: bool | Unset = UNSET
    is_mutable: bool | Unset = UNSET
    modified_at: datetime.datetime | Unset = UNSET
    modified_by: BTUserBasicSummaryInfo | Unset = UNSET
    name: str | Unset = UNSET
    owner: BTOwnerInfo | Unset = UNSET
    parent_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    resource_type: str | Unset = UNSET
    tree_href: str | Unset = UNSET
    unparent_href: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    anonymous_access_allowed: bool | Unset = UNSET
    anonymous_allows_export: bool | Unset = UNSET
    can_unshare: bool | Unset = UNSET
    created_with_education_plan: bool | Unset = UNSET
    default_element_id: str | Unset = UNSET
    default_version_graph_mode: BTVersionGraphMode | Unset = UNSET
    default_version_graph_show_auto_versions: bool | Unset = UNSET
    default_version_graph_show_merges: bool | Unset = UNSET
    default_workspace: BTWorkspaceInfo | Unset = UNSET
    document_labels: list[BTDocumentLabelInfo] | Unset = UNSET
    document_type: int | Unset = UNSET
    element_library_summary_info: list[BTElementLibrarySummaryInfo] | Unset = UNSET
    force_export_rules: bool | Unset = UNSET
    has_release_revisionable_objects: bool | Unset = UNSET
    has_relevant_insertables: bool | Unset = UNSET
    is_orphaned: bool | Unset = UNSET
    is_using_managed_workflow: bool | Unset = UNSET
    liked_by_current_user: bool | Unset = UNSET
    likes: int | Unset = UNSET
    not_revision_managed: bool | Unset = UNSET
    notes: str | Unset = UNSET
    number_of_times_copied: int | Unset = UNSET
    number_of_times_referenced: int | Unset = UNSET
    permission: BTOldPermission | Unset = UNSET
    permission_set: list[str] | Unset = UNSET
    public: bool | Unset = UNSET
    published_version_id: str | Unset = UNSET
    recent_version: BTBaseInfo | Unset = UNSET
    sequence: str | Unset = UNSET
    support_team_user_and_shared: bool | Unset = UNSET
    tags: list[str] | Unset = UNSET
    thumbnail: BTThumbnailInfo | Unset = UNSET
    total_workspaces_scheduled_for_update: int | Unset = UNSET
    total_workspaces_updating: int | Unset = UNSET
    trash: bool | Unset = UNSET
    trashed_at: datetime.datetime | Unset = UNSET
    user_account_limits_breached: bool | Unset = UNSET
    search_hits: list[BTDocumentSearchHitInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        json_type = self.json_type

        can_move = self.can_move

        connection_name = self.connection_name

        connection_names: list[str] | Unset = UNSET
        if not isinstance(self.connection_names, Unset):
            connection_names = self.connection_names

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        description = self.description

        href = self.href

        id = self.id

        is_container = self.is_container

        is_enterprise_owned = self.is_enterprise_owned

        is_external_connection_resource = self.is_external_connection_resource

        is_mutable = self.is_mutable

        modified_at: str | Unset = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        modified_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.modified_by, Unset):
            modified_by = self.modified_by.to_dict()

        name = self.name

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        parent_id = self.parent_id

        project_id = self.project_id

        resource_type = self.resource_type

        tree_href = self.tree_href

        unparent_href = self.unparent_href

        view_ref = self.view_ref

        anonymous_access_allowed = self.anonymous_access_allowed

        anonymous_allows_export = self.anonymous_allows_export

        can_unshare = self.can_unshare

        created_with_education_plan = self.created_with_education_plan

        default_element_id = self.default_element_id

        default_version_graph_mode: str | Unset = UNSET
        if not isinstance(self.default_version_graph_mode, Unset):
            default_version_graph_mode = self.default_version_graph_mode.value

        default_version_graph_show_auto_versions = self.default_version_graph_show_auto_versions

        default_version_graph_show_merges = self.default_version_graph_show_merges

        default_workspace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_workspace, Unset):
            default_workspace = self.default_workspace.to_dict()

        document_labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.document_labels, Unset):
            document_labels = []
            for document_labels_item_data in self.document_labels:
                document_labels_item = document_labels_item_data.to_dict()
                document_labels.append(document_labels_item)

        document_type = self.document_type

        element_library_summary_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.element_library_summary_info, Unset):
            element_library_summary_info = []
            for element_library_summary_info_item_data in self.element_library_summary_info:
                element_library_summary_info_item = element_library_summary_info_item_data.to_dict()
                element_library_summary_info.append(element_library_summary_info_item)

        force_export_rules = self.force_export_rules

        has_release_revisionable_objects = self.has_release_revisionable_objects

        has_relevant_insertables = self.has_relevant_insertables

        is_orphaned = self.is_orphaned

        is_using_managed_workflow = self.is_using_managed_workflow

        liked_by_current_user = self.liked_by_current_user

        likes = self.likes

        not_revision_managed = self.not_revision_managed

        notes = self.notes

        number_of_times_copied = self.number_of_times_copied

        number_of_times_referenced = self.number_of_times_referenced

        permission: str | Unset = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        permission_set: list[str] | Unset = UNSET
        if not isinstance(self.permission_set, Unset):
            permission_set = self.permission_set

        public = self.public

        published_version_id = self.published_version_id

        recent_version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recent_version, Unset):
            recent_version = self.recent_version.to_dict()

        sequence = self.sequence

        support_team_user_and_shared = self.support_team_user_and_shared

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        thumbnail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail, Unset):
            thumbnail = self.thumbnail.to_dict()

        total_workspaces_scheduled_for_update = self.total_workspaces_scheduled_for_update

        total_workspaces_updating = self.total_workspaces_updating

        trash = self.trash

        trashed_at: str | Unset = UNSET
        if not isinstance(self.trashed_at, Unset):
            trashed_at = self.trashed_at.isoformat()

        user_account_limits_breached = self.user_account_limits_breached

        search_hits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.search_hits, Unset):
            search_hits = []
            for search_hits_item_data in self.search_hits:
                search_hits_item = search_hits_item_data.to_dict()
                search_hits.append(search_hits_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jsonType": json_type,
            }
        )
        if can_move is not UNSET:
            field_dict["canMove"] = can_move
        if connection_name is not UNSET:
            field_dict["connectionName"] = connection_name
        if connection_names is not UNSET:
            field_dict["connectionNames"] = connection_names
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if is_container is not UNSET:
            field_dict["isContainer"] = is_container
        if is_enterprise_owned is not UNSET:
            field_dict["isEnterpriseOwned"] = is_enterprise_owned
        if is_external_connection_resource is not UNSET:
            field_dict["isExternalConnectionResource"] = is_external_connection_resource
        if is_mutable is not UNSET:
            field_dict["isMutable"] = is_mutable
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if name is not UNSET:
            field_dict["name"] = name
        if owner is not UNSET:
            field_dict["owner"] = owner
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if tree_href is not UNSET:
            field_dict["treeHref"] = tree_href
        if unparent_href is not UNSET:
            field_dict["unparentHref"] = unparent_href
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if anonymous_access_allowed is not UNSET:
            field_dict["anonymousAccessAllowed"] = anonymous_access_allowed
        if anonymous_allows_export is not UNSET:
            field_dict["anonymousAllowsExport"] = anonymous_allows_export
        if can_unshare is not UNSET:
            field_dict["canUnshare"] = can_unshare
        if created_with_education_plan is not UNSET:
            field_dict["createdWithEducationPlan"] = created_with_education_plan
        if default_element_id is not UNSET:
            field_dict["defaultElementId"] = default_element_id
        if default_version_graph_mode is not UNSET:
            field_dict["defaultVersionGraphMode"] = default_version_graph_mode
        if default_version_graph_show_auto_versions is not UNSET:
            field_dict["defaultVersionGraphShowAutoVersions"] = default_version_graph_show_auto_versions
        if default_version_graph_show_merges is not UNSET:
            field_dict["defaultVersionGraphShowMerges"] = default_version_graph_show_merges
        if default_workspace is not UNSET:
            field_dict["defaultWorkspace"] = default_workspace
        if document_labels is not UNSET:
            field_dict["documentLabels"] = document_labels
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if element_library_summary_info is not UNSET:
            field_dict["elementLibrarySummaryInfo"] = element_library_summary_info
        if force_export_rules is not UNSET:
            field_dict["forceExportRules"] = force_export_rules
        if has_release_revisionable_objects is not UNSET:
            field_dict["hasReleaseRevisionableObjects"] = has_release_revisionable_objects
        if has_relevant_insertables is not UNSET:
            field_dict["hasRelevantInsertables"] = has_relevant_insertables
        if is_orphaned is not UNSET:
            field_dict["isOrphaned"] = is_orphaned
        if is_using_managed_workflow is not UNSET:
            field_dict["isUsingManagedWorkflow"] = is_using_managed_workflow
        if liked_by_current_user is not UNSET:
            field_dict["likedByCurrentUser"] = liked_by_current_user
        if likes is not UNSET:
            field_dict["likes"] = likes
        if not_revision_managed is not UNSET:
            field_dict["notRevisionManaged"] = not_revision_managed
        if notes is not UNSET:
            field_dict["notes"] = notes
        if number_of_times_copied is not UNSET:
            field_dict["numberOfTimesCopied"] = number_of_times_copied
        if number_of_times_referenced is not UNSET:
            field_dict["numberOfTimesReferenced"] = number_of_times_referenced
        if permission is not UNSET:
            field_dict["permission"] = permission
        if permission_set is not UNSET:
            field_dict["permissionSet"] = permission_set
        if public is not UNSET:
            field_dict["public"] = public
        if published_version_id is not UNSET:
            field_dict["publishedVersionId"] = published_version_id
        if recent_version is not UNSET:
            field_dict["recentVersion"] = recent_version
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if support_team_user_and_shared is not UNSET:
            field_dict["supportTeamUserAndShared"] = support_team_user_and_shared
        if tags is not UNSET:
            field_dict["tags"] = tags
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if total_workspaces_scheduled_for_update is not UNSET:
            field_dict["totalWorkspacesScheduledForUpdate"] = total_workspaces_scheduled_for_update
        if total_workspaces_updating is not UNSET:
            field_dict["totalWorkspacesUpdating"] = total_workspaces_updating
        if trash is not UNSET:
            field_dict["trash"] = trash
        if trashed_at is not UNSET:
            field_dict["trashedAt"] = trashed_at
        if user_account_limits_breached is not UNSET:
            field_dict["userAccountLimitsBreached"] = user_account_limits_breached
        if search_hits is not UNSET:
            field_dict["searchHits"] = search_hits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_base_info import BTBaseInfo
        from ..models.bt_document_label_info import BTDocumentLabelInfo
        from ..models.bt_document_search_hit_info import BTDocumentSearchHitInfo
        from ..models.bt_element_library_summary_info import BTElementLibrarySummaryInfo
        from ..models.bt_owner_info import BTOwnerInfo
        from ..models.bt_thumbnail_info import BTThumbnailInfo
        from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo
        from ..models.bt_workspace_info import BTWorkspaceInfo

        d = dict(src_dict)
        json_type = d.pop("jsonType")

        can_move = d.pop("canMove", UNSET)

        connection_name = d.pop("connectionName", UNSET)

        connection_names = cast(list[str], d.pop("connectionNames", UNSET))

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

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        is_container = d.pop("isContainer", UNSET)

        is_enterprise_owned = d.pop("isEnterpriseOwned", UNSET)

        is_external_connection_resource = d.pop("isExternalConnectionResource", UNSET)

        is_mutable = d.pop("isMutable", UNSET)

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

        _owner = d.pop("owner", UNSET)
        owner: BTOwnerInfo | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = BTOwnerInfo.from_dict(_owner)

        parent_id = d.pop("parentId", UNSET)

        project_id = d.pop("projectId", UNSET)

        resource_type = d.pop("resourceType", UNSET)

        tree_href = d.pop("treeHref", UNSET)

        unparent_href = d.pop("unparentHref", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        anonymous_access_allowed = d.pop("anonymousAccessAllowed", UNSET)

        anonymous_allows_export = d.pop("anonymousAllowsExport", UNSET)

        can_unshare = d.pop("canUnshare", UNSET)

        created_with_education_plan = d.pop("createdWithEducationPlan", UNSET)

        default_element_id = d.pop("defaultElementId", UNSET)

        _default_version_graph_mode = d.pop("defaultVersionGraphMode", UNSET)
        default_version_graph_mode: BTVersionGraphMode | Unset
        if isinstance(_default_version_graph_mode, Unset):
            default_version_graph_mode = UNSET
        else:
            default_version_graph_mode = BTVersionGraphMode(_default_version_graph_mode)

        default_version_graph_show_auto_versions = d.pop("defaultVersionGraphShowAutoVersions", UNSET)

        default_version_graph_show_merges = d.pop("defaultVersionGraphShowMerges", UNSET)

        _default_workspace = d.pop("defaultWorkspace", UNSET)
        default_workspace: BTWorkspaceInfo | Unset
        if isinstance(_default_workspace, Unset):
            default_workspace = UNSET
        else:
            default_workspace = BTWorkspaceInfo.from_dict(_default_workspace)

        _document_labels = d.pop("documentLabels", UNSET)
        document_labels: list[BTDocumentLabelInfo] | Unset = UNSET
        if _document_labels is not UNSET:
            document_labels = []
            for document_labels_item_data in _document_labels:
                document_labels_item = BTDocumentLabelInfo.from_dict(document_labels_item_data)

                document_labels.append(document_labels_item)

        document_type = d.pop("documentType", UNSET)

        _element_library_summary_info = d.pop("elementLibrarySummaryInfo", UNSET)
        element_library_summary_info: list[BTElementLibrarySummaryInfo] | Unset = UNSET
        if _element_library_summary_info is not UNSET:
            element_library_summary_info = []
            for element_library_summary_info_item_data in _element_library_summary_info:
                element_library_summary_info_item = BTElementLibrarySummaryInfo.from_dict(
                    element_library_summary_info_item_data
                )

                element_library_summary_info.append(element_library_summary_info_item)

        force_export_rules = d.pop("forceExportRules", UNSET)

        has_release_revisionable_objects = d.pop("hasReleaseRevisionableObjects", UNSET)

        has_relevant_insertables = d.pop("hasRelevantInsertables", UNSET)

        is_orphaned = d.pop("isOrphaned", UNSET)

        is_using_managed_workflow = d.pop("isUsingManagedWorkflow", UNSET)

        liked_by_current_user = d.pop("likedByCurrentUser", UNSET)

        likes = d.pop("likes", UNSET)

        not_revision_managed = d.pop("notRevisionManaged", UNSET)

        notes = d.pop("notes", UNSET)

        number_of_times_copied = d.pop("numberOfTimesCopied", UNSET)

        number_of_times_referenced = d.pop("numberOfTimesReferenced", UNSET)

        _permission = d.pop("permission", UNSET)
        permission: BTOldPermission | Unset
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = BTOldPermission(_permission)

        permission_set = cast(list[str], d.pop("permissionSet", UNSET))

        public = d.pop("public", UNSET)

        published_version_id = d.pop("publishedVersionId", UNSET)

        _recent_version = d.pop("recentVersion", UNSET)
        recent_version: BTBaseInfo | Unset
        if isinstance(_recent_version, Unset):
            recent_version = UNSET
        else:
            recent_version = BTBaseInfo.from_dict(_recent_version)

        sequence = d.pop("sequence", UNSET)

        support_team_user_and_shared = d.pop("supportTeamUserAndShared", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        _thumbnail = d.pop("thumbnail", UNSET)
        thumbnail: BTThumbnailInfo | Unset
        if isinstance(_thumbnail, Unset):
            thumbnail = UNSET
        else:
            thumbnail = BTThumbnailInfo.from_dict(_thumbnail)

        total_workspaces_scheduled_for_update = d.pop("totalWorkspacesScheduledForUpdate", UNSET)

        total_workspaces_updating = d.pop("totalWorkspacesUpdating", UNSET)

        trash = d.pop("trash", UNSET)

        _trashed_at = d.pop("trashedAt", UNSET)
        trashed_at: datetime.datetime | Unset
        if isinstance(_trashed_at, Unset):
            trashed_at = UNSET
        else:
            trashed_at = isoparse(_trashed_at)

        user_account_limits_breached = d.pop("userAccountLimitsBreached", UNSET)

        _search_hits = d.pop("searchHits", UNSET)
        search_hits: list[BTDocumentSearchHitInfo] | Unset = UNSET
        if _search_hits is not UNSET:
            search_hits = []
            for search_hits_item_data in _search_hits:
                search_hits_item = BTDocumentSearchHitInfo.from_dict(search_hits_item_data)

                search_hits.append(search_hits_item)

        bt_document_summary_search_info = cls(
            json_type=json_type,
            can_move=can_move,
            connection_name=connection_name,
            connection_names=connection_names,
            created_at=created_at,
            created_by=created_by,
            description=description,
            href=href,
            id=id,
            is_container=is_container,
            is_enterprise_owned=is_enterprise_owned,
            is_external_connection_resource=is_external_connection_resource,
            is_mutable=is_mutable,
            modified_at=modified_at,
            modified_by=modified_by,
            name=name,
            owner=owner,
            parent_id=parent_id,
            project_id=project_id,
            resource_type=resource_type,
            tree_href=tree_href,
            unparent_href=unparent_href,
            view_ref=view_ref,
            anonymous_access_allowed=anonymous_access_allowed,
            anonymous_allows_export=anonymous_allows_export,
            can_unshare=can_unshare,
            created_with_education_plan=created_with_education_plan,
            default_element_id=default_element_id,
            default_version_graph_mode=default_version_graph_mode,
            default_version_graph_show_auto_versions=default_version_graph_show_auto_versions,
            default_version_graph_show_merges=default_version_graph_show_merges,
            default_workspace=default_workspace,
            document_labels=document_labels,
            document_type=document_type,
            element_library_summary_info=element_library_summary_info,
            force_export_rules=force_export_rules,
            has_release_revisionable_objects=has_release_revisionable_objects,
            has_relevant_insertables=has_relevant_insertables,
            is_orphaned=is_orphaned,
            is_using_managed_workflow=is_using_managed_workflow,
            liked_by_current_user=liked_by_current_user,
            likes=likes,
            not_revision_managed=not_revision_managed,
            notes=notes,
            number_of_times_copied=number_of_times_copied,
            number_of_times_referenced=number_of_times_referenced,
            permission=permission,
            permission_set=permission_set,
            public=public,
            published_version_id=published_version_id,
            recent_version=recent_version,
            sequence=sequence,
            support_team_user_and_shared=support_team_user_and_shared,
            tags=tags,
            thumbnail=thumbnail,
            total_workspaces_scheduled_for_update=total_workspaces_scheduled_for_update,
            total_workspaces_updating=total_workspaces_updating,
            trash=trash,
            trashed_at=trashed_at,
            user_account_limits_breached=user_account_limits_breached,
            search_hits=search_hits,
        )

        bt_document_summary_search_info.additional_properties = d
        return bt_document_summary_search_info

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
