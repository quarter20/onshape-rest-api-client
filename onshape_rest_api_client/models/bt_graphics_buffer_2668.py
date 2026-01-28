from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_graphics_buffer_target import GBTGraphicsBufferTarget
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_graphics_buffer_2668_map_graphics_attribute_to_component_count import (
        BTGraphicsBuffer2668MapGraphicsAttributeToComponentCount,
    )
    from ..models.bt_immutable_byte_array import BTImmutableByteArray


T = TypeVar("T", bound="BTGraphicsBuffer2668")


@_attrs_define
class BTGraphicsBuffer2668:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        buffer_data (BTImmutableByteArray | Unset):
        map_graphics_attribute_to_component_count (BTGraphicsBuffer2668MapGraphicsAttributeToComponentCount | Unset):
        target (GBTGraphicsBufferTarget | Unset):
    """

    bt_type: str | Unset = UNSET
    buffer_data: BTImmutableByteArray | Unset = UNSET
    map_graphics_attribute_to_component_count: BTGraphicsBuffer2668MapGraphicsAttributeToComponentCount | Unset = UNSET
    target: GBTGraphicsBufferTarget | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        buffer_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buffer_data, Unset):
            buffer_data = self.buffer_data.to_dict()

        map_graphics_attribute_to_component_count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.map_graphics_attribute_to_component_count, Unset):
            map_graphics_attribute_to_component_count = self.map_graphics_attribute_to_component_count.to_dict()

        target: str | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if buffer_data is not UNSET:
            field_dict["bufferData"] = buffer_data
        if map_graphics_attribute_to_component_count is not UNSET:
            field_dict["mapGraphicsAttributeToComponentCount"] = map_graphics_attribute_to_component_count
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_graphics_buffer_2668_map_graphics_attribute_to_component_count import (
            BTGraphicsBuffer2668MapGraphicsAttributeToComponentCount,
        )
        from ..models.bt_immutable_byte_array import BTImmutableByteArray

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _buffer_data = d.pop("bufferData", UNSET)
        buffer_data: BTImmutableByteArray | Unset
        if isinstance(_buffer_data, Unset):
            buffer_data = UNSET
        else:
            buffer_data = BTImmutableByteArray.from_dict(_buffer_data)

        _map_graphics_attribute_to_component_count = d.pop("mapGraphicsAttributeToComponentCount", UNSET)
        map_graphics_attribute_to_component_count: BTGraphicsBuffer2668MapGraphicsAttributeToComponentCount | Unset
        if isinstance(_map_graphics_attribute_to_component_count, Unset):
            map_graphics_attribute_to_component_count = UNSET
        else:
            map_graphics_attribute_to_component_count = (
                BTGraphicsBuffer2668MapGraphicsAttributeToComponentCount.from_dict(
                    _map_graphics_attribute_to_component_count
                )
            )

        _target = d.pop("target", UNSET)
        target: GBTGraphicsBufferTarget | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = GBTGraphicsBufferTarget(_target)

        bt_graphics_buffer_2668 = cls(
            bt_type=bt_type,
            buffer_data=buffer_data,
            map_graphics_attribute_to_component_count=map_graphics_attribute_to_component_count,
            target=target,
        )

        bt_graphics_buffer_2668.additional_properties = d
        return bt_graphics_buffer_2668

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
