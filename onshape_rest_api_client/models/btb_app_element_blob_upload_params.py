from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="BTBAppElementBlobUploadParams")


@_attrs_define
class BTBAppElementBlobUploadParams:
    """
    Attributes:
        description (str | Unset):
        file (File | Unset): File to upload.
        file_content_length (int | Unset):
        parent_change_id (str | Unset):
        transaction_id (str | Unset):
    """

    description: str | Unset = UNSET
    file: File | Unset = UNSET
    file_content_length: int | Unset = UNSET
    parent_change_id: str | Unset = UNSET
    transaction_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        file: FileTypes | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        file_content_length = self.file_content_length

        parent_change_id = self.parent_change_id

        transaction_id = self.transaction_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if file is not UNSET:
            field_dict["file"] = file
        if file_content_length is not UNSET:
            field_dict["fileContentLength"] = file_content_length
        if parent_change_id is not UNSET:
            field_dict["parentChangeId"] = parent_change_id
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.file, Unset):
            files.append(("file", self.file.to_tuple()))

        if not isinstance(self.file_content_length, Unset):
            files.append(("fileContentLength", (None, str(self.file_content_length).encode(), "text/plain")))

        if not isinstance(self.parent_change_id, Unset):
            files.append(("parentChangeId", (None, str(self.parent_change_id).encode(), "text/plain")))

        if not isinstance(self.transaction_id, Unset):
            files.append(("transactionId", (None, str(self.transaction_id).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _file = d.pop("file", UNSET)
        file: File | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        file_content_length = d.pop("fileContentLength", UNSET)

        parent_change_id = d.pop("parentChangeId", UNSET)

        transaction_id = d.pop("transactionId", UNSET)

        btb_app_element_blob_upload_params = cls(
            description=description,
            file=file,
            file_content_length=file_content_length,
            parent_change_id=parent_change_id,
            transaction_id=transaction_id,
        )

        btb_app_element_blob_upload_params.additional_properties = d
        return btb_app_element_blob_upload_params

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
