from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category import Category


T = TypeVar("T", bound="BTNextPartNumber")


@_attrs_define
class BTNextPartNumber:
    """
    Attributes:
        categories (list[Category] | Unset):
        configuration (str | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        element_type (int | Unset):
        error_message (str | Unset):
        id (str | Unset):
        mime_type (str | Unset):
        part_id (str | Unset):
        part_number (str | Unset):
        prefix (str | Unset):
        resource_type (int | Unset):
        version_id (str | Unset):
        workspace_id (str | Unset):
    """

    categories: list[Category] | Unset = UNSET
    configuration: str | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_type: int | Unset = UNSET
    error_message: str | Unset = UNSET
    id: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    part_id: str | Unset = UNSET
    part_number: str | Unset = UNSET
    prefix: str | Unset = UNSET
    resource_type: int | Unset = UNSET
    version_id: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        configuration = self.configuration

        document_id = self.document_id

        element_id = self.element_id

        element_type = self.element_type

        error_message = self.error_message

        id = self.id

        mime_type = self.mime_type

        part_id = self.part_id

        part_number = self.part_number

        prefix = self.prefix

        resource_type = self.resource_type

        version_id = self.version_id

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_type is not UNSET:
            field_dict["elementType"] = element_type
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if id is not UNSET:
            field_dict["id"] = id
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category import Category

        d = dict(src_dict)
        _categories = d.pop("categories", UNSET)
        categories: list[Category] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = Category.from_dict(categories_item_data)

                categories.append(categories_item)

        configuration = d.pop("configuration", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        element_type = d.pop("elementType", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        id = d.pop("id", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        part_id = d.pop("partId", UNSET)

        part_number = d.pop("partNumber", UNSET)

        prefix = d.pop("prefix", UNSET)

        resource_type = d.pop("resourceType", UNSET)

        version_id = d.pop("versionId", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_next_part_number = cls(
            categories=categories,
            configuration=configuration,
            document_id=document_id,
            element_id=element_id,
            element_type=element_type,
            error_message=error_message,
            id=id,
            mime_type=mime_type,
            part_id=part_id,
            part_number=part_number,
            prefix=prefix,
            resource_type=resource_type,
            version_id=version_id,
            workspace_id=workspace_id,
        )

        bt_next_part_number.additional_properties = d
        return bt_next_part_number

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
