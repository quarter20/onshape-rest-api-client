from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTUniqueDocumentItemParams")


@_attrs_define
class BTUniqueDocumentItemParams:
    """
    Attributes:
        api_configuration (str | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        element_type (str | Unset):
        part_id (str | Unset):
        part_number (str | Unset):
        revision (str | Unset):
        version_id (str | Unset):
        workspace_id (str | Unset):
    """

    api_configuration: str | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_type: str | Unset = UNSET
    part_id: str | Unset = UNSET
    part_number: str | Unset = UNSET
    revision: str | Unset = UNSET
    version_id: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_configuration = self.api_configuration

        document_id = self.document_id

        element_id = self.element_id

        element_type = self.element_type

        part_id = self.part_id

        part_number = self.part_number

        revision = self.revision

        version_id = self.version_id

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_configuration is not UNSET:
            field_dict["apiConfiguration"] = api_configuration
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_type is not UNSET:
            field_dict["elementType"] = element_type
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if revision is not UNSET:
            field_dict["revision"] = revision
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_configuration = d.pop("apiConfiguration", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        element_type = d.pop("elementType", UNSET)

        part_id = d.pop("partId", UNSET)

        part_number = d.pop("partNumber", UNSET)

        revision = d.pop("revision", UNSET)

        version_id = d.pop("versionId", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_unique_document_item_params = cls(
            api_configuration=api_configuration,
            document_id=document_id,
            element_id=element_id,
            element_type=element_type,
            part_id=part_id,
            part_number=part_number,
            revision=revision,
            version_id=version_id,
            workspace_id=workspace_id,
        )

        bt_unique_document_item_params.additional_properties = d
        return bt_unique_document_item_params

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
