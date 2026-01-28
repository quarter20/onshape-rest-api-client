from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_move_element_params_element_original_to_new_map import BTMoveElementParamsElementOriginalToNewMap


T = TypeVar("T", bound="BTMoveElementParams")


@_attrs_define
class BTMoveElementParams:
    """
    Attributes:
        anchor_element_id (str | Unset):
        description (str | Unset):
        element_original_to_new_map (BTMoveElementParamsElementOriginalToNewMap | Unset):
        elements (list[str] | Unset):
        generate_unknown_messages (bool | Unset):
        import_data (list[str] | Unset):
        is_copy (bool | Unset):
        is_deep_copy (bool | Unset):
        is_group_anchor (bool | Unset):
        is_new_document (bool | Unset):
        is_public (bool | Unset):
        is_selective_part_out (bool | Unset):
        name (str | Unset):
        need_new_version (bool | Unset):
        owner_email (str | Unset):
        owner_id (str | Unset):
        owner_type (int | Unset):
        parent_id (str | Unset):
        project_id (str | Unset):
        selected_group_ids (list[str] | Unset):
        source_document_id (str | Unset):
        source_version_id (str | Unset):
        source_version_name (str | Unset): Name of version to move elements from (source).
        source_workspace_id (str | Unset):
        tags (list[str] | Unset):
        target_document_id (str | Unset):
        target_version_name (str | Unset): Name of version to move elements to (target).
        target_workspace_id (str | Unset):
        version_name (str | Unset):
    """

    anchor_element_id: str | Unset = UNSET
    description: str | Unset = UNSET
    element_original_to_new_map: BTMoveElementParamsElementOriginalToNewMap | Unset = UNSET
    elements: list[str] | Unset = UNSET
    generate_unknown_messages: bool | Unset = UNSET
    import_data: list[str] | Unset = UNSET
    is_copy: bool | Unset = UNSET
    is_deep_copy: bool | Unset = UNSET
    is_group_anchor: bool | Unset = UNSET
    is_new_document: bool | Unset = UNSET
    is_public: bool | Unset = UNSET
    is_selective_part_out: bool | Unset = UNSET
    name: str | Unset = UNSET
    need_new_version: bool | Unset = UNSET
    owner_email: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: int | Unset = UNSET
    parent_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    selected_group_ids: list[str] | Unset = UNSET
    source_document_id: str | Unset = UNSET
    source_version_id: str | Unset = UNSET
    source_version_name: str | Unset = UNSET
    source_workspace_id: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    target_document_id: str | Unset = UNSET
    target_version_name: str | Unset = UNSET
    target_workspace_id: str | Unset = UNSET
    version_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anchor_element_id = self.anchor_element_id

        description = self.description

        element_original_to_new_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.element_original_to_new_map, Unset):
            element_original_to_new_map = self.element_original_to_new_map.to_dict()

        elements: list[str] | Unset = UNSET
        if not isinstance(self.elements, Unset):
            elements = self.elements

        generate_unknown_messages = self.generate_unknown_messages

        import_data: list[str] | Unset = UNSET
        if not isinstance(self.import_data, Unset):
            import_data = self.import_data

        is_copy = self.is_copy

        is_deep_copy = self.is_deep_copy

        is_group_anchor = self.is_group_anchor

        is_new_document = self.is_new_document

        is_public = self.is_public

        is_selective_part_out = self.is_selective_part_out

        name = self.name

        need_new_version = self.need_new_version

        owner_email = self.owner_email

        owner_id = self.owner_id

        owner_type = self.owner_type

        parent_id = self.parent_id

        project_id = self.project_id

        selected_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.selected_group_ids, Unset):
            selected_group_ids = self.selected_group_ids

        source_document_id = self.source_document_id

        source_version_id = self.source_version_id

        source_version_name = self.source_version_name

        source_workspace_id = self.source_workspace_id

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        target_document_id = self.target_document_id

        target_version_name = self.target_version_name

        target_workspace_id = self.target_workspace_id

        version_name = self.version_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anchor_element_id is not UNSET:
            field_dict["anchorElementId"] = anchor_element_id
        if description is not UNSET:
            field_dict["description"] = description
        if element_original_to_new_map is not UNSET:
            field_dict["elementOriginalToNewMap"] = element_original_to_new_map
        if elements is not UNSET:
            field_dict["elements"] = elements
        if generate_unknown_messages is not UNSET:
            field_dict["generateUnknownMessages"] = generate_unknown_messages
        if import_data is not UNSET:
            field_dict["importData"] = import_data
        if is_copy is not UNSET:
            field_dict["isCopy"] = is_copy
        if is_deep_copy is not UNSET:
            field_dict["isDeepCopy"] = is_deep_copy
        if is_group_anchor is not UNSET:
            field_dict["isGroupAnchor"] = is_group_anchor
        if is_new_document is not UNSET:
            field_dict["isNewDocument"] = is_new_document
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if is_selective_part_out is not UNSET:
            field_dict["isSelectivePartOut"] = is_selective_part_out
        if name is not UNSET:
            field_dict["name"] = name
        if need_new_version is not UNSET:
            field_dict["needNewVersion"] = need_new_version
        if owner_email is not UNSET:
            field_dict["ownerEmail"] = owner_email
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if owner_type is not UNSET:
            field_dict["ownerType"] = owner_type
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if selected_group_ids is not UNSET:
            field_dict["selectedGroupIds"] = selected_group_ids
        if source_document_id is not UNSET:
            field_dict["sourceDocumentId"] = source_document_id
        if source_version_id is not UNSET:
            field_dict["sourceVersionId"] = source_version_id
        if source_version_name is not UNSET:
            field_dict["sourceVersionName"] = source_version_name
        if source_workspace_id is not UNSET:
            field_dict["sourceWorkspaceId"] = source_workspace_id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if target_document_id is not UNSET:
            field_dict["targetDocumentId"] = target_document_id
        if target_version_name is not UNSET:
            field_dict["targetVersionName"] = target_version_name
        if target_workspace_id is not UNSET:
            field_dict["targetWorkspaceId"] = target_workspace_id
        if version_name is not UNSET:
            field_dict["versionName"] = version_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_move_element_params_element_original_to_new_map import (
            BTMoveElementParamsElementOriginalToNewMap,
        )

        d = dict(src_dict)
        anchor_element_id = d.pop("anchorElementId", UNSET)

        description = d.pop("description", UNSET)

        _element_original_to_new_map = d.pop("elementOriginalToNewMap", UNSET)
        element_original_to_new_map: BTMoveElementParamsElementOriginalToNewMap | Unset
        if isinstance(_element_original_to_new_map, Unset):
            element_original_to_new_map = UNSET
        else:
            element_original_to_new_map = BTMoveElementParamsElementOriginalToNewMap.from_dict(
                _element_original_to_new_map
            )

        elements = cast(list[str], d.pop("elements", UNSET))

        generate_unknown_messages = d.pop("generateUnknownMessages", UNSET)

        import_data = cast(list[str], d.pop("importData", UNSET))

        is_copy = d.pop("isCopy", UNSET)

        is_deep_copy = d.pop("isDeepCopy", UNSET)

        is_group_anchor = d.pop("isGroupAnchor", UNSET)

        is_new_document = d.pop("isNewDocument", UNSET)

        is_public = d.pop("isPublic", UNSET)

        is_selective_part_out = d.pop("isSelectivePartOut", UNSET)

        name = d.pop("name", UNSET)

        need_new_version = d.pop("needNewVersion", UNSET)

        owner_email = d.pop("ownerEmail", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        owner_type = d.pop("ownerType", UNSET)

        parent_id = d.pop("parentId", UNSET)

        project_id = d.pop("projectId", UNSET)

        selected_group_ids = cast(list[str], d.pop("selectedGroupIds", UNSET))

        source_document_id = d.pop("sourceDocumentId", UNSET)

        source_version_id = d.pop("sourceVersionId", UNSET)

        source_version_name = d.pop("sourceVersionName", UNSET)

        source_workspace_id = d.pop("sourceWorkspaceId", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        target_document_id = d.pop("targetDocumentId", UNSET)

        target_version_name = d.pop("targetVersionName", UNSET)

        target_workspace_id = d.pop("targetWorkspaceId", UNSET)

        version_name = d.pop("versionName", UNSET)

        bt_move_element_params = cls(
            anchor_element_id=anchor_element_id,
            description=description,
            element_original_to_new_map=element_original_to_new_map,
            elements=elements,
            generate_unknown_messages=generate_unknown_messages,
            import_data=import_data,
            is_copy=is_copy,
            is_deep_copy=is_deep_copy,
            is_group_anchor=is_group_anchor,
            is_new_document=is_new_document,
            is_public=is_public,
            is_selective_part_out=is_selective_part_out,
            name=name,
            need_new_version=need_new_version,
            owner_email=owner_email,
            owner_id=owner_id,
            owner_type=owner_type,
            parent_id=parent_id,
            project_id=project_id,
            selected_group_ids=selected_group_ids,
            source_document_id=source_document_id,
            source_version_id=source_version_id,
            source_version_name=source_version_name,
            source_workspace_id=source_workspace_id,
            tags=tags,
            target_document_id=target_document_id,
            target_version_name=target_version_name,
            target_workspace_id=target_workspace_id,
            version_name=version_name,
        )

        bt_move_element_params.additional_properties = d
        return bt_move_element_params

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
