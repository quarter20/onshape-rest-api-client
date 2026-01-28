from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.style_enum import StyleEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.encoding_extensions import EncodingExtensions
    from ..models.encoding_headers import EncodingHeaders


T = TypeVar("T", bound="Encoding")


@_attrs_define
class Encoding:
    """
    Attributes:
        allow_reserved (bool | Unset):
        content_type (str | Unset):
        explode (bool | Unset):
        extensions (EncodingExtensions | Unset):
        headers (EncodingHeaders | Unset):
        style (StyleEnum | Unset):
    """

    allow_reserved: bool | Unset = UNSET
    content_type: str | Unset = UNSET
    explode: bool | Unset = UNSET
    extensions: EncodingExtensions | Unset = UNSET
    headers: EncodingHeaders | Unset = UNSET
    style: StyleEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_reserved = self.allow_reserved

        content_type = self.content_type

        explode = self.explode

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        style: str | Unset = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_reserved is not UNSET:
            field_dict["allowReserved"] = allow_reserved
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if explode is not UNSET:
            field_dict["explode"] = explode
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if headers is not UNSET:
            field_dict["headers"] = headers
        if style is not UNSET:
            field_dict["style"] = style

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.encoding_extensions import EncodingExtensions
        from ..models.encoding_headers import EncodingHeaders

        d = dict(src_dict)
        allow_reserved = d.pop("allowReserved", UNSET)

        content_type = d.pop("contentType", UNSET)

        explode = d.pop("explode", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: EncodingExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = EncodingExtensions.from_dict(_extensions)

        _headers = d.pop("headers", UNSET)
        headers: EncodingHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = EncodingHeaders.from_dict(_headers)

        _style = d.pop("style", UNSET)
        style: StyleEnum | Unset
        if isinstance(_style, Unset):
            style = UNSET
        else:
            style = StyleEnum(_style)

        encoding = cls(
            allow_reserved=allow_reserved,
            content_type=content_type,
            explode=explode,
            extensions=extensions,
            headers=headers,
            style=style,
        )

        encoding.additional_properties = d
        return encoding

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
