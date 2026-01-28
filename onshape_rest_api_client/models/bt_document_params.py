from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_document_element_creation_descriptor import BTDocumentElementCreationDescriptor


T = TypeVar("T", bound="BTDocumentParams")


@_attrs_define
class BTDocumentParams:
    """Parameters for creating and updating documents.

    Attributes:
        description (str | Unset): Document description.
        elements (list[BTDocumentElementCreationDescriptor] | Unset): List of element IDs to include in the document.
        force_export_rules (bool | Unset): `true` if the current user can toggle the Force Export Rule flag on a
            document.
        generate_unknown_messages (bool | Unset): Set to `true` for debugging.
        is_empty_content (bool | Unset): Set to `true` to generate an empty document.
        is_public (bool | Unset): Set to `true` to make the document public.
        name (str | Unset): Document name.
        not_revision_managed (bool | Unset): Set to `true` to indicate that revisions are not managed for this document.
        notes (str | Unset): Document notes.
        old_client_notes (str | Unset): Historical document notes.
        owner_email (str | Unset): The document owner's email address.
        owner_id (str | Unset): If `ownerType=USER`, this is the user ID. If `ownerType=COMPANY`, this is the company
            ID.
        owner_type (int | Unset): The document's owner type. `USER=0` | `COMPANY=1` | `ONSHAPE=2` Default: 0.
        parent_id (str | Unset): Document ID of this document's parent.
        project_id (str | Unset): ID of the project this document belongs to.
        tags (list[str] | Unset): Array of strings to set as tags for the document.
    """

    description: str | Unset = UNSET
    elements: list[BTDocumentElementCreationDescriptor] | Unset = UNSET
    force_export_rules: bool | Unset = UNSET
    generate_unknown_messages: bool | Unset = UNSET
    is_empty_content: bool | Unset = UNSET
    is_public: bool | Unset = UNSET
    name: str | Unset = UNSET
    not_revision_managed: bool | Unset = UNSET
    notes: str | Unset = UNSET
    old_client_notes: str | Unset = UNSET
    owner_email: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: int | Unset = 0
    parent_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        elements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.elements, Unset):
            elements = []
            for elements_item_data in self.elements:
                elements_item = elements_item_data.to_dict()
                elements.append(elements_item)

        force_export_rules = self.force_export_rules

        generate_unknown_messages = self.generate_unknown_messages

        is_empty_content = self.is_empty_content

        is_public = self.is_public

        name = self.name

        not_revision_managed = self.not_revision_managed

        notes = self.notes

        old_client_notes = self.old_client_notes

        owner_email = self.owner_email

        owner_id = self.owner_id

        owner_type = self.owner_type

        parent_id = self.parent_id

        project_id = self.project_id

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if elements is not UNSET:
            field_dict["elements"] = elements
        if force_export_rules is not UNSET:
            field_dict["forceExportRules"] = force_export_rules
        if generate_unknown_messages is not UNSET:
            field_dict["generateUnknownMessages"] = generate_unknown_messages
        if is_empty_content is not UNSET:
            field_dict["isEmptyContent"] = is_empty_content
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if name is not UNSET:
            field_dict["name"] = name
        if not_revision_managed is not UNSET:
            field_dict["notRevisionManaged"] = not_revision_managed
        if notes is not UNSET:
            field_dict["notes"] = notes
        if old_client_notes is not UNSET:
            field_dict["oldClientNotes"] = old_client_notes
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
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_document_element_creation_descriptor import BTDocumentElementCreationDescriptor

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _elements = d.pop("elements", UNSET)
        elements: list[BTDocumentElementCreationDescriptor] | Unset = UNSET
        if _elements is not UNSET:
            elements = []
            for elements_item_data in _elements:
                elements_item = BTDocumentElementCreationDescriptor.from_dict(elements_item_data)

                elements.append(elements_item)

        force_export_rules = d.pop("forceExportRules", UNSET)

        generate_unknown_messages = d.pop("generateUnknownMessages", UNSET)

        is_empty_content = d.pop("isEmptyContent", UNSET)

        is_public = d.pop("isPublic", UNSET)

        name = d.pop("name", UNSET)

        not_revision_managed = d.pop("notRevisionManaged", UNSET)

        notes = d.pop("notes", UNSET)

        old_client_notes = d.pop("oldClientNotes", UNSET)

        owner_email = d.pop("ownerEmail", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        owner_type = d.pop("ownerType", UNSET)

        parent_id = d.pop("parentId", UNSET)

        project_id = d.pop("projectId", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        bt_document_params = cls(
            description=description,
            elements=elements,
            force_export_rules=force_export_rules,
            generate_unknown_messages=generate_unknown_messages,
            is_empty_content=is_empty_content,
            is_public=is_public,
            name=name,
            not_revision_managed=not_revision_managed,
            notes=notes,
            old_client_notes=old_client_notes,
            owner_email=owner_email,
            owner_id=owner_id,
            owner_type=owner_type,
            parent_id=parent_id,
            project_id=project_id,
            tags=tags,
        )

        bt_document_params.additional_properties = d
        return bt_document_params

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
