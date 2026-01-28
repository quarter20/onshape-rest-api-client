from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types

if TYPE_CHECKING:
    from ..models.add_attachment_body_file import AddAttachmentBodyFile


T = TypeVar("T", bound="AddAttachmentBody")


@_attrs_define
class AddAttachmentBody:
    """
    Attributes:
        file (AddAttachmentBodyFile): The file to upload.
        is_markup (bool):
    """

    file: AddAttachmentBodyFile
    is_markup: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_dict()

        is_markup = self.is_markup

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "isMarkup": is_markup,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", (None, json.dumps(self.file.to_dict()).encode(), "application/json")))

        files.append(("isMarkup", (None, str(self.is_markup).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_attachment_body_file import AddAttachmentBodyFile

        d = dict(src_dict)
        file = AddAttachmentBodyFile.from_dict(d.pop("file"))

        is_markup = d.pop("isMarkup")

        add_attachment_body = cls(
            file=file,
            is_markup=is_markup,
        )

        add_attachment_body.additional_properties = d
        return add_attachment_body

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
