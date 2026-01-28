from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTCommentAttachmentInfo")


@_attrs_define
class BTCommentAttachmentInfo:
    """
    Attributes:
        file_name (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        mime_type (str | Unset):
        name (str | Unset): Name of the resource.
        thumbnail_for (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    file_name: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    name: str | Unset = UNSET
    thumbnail_for: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        href = self.href

        id = self.id

        mime_type = self.mime_type

        name = self.name

        thumbnail_for = self.thumbnail_for

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if name is not UNSET:
            field_dict["name"] = name
        if thumbnail_for is not UNSET:
            field_dict["thumbnailFor"] = thumbnail_for
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("fileName", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        name = d.pop("name", UNSET)

        thumbnail_for = d.pop("thumbnailFor", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_comment_attachment_info = cls(
            file_name=file_name,
            href=href,
            id=id,
            mime_type=mime_type,
            name=name,
            thumbnail_for=thumbnail_for,
            view_ref=view_ref,
        )

        bt_comment_attachment_info.additional_properties = d
        return bt_comment_attachment_info

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
