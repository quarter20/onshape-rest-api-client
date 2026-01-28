from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_revision_approver_info import BTRevisionApproverInfo
    from ..models.bt_user_summary_info import BTUserSummaryInfo


T = TypeVar("T", bound="BTRevisionInfo")


@_attrs_define
class BTRevisionInfo:
    """Revision details.

    Attributes:
        approvers (list[BTRevisionApproverInfo] | Unset): The users who approved the release package that created this
            revision.
        auto_obsoletion_release_id (str | Unset):
        auto_obsoletion_release_name (str | Unset):
        can_change_type (bool | Unset): Whether the revision can change object type. Used in reuse part number flow.
            Default: False.
        can_export (bool | Unset):
        company_id (str | Unset): The company or enterprise ID that owns the resource.
        configuration (str | Unset):
        created_at (datetime.datetime | Unset):
        description (str | Unset): The Revision Description metadata property if revision is of a drawing.
        document_id (str | Unset): The document that contains the revision object.
        document_name (str | Unset): The name of the document that contains the revision object.
        document_state (int | Unset): The state of document containing this revision. Used in reuse part number flow
        element_id (str | Unset): The element that contains the revision object.
        element_type (int | Unset): The type of item Element Type. Must be one of: `-1`: Unknown, `0`: Part Studio, `1`:
            Assembly, `2`: Drawing. `4` : Blob, `8`: Variable Studio
        error_message (str | Unset):
        flat_part_insertable_id (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        insertable_id (str | Unset):
        is_obsolete (bool | Unset): Whether the revision has been obsoleted.
        is_rereleasable (bool | Unset): If true, the revision can be created again.
        is_translatable (bool | Unset):
        mime_type (str | Unset):
        name (str | Unset): Name of the resource.
        next_revision_id (str | Unset): The next revision if applicable. null for the latest revision.
        obsoletion_package_id (str | Unset): The OBSOLETION release package that obsoleted this revision if applicable.
        part_id (str | Unset):
        part_identity (str | Unset):
        part_number (str | Unset): The part number with which the object was revised.
        previous_revision_id (str | Unset): The previous revision if applicable. null for first revision.
        release_created_date (datetime.datetime | Unset):
        release_id (str | Unset): The release package that created this revision.
        release_name (str | Unset): The name of the release package that created this item.
        released_by (BTUserSummaryInfo | Unset):
        revision (str | Unset): The id of the revision.
        revision_rule_id (str | Unset):
        version_id (str | Unset): The version of the document that contains this revision.
        version_name (str | Unset): The name of the version of the document that contains this revision.
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    approvers: list[BTRevisionApproverInfo] | Unset = UNSET
    auto_obsoletion_release_id: str | Unset = UNSET
    auto_obsoletion_release_name: str | Unset = UNSET
    can_change_type: bool | Unset = False
    can_export: bool | Unset = UNSET
    company_id: str | Unset = UNSET
    configuration: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    document_id: str | Unset = UNSET
    document_name: str | Unset = UNSET
    document_state: int | Unset = UNSET
    element_id: str | Unset = UNSET
    element_type: int | Unset = UNSET
    error_message: str | Unset = UNSET
    flat_part_insertable_id: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    insertable_id: str | Unset = UNSET
    is_obsolete: bool | Unset = UNSET
    is_rereleasable: bool | Unset = UNSET
    is_translatable: bool | Unset = UNSET
    mime_type: str | Unset = UNSET
    name: str | Unset = UNSET
    next_revision_id: str | Unset = UNSET
    obsoletion_package_id: str | Unset = UNSET
    part_id: str | Unset = UNSET
    part_identity: str | Unset = UNSET
    part_number: str | Unset = UNSET
    previous_revision_id: str | Unset = UNSET
    release_created_date: datetime.datetime | Unset = UNSET
    release_id: str | Unset = UNSET
    release_name: str | Unset = UNSET
    released_by: BTUserSummaryInfo | Unset = UNSET
    revision: str | Unset = UNSET
    revision_rule_id: str | Unset = UNSET
    version_id: str | Unset = UNSET
    version_name: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approvers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.approvers, Unset):
            approvers = []
            for approvers_item_data in self.approvers:
                approvers_item = approvers_item_data.to_dict()
                approvers.append(approvers_item)

        auto_obsoletion_release_id = self.auto_obsoletion_release_id

        auto_obsoletion_release_name = self.auto_obsoletion_release_name

        can_change_type = self.can_change_type

        can_export = self.can_export

        company_id = self.company_id

        configuration = self.configuration

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        description = self.description

        document_id = self.document_id

        document_name = self.document_name

        document_state = self.document_state

        element_id = self.element_id

        element_type = self.element_type

        error_message = self.error_message

        flat_part_insertable_id = self.flat_part_insertable_id

        href = self.href

        id = self.id

        insertable_id = self.insertable_id

        is_obsolete = self.is_obsolete

        is_rereleasable = self.is_rereleasable

        is_translatable = self.is_translatable

        mime_type = self.mime_type

        name = self.name

        next_revision_id = self.next_revision_id

        obsoletion_package_id = self.obsoletion_package_id

        part_id = self.part_id

        part_identity = self.part_identity

        part_number = self.part_number

        previous_revision_id = self.previous_revision_id

        release_created_date: str | Unset = UNSET
        if not isinstance(self.release_created_date, Unset):
            release_created_date = self.release_created_date.isoformat()

        release_id = self.release_id

        release_name = self.release_name

        released_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.released_by, Unset):
            released_by = self.released_by.to_dict()

        revision = self.revision

        revision_rule_id = self.revision_rule_id

        version_id = self.version_id

        version_name = self.version_name

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approvers is not UNSET:
            field_dict["approvers"] = approvers
        if auto_obsoletion_release_id is not UNSET:
            field_dict["autoObsoletionReleaseId"] = auto_obsoletion_release_id
        if auto_obsoletion_release_name is not UNSET:
            field_dict["autoObsoletionReleaseName"] = auto_obsoletion_release_name
        if can_change_type is not UNSET:
            field_dict["canChangeType"] = can_change_type
        if can_export is not UNSET:
            field_dict["canExport"] = can_export
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if document_name is not UNSET:
            field_dict["documentName"] = document_name
        if document_state is not UNSET:
            field_dict["documentState"] = document_state
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_type is not UNSET:
            field_dict["elementType"] = element_type
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if flat_part_insertable_id is not UNSET:
            field_dict["flatPartInsertableId"] = flat_part_insertable_id
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if insertable_id is not UNSET:
            field_dict["insertableId"] = insertable_id
        if is_obsolete is not UNSET:
            field_dict["isObsolete"] = is_obsolete
        if is_rereleasable is not UNSET:
            field_dict["isRereleasable"] = is_rereleasable
        if is_translatable is not UNSET:
            field_dict["isTranslatable"] = is_translatable
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if name is not UNSET:
            field_dict["name"] = name
        if next_revision_id is not UNSET:
            field_dict["nextRevisionId"] = next_revision_id
        if obsoletion_package_id is not UNSET:
            field_dict["obsoletionPackageId"] = obsoletion_package_id
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_identity is not UNSET:
            field_dict["partIdentity"] = part_identity
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if previous_revision_id is not UNSET:
            field_dict["previousRevisionId"] = previous_revision_id
        if release_created_date is not UNSET:
            field_dict["releaseCreatedDate"] = release_created_date
        if release_id is not UNSET:
            field_dict["releaseId"] = release_id
        if release_name is not UNSET:
            field_dict["releaseName"] = release_name
        if released_by is not UNSET:
            field_dict["releasedBy"] = released_by
        if revision is not UNSET:
            field_dict["revision"] = revision
        if revision_rule_id is not UNSET:
            field_dict["revisionRuleId"] = revision_rule_id
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if version_name is not UNSET:
            field_dict["versionName"] = version_name
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_revision_approver_info import BTRevisionApproverInfo
        from ..models.bt_user_summary_info import BTUserSummaryInfo

        d = dict(src_dict)
        _approvers = d.pop("approvers", UNSET)
        approvers: list[BTRevisionApproverInfo] | Unset = UNSET
        if _approvers is not UNSET:
            approvers = []
            for approvers_item_data in _approvers:
                approvers_item = BTRevisionApproverInfo.from_dict(approvers_item_data)

                approvers.append(approvers_item)

        auto_obsoletion_release_id = d.pop("autoObsoletionReleaseId", UNSET)

        auto_obsoletion_release_name = d.pop("autoObsoletionReleaseName", UNSET)

        can_change_type = d.pop("canChangeType", UNSET)

        can_export = d.pop("canExport", UNSET)

        company_id = d.pop("companyId", UNSET)

        configuration = d.pop("configuration", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        description = d.pop("description", UNSET)

        document_id = d.pop("documentId", UNSET)

        document_name = d.pop("documentName", UNSET)

        document_state = d.pop("documentState", UNSET)

        element_id = d.pop("elementId", UNSET)

        element_type = d.pop("elementType", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        flat_part_insertable_id = d.pop("flatPartInsertableId", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        insertable_id = d.pop("insertableId", UNSET)

        is_obsolete = d.pop("isObsolete", UNSET)

        is_rereleasable = d.pop("isRereleasable", UNSET)

        is_translatable = d.pop("isTranslatable", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        name = d.pop("name", UNSET)

        next_revision_id = d.pop("nextRevisionId", UNSET)

        obsoletion_package_id = d.pop("obsoletionPackageId", UNSET)

        part_id = d.pop("partId", UNSET)

        part_identity = d.pop("partIdentity", UNSET)

        part_number = d.pop("partNumber", UNSET)

        previous_revision_id = d.pop("previousRevisionId", UNSET)

        _release_created_date = d.pop("releaseCreatedDate", UNSET)
        release_created_date: datetime.datetime | Unset
        if isinstance(_release_created_date, Unset):
            release_created_date = UNSET
        else:
            release_created_date = isoparse(_release_created_date)

        release_id = d.pop("releaseId", UNSET)

        release_name = d.pop("releaseName", UNSET)

        _released_by = d.pop("releasedBy", UNSET)
        released_by: BTUserSummaryInfo | Unset
        if isinstance(_released_by, Unset):
            released_by = UNSET
        else:
            released_by = BTUserSummaryInfo.from_dict(_released_by)

        revision = d.pop("revision", UNSET)

        revision_rule_id = d.pop("revisionRuleId", UNSET)

        version_id = d.pop("versionId", UNSET)

        version_name = d.pop("versionName", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_revision_info = cls(
            approvers=approvers,
            auto_obsoletion_release_id=auto_obsoletion_release_id,
            auto_obsoletion_release_name=auto_obsoletion_release_name,
            can_change_type=can_change_type,
            can_export=can_export,
            company_id=company_id,
            configuration=configuration,
            created_at=created_at,
            description=description,
            document_id=document_id,
            document_name=document_name,
            document_state=document_state,
            element_id=element_id,
            element_type=element_type,
            error_message=error_message,
            flat_part_insertable_id=flat_part_insertable_id,
            href=href,
            id=id,
            insertable_id=insertable_id,
            is_obsolete=is_obsolete,
            is_rereleasable=is_rereleasable,
            is_translatable=is_translatable,
            mime_type=mime_type,
            name=name,
            next_revision_id=next_revision_id,
            obsoletion_package_id=obsoletion_package_id,
            part_id=part_id,
            part_identity=part_identity,
            part_number=part_number,
            previous_revision_id=previous_revision_id,
            release_created_date=release_created_date,
            release_id=release_id,
            release_name=release_name,
            released_by=released_by,
            revision=revision,
            revision_rule_id=revision_rule_id,
            version_id=version_id,
            version_name=version_name,
            view_ref=view_ref,
        )

        bt_revision_info.additional_properties = d
        return bt_revision_info

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
