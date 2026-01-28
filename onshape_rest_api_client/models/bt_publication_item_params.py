from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTPublicationItemParams")


@_attrs_define
class BTPublicationItemParams:
    """
    Attributes:
        data_type (str | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        encoded_configuration (str | Unset):
        is_application (bool | Unset):
        is_assembly (bool | Unset):
        is_blob (bool | Unset):
        is_whole_part_studio (bool | Unset):
        mime_type (str | Unset):
        part_id (str | Unset):
        part_name (str | Unset):
        part_number (str | Unset):
        revision (str | Unset):
        revision_id (str | Unset):
        version_id (str | Unset):
    """

    data_type: str | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    encoded_configuration: str | Unset = UNSET
    is_application: bool | Unset = UNSET
    is_assembly: bool | Unset = UNSET
    is_blob: bool | Unset = UNSET
    is_whole_part_studio: bool | Unset = UNSET
    mime_type: str | Unset = UNSET
    part_id: str | Unset = UNSET
    part_name: str | Unset = UNSET
    part_number: str | Unset = UNSET
    revision: str | Unset = UNSET
    revision_id: str | Unset = UNSET
    version_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_type = self.data_type

        document_id = self.document_id

        element_id = self.element_id

        encoded_configuration = self.encoded_configuration

        is_application = self.is_application

        is_assembly = self.is_assembly

        is_blob = self.is_blob

        is_whole_part_studio = self.is_whole_part_studio

        mime_type = self.mime_type

        part_id = self.part_id

        part_name = self.part_name

        part_number = self.part_number

        revision = self.revision

        revision_id = self.revision_id

        version_id = self.version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if encoded_configuration is not UNSET:
            field_dict["encodedConfiguration"] = encoded_configuration
        if is_application is not UNSET:
            field_dict["isApplication"] = is_application
        if is_assembly is not UNSET:
            field_dict["isAssembly"] = is_assembly
        if is_blob is not UNSET:
            field_dict["isBlob"] = is_blob
        if is_whole_part_studio is not UNSET:
            field_dict["isWholePartStudio"] = is_whole_part_studio
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_name is not UNSET:
            field_dict["partName"] = part_name
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if revision is not UNSET:
            field_dict["revision"] = revision
        if revision_id is not UNSET:
            field_dict["revisionId"] = revision_id
        if version_id is not UNSET:
            field_dict["versionId"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_type = d.pop("dataType", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        encoded_configuration = d.pop("encodedConfiguration", UNSET)

        is_application = d.pop("isApplication", UNSET)

        is_assembly = d.pop("isAssembly", UNSET)

        is_blob = d.pop("isBlob", UNSET)

        is_whole_part_studio = d.pop("isWholePartStudio", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        part_id = d.pop("partId", UNSET)

        part_name = d.pop("partName", UNSET)

        part_number = d.pop("partNumber", UNSET)

        revision = d.pop("revision", UNSET)

        revision_id = d.pop("revisionId", UNSET)

        version_id = d.pop("versionId", UNSET)

        bt_publication_item_params = cls(
            data_type=data_type,
            document_id=document_id,
            element_id=element_id,
            encoded_configuration=encoded_configuration,
            is_application=is_application,
            is_assembly=is_assembly,
            is_blob=is_blob,
            is_whole_part_studio=is_whole_part_studio,
            mime_type=mime_type,
            part_id=part_id,
            part_name=part_name,
            part_number=part_number,
            revision=revision,
            revision_id=revision_id,
            version_id=version_id,
        )

        bt_publication_item_params.additional_properties = d
        return bt_publication_item_params

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
