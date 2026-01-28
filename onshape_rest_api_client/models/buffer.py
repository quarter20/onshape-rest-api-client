from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buffer_extensions import BufferExtensions
    from ..models.buffer_extras import BufferExtras


T = TypeVar("T", bound="Buffer")


@_attrs_define
class Buffer:
    """
    Attributes:
        byte_length (int | Unset):
        extensions (BufferExtensions | Unset):
        extras (BufferExtras | Unset):
        name (str | Unset):
        uri (str | Unset):
    """

    byte_length: int | Unset = UNSET
    extensions: BufferExtensions | Unset = UNSET
    extras: BufferExtras | Unset = UNSET
    name: str | Unset = UNSET
    uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        byte_length = self.byte_length

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        name = self.name

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if byte_length is not UNSET:
            field_dict["byteLength"] = byte_length
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if name is not UNSET:
            field_dict["name"] = name
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.buffer_extensions import BufferExtensions
        from ..models.buffer_extras import BufferExtras

        d = dict(src_dict)
        byte_length = d.pop("byteLength", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: BufferExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = BufferExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: BufferExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = BufferExtras.from_dict(_extras)

        name = d.pop("name", UNSET)

        uri = d.pop("uri", UNSET)

        buffer = cls(
            byte_length=byte_length,
            extensions=extensions,
            extras=extras,
            name=name,
            uri=uri,
        )

        buffer.additional_properties = d
        return buffer

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
