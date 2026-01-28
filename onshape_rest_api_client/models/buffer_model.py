from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buffer_model_buffer_data import BufferModelBufferData


T = TypeVar("T", bound="BufferModel")


@_attrs_define
class BufferModel:
    """
    Attributes:
        buffer_data (BufferModelBufferData | Unset):
        byte_length (int | Unset):
        name (str | Unset):
        uri (str | Unset):
    """

    buffer_data: BufferModelBufferData | Unset = UNSET
    byte_length: int | Unset = UNSET
    name: str | Unset = UNSET
    uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buffer_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buffer_data, Unset):
            buffer_data = self.buffer_data.to_dict()

        byte_length = self.byte_length

        name = self.name

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buffer_data is not UNSET:
            field_dict["bufferData"] = buffer_data
        if byte_length is not UNSET:
            field_dict["byteLength"] = byte_length
        if name is not UNSET:
            field_dict["name"] = name
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.buffer_model_buffer_data import BufferModelBufferData

        d = dict(src_dict)
        _buffer_data = d.pop("bufferData", UNSET)
        buffer_data: BufferModelBufferData | Unset
        if isinstance(_buffer_data, Unset):
            buffer_data = UNSET
        else:
            buffer_data = BufferModelBufferData.from_dict(_buffer_data)

        byte_length = d.pop("byteLength", UNSET)

        name = d.pop("name", UNSET)

        uri = d.pop("uri", UNSET)

        buffer_model = cls(
            buffer_data=buffer_data,
            byte_length=byte_length,
            name=name,
            uri=uri,
        )

        buffer_model.additional_properties = d
        return buffer_model

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
