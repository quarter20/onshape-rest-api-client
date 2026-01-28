from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_active_workflow_info_os_category_id_to_arena_number_format_id import (
        BTActiveWorkflowInfoOsCategoryIdToArenaNumberFormatId,
    )
    from ..models.bt_active_workflow_type_info import BTActiveWorkflowTypeInfo
    from ..models.bt_published_workflow_info import BTPublishedWorkflowInfo


T = TypeVar("T", bound="BTActiveWorkflowInfo")


@_attrs_define
class BTActiveWorkflowInfo:
    """
    Attributes:
        allow_release_items_from_other_documents (bool | Unset):
        can_current_user_create_releases (bool | Unset):
        can_current_user_edit_standard_content (bool | Unset):
        can_current_user_manage_workflows (bool | Unset):
        can_current_user_see_arena_item_link (bool | Unset): Deprecated, use canCurrentUserSeePLMItemLink
        can_current_user_see_plm_item_link (bool | Unset):
        can_current_user_sync_bom_to_arena (bool | Unset): Deprecated, use canCurrentUserSyncBomToPLM
        can_current_user_sync_bom_to_plm (bool | Unset):
        can_current_user_sync_drawing_to_plm (bool | Unset):
        can_current_user_sync_revisions_to_arena (bool | Unset): Deprecated, use canCurrentUserSyncRevisionsToPLM
        can_current_user_sync_revisions_to_plm (bool | Unset):
        can_current_user_sync_standard_content_to_arena (bool | Unset): Deprecated, use
            canCurrentUserSyncStandardContentToPLM
        can_current_user_sync_standard_content_to_plm (bool | Unset):
        can_current_user_sync_to_arena (bool | Unset): Deprecated, use canCurrentUserSyncToPLM
        can_current_user_sync_to_plm (bool | Unset):
        company_id (str | Unset):
        document_id (str | Unset):
        drawing_can_duplicate_part_number (bool | Unset):
        enabled_active_multiple_workflows (bool | Unset): Deprecated, can be determined by checking if the length of
            releaseWorkflowInfo.pickableWorkflows > 1
        has_inactive_custom_workflows (bool | Unset): Deprecated, use hasInactiveCustomWorkflows field on the
            workflowInfo object
        is_current_user_logged_into_to_plm (bool | Unset): Whether user has even authenticated against PLM. Used to
            trigger OAuth handshake
        obsoletion_workflow (BTPublishedWorkflowInfo | Unset): Captures information about a published workflow
        obsoletion_workflow_id (str | Unset): Deprecated, use obsoletionWorkflowInfo.workflow.id instead
        obsoletion_workflow_info (BTActiveWorkflowTypeInfo | Unset):
        os_category_id_to_arena_number_format_id (BTActiveWorkflowInfoOsCategoryIdToArenaNumberFormatId | Unset):
            Deprecated, no current alternative
        p_lm_integration_type (int | Unset):
        p_lm_name (str | Unset):
        part_numbering_scheme_id (str | Unset):
        pickable_workflows (list[BTPublishedWorkflowInfo] | Unset): Deprecated, use the pickableWorkflows field on the
            workflowInfo object
        release_workflow (BTPublishedWorkflowInfo | Unset): Captures information about a published workflow
        release_workflow_id (str | Unset): Deprecated, use releaseWorkflowInfo.workflow.id instead
        release_workflow_info (BTActiveWorkflowTypeInfo | Unset):
        releaseable_applications (list[str] | Unset): Deprecated, no current alternative
        standard_content_numbering_scheme_id (str | Unset):
        standard_content_using_auto_numbering (bool | Unset):
        standard_content_using_third_party_part_numbering (bool | Unset):
        task_workflow (BTPublishedWorkflowInfo | Unset): Captures information about a published workflow
        task_workflow_info (BTActiveWorkflowTypeInfo | Unset):
        using_auto_part_numbering (bool | Unset):
        using_managed_workflow (bool | Unset):
        using_third_party_part_numbering (bool | Unset):
    """

    allow_release_items_from_other_documents: bool | Unset = UNSET
    can_current_user_create_releases: bool | Unset = UNSET
    can_current_user_edit_standard_content: bool | Unset = UNSET
    can_current_user_manage_workflows: bool | Unset = UNSET
    can_current_user_see_arena_item_link: bool | Unset = UNSET
    can_current_user_see_plm_item_link: bool | Unset = UNSET
    can_current_user_sync_bom_to_arena: bool | Unset = UNSET
    can_current_user_sync_bom_to_plm: bool | Unset = UNSET
    can_current_user_sync_drawing_to_plm: bool | Unset = UNSET
    can_current_user_sync_revisions_to_arena: bool | Unset = UNSET
    can_current_user_sync_revisions_to_plm: bool | Unset = UNSET
    can_current_user_sync_standard_content_to_arena: bool | Unset = UNSET
    can_current_user_sync_standard_content_to_plm: bool | Unset = UNSET
    can_current_user_sync_to_arena: bool | Unset = UNSET
    can_current_user_sync_to_plm: bool | Unset = UNSET
    company_id: str | Unset = UNSET
    document_id: str | Unset = UNSET
    drawing_can_duplicate_part_number: bool | Unset = UNSET
    enabled_active_multiple_workflows: bool | Unset = UNSET
    has_inactive_custom_workflows: bool | Unset = UNSET
    is_current_user_logged_into_to_plm: bool | Unset = UNSET
    obsoletion_workflow: BTPublishedWorkflowInfo | Unset = UNSET
    obsoletion_workflow_id: str | Unset = UNSET
    obsoletion_workflow_info: BTActiveWorkflowTypeInfo | Unset = UNSET
    os_category_id_to_arena_number_format_id: BTActiveWorkflowInfoOsCategoryIdToArenaNumberFormatId | Unset = UNSET
    p_lm_integration_type: int | Unset = UNSET
    p_lm_name: str | Unset = UNSET
    part_numbering_scheme_id: str | Unset = UNSET
    pickable_workflows: list[BTPublishedWorkflowInfo] | Unset = UNSET
    release_workflow: BTPublishedWorkflowInfo | Unset = UNSET
    release_workflow_id: str | Unset = UNSET
    release_workflow_info: BTActiveWorkflowTypeInfo | Unset = UNSET
    releaseable_applications: list[str] | Unset = UNSET
    standard_content_numbering_scheme_id: str | Unset = UNSET
    standard_content_using_auto_numbering: bool | Unset = UNSET
    standard_content_using_third_party_part_numbering: bool | Unset = UNSET
    task_workflow: BTPublishedWorkflowInfo | Unset = UNSET
    task_workflow_info: BTActiveWorkflowTypeInfo | Unset = UNSET
    using_auto_part_numbering: bool | Unset = UNSET
    using_managed_workflow: bool | Unset = UNSET
    using_third_party_part_numbering: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_release_items_from_other_documents = self.allow_release_items_from_other_documents

        can_current_user_create_releases = self.can_current_user_create_releases

        can_current_user_edit_standard_content = self.can_current_user_edit_standard_content

        can_current_user_manage_workflows = self.can_current_user_manage_workflows

        can_current_user_see_arena_item_link = self.can_current_user_see_arena_item_link

        can_current_user_see_plm_item_link = self.can_current_user_see_plm_item_link

        can_current_user_sync_bom_to_arena = self.can_current_user_sync_bom_to_arena

        can_current_user_sync_bom_to_plm = self.can_current_user_sync_bom_to_plm

        can_current_user_sync_drawing_to_plm = self.can_current_user_sync_drawing_to_plm

        can_current_user_sync_revisions_to_arena = self.can_current_user_sync_revisions_to_arena

        can_current_user_sync_revisions_to_plm = self.can_current_user_sync_revisions_to_plm

        can_current_user_sync_standard_content_to_arena = self.can_current_user_sync_standard_content_to_arena

        can_current_user_sync_standard_content_to_plm = self.can_current_user_sync_standard_content_to_plm

        can_current_user_sync_to_arena = self.can_current_user_sync_to_arena

        can_current_user_sync_to_plm = self.can_current_user_sync_to_plm

        company_id = self.company_id

        document_id = self.document_id

        drawing_can_duplicate_part_number = self.drawing_can_duplicate_part_number

        enabled_active_multiple_workflows = self.enabled_active_multiple_workflows

        has_inactive_custom_workflows = self.has_inactive_custom_workflows

        is_current_user_logged_into_to_plm = self.is_current_user_logged_into_to_plm

        obsoletion_workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.obsoletion_workflow, Unset):
            obsoletion_workflow = self.obsoletion_workflow.to_dict()

        obsoletion_workflow_id = self.obsoletion_workflow_id

        obsoletion_workflow_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.obsoletion_workflow_info, Unset):
            obsoletion_workflow_info = self.obsoletion_workflow_info.to_dict()

        os_category_id_to_arena_number_format_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.os_category_id_to_arena_number_format_id, Unset):
            os_category_id_to_arena_number_format_id = self.os_category_id_to_arena_number_format_id.to_dict()

        p_lm_integration_type = self.p_lm_integration_type

        p_lm_name = self.p_lm_name

        part_numbering_scheme_id = self.part_numbering_scheme_id

        pickable_workflows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pickable_workflows, Unset):
            pickable_workflows = []
            for pickable_workflows_item_data in self.pickable_workflows:
                pickable_workflows_item = pickable_workflows_item_data.to_dict()
                pickable_workflows.append(pickable_workflows_item)

        release_workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.release_workflow, Unset):
            release_workflow = self.release_workflow.to_dict()

        release_workflow_id = self.release_workflow_id

        release_workflow_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.release_workflow_info, Unset):
            release_workflow_info = self.release_workflow_info.to_dict()

        releaseable_applications: list[str] | Unset = UNSET
        if not isinstance(self.releaseable_applications, Unset):
            releaseable_applications = self.releaseable_applications

        standard_content_numbering_scheme_id = self.standard_content_numbering_scheme_id

        standard_content_using_auto_numbering = self.standard_content_using_auto_numbering

        standard_content_using_third_party_part_numbering = self.standard_content_using_third_party_part_numbering

        task_workflow: dict[str, Any] | Unset = UNSET
        if not isinstance(self.task_workflow, Unset):
            task_workflow = self.task_workflow.to_dict()

        task_workflow_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.task_workflow_info, Unset):
            task_workflow_info = self.task_workflow_info.to_dict()

        using_auto_part_numbering = self.using_auto_part_numbering

        using_managed_workflow = self.using_managed_workflow

        using_third_party_part_numbering = self.using_third_party_part_numbering

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_release_items_from_other_documents is not UNSET:
            field_dict["allowReleaseItemsFromOtherDocuments"] = allow_release_items_from_other_documents
        if can_current_user_create_releases is not UNSET:
            field_dict["canCurrentUserCreateReleases"] = can_current_user_create_releases
        if can_current_user_edit_standard_content is not UNSET:
            field_dict["canCurrentUserEditStandardContent"] = can_current_user_edit_standard_content
        if can_current_user_manage_workflows is not UNSET:
            field_dict["canCurrentUserManageWorkflows"] = can_current_user_manage_workflows
        if can_current_user_see_arena_item_link is not UNSET:
            field_dict["canCurrentUserSeeArenaItemLink"] = can_current_user_see_arena_item_link
        if can_current_user_see_plm_item_link is not UNSET:
            field_dict["canCurrentUserSeePLMItemLink"] = can_current_user_see_plm_item_link
        if can_current_user_sync_bom_to_arena is not UNSET:
            field_dict["canCurrentUserSyncBomToArena"] = can_current_user_sync_bom_to_arena
        if can_current_user_sync_bom_to_plm is not UNSET:
            field_dict["canCurrentUserSyncBomToPLM"] = can_current_user_sync_bom_to_plm
        if can_current_user_sync_drawing_to_plm is not UNSET:
            field_dict["canCurrentUserSyncDrawingToPLM"] = can_current_user_sync_drawing_to_plm
        if can_current_user_sync_revisions_to_arena is not UNSET:
            field_dict["canCurrentUserSyncRevisionsToArena"] = can_current_user_sync_revisions_to_arena
        if can_current_user_sync_revisions_to_plm is not UNSET:
            field_dict["canCurrentUserSyncRevisionsToPLM"] = can_current_user_sync_revisions_to_plm
        if can_current_user_sync_standard_content_to_arena is not UNSET:
            field_dict["canCurrentUserSyncStandardContentToArena"] = can_current_user_sync_standard_content_to_arena
        if can_current_user_sync_standard_content_to_plm is not UNSET:
            field_dict["canCurrentUserSyncStandardContentToPLM"] = can_current_user_sync_standard_content_to_plm
        if can_current_user_sync_to_arena is not UNSET:
            field_dict["canCurrentUserSyncToArena"] = can_current_user_sync_to_arena
        if can_current_user_sync_to_plm is not UNSET:
            field_dict["canCurrentUserSyncToPLM"] = can_current_user_sync_to_plm
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if drawing_can_duplicate_part_number is not UNSET:
            field_dict["drawingCanDuplicatePartNumber"] = drawing_can_duplicate_part_number
        if enabled_active_multiple_workflows is not UNSET:
            field_dict["enabledActiveMultipleWorkflows"] = enabled_active_multiple_workflows
        if has_inactive_custom_workflows is not UNSET:
            field_dict["hasInactiveCustomWorkflows"] = has_inactive_custom_workflows
        if is_current_user_logged_into_to_plm is not UNSET:
            field_dict["isCurrentUserLoggedIntoToPLM"] = is_current_user_logged_into_to_plm
        if obsoletion_workflow is not UNSET:
            field_dict["obsoletionWorkflow"] = obsoletion_workflow
        if obsoletion_workflow_id is not UNSET:
            field_dict["obsoletionWorkflowId"] = obsoletion_workflow_id
        if obsoletion_workflow_info is not UNSET:
            field_dict["obsoletionWorkflowInfo"] = obsoletion_workflow_info
        if os_category_id_to_arena_number_format_id is not UNSET:
            field_dict["osCategoryIdToArenaNumberFormatId"] = os_category_id_to_arena_number_format_id
        if p_lm_integration_type is not UNSET:
            field_dict["pLMIntegrationType"] = p_lm_integration_type
        if p_lm_name is not UNSET:
            field_dict["pLMName"] = p_lm_name
        if part_numbering_scheme_id is not UNSET:
            field_dict["partNumberingSchemeId"] = part_numbering_scheme_id
        if pickable_workflows is not UNSET:
            field_dict["pickableWorkflows"] = pickable_workflows
        if release_workflow is not UNSET:
            field_dict["releaseWorkflow"] = release_workflow
        if release_workflow_id is not UNSET:
            field_dict["releaseWorkflowId"] = release_workflow_id
        if release_workflow_info is not UNSET:
            field_dict["releaseWorkflowInfo"] = release_workflow_info
        if releaseable_applications is not UNSET:
            field_dict["releaseableApplications"] = releaseable_applications
        if standard_content_numbering_scheme_id is not UNSET:
            field_dict["standardContentNumberingSchemeId"] = standard_content_numbering_scheme_id
        if standard_content_using_auto_numbering is not UNSET:
            field_dict["standardContentUsingAutoNumbering"] = standard_content_using_auto_numbering
        if standard_content_using_third_party_part_numbering is not UNSET:
            field_dict["standardContentUsingThirdPartyPartNumbering"] = (
                standard_content_using_third_party_part_numbering
            )
        if task_workflow is not UNSET:
            field_dict["taskWorkflow"] = task_workflow
        if task_workflow_info is not UNSET:
            field_dict["taskWorkflowInfo"] = task_workflow_info
        if using_auto_part_numbering is not UNSET:
            field_dict["usingAutoPartNumbering"] = using_auto_part_numbering
        if using_managed_workflow is not UNSET:
            field_dict["usingManagedWorkflow"] = using_managed_workflow
        if using_third_party_part_numbering is not UNSET:
            field_dict["usingThirdPartyPartNumbering"] = using_third_party_part_numbering

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_active_workflow_info_os_category_id_to_arena_number_format_id import (
            BTActiveWorkflowInfoOsCategoryIdToArenaNumberFormatId,
        )
        from ..models.bt_active_workflow_type_info import BTActiveWorkflowTypeInfo
        from ..models.bt_published_workflow_info import BTPublishedWorkflowInfo

        d = dict(src_dict)
        allow_release_items_from_other_documents = d.pop("allowReleaseItemsFromOtherDocuments", UNSET)

        can_current_user_create_releases = d.pop("canCurrentUserCreateReleases", UNSET)

        can_current_user_edit_standard_content = d.pop("canCurrentUserEditStandardContent", UNSET)

        can_current_user_manage_workflows = d.pop("canCurrentUserManageWorkflows", UNSET)

        can_current_user_see_arena_item_link = d.pop("canCurrentUserSeeArenaItemLink", UNSET)

        can_current_user_see_plm_item_link = d.pop("canCurrentUserSeePLMItemLink", UNSET)

        can_current_user_sync_bom_to_arena = d.pop("canCurrentUserSyncBomToArena", UNSET)

        can_current_user_sync_bom_to_plm = d.pop("canCurrentUserSyncBomToPLM", UNSET)

        can_current_user_sync_drawing_to_plm = d.pop("canCurrentUserSyncDrawingToPLM", UNSET)

        can_current_user_sync_revisions_to_arena = d.pop("canCurrentUserSyncRevisionsToArena", UNSET)

        can_current_user_sync_revisions_to_plm = d.pop("canCurrentUserSyncRevisionsToPLM", UNSET)

        can_current_user_sync_standard_content_to_arena = d.pop("canCurrentUserSyncStandardContentToArena", UNSET)

        can_current_user_sync_standard_content_to_plm = d.pop("canCurrentUserSyncStandardContentToPLM", UNSET)

        can_current_user_sync_to_arena = d.pop("canCurrentUserSyncToArena", UNSET)

        can_current_user_sync_to_plm = d.pop("canCurrentUserSyncToPLM", UNSET)

        company_id = d.pop("companyId", UNSET)

        document_id = d.pop("documentId", UNSET)

        drawing_can_duplicate_part_number = d.pop("drawingCanDuplicatePartNumber", UNSET)

        enabled_active_multiple_workflows = d.pop("enabledActiveMultipleWorkflows", UNSET)

        has_inactive_custom_workflows = d.pop("hasInactiveCustomWorkflows", UNSET)

        is_current_user_logged_into_to_plm = d.pop("isCurrentUserLoggedIntoToPLM", UNSET)

        _obsoletion_workflow = d.pop("obsoletionWorkflow", UNSET)
        obsoletion_workflow: BTPublishedWorkflowInfo | Unset
        if isinstance(_obsoletion_workflow, Unset):
            obsoletion_workflow = UNSET
        else:
            obsoletion_workflow = BTPublishedWorkflowInfo.from_dict(_obsoletion_workflow)

        obsoletion_workflow_id = d.pop("obsoletionWorkflowId", UNSET)

        _obsoletion_workflow_info = d.pop("obsoletionWorkflowInfo", UNSET)
        obsoletion_workflow_info: BTActiveWorkflowTypeInfo | Unset
        if isinstance(_obsoletion_workflow_info, Unset):
            obsoletion_workflow_info = UNSET
        else:
            obsoletion_workflow_info = BTActiveWorkflowTypeInfo.from_dict(_obsoletion_workflow_info)

        _os_category_id_to_arena_number_format_id = d.pop("osCategoryIdToArenaNumberFormatId", UNSET)
        os_category_id_to_arena_number_format_id: BTActiveWorkflowInfoOsCategoryIdToArenaNumberFormatId | Unset
        if isinstance(_os_category_id_to_arena_number_format_id, Unset):
            os_category_id_to_arena_number_format_id = UNSET
        else:
            os_category_id_to_arena_number_format_id = BTActiveWorkflowInfoOsCategoryIdToArenaNumberFormatId.from_dict(
                _os_category_id_to_arena_number_format_id
            )

        p_lm_integration_type = d.pop("pLMIntegrationType", UNSET)

        p_lm_name = d.pop("pLMName", UNSET)

        part_numbering_scheme_id = d.pop("partNumberingSchemeId", UNSET)

        _pickable_workflows = d.pop("pickableWorkflows", UNSET)
        pickable_workflows: list[BTPublishedWorkflowInfo] | Unset = UNSET
        if _pickable_workflows is not UNSET:
            pickable_workflows = []
            for pickable_workflows_item_data in _pickable_workflows:
                pickable_workflows_item = BTPublishedWorkflowInfo.from_dict(pickable_workflows_item_data)

                pickable_workflows.append(pickable_workflows_item)

        _release_workflow = d.pop("releaseWorkflow", UNSET)
        release_workflow: BTPublishedWorkflowInfo | Unset
        if isinstance(_release_workflow, Unset):
            release_workflow = UNSET
        else:
            release_workflow = BTPublishedWorkflowInfo.from_dict(_release_workflow)

        release_workflow_id = d.pop("releaseWorkflowId", UNSET)

        _release_workflow_info = d.pop("releaseWorkflowInfo", UNSET)
        release_workflow_info: BTActiveWorkflowTypeInfo | Unset
        if isinstance(_release_workflow_info, Unset):
            release_workflow_info = UNSET
        else:
            release_workflow_info = BTActiveWorkflowTypeInfo.from_dict(_release_workflow_info)

        releaseable_applications = cast(list[str], d.pop("releaseableApplications", UNSET))

        standard_content_numbering_scheme_id = d.pop("standardContentNumberingSchemeId", UNSET)

        standard_content_using_auto_numbering = d.pop("standardContentUsingAutoNumbering", UNSET)

        standard_content_using_third_party_part_numbering = d.pop("standardContentUsingThirdPartyPartNumbering", UNSET)

        _task_workflow = d.pop("taskWorkflow", UNSET)
        task_workflow: BTPublishedWorkflowInfo | Unset
        if isinstance(_task_workflow, Unset):
            task_workflow = UNSET
        else:
            task_workflow = BTPublishedWorkflowInfo.from_dict(_task_workflow)

        _task_workflow_info = d.pop("taskWorkflowInfo", UNSET)
        task_workflow_info: BTActiveWorkflowTypeInfo | Unset
        if isinstance(_task_workflow_info, Unset):
            task_workflow_info = UNSET
        else:
            task_workflow_info = BTActiveWorkflowTypeInfo.from_dict(_task_workflow_info)

        using_auto_part_numbering = d.pop("usingAutoPartNumbering", UNSET)

        using_managed_workflow = d.pop("usingManagedWorkflow", UNSET)

        using_third_party_part_numbering = d.pop("usingThirdPartyPartNumbering", UNSET)

        bt_active_workflow_info = cls(
            allow_release_items_from_other_documents=allow_release_items_from_other_documents,
            can_current_user_create_releases=can_current_user_create_releases,
            can_current_user_edit_standard_content=can_current_user_edit_standard_content,
            can_current_user_manage_workflows=can_current_user_manage_workflows,
            can_current_user_see_arena_item_link=can_current_user_see_arena_item_link,
            can_current_user_see_plm_item_link=can_current_user_see_plm_item_link,
            can_current_user_sync_bom_to_arena=can_current_user_sync_bom_to_arena,
            can_current_user_sync_bom_to_plm=can_current_user_sync_bom_to_plm,
            can_current_user_sync_drawing_to_plm=can_current_user_sync_drawing_to_plm,
            can_current_user_sync_revisions_to_arena=can_current_user_sync_revisions_to_arena,
            can_current_user_sync_revisions_to_plm=can_current_user_sync_revisions_to_plm,
            can_current_user_sync_standard_content_to_arena=can_current_user_sync_standard_content_to_arena,
            can_current_user_sync_standard_content_to_plm=can_current_user_sync_standard_content_to_plm,
            can_current_user_sync_to_arena=can_current_user_sync_to_arena,
            can_current_user_sync_to_plm=can_current_user_sync_to_plm,
            company_id=company_id,
            document_id=document_id,
            drawing_can_duplicate_part_number=drawing_can_duplicate_part_number,
            enabled_active_multiple_workflows=enabled_active_multiple_workflows,
            has_inactive_custom_workflows=has_inactive_custom_workflows,
            is_current_user_logged_into_to_plm=is_current_user_logged_into_to_plm,
            obsoletion_workflow=obsoletion_workflow,
            obsoletion_workflow_id=obsoletion_workflow_id,
            obsoletion_workflow_info=obsoletion_workflow_info,
            os_category_id_to_arena_number_format_id=os_category_id_to_arena_number_format_id,
            p_lm_integration_type=p_lm_integration_type,
            p_lm_name=p_lm_name,
            part_numbering_scheme_id=part_numbering_scheme_id,
            pickable_workflows=pickable_workflows,
            release_workflow=release_workflow,
            release_workflow_id=release_workflow_id,
            release_workflow_info=release_workflow_info,
            releaseable_applications=releaseable_applications,
            standard_content_numbering_scheme_id=standard_content_numbering_scheme_id,
            standard_content_using_auto_numbering=standard_content_using_auto_numbering,
            standard_content_using_third_party_part_numbering=standard_content_using_third_party_part_numbering,
            task_workflow=task_workflow,
            task_workflow_info=task_workflow_info,
            using_auto_part_numbering=using_auto_part_numbering,
            using_managed_workflow=using_managed_workflow,
            using_third_party_part_numbering=using_third_party_part_numbering,
        )

        bt_active_workflow_info.additional_properties = d
        return bt_active_workflow_info

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
