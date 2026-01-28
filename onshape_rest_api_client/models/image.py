from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_extensions import ImageExtensions
    from ..models.image_extras import ImageExtras


T = TypeVar("T", bound="Image")


@_attrs_define
class Image:
    """
    Attributes:
        buffer_view (int | Unset):
        extensions (ImageExtensions | Unset):
        extras (ImageExtras | Unset):
        mime_type (str | Unset):
        name (str | Unset):
        uri (str | Unset):
    """

    buffer_view: int | Unset = UNSET
    extensions: ImageExtensions | Unset = UNSET
    extras: ImageExtras | Unset = UNSET
    mime_type: str | Unset = UNSET
    name: str | Unset = UNSET
    uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buffer_view = self.buffer_view

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        mime_type = self.mime_type

        name = self.name

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buffer_view is not UNSET:
            field_dict["bufferView"] = buffer_view
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if name is not UNSET:
            field_dict["name"] = name
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_extensions import ImageExtensions
        from ..models.image_extras import ImageExtras

        d = dict(src_dict)
        buffer_view = d.pop("bufferView", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: ImageExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = ImageExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: ImageExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = ImageExtras.from_dict(_extras)

        mime_type = d.pop("mimeType", UNSET)

        name = d.pop("name", UNSET)

        uri = d.pop("uri", UNSET)

        image = cls(
            buffer_view=buffer_view,
            extensions=extensions,
            extras=extras,
            mime_type=mime_type,
            name=name,
            uri=uri,
        )

        image.additional_properties = d
        return image

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
