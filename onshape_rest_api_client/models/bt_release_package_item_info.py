from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_metadata_property_info import BTMetadataPropertyInfo
    from ..models.bt_release_item_error_info import BTReleaseItemErrorInfo


T = TypeVar("T", bound="BTReleasePackageItemInfo")


@_attrs_define
class BTReleasePackageItemInfo:
    """
    Attributes:
        added_automatically (bool | Unset):
        can_export (bool | Unset):
        change_detection_status (int | Unset):
        company_id (str | Unset):
        configuration (str | Unset):
        configuration_key (str | Unset):
        diff_thumbnail_configuration_key (str | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        element_type (int | Unset):
        errors (list[BTReleaseItemErrorInfo] | Unset):
        flat_part_id (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        is_revision_managed (bool | Unset):
        is_root_item (bool | Unset):
        is_translatable (bool | Unset):
        manually_removed_children_ids (list[str] | Unset):
        mesh_state (int | Unset):
        mime_type (str | Unset):
        name (str | Unset): Name of the resource.
        obsoletion_revision_id (str | Unset):
        original_workspace_id (str | Unset):
        parent_id (str | Unset):
        part_id (str | Unset):
        part_identity (str | Unset):
        part_type (str | Unset):
        properties (list[BTMetadataPropertyInfo] | Unset):
        reference_ids (list[str] | Unset):
        reference_ids_from_original_workspace (list[str] | Unset):
        rpid (str | Unset):
        small_thumbnail_href (str | Unset):
        subassembly_bom_behavior (str | Unset):
        synced_with_plm (bool | Unset):
        version_id (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        workspace_id (str | Unset):
    """

    added_automatically: bool | Unset = UNSET
    can_export: bool | Unset = UNSET
    change_detection_status: int | Unset = UNSET
    company_id: str | Unset = UNSET
    configuration: str | Unset = UNSET
    configuration_key: str | Unset = UNSET
    diff_thumbnail_configuration_key: str | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_type: int | Unset = UNSET
    errors: list[BTReleaseItemErrorInfo] | Unset = UNSET
    flat_part_id: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    is_revision_managed: bool | Unset = UNSET
    is_root_item: bool | Unset = UNSET
    is_translatable: bool | Unset = UNSET
    manually_removed_children_ids: list[str] | Unset = UNSET
    mesh_state: int | Unset = UNSET
    mime_type: str | Unset = UNSET
    name: str | Unset = UNSET
    obsoletion_revision_id: str | Unset = UNSET
    original_workspace_id: str | Unset = UNSET
    parent_id: str | Unset = UNSET
    part_id: str | Unset = UNSET
    part_identity: str | Unset = UNSET
    part_type: str | Unset = UNSET
    properties: list[BTMetadataPropertyInfo] | Unset = UNSET
    reference_ids: list[str] | Unset = UNSET
    reference_ids_from_original_workspace: list[str] | Unset = UNSET
    rpid: str | Unset = UNSET
    small_thumbnail_href: str | Unset = UNSET
    subassembly_bom_behavior: str | Unset = UNSET
    synced_with_plm: bool | Unset = UNSET
    version_id: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added_automatically = self.added_automatically

        can_export = self.can_export

        change_detection_status = self.change_detection_status

        company_id = self.company_id

        configuration = self.configuration

        configuration_key = self.configuration_key

        diff_thumbnail_configuration_key = self.diff_thumbnail_configuration_key

        document_id = self.document_id

        element_id = self.element_id

        element_type = self.element_type

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        flat_part_id = self.flat_part_id

        href = self.href

        id = self.id

        is_revision_managed = self.is_revision_managed

        is_root_item = self.is_root_item

        is_translatable = self.is_translatable

        manually_removed_children_ids: list[str] | Unset = UNSET
        if not isinstance(self.manually_removed_children_ids, Unset):
            manually_removed_children_ids = self.manually_removed_children_ids

        mesh_state = self.mesh_state

        mime_type = self.mime_type

        name = self.name

        obsoletion_revision_id = self.obsoletion_revision_id

        original_workspace_id = self.original_workspace_id

        parent_id = self.parent_id

        part_id = self.part_id

        part_identity = self.part_identity

        part_type = self.part_type

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        reference_ids: list[str] | Unset = UNSET
        if not isinstance(self.reference_ids, Unset):
            reference_ids = self.reference_ids

        reference_ids_from_original_workspace: list[str] | Unset = UNSET
        if not isinstance(self.reference_ids_from_original_workspace, Unset):
            reference_ids_from_original_workspace = self.reference_ids_from_original_workspace

        rpid = self.rpid

        small_thumbnail_href = self.small_thumbnail_href

        subassembly_bom_behavior = self.subassembly_bom_behavior

        synced_with_plm = self.synced_with_plm

        version_id = self.version_id

        view_ref = self.view_ref

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if added_automatically is not UNSET:
            field_dict["addedAutomatically"] = added_automatically
        if can_export is not UNSET:
            field_dict["canExport"] = can_export
        if change_detection_status is not UNSET:
            field_dict["changeDetectionStatus"] = change_detection_status
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if configuration_key is not UNSET:
            field_dict["configurationKey"] = configuration_key
        if diff_thumbnail_configuration_key is not UNSET:
            field_dict["diffThumbnailConfigurationKey"] = diff_thumbnail_configuration_key
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_type is not UNSET:
            field_dict["elementType"] = element_type
        if errors is not UNSET:
            field_dict["errors"] = errors
        if flat_part_id is not UNSET:
            field_dict["flatPartId"] = flat_part_id
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if is_revision_managed is not UNSET:
            field_dict["isRevisionManaged"] = is_revision_managed
        if is_root_item is not UNSET:
            field_dict["isRootItem"] = is_root_item
        if is_translatable is not UNSET:
            field_dict["isTranslatable"] = is_translatable
        if manually_removed_children_ids is not UNSET:
            field_dict["manuallyRemovedChildrenIds"] = manually_removed_children_ids
        if mesh_state is not UNSET:
            field_dict["meshState"] = mesh_state
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if name is not UNSET:
            field_dict["name"] = name
        if obsoletion_revision_id is not UNSET:
            field_dict["obsoletionRevisionId"] = obsoletion_revision_id
        if original_workspace_id is not UNSET:
            field_dict["originalWorkspaceId"] = original_workspace_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_identity is not UNSET:
            field_dict["partIdentity"] = part_identity
        if part_type is not UNSET:
            field_dict["partType"] = part_type
        if properties is not UNSET:
            field_dict["properties"] = properties
        if reference_ids is not UNSET:
            field_dict["referenceIds"] = reference_ids
        if reference_ids_from_original_workspace is not UNSET:
            field_dict["referenceIdsFromOriginalWorkspace"] = reference_ids_from_original_workspace
        if rpid is not UNSET:
            field_dict["rpid"] = rpid
        if small_thumbnail_href is not UNSET:
            field_dict["smallThumbnailHref"] = small_thumbnail_href
        if subassembly_bom_behavior is not UNSET:
            field_dict["subassemblyBomBehavior"] = subassembly_bom_behavior
        if synced_with_plm is not UNSET:
            field_dict["syncedWithPLM"] = synced_with_plm
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_metadata_property_info import BTMetadataPropertyInfo
        from ..models.bt_release_item_error_info import BTReleaseItemErrorInfo

        d = dict(src_dict)
        added_automatically = d.pop("addedAutomatically", UNSET)

        can_export = d.pop("canExport", UNSET)

        change_detection_status = d.pop("changeDetectionStatus", UNSET)

        company_id = d.pop("companyId", UNSET)

        configuration = d.pop("configuration", UNSET)

        configuration_key = d.pop("configurationKey", UNSET)

        diff_thumbnail_configuration_key = d.pop("diffThumbnailConfigurationKey", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        element_type = d.pop("elementType", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[BTReleaseItemErrorInfo] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = BTReleaseItemErrorInfo.from_dict(errors_item_data)

                errors.append(errors_item)

        flat_part_id = d.pop("flatPartId", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        is_revision_managed = d.pop("isRevisionManaged", UNSET)

        is_root_item = d.pop("isRootItem", UNSET)

        is_translatable = d.pop("isTranslatable", UNSET)

        manually_removed_children_ids = cast(list[str], d.pop("manuallyRemovedChildrenIds", UNSET))

        mesh_state = d.pop("meshState", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        name = d.pop("name", UNSET)

        obsoletion_revision_id = d.pop("obsoletionRevisionId", UNSET)

        original_workspace_id = d.pop("originalWorkspaceId", UNSET)

        parent_id = d.pop("parentId", UNSET)

        part_id = d.pop("partId", UNSET)

        part_identity = d.pop("partIdentity", UNSET)

        part_type = d.pop("partType", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: list[BTMetadataPropertyInfo] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = BTMetadataPropertyInfo.from_dict(properties_item_data)

                properties.append(properties_item)

        reference_ids = cast(list[str], d.pop("referenceIds", UNSET))

        reference_ids_from_original_workspace = cast(list[str], d.pop("referenceIdsFromOriginalWorkspace", UNSET))

        rpid = d.pop("rpid", UNSET)

        small_thumbnail_href = d.pop("smallThumbnailHref", UNSET)

        subassembly_bom_behavior = d.pop("subassemblyBomBehavior", UNSET)

        synced_with_plm = d.pop("syncedWithPLM", UNSET)

        version_id = d.pop("versionId", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_release_package_item_info = cls(
            added_automatically=added_automatically,
            can_export=can_export,
            change_detection_status=change_detection_status,
            company_id=company_id,
            configuration=configuration,
            configuration_key=configuration_key,
            diff_thumbnail_configuration_key=diff_thumbnail_configuration_key,
            document_id=document_id,
            element_id=element_id,
            element_type=element_type,
            errors=errors,
            flat_part_id=flat_part_id,
            href=href,
            id=id,
            is_revision_managed=is_revision_managed,
            is_root_item=is_root_item,
            is_translatable=is_translatable,
            manually_removed_children_ids=manually_removed_children_ids,
            mesh_state=mesh_state,
            mime_type=mime_type,
            name=name,
            obsoletion_revision_id=obsoletion_revision_id,
            original_workspace_id=original_workspace_id,
            parent_id=parent_id,
            part_id=part_id,
            part_identity=part_identity,
            part_type=part_type,
            properties=properties,
            reference_ids=reference_ids,
            reference_ids_from_original_workspace=reference_ids_from_original_workspace,
            rpid=rpid,
            small_thumbnail_href=small_thumbnail_href,
            subassembly_bom_behavior=subassembly_bom_behavior,
            synced_with_plm=synced_with_plm,
            version_id=version_id,
            view_ref=view_ref,
            workspace_id=workspace_id,
        )

        bt_release_package_item_info.additional_properties = d
        return bt_release_package_item_info

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
