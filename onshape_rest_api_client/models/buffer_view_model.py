from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.buffer_model import BufferModel
    from ..models.buffer_view_model_buffer_view_data import BufferViewModelBufferViewData


T = TypeVar("T", bound="BufferViewModel")


@_attrs_define
class BufferViewModel:
    """
    Attributes:
        buffer_model (BufferModel | Unset):
        buffer_view_data (BufferViewModelBufferViewData | Unset):
        byte_length (int | Unset):
        byte_offset (int | Unset):
        byte_stride (int | Unset):
        name (str | Unset):
        target (int | Unset):
    """

    buffer_model: BufferModel | Unset = UNSET
    buffer_view_data: BufferViewModelBufferViewData | Unset = UNSET
    byte_length: int | Unset = UNSET
    byte_offset: int | Unset = UNSET
    byte_stride: int | Unset = UNSET
    name: str | Unset = UNSET
    target: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buffer_model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buffer_model, Unset):
            buffer_model = self.buffer_model.to_dict()

        buffer_view_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buffer_view_data, Unset):
            buffer_view_data = self.buffer_view_data.to_dict()

        byte_length = self.byte_length

        byte_offset = self.byte_offset

        byte_stride = self.byte_stride

        name = self.name

        target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buffer_model is not UNSET:
            field_dict["bufferModel"] = buffer_model
        if buffer_view_data is not UNSET:
            field_dict["bufferViewData"] = buffer_view_data
        if byte_length is not UNSET:
            field_dict["byteLength"] = byte_length
        if byte_offset is not UNSET:
            field_dict["byteOffset"] = byte_offset
        if byte_stride is not UNSET:
            field_dict["byteStride"] = byte_stride
        if name is not UNSET:
            field_dict["name"] = name
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.buffer_model import BufferModel
        from ..models.buffer_view_model_buffer_view_data import BufferViewModelBufferViewData

        d = dict(src_dict)
        _buffer_model = d.pop("bufferModel", UNSET)
        buffer_model: BufferModel | Unset
        if isinstance(_buffer_model, Unset):
            buffer_model = UNSET
        else:
            buffer_model = BufferModel.from_dict(_buffer_model)

        _buffer_view_data = d.pop("bufferViewData", UNSET)
        buffer_view_data: BufferViewModelBufferViewData | Unset
        if isinstance(_buffer_view_data, Unset):
            buffer_view_data = UNSET
        else:
            buffer_view_data = BufferViewModelBufferViewData.from_dict(_buffer_view_data)

        byte_length = d.pop("byteLength", UNSET)

        byte_offset = d.pop("byteOffset", UNSET)

        byte_stride = d.pop("byteStride", UNSET)

        name = d.pop("name", UNSET)

        target = d.pop("target", UNSET)

        buffer_view_model = cls(
            buffer_model=buffer_model,
            buffer_view_data=buffer_view_data,
            byte_length=byte_length,
            byte_offset=byte_offset,
            byte_stride=byte_stride,
            name=name,
            target=target,
        )

        buffer_view_model.additional_properties = d
        return buffer_view_model

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
