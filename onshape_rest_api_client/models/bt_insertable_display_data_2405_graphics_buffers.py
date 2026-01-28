from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bt_insertable_display_data_2405_graphics_buffers_additional_property import (
        BTInsertableDisplayData2405GraphicsBuffersAdditionalProperty,
    )


T = TypeVar("T", bound="BTInsertableDisplayData2405GraphicsBuffers")


@_attrs_define
class BTInsertableDisplayData2405GraphicsBuffers:
    """ """

    additional_properties: dict[str, BTInsertableDisplayData2405GraphicsBuffersAdditionalProperty] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_insertable_display_data_2405_graphics_buffers_additional_property import (
            BTInsertableDisplayData2405GraphicsBuffersAdditionalProperty,
        )

        d = dict(src_dict)
        bt_insertable_display_data_2405_graphics_buffers = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = BTInsertableDisplayData2405GraphicsBuffersAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        bt_insertable_display_data_2405_graphics_buffers.additional_properties = additional_properties
        return bt_insertable_display_data_2405_graphics_buffers

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> BTInsertableDisplayData2405GraphicsBuffersAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: BTInsertableDisplayData2405GraphicsBuffersAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
