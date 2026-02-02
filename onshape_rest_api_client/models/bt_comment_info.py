from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_comment_attachment_info import BTCommentAttachmentInfo
    from ..models.bt_user_summary_info import BTUserSummaryInfo
    from ..models.bt_view_data_info import BTViewDataInfo
    from ..models.coordinates_info import CoordinatesInfo


T = TypeVar("T", bound="BTCommentInfo")


@_attrs_define
class BTCommentInfo:
    """
    Attributes:
        annotation_id (str | Unset):
        annotation_type (int | Unset):
        assembly_features (list[str] | Unset):
        assigned_at (datetime.datetime | Unset):
        assignee (BTUserSummaryInfo | Unset):
        attachment (BTCommentAttachmentInfo | Unset):
        can_delete (bool | Unset):
        can_resolve_or_reopen (bool | Unset):
        coordinates (CoordinatesInfo | Unset):
        created_at (datetime.datetime | Unset):
        dimension_constraint_id (str | Unset):
        dimension_feature_id (str | Unset):
        dimension_parameter_id (str | Unset):
        dimension_part_query (str | Unset):
        document_id (str | Unset):
        element_feature (str | Unset):
        element_id (str | Unset):
        element_occurrences (list[str] | Unset):
        element_query (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        message (str | Unset):
        name (str | Unset): Name of the resource.
        object_id (str | Unset):
        object_type (int | Unset):
        parent_id (str | Unset):
        release_package_id (str | Unset):
        reopened_at (datetime.datetime | Unset):
        reopened_by (BTUserSummaryInfo | Unset):
        reply_count (int | Unset):
        resolved_at (datetime.datetime | Unset):
        resolved_by (BTUserSummaryInfo | Unset):
        state (int | Unset):
        thumbnail (BTCommentAttachmentInfo | Unset):
        top_level (bool | Unset):
        user (BTUserSummaryInfo | Unset):
        user_company (str | Unset):
        version_id (str | Unset):
        view_data (BTViewDataInfo | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        workspace_id (str | Unset):
    """

    annotation_id: str | Unset = UNSET
    annotation_type: int | Unset = UNSET
    assembly_features: list[str] | Unset = UNSET
    assigned_at: datetime.datetime | Unset = UNSET
    assignee: BTUserSummaryInfo | Unset = UNSET
    attachment: BTCommentAttachmentInfo | Unset = UNSET
    can_delete: bool | Unset = UNSET
    can_resolve_or_reopen: bool | Unset = UNSET
    coordinates: CoordinatesInfo | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    dimension_constraint_id: str | Unset = UNSET
    dimension_feature_id: str | Unset = UNSET
    dimension_parameter_id: str | Unset = UNSET
    dimension_part_query: str | Unset = UNSET
    document_id: str | Unset = UNSET
    element_feature: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_occurrences: list[str] | Unset = UNSET
    element_query: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    message: str | Unset = UNSET
    name: str | Unset = UNSET
    object_id: str | Unset = UNSET
    object_type: int | Unset = UNSET
    parent_id: str | Unset = UNSET
    release_package_id: str | Unset = UNSET
    reopened_at: datetime.datetime | Unset = UNSET
    reopened_by: BTUserSummaryInfo | Unset = UNSET
    reply_count: int | Unset = UNSET
    resolved_at: datetime.datetime | Unset = UNSET
    resolved_by: BTUserSummaryInfo | Unset = UNSET
    state: int | Unset = UNSET
    thumbnail: BTCommentAttachmentInfo | Unset = UNSET
    top_level: bool | Unset = UNSET
    user: BTUserSummaryInfo | Unset = UNSET
    user_company: str | Unset = UNSET
    version_id: str | Unset = UNSET
    view_data: BTViewDataInfo | Unset = UNSET
    view_ref: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotation_id = self.annotation_id

        annotation_type = self.annotation_type

        assembly_features: list[str] | Unset = UNSET
        if not isinstance(self.assembly_features, Unset):
            assembly_features = self.assembly_features

        assigned_at: str | Unset = UNSET
        if not isinstance(self.assigned_at, Unset):
            assigned_at = self.assigned_at.isoformat()

        assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        attachment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attachment, Unset):
            attachment = self.attachment.to_dict()

        can_delete = self.can_delete

        can_resolve_or_reopen = self.can_resolve_or_reopen

        coordinates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = self.coordinates.to_dict()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        dimension_constraint_id = self.dimension_constraint_id

        dimension_feature_id = self.dimension_feature_id

        dimension_parameter_id = self.dimension_parameter_id

        dimension_part_query = self.dimension_part_query

        document_id = self.document_id

        element_feature = self.element_feature

        element_id = self.element_id

        element_occurrences: list[str] | Unset = UNSET
        if not isinstance(self.element_occurrences, Unset):
            element_occurrences = self.element_occurrences

        element_query = self.element_query

        href = self.href

        id = self.id

        message = self.message

        name = self.name

        object_id = self.object_id

        object_type = self.object_type

        parent_id = self.parent_id

        release_package_id = self.release_package_id

        reopened_at: str | Unset = UNSET
        if not isinstance(self.reopened_at, Unset):
            reopened_at = self.reopened_at.isoformat()

        reopened_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reopened_by, Unset):
            reopened_by = self.reopened_by.to_dict()

        reply_count = self.reply_count

        resolved_at: str | Unset = UNSET
        if not isinstance(self.resolved_at, Unset):
            resolved_at = self.resolved_at.isoformat()

        resolved_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resolved_by, Unset):
            resolved_by = self.resolved_by.to_dict()

        state = self.state

        thumbnail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail, Unset):
            thumbnail = self.thumbnail.to_dict()

        top_level = self.top_level

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        user_company = self.user_company

        version_id = self.version_id

        view_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.view_data, Unset):
            view_data = self.view_data.to_dict()

        view_ref = self.view_ref

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotation_id is not UNSET:
            field_dict["annotationId"] = annotation_id
        if annotation_type is not UNSET:
            field_dict["annotationType"] = annotation_type
        if assembly_features is not UNSET:
            field_dict["assemblyFeatures"] = assembly_features
        if assigned_at is not UNSET:
            field_dict["assignedAt"] = assigned_at
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if attachment is not UNSET:
            field_dict["attachment"] = attachment
        if can_delete is not UNSET:
            field_dict["canDelete"] = can_delete
        if can_resolve_or_reopen is not UNSET:
            field_dict["canResolveOrReopen"] = can_resolve_or_reopen
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if dimension_constraint_id is not UNSET:
            field_dict["dimensionConstraintId"] = dimension_constraint_id
        if dimension_feature_id is not UNSET:
            field_dict["dimensionFeatureId"] = dimension_feature_id
        if dimension_parameter_id is not UNSET:
            field_dict["dimensionParameterId"] = dimension_parameter_id
        if dimension_part_query is not UNSET:
            field_dict["dimensionPartQuery"] = dimension_part_query
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_feature is not UNSET:
            field_dict["elementFeature"] = element_feature
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_occurrences is not UNSET:
            field_dict["elementOccurrences"] = element_occurrences
        if element_query is not UNSET:
            field_dict["elementQuery"] = element_query
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if name is not UNSET:
            field_dict["name"] = name
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if release_package_id is not UNSET:
            field_dict["releasePackageId"] = release_package_id
        if reopened_at is not UNSET:
            field_dict["reopenedAt"] = reopened_at
        if reopened_by is not UNSET:
            field_dict["reopenedBy"] = reopened_by
        if reply_count is not UNSET:
            field_dict["replyCount"] = reply_count
        if resolved_at is not UNSET:
            field_dict["resolvedAt"] = resolved_at
        if resolved_by is not UNSET:
            field_dict["resolvedBy"] = resolved_by
        if state is not UNSET:
            field_dict["state"] = state
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if top_level is not UNSET:
            field_dict["topLevel"] = top_level
        if user is not UNSET:
            field_dict["user"] = user
        if user_company is not UNSET:
            field_dict["userCompany"] = user_company
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if view_data is not UNSET:
            field_dict["viewData"] = view_data
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_comment_attachment_info import BTCommentAttachmentInfo
        from ..models.bt_user_summary_info import BTUserSummaryInfo
        from ..models.bt_view_data_info import BTViewDataInfo
        from ..models.coordinates_info import CoordinatesInfo

        d = dict(src_dict)
        annotation_id = d.pop("annotationId", UNSET)

        annotation_type = d.pop("annotationType", UNSET)

        assembly_features = cast(list[str], d.pop("assemblyFeatures", UNSET))

        _assigned_at = d.pop("assignedAt", UNSET)
        assigned_at: datetime.datetime | Unset
        if isinstance(_assigned_at, Unset):
            assigned_at = UNSET
        else:
            assigned_at = isoparse(_assigned_at)

        _assignee = d.pop("assignee", UNSET)
        assignee: BTUserSummaryInfo | Unset
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = BTUserSummaryInfo.from_dict(_assignee)

        _attachment = d.pop("attachment", UNSET)
        attachment: BTCommentAttachmentInfo | Unset
        if isinstance(_attachment, Unset):
            attachment = UNSET
        else:
            attachment = BTCommentAttachmentInfo.from_dict(_attachment)

        can_delete = d.pop("canDelete", UNSET)

        can_resolve_or_reopen = d.pop("canResolveOrReopen", UNSET)

        _coordinates = d.pop("coordinates", UNSET)
        coordinates: CoordinatesInfo | Unset
        if isinstance(_coordinates, Unset):
            coordinates = UNSET
        else:
            coordinates = CoordinatesInfo.from_dict(_coordinates)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        dimension_constraint_id = d.pop("dimensionConstraintId", UNSET)

        dimension_feature_id = d.pop("dimensionFeatureId", UNSET)

        dimension_parameter_id = d.pop("dimensionParameterId", UNSET)

        dimension_part_query = d.pop("dimensionPartQuery", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_feature = d.pop("elementFeature", UNSET)

        element_id = d.pop("elementId", UNSET)

        element_occurrences = cast(list[str], d.pop("elementOccurrences", UNSET))

        element_query = d.pop("elementQuery", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        name = d.pop("name", UNSET)

        object_id = d.pop("objectId", UNSET)

        object_type = d.pop("objectType", UNSET)

        parent_id = d.pop("parentId", UNSET)

        release_package_id = d.pop("releasePackageId", UNSET)

        _reopened_at = d.pop("reopenedAt", UNSET)
        reopened_at: datetime.datetime | Unset
        if isinstance(_reopened_at, Unset):
            reopened_at = UNSET
        else:
            reopened_at = isoparse(_reopened_at)

        _reopened_by = d.pop("reopenedBy", UNSET)
        reopened_by: BTUserSummaryInfo | Unset
        if isinstance(_reopened_by, Unset):
            reopened_by = UNSET
        else:
            reopened_by = BTUserSummaryInfo.from_dict(_reopened_by)

        reply_count = d.pop("replyCount", UNSET)

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

        state = d.pop("state", UNSET)

        _thumbnail = d.pop("thumbnail", UNSET)
        thumbnail: BTCommentAttachmentInfo | Unset
        if isinstance(_thumbnail, Unset):
            thumbnail = UNSET
        else:
            thumbnail = BTCommentAttachmentInfo.from_dict(_thumbnail)

        top_level = d.pop("topLevel", UNSET)

        _user = d.pop("user", UNSET)
        user: BTUserSummaryInfo | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = BTUserSummaryInfo.from_dict(_user)

        user_company = d.pop("userCompany", UNSET)

        version_id = d.pop("versionId", UNSET)

        _view_data = d.pop("viewData", UNSET)
        view_data: BTViewDataInfo | Unset
        if isinstance(_view_data, Unset):
            view_data = UNSET
        else:
            view_data = BTViewDataInfo.from_dict(_view_data)

        view_ref = d.pop("viewRef", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_comment_info = cls(
            annotation_id=annotation_id,
            annotation_type=annotation_type,
            assembly_features=assembly_features,
            assigned_at=assigned_at,
            assignee=assignee,
            attachment=attachment,
            can_delete=can_delete,
            can_resolve_or_reopen=can_resolve_or_reopen,
            coordinates=coordinates,
            created_at=created_at,
            dimension_constraint_id=dimension_constraint_id,
            dimension_feature_id=dimension_feature_id,
            dimension_parameter_id=dimension_parameter_id,
            dimension_part_query=dimension_part_query,
            document_id=document_id,
            element_feature=element_feature,
            element_id=element_id,
            element_occurrences=element_occurrences,
            element_query=element_query,
            href=href,
            id=id,
            message=message,
            name=name,
            object_id=object_id,
            object_type=object_type,
            parent_id=parent_id,
            release_package_id=release_package_id,
            reopened_at=reopened_at,
            reopened_by=reopened_by,
            reply_count=reply_count,
            resolved_at=resolved_at,
            resolved_by=resolved_by,
            state=state,
            thumbnail=thumbnail,
            top_level=top_level,
            user=user,
            user_company=user_company,
            version_id=version_id,
            view_data=view_data,
            view_ref=view_ref,
            workspace_id=workspace_id,
        )

        bt_comment_info.additional_properties = d
        return bt_comment_info

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
