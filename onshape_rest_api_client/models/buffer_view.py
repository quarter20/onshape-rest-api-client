from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buffer_view_extensions import BufferViewExtensions
    from ..models.buffer_view_extras import BufferViewExtras


T = TypeVar("T", bound="BufferView")


@_attrs_define
class BufferView:
    """
    Attributes:
        buffer (int | Unset):
        byte_length (int | Unset):
        byte_offset (int | Unset):
        byte_stride (int | Unset):
        extensions (BufferViewExtensions | Unset):
        extras (BufferViewExtras | Unset):
        name (str | Unset):
        target (int | Unset):
    """

    buffer: int | Unset = UNSET
    byte_length: int | Unset = UNSET
    byte_offset: int | Unset = UNSET
    byte_stride: int | Unset = UNSET
    extensions: BufferViewExtensions | Unset = UNSET
    extras: BufferViewExtras | Unset = UNSET
    name: str | Unset = UNSET
    target: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buffer = self.buffer

        byte_length = self.byte_length

        byte_offset = self.byte_offset

        byte_stride = self.byte_stride

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        extras: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extras, Unset):
            extras = self.extras.to_dict()

        name = self.name

        target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buffer is not UNSET:
            field_dict["buffer"] = buffer
        if byte_length is not UNSET:
            field_dict["byteLength"] = byte_length
        if byte_offset is not UNSET:
            field_dict["byteOffset"] = byte_offset
        if byte_stride is not UNSET:
            field_dict["byteStride"] = byte_stride
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if extras is not UNSET:
            field_dict["extras"] = extras
        if name is not UNSET:
            field_dict["name"] = name
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.buffer_view_extensions import BufferViewExtensions
        from ..models.buffer_view_extras import BufferViewExtras

        d = dict(src_dict)
        buffer = d.pop("buffer", UNSET)

        byte_length = d.pop("byteLength", UNSET)

        byte_offset = d.pop("byteOffset", UNSET)

        byte_stride = d.pop("byteStride", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: BufferViewExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = BufferViewExtensions.from_dict(_extensions)

        _extras = d.pop("extras", UNSET)
        extras: BufferViewExtras | Unset
        if isinstance(_extras, Unset):
            extras = UNSET
        else:
            extras = BufferViewExtras.from_dict(_extras)

        name = d.pop("name", UNSET)

        target = d.pop("target", UNSET)

        buffer_view = cls(
            buffer=buffer,
            byte_length=byte_length,
            byte_offset=byte_offset,
            byte_stride=byte_stride,
            extensions=extensions,
            extras=extras,
            name=name,
            target=target,
        )

        buffer_view.additional_properties = d
        return buffer_view

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
