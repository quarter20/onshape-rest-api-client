from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_full_element_id_756 import BTFullElementId756
    from ..models.bt_insertable_display_data_2405_graphics_buffers import BTInsertableDisplayData2405GraphicsBuffers
    from ..models.bt_part_data_16 import BTPartData16
    from ..models.bt_part_display_data_17 import BTPartDisplayData17


T = TypeVar("T", bound="BTInsertablePartDisplayData3103")


@_attrs_define
class BTInsertablePartDisplayData3103:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        full_element_id (BTFullElementId756 | Unset):
        graphics_buffers (BTInsertableDisplayData2405GraphicsBuffers | Unset):
        id (str | Unset):
        part (bool | Unset):
        sketch_feature (bool | Unset):
        tessellation_setting_index (int | Unset):
        part_data (BTPartData16 | Unset):
        part_display_data (BTPartDisplayData17 | Unset):
        part_id (str | Unset):
        tessellation_setting (int | Unset):
    """

    bt_type: str | Unset = UNSET
    full_element_id: BTFullElementId756 | Unset = UNSET
    graphics_buffers: BTInsertableDisplayData2405GraphicsBuffers | Unset = UNSET
    id: str | Unset = UNSET
    part: bool | Unset = UNSET
    sketch_feature: bool | Unset = UNSET
    tessellation_setting_index: int | Unset = UNSET
    part_data: BTPartData16 | Unset = UNSET
    part_display_data: BTPartDisplayData17 | Unset = UNSET
    part_id: str | Unset = UNSET
    tessellation_setting: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        full_element_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.full_element_id, Unset):
            full_element_id = self.full_element_id.to_dict()

        graphics_buffers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.graphics_buffers, Unset):
            graphics_buffers = self.graphics_buffers.to_dict()

        id = self.id

        part = self.part

        sketch_feature = self.sketch_feature

        tessellation_setting_index = self.tessellation_setting_index

        part_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.part_data, Unset):
            part_data = self.part_data.to_dict()

        part_display_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.part_display_data, Unset):
            part_display_data = self.part_display_data.to_dict()

        part_id = self.part_id

        tessellation_setting = self.tessellation_setting

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if full_element_id is not UNSET:
            field_dict["fullElementId"] = full_element_id
        if graphics_buffers is not UNSET:
            field_dict["graphicsBuffers"] = graphics_buffers
        if id is not UNSET:
            field_dict["id"] = id
        if part is not UNSET:
            field_dict["part"] = part
        if sketch_feature is not UNSET:
            field_dict["sketchFeature"] = sketch_feature
        if tessellation_setting_index is not UNSET:
            field_dict["tessellationSettingIndex"] = tessellation_setting_index
        if part_data is not UNSET:
            field_dict["partData"] = part_data
        if part_display_data is not UNSET:
            field_dict["partDisplayData"] = part_display_data
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if tessellation_setting is not UNSET:
            field_dict["tessellationSetting"] = tessellation_setting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_full_element_id_756 import BTFullElementId756
        from ..models.bt_insertable_display_data_2405_graphics_buffers import BTInsertableDisplayData2405GraphicsBuffers
        from ..models.bt_part_data_16 import BTPartData16
        from ..models.bt_part_display_data_17 import BTPartDisplayData17

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _full_element_id = d.pop("fullElementId", UNSET)
        full_element_id: BTFullElementId756 | Unset
        if isinstance(_full_element_id, Unset):
            full_element_id = UNSET
        else:
            full_element_id = BTFullElementId756.from_dict(_full_element_id)

        _graphics_buffers = d.pop("graphicsBuffers", UNSET)
        graphics_buffers: BTInsertableDisplayData2405GraphicsBuffers | Unset
        if isinstance(_graphics_buffers, Unset):
            graphics_buffers = UNSET
        else:
            graphics_buffers = BTInsertableDisplayData2405GraphicsBuffers.from_dict(_graphics_buffers)

        id = d.pop("id", UNSET)

        part = d.pop("part", UNSET)

        sketch_feature = d.pop("sketchFeature", UNSET)

        tessellation_setting_index = d.pop("tessellationSettingIndex", UNSET)

        _part_data = d.pop("partData", UNSET)
        part_data: BTPartData16 | Unset
        if isinstance(_part_data, Unset):
            part_data = UNSET
        else:
            part_data = BTPartData16.from_dict(_part_data)

        _part_display_data = d.pop("partDisplayData", UNSET)
        part_display_data: BTPartDisplayData17 | Unset
        if isinstance(_part_display_data, Unset):
            part_display_data = UNSET
        else:
            part_display_data = BTPartDisplayData17.from_dict(_part_display_data)

        part_id = d.pop("partId", UNSET)

        tessellation_setting = d.pop("tessellationSetting", UNSET)

        bt_insertable_part_display_data_3103 = cls(
            bt_type=bt_type,
            full_element_id=full_element_id,
            graphics_buffers=graphics_buffers,
            id=id,
            part=part,
            sketch_feature=sketch_feature,
            tessellation_setting_index=tessellation_setting_index,
            part_data=part_data,
            part_display_data=part_display_data,
            part_id=part_id,
            tessellation_setting=tessellation_setting,
        )

        bt_insertable_part_display_data_3103.additional_properties = d
        return bt_insertable_part_display_data_3103

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
