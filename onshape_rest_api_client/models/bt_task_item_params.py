from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTTaskItemParams")


@_attrs_define
class BTTaskItemParams:
    """References to add to the task.

    Attributes:
        body_type (str | Unset): Body type to reference from a task.
        configuration (str | Unset): Configuration of reference. Used to restrict a reference to a specific
            configuration of an element.
        description (str | Unset): Description of the reference.
        document_id (str | Unset): Id of a document. Required to reference a document or anything contained within it.
        element_id (str | Unset): Id of an element reference. Used when referencing an element.
        element_type (int | Unset): Type of element reference. Options are 0 (Part Studio), 1 (Assembly), 2 (Drawing), 3
            (Feature Studio), 4 (Blob), 5 (Application), 6 (Table), 7 (Bill of Materials),  8 (Variable Studio), or 9
            (Publication Item).
        mime_type (str | Unset): Mimetype of reference. Used when referencing blob elements.
        name (str | Unset): Name of the reference.
        part_id (str | Unset): Deterministic Id of a part. Used when referencing parts.
        revision_id (str | Unset): Id of a revision to reference from a task.
        version_id (str | Unset): Id of a document version. Used when referencing the version itself or an element or
            part in it.
        workspace_id (str | Unset): Id of a document workspace. Used when referencing the workspace itself or an element
            or part in it.
    """

    body_type: str | Unset = UNSET
    configuration: str | Unset = UNSET
    description: str | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_type: int | Unset = UNSET
    mime_type: str | Unset = UNSET
    name: str | Unset = UNSET
    part_id: str | Unset = UNSET
    revision_id: str | Unset = UNSET
    version_id: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body_type = self.body_type

        configuration = self.configuration

        description = self.description

        document_id = self.document_id

        element_id = self.element_id

        element_type = self.element_type

        mime_type = self.mime_type

        name = self.name

        part_id = self.part_id

        revision_id = self.revision_id

        version_id = self.version_id

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body_type is not UNSET:
            field_dict["bodyType"] = body_type
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if description is not UNSET:
            field_dict["description"] = description
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_type is not UNSET:
            field_dict["elementType"] = element_type
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if name is not UNSET:
            field_dict["name"] = name
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if revision_id is not UNSET:
            field_dict["revisionId"] = revision_id
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body_type = d.pop("bodyType", UNSET)

        configuration = d.pop("configuration", UNSET)

        description = d.pop("description", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        element_type = d.pop("elementType", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        name = d.pop("name", UNSET)

        part_id = d.pop("partId", UNSET)

        revision_id = d.pop("revisionId", UNSET)

        version_id = d.pop("versionId", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_task_item_params = cls(
            body_type=body_type,
            configuration=configuration,
            description=description,
            document_id=document_id,
            element_id=element_id,
            element_type=element_type,
            mime_type=mime_type,
            name=name,
            part_id=part_id,
            revision_id=revision_id,
            version_id=version_id,
            workspace_id=workspace_id,
        )

        bt_task_item_params.additional_properties = d
        return bt_task_item_params

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
