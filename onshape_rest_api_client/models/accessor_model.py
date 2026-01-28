from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.element_type import ElementType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.accessor_data import AccessorData
    from ..models.buffer_view_model import BufferViewModel


T = TypeVar("T", bound="AccessorModel")


@_attrs_define
class AccessorModel:
    """
    Attributes:
        accessor_data (AccessorData | Unset):
        buffer_view_model (BufferViewModel | Unset):
        byte_offset (int | Unset):
        byte_stride (int | Unset):
        component_size_in_bytes (int | Unset):
        component_type (int | Unset):
        count (int | Unset):
        element_size_in_bytes (int | Unset):
        element_type (ElementType | Unset):
        max_ (list[float] | Unset):
        min_ (list[float] | Unset):
        name (str | Unset):
    """

    accessor_data: AccessorData | Unset = UNSET
    buffer_view_model: BufferViewModel | Unset = UNSET
    byte_offset: int | Unset = UNSET
    byte_stride: int | Unset = UNSET
    component_size_in_bytes: int | Unset = UNSET
    component_type: int | Unset = UNSET
    count: int | Unset = UNSET
    element_size_in_bytes: int | Unset = UNSET
    element_type: ElementType | Unset = UNSET
    max_: list[float] | Unset = UNSET
    min_: list[float] | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accessor_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accessor_data, Unset):
            accessor_data = self.accessor_data.to_dict()

        buffer_view_model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buffer_view_model, Unset):
            buffer_view_model = self.buffer_view_model.to_dict()

        byte_offset = self.byte_offset

        byte_stride = self.byte_stride

        component_size_in_bytes = self.component_size_in_bytes

        component_type = self.component_type

        count = self.count

        element_size_in_bytes = self.element_size_in_bytes

        element_type: str | Unset = UNSET
        if not isinstance(self.element_type, Unset):
            element_type = self.element_type.value

        max_: list[float] | Unset = UNSET
        if not isinstance(self.max_, Unset):
            max_ = self.max_

        min_: list[float] | Unset = UNSET
        if not isinstance(self.min_, Unset):
            min_ = self.min_

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accessor_data is not UNSET:
            field_dict["accessorData"] = accessor_data
        if buffer_view_model is not UNSET:
            field_dict["bufferViewModel"] = buffer_view_model
        if byte_offset is not UNSET:
            field_dict["byteOffset"] = byte_offset
        if byte_stride is not UNSET:
            field_dict["byteStride"] = byte_stride
        if component_size_in_bytes is not UNSET:
            field_dict["componentSizeInBytes"] = component_size_in_bytes
        if component_type is not UNSET:
            field_dict["componentType"] = component_type
        if count is not UNSET:
            field_dict["count"] = count
        if element_size_in_bytes is not UNSET:
            field_dict["elementSizeInBytes"] = element_size_in_bytes
        if element_type is not UNSET:
            field_dict["elementType"] = element_type
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accessor_data import AccessorData
        from ..models.buffer_view_model import BufferViewModel

        d = dict(src_dict)
        _accessor_data = d.pop("accessorData", UNSET)
        accessor_data: AccessorData | Unset
        if isinstance(_accessor_data, Unset):
            accessor_data = UNSET
        else:
            accessor_data = AccessorData.from_dict(_accessor_data)

        _buffer_view_model = d.pop("bufferViewModel", UNSET)
        buffer_view_model: BufferViewModel | Unset
        if isinstance(_buffer_view_model, Unset):
            buffer_view_model = UNSET
        else:
            buffer_view_model = BufferViewModel.from_dict(_buffer_view_model)

        byte_offset = d.pop("byteOffset", UNSET)

        byte_stride = d.pop("byteStride", UNSET)

        component_size_in_bytes = d.pop("componentSizeInBytes", UNSET)

        component_type = d.pop("componentType", UNSET)

        count = d.pop("count", UNSET)

        element_size_in_bytes = d.pop("elementSizeInBytes", UNSET)

        _element_type = d.pop("elementType", UNSET)
        element_type: ElementType | Unset
        if isinstance(_element_type, Unset):
            element_type = UNSET
        else:
            element_type = ElementType(_element_type)

        max_ = cast(list[float], d.pop("max", UNSET))

        min_ = cast(list[float], d.pop("min", UNSET))

        name = d.pop("name", UNSET)

        accessor_model = cls(
            accessor_data=accessor_data,
            buffer_view_model=buffer_view_model,
            byte_offset=byte_offset,
            byte_stride=byte_stride,
            component_size_in_bytes=component_size_in_bytes,
            component_type=component_type,
            count=count,
            element_size_in_bytes=element_size_in_bytes,
            element_type=element_type,
            max_=max_,
            min_=min_,
            name=name,
        )

        accessor_model.additional_properties = d
        return accessor_model

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
