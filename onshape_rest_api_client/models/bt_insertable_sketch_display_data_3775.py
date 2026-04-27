from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_full_element_id_756 import BTFullElementId756
    from ..models.bt_graphics_buffer_2668 import BTGraphicsBuffer2668
    from ..models.bt_immutable_byte_array import BTImmutableByteArray
    from ..models.bt_insertable_display_data_2405_graphics_buffers import BTInsertableDisplayData2405GraphicsBuffers
    from ..models.bt_insertable_sketch_display_data_3775_body_id_to_part_data import (
        BTInsertableSketchDisplayData3775BodyIdToPartData,
    )
    from ..models.bt_part_data_16 import BTPartData16


T = TypeVar("T", bound="BTInsertableSketchDisplayData3775")


@_attrs_define
class BTInsertableSketchDisplayData3775:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        buffers (list[BTGraphicsBuffer2668] | Unset):
        full_element_id (BTFullElementId756 | Unset):
        graphics_buffers (BTInsertableDisplayData2405GraphicsBuffers | Unset):
        id (str | Unset):
        insertable_entity_data (BTImmutableByteArray | Unset):
        part (bool | Unset):
        sketch_feature (bool | Unset):
        tessellation_setting_index (int | Unset):
        body_d_id_list (list[str] | Unset):
        body_id_to_part_data (BTInsertableSketchDisplayData3775BodyIdToPartData | Unset):
        body_part_data_list (list[BTPartData16] | Unset):
        sketch_feature_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    buffers: list[BTGraphicsBuffer2668] | Unset = UNSET
    full_element_id: BTFullElementId756 | Unset = UNSET
    graphics_buffers: BTInsertableDisplayData2405GraphicsBuffers | Unset = UNSET
    id: str | Unset = UNSET
    insertable_entity_data: BTImmutableByteArray | Unset = UNSET
    part: bool | Unset = UNSET
    sketch_feature: bool | Unset = UNSET
    tessellation_setting_index: int | Unset = UNSET
    body_d_id_list: list[str] | Unset = UNSET
    body_id_to_part_data: BTInsertableSketchDisplayData3775BodyIdToPartData | Unset = UNSET
    body_part_data_list: list[BTPartData16] | Unset = UNSET
    sketch_feature_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        buffers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buffers, Unset):
            buffers = []
            for buffers_item_data in self.buffers:
                buffers_item = buffers_item_data.to_dict()
                buffers.append(buffers_item)

        full_element_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.full_element_id, Unset):
            full_element_id = self.full_element_id.to_dict()

        graphics_buffers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.graphics_buffers, Unset):
            graphics_buffers = self.graphics_buffers.to_dict()

        id = self.id

        insertable_entity_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insertable_entity_data, Unset):
            insertable_entity_data = self.insertable_entity_data.to_dict()

        part = self.part

        sketch_feature = self.sketch_feature

        tessellation_setting_index = self.tessellation_setting_index

        body_d_id_list: list[str] | Unset = UNSET
        if not isinstance(self.body_d_id_list, Unset):
            body_d_id_list = self.body_d_id_list

        body_id_to_part_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body_id_to_part_data, Unset):
            body_id_to_part_data = self.body_id_to_part_data.to_dict()

        body_part_data_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.body_part_data_list, Unset):
            body_part_data_list = []
            for body_part_data_list_item_data in self.body_part_data_list:
                body_part_data_list_item = body_part_data_list_item_data.to_dict()
                body_part_data_list.append(body_part_data_list_item)

        sketch_feature_id = self.sketch_feature_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if buffers is not UNSET:
            field_dict["buffers"] = buffers
        if full_element_id is not UNSET:
            field_dict["fullElementId"] = full_element_id
        if graphics_buffers is not UNSET:
            field_dict["graphicsBuffers"] = graphics_buffers
        if id is not UNSET:
            field_dict["id"] = id
        if insertable_entity_data is not UNSET:
            field_dict["insertableEntityData"] = insertable_entity_data
        if part is not UNSET:
            field_dict["part"] = part
        if sketch_feature is not UNSET:
            field_dict["sketchFeature"] = sketch_feature
        if tessellation_setting_index is not UNSET:
            field_dict["tessellationSettingIndex"] = tessellation_setting_index
        if body_d_id_list is not UNSET:
            field_dict["bodyDIdList"] = body_d_id_list
        if body_id_to_part_data is not UNSET:
            field_dict["bodyIdToPartData"] = body_id_to_part_data
        if body_part_data_list is not UNSET:
            field_dict["bodyPartDataList"] = body_part_data_list
        if sketch_feature_id is not UNSET:
            field_dict["sketchFeatureId"] = sketch_feature_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_full_element_id_756 import BTFullElementId756
        from ..models.bt_graphics_buffer_2668 import BTGraphicsBuffer2668
        from ..models.bt_immutable_byte_array import BTImmutableByteArray
        from ..models.bt_insertable_display_data_2405_graphics_buffers import BTInsertableDisplayData2405GraphicsBuffers
        from ..models.bt_insertable_sketch_display_data_3775_body_id_to_part_data import (
            BTInsertableSketchDisplayData3775BodyIdToPartData,
        )
        from ..models.bt_part_data_16 import BTPartData16

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _buffers = d.pop("buffers", UNSET)
        buffers: list[BTGraphicsBuffer2668] | Unset = UNSET
        if _buffers is not UNSET:
            buffers = []
            for buffers_item_data in _buffers:
                buffers_item = BTGraphicsBuffer2668.from_dict(buffers_item_data)

                buffers.append(buffers_item)

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

        _insertable_entity_data = d.pop("insertableEntityData", UNSET)
        insertable_entity_data: BTImmutableByteArray | Unset
        if isinstance(_insertable_entity_data, Unset):
            insertable_entity_data = UNSET
        else:
            insertable_entity_data = BTImmutableByteArray.from_dict(_insertable_entity_data)

        part = d.pop("part", UNSET)

        sketch_feature = d.pop("sketchFeature", UNSET)

        tessellation_setting_index = d.pop("tessellationSettingIndex", UNSET)

        body_d_id_list = cast(list[str], d.pop("bodyDIdList", UNSET))

        _body_id_to_part_data = d.pop("bodyIdToPartData", UNSET)
        body_id_to_part_data: BTInsertableSketchDisplayData3775BodyIdToPartData | Unset
        if isinstance(_body_id_to_part_data, Unset):
            body_id_to_part_data = UNSET
        else:
            body_id_to_part_data = BTInsertableSketchDisplayData3775BodyIdToPartData.from_dict(_body_id_to_part_data)

        _body_part_data_list = d.pop("bodyPartDataList", UNSET)
        body_part_data_list: list[BTPartData16] | Unset = UNSET
        if _body_part_data_list is not UNSET:
            body_part_data_list = []
            for body_part_data_list_item_data in _body_part_data_list:
                body_part_data_list_item = BTPartData16.from_dict(body_part_data_list_item_data)

                body_part_data_list.append(body_part_data_list_item)

        sketch_feature_id = d.pop("sketchFeatureId", UNSET)

        bt_insertable_sketch_display_data_3775 = cls(
            bt_type=bt_type,
            buffers=buffers,
            full_element_id=full_element_id,
            graphics_buffers=graphics_buffers,
            id=id,
            insertable_entity_data=insertable_entity_data,
            part=part,
            sketch_feature=sketch_feature,
            tessellation_setting_index=tessellation_setting_index,
            body_d_id_list=body_d_id_list,
            body_id_to_part_data=body_id_to_part_data,
            body_part_data_list=body_part_data_list,
            sketch_feature_id=sketch_feature_id,
        )

        bt_insertable_sketch_display_data_3775.additional_properties = d
        return bt_insertable_sketch_display_data_3775

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
