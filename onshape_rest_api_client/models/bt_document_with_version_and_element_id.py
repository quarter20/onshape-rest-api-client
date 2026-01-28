from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_id import ObjectId


T = TypeVar("T", bound="BTDocumentWithVersionAndElementId")


@_attrs_define
class BTDocumentWithVersionAndElementId:
    """
    Attributes:
        document_id (str | Unset):
        document_version_id (str | Unset):
        element_id (str | Unset):
        element_library_id (ObjectId | Unset):
        element_library_version (ObjectId | Unset):
        part_number (str | Unset):
        revision (str | Unset):
        unique_version_id (str | Unset):
        valid_element_library_reference (bool | Unset):
        valid_revision_reference (bool | Unset):
    """

    document_id: str | Unset = UNSET
    document_version_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_library_id: ObjectId | Unset = UNSET
    element_library_version: ObjectId | Unset = UNSET
    part_number: str | Unset = UNSET
    revision: str | Unset = UNSET
    unique_version_id: str | Unset = UNSET
    valid_element_library_reference: bool | Unset = UNSET
    valid_revision_reference: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        document_version_id = self.document_version_id

        element_id = self.element_id

        element_library_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.element_library_id, Unset):
            element_library_id = self.element_library_id.to_dict()

        element_library_version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.element_library_version, Unset):
            element_library_version = self.element_library_version.to_dict()

        part_number = self.part_number

        revision = self.revision

        unique_version_id = self.unique_version_id

        valid_element_library_reference = self.valid_element_library_reference

        valid_revision_reference = self.valid_revision_reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if document_version_id is not UNSET:
            field_dict["documentVersionId"] = document_version_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_library_id is not UNSET:
            field_dict["elementLibraryId"] = element_library_id
        if element_library_version is not UNSET:
            field_dict["elementLibraryVersion"] = element_library_version
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if revision is not UNSET:
            field_dict["revision"] = revision
        if unique_version_id is not UNSET:
            field_dict["uniqueVersionId"] = unique_version_id
        if valid_element_library_reference is not UNSET:
            field_dict["validElementLibraryReference"] = valid_element_library_reference
        if valid_revision_reference is not UNSET:
            field_dict["validRevisionReference"] = valid_revision_reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_id import ObjectId

        d = dict(src_dict)
        document_id = d.pop("documentId", UNSET)

        document_version_id = d.pop("documentVersionId", UNSET)

        element_id = d.pop("elementId", UNSET)

        _element_library_id = d.pop("elementLibraryId", UNSET)
        element_library_id: ObjectId | Unset
        if isinstance(_element_library_id, Unset):
            element_library_id = UNSET
        else:
            element_library_id = ObjectId.from_dict(_element_library_id)

        _element_library_version = d.pop("elementLibraryVersion", UNSET)
        element_library_version: ObjectId | Unset
        if isinstance(_element_library_version, Unset):
            element_library_version = UNSET
        else:
            element_library_version = ObjectId.from_dict(_element_library_version)

        part_number = d.pop("partNumber", UNSET)

        revision = d.pop("revision", UNSET)

        unique_version_id = d.pop("uniqueVersionId", UNSET)

        valid_element_library_reference = d.pop("validElementLibraryReference", UNSET)

        valid_revision_reference = d.pop("validRevisionReference", UNSET)

        bt_document_with_version_and_element_id = cls(
            document_id=document_id,
            document_version_id=document_version_id,
            element_id=element_id,
            element_library_id=element_library_id,
            element_library_version=element_library_version,
            part_number=part_number,
            revision=revision,
            unique_version_id=unique_version_id,
            valid_element_library_reference=valid_element_library_reference,
            valid_revision_reference=valid_revision_reference,
        )

        bt_document_with_version_and_element_id.additional_properties = d
        return bt_document_with_version_and_element_id

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
