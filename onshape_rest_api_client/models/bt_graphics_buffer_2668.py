from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_graphics_buffer_target import GBTGraphicsBufferTarget
from ..models.gbt_graphics_primitive_type import GBTGraphicsPrimitiveType
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
        group_type_offset_and_count (list[int] | Unset):
        map_graphics_attribute_to_component_count (BTGraphicsBuffer2668MapGraphicsAttributeToComponentCount | Unset):
        primitive_type (GBTGraphicsPrimitiveType | Unset):
        target (GBTGraphicsBufferTarget | Unset):
        target_byte_offset_and_count (list[int] | Unset):
        targets (list[GBTGraphicsBufferTarget] | Unset):
    """

    bt_type: str | Unset = UNSET
    buffer_data: BTImmutableByteArray | Unset = UNSET
    group_type_offset_and_count: list[int] | Unset = UNSET
    map_graphics_attribute_to_component_count: BTGraphicsBuffer2668MapGraphicsAttributeToComponentCount | Unset = UNSET
    primitive_type: GBTGraphicsPrimitiveType | Unset = UNSET
    target: GBTGraphicsBufferTarget | Unset = UNSET
    target_byte_offset_and_count: list[int] | Unset = UNSET
    targets: list[GBTGraphicsBufferTarget] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        buffer_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.buffer_data, Unset):
            buffer_data = self.buffer_data.to_dict()

        group_type_offset_and_count: list[int] | Unset = UNSET
        if not isinstance(self.group_type_offset_and_count, Unset):
            group_type_offset_and_count = self.group_type_offset_and_count

        map_graphics_attribute_to_component_count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.map_graphics_attribute_to_component_count, Unset):
            map_graphics_attribute_to_component_count = self.map_graphics_attribute_to_component_count.to_dict()

        primitive_type: str | Unset = UNSET
        if not isinstance(self.primitive_type, Unset):
            primitive_type = self.primitive_type.value

        target: str | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.value

        target_byte_offset_and_count: list[int] | Unset = UNSET
        if not isinstance(self.target_byte_offset_and_count, Unset):
            target_byte_offset_and_count = self.target_byte_offset_and_count

        targets: list[str] | Unset = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.value
                targets.append(targets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if buffer_data is not UNSET:
            field_dict["bufferData"] = buffer_data
        if group_type_offset_and_count is not UNSET:
            field_dict["groupTypeOffsetAndCount"] = group_type_offset_and_count
        if map_graphics_attribute_to_component_count is not UNSET:
            field_dict["mapGraphicsAttributeToComponentCount"] = map_graphics_attribute_to_component_count
        if primitive_type is not UNSET:
            field_dict["primitiveType"] = primitive_type
        if target is not UNSET:
            field_dict["target"] = target
        if target_byte_offset_and_count is not UNSET:
            field_dict["targetByteOffsetAndCount"] = target_byte_offset_and_count
        if targets is not UNSET:
            field_dict["targets"] = targets

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

        group_type_offset_and_count = cast(list[int], d.pop("groupTypeOffsetAndCount", UNSET))

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

        _primitive_type = d.pop("primitiveType", UNSET)
        primitive_type: GBTGraphicsPrimitiveType | Unset
        if isinstance(_primitive_type, Unset):
            primitive_type = UNSET
        else:
            primitive_type = GBTGraphicsPrimitiveType(_primitive_type)

        _target = d.pop("target", UNSET)
        target: GBTGraphicsBufferTarget | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = GBTGraphicsBufferTarget(_target)

        target_byte_offset_and_count = cast(list[int], d.pop("targetByteOffsetAndCount", UNSET))

        _targets = d.pop("targets", UNSET)
        targets: list[GBTGraphicsBufferTarget] | Unset = UNSET
        if _targets is not UNSET:
            targets = []
            for targets_item_data in _targets:
                targets_item = GBTGraphicsBufferTarget(targets_item_data)

                targets.append(targets_item)

        bt_graphics_buffer_2668 = cls(
            bt_type=bt_type,
            buffer_data=buffer_data,
            group_type_offset_and_count=group_type_offset_and_count,
            map_graphics_attribute_to_component_count=map_graphics_attribute_to_component_count,
            primitive_type=primitive_type,
            target=target,
            target_byte_offset_and_count=target_byte_offset_and_count,
            targets=targets,
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
