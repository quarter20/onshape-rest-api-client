from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_tessellation_setting_enum import GBTTessellationSettingEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_closed_constituent_part_data_2911 import BTClosedConstituentPartData2911
    from ..models.bt_part_data_16_flattened_to_unflattened_entities_mapping import (
        BTPartData16FlattenedToUnflattenedEntitiesMapping,
    )
    from ..models.bt_part_data_16_flattened_to_unflattened_mapping import BTPartData16FlattenedToUnflattenedMapping
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTPartData16")


@_attrs_define
class BTPartData16:
    """
    Attributes:
        best_available_tessellation_setting (GBTTessellationSettingEnum | Unset):
        bounds_diameter (float | Unset):
        bt_type (str | Unset): Type of JSON object.
        closed_constituent_part_data (BTClosedConstituentPartData2911 | Unset):
        coarse_planar_face_triangle_count (int | Unset):
        coarse_triangle_count (int | Unset):
        constituent_body_deterministic_ids (list[str] | Unset):
        copy_without_entities (BTPartData16 | Unset):
        entity_d_ids (list[str] | Unset):
        entity_deterministic_ids (list[str] | Unset):
        flattened_to_unflattened_entities_mapping (BTPartData16FlattenedToUnflattenedEntitiesMapping | Unset):
        flattened_to_unflattened_mapping (BTPartData16FlattenedToUnflattenedMapping | Unset):
        high_box_corner (BTVector3D389 | Unset):
        is_a_copy_for_tessellation_settings (bool | Unset):
        is_associated_with_flat (bool | Unset):
        is_bend_center_line_body (bool | Unset):
        is_closed_composite (bool | Unset):
        is_composite (bool | Unset):
        is_deletion (bool | Unset):
        is_entityless_part_data (bool | Unset):
        is_flattened_sheet_metal_body (bool | Unset):
        is_open_composite (bool | Unset):
        low_box_corner (BTVector3D389 | Unset):
        owner_flattened_body_id (str | Unset):
        sheet_metal_model_id (str | Unset):
        sheet_metal_order_id (str | Unset):
        should_always_use_highest_quality_tessellation (bool | Unset):
        tessellation_settings (list[int] | Unset):
        total_entity_count (int | Unset):
        user_tessellation_setting (GBTTessellationSettingEnum | Unset):
    """

    best_available_tessellation_setting: GBTTessellationSettingEnum | Unset = UNSET
    bounds_diameter: float | Unset = UNSET
    bt_type: str | Unset = UNSET
    closed_constituent_part_data: BTClosedConstituentPartData2911 | Unset = UNSET
    coarse_planar_face_triangle_count: int | Unset = UNSET
    coarse_triangle_count: int | Unset = UNSET
    constituent_body_deterministic_ids: list[str] | Unset = UNSET
    copy_without_entities: BTPartData16 | Unset = UNSET
    entity_d_ids: list[str] | Unset = UNSET
    entity_deterministic_ids: list[str] | Unset = UNSET
    flattened_to_unflattened_entities_mapping: BTPartData16FlattenedToUnflattenedEntitiesMapping | Unset = UNSET
    flattened_to_unflattened_mapping: BTPartData16FlattenedToUnflattenedMapping | Unset = UNSET
    high_box_corner: BTVector3D389 | Unset = UNSET
    is_a_copy_for_tessellation_settings: bool | Unset = UNSET
    is_associated_with_flat: bool | Unset = UNSET
    is_bend_center_line_body: bool | Unset = UNSET
    is_closed_composite: bool | Unset = UNSET
    is_composite: bool | Unset = UNSET
    is_deletion: bool | Unset = UNSET
    is_entityless_part_data: bool | Unset = UNSET
    is_flattened_sheet_metal_body: bool | Unset = UNSET
    is_open_composite: bool | Unset = UNSET
    low_box_corner: BTVector3D389 | Unset = UNSET
    owner_flattened_body_id: str | Unset = UNSET
    sheet_metal_model_id: str | Unset = UNSET
    sheet_metal_order_id: str | Unset = UNSET
    should_always_use_highest_quality_tessellation: bool | Unset = UNSET
    tessellation_settings: list[int] | Unset = UNSET
    total_entity_count: int | Unset = UNSET
    user_tessellation_setting: GBTTessellationSettingEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        best_available_tessellation_setting: str | Unset = UNSET
        if not isinstance(self.best_available_tessellation_setting, Unset):
            best_available_tessellation_setting = self.best_available_tessellation_setting.value

        bounds_diameter = self.bounds_diameter

        bt_type = self.bt_type

        closed_constituent_part_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.closed_constituent_part_data, Unset):
            closed_constituent_part_data = self.closed_constituent_part_data.to_dict()

        coarse_planar_face_triangle_count = self.coarse_planar_face_triangle_count

        coarse_triangle_count = self.coarse_triangle_count

        constituent_body_deterministic_ids: list[str] | Unset = UNSET
        if not isinstance(self.constituent_body_deterministic_ids, Unset):
            constituent_body_deterministic_ids = self.constituent_body_deterministic_ids

        copy_without_entities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.copy_without_entities, Unset):
            copy_without_entities = self.copy_without_entities.to_dict()

        entity_d_ids: list[str] | Unset = UNSET
        if not isinstance(self.entity_d_ids, Unset):
            entity_d_ids = self.entity_d_ids

        entity_deterministic_ids: list[str] | Unset = UNSET
        if not isinstance(self.entity_deterministic_ids, Unset):
            entity_deterministic_ids = self.entity_deterministic_ids

        flattened_to_unflattened_entities_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.flattened_to_unflattened_entities_mapping, Unset):
            flattened_to_unflattened_entities_mapping = self.flattened_to_unflattened_entities_mapping.to_dict()

        flattened_to_unflattened_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.flattened_to_unflattened_mapping, Unset):
            flattened_to_unflattened_mapping = self.flattened_to_unflattened_mapping.to_dict()

        high_box_corner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.high_box_corner, Unset):
            high_box_corner = self.high_box_corner.to_dict()

        is_a_copy_for_tessellation_settings = self.is_a_copy_for_tessellation_settings

        is_associated_with_flat = self.is_associated_with_flat

        is_bend_center_line_body = self.is_bend_center_line_body

        is_closed_composite = self.is_closed_composite

        is_composite = self.is_composite

        is_deletion = self.is_deletion

        is_entityless_part_data = self.is_entityless_part_data

        is_flattened_sheet_metal_body = self.is_flattened_sheet_metal_body

        is_open_composite = self.is_open_composite

        low_box_corner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.low_box_corner, Unset):
            low_box_corner = self.low_box_corner.to_dict()

        owner_flattened_body_id = self.owner_flattened_body_id

        sheet_metal_model_id = self.sheet_metal_model_id

        sheet_metal_order_id = self.sheet_metal_order_id

        should_always_use_highest_quality_tessellation = self.should_always_use_highest_quality_tessellation

        tessellation_settings: list[int] | Unset = UNSET
        if not isinstance(self.tessellation_settings, Unset):
            tessellation_settings = self.tessellation_settings

        total_entity_count = self.total_entity_count

        user_tessellation_setting: str | Unset = UNSET
        if not isinstance(self.user_tessellation_setting, Unset):
            user_tessellation_setting = self.user_tessellation_setting.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if best_available_tessellation_setting is not UNSET:
            field_dict["bestAvailableTessellationSetting"] = best_available_tessellation_setting
        if bounds_diameter is not UNSET:
            field_dict["boundsDiameter"] = bounds_diameter
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if closed_constituent_part_data is not UNSET:
            field_dict["closedConstituentPartData"] = closed_constituent_part_data
        if coarse_planar_face_triangle_count is not UNSET:
            field_dict["coarsePlanarFaceTriangleCount"] = coarse_planar_face_triangle_count
        if coarse_triangle_count is not UNSET:
            field_dict["coarseTriangleCount"] = coarse_triangle_count
        if constituent_body_deterministic_ids is not UNSET:
            field_dict["constituentBodyDeterministicIds"] = constituent_body_deterministic_ids
        if copy_without_entities is not UNSET:
            field_dict["copyWithoutEntities"] = copy_without_entities
        if entity_d_ids is not UNSET:
            field_dict["entityDIds"] = entity_d_ids
        if entity_deterministic_ids is not UNSET:
            field_dict["entityDeterministicIds"] = entity_deterministic_ids
        if flattened_to_unflattened_entities_mapping is not UNSET:
            field_dict["flattenedToUnflattenedEntitiesMapping"] = flattened_to_unflattened_entities_mapping
        if flattened_to_unflattened_mapping is not UNSET:
            field_dict["flattenedToUnflattenedMapping"] = flattened_to_unflattened_mapping
        if high_box_corner is not UNSET:
            field_dict["highBoxCorner"] = high_box_corner
        if is_a_copy_for_tessellation_settings is not UNSET:
            field_dict["isACopyForTessellationSettings"] = is_a_copy_for_tessellation_settings
        if is_associated_with_flat is not UNSET:
            field_dict["isAssociatedWithFlat"] = is_associated_with_flat
        if is_bend_center_line_body is not UNSET:
            field_dict["isBendCenterLineBody"] = is_bend_center_line_body
        if is_closed_composite is not UNSET:
            field_dict["isClosedComposite"] = is_closed_composite
        if is_composite is not UNSET:
            field_dict["isComposite"] = is_composite
        if is_deletion is not UNSET:
            field_dict["isDeletion"] = is_deletion
        if is_entityless_part_data is not UNSET:
            field_dict["isEntitylessPartData"] = is_entityless_part_data
        if is_flattened_sheet_metal_body is not UNSET:
            field_dict["isFlattenedSheetMetalBody"] = is_flattened_sheet_metal_body
        if is_open_composite is not UNSET:
            field_dict["isOpenComposite"] = is_open_composite
        if low_box_corner is not UNSET:
            field_dict["lowBoxCorner"] = low_box_corner
        if owner_flattened_body_id is not UNSET:
            field_dict["ownerFlattenedBodyId"] = owner_flattened_body_id
        if sheet_metal_model_id is not UNSET:
            field_dict["sheetMetalModelId"] = sheet_metal_model_id
        if sheet_metal_order_id is not UNSET:
            field_dict["sheetMetalOrderId"] = sheet_metal_order_id
        if should_always_use_highest_quality_tessellation is not UNSET:
            field_dict["shouldAlwaysUseHighestQualityTessellation"] = should_always_use_highest_quality_tessellation
        if tessellation_settings is not UNSET:
            field_dict["tessellationSettings"] = tessellation_settings
        if total_entity_count is not UNSET:
            field_dict["totalEntityCount"] = total_entity_count
        if user_tessellation_setting is not UNSET:
            field_dict["userTessellationSetting"] = user_tessellation_setting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_closed_constituent_part_data_2911 import BTClosedConstituentPartData2911
        from ..models.bt_part_data_16_flattened_to_unflattened_entities_mapping import (
            BTPartData16FlattenedToUnflattenedEntitiesMapping,
        )
        from ..models.bt_part_data_16_flattened_to_unflattened_mapping import BTPartData16FlattenedToUnflattenedMapping
        from ..models.bt_vector_3d389 import BTVector3D389

        d = dict(src_dict)
        _best_available_tessellation_setting = d.pop("bestAvailableTessellationSetting", UNSET)
        best_available_tessellation_setting: GBTTessellationSettingEnum | Unset
        if isinstance(_best_available_tessellation_setting, Unset):
            best_available_tessellation_setting = UNSET
        else:
            best_available_tessellation_setting = GBTTessellationSettingEnum(_best_available_tessellation_setting)

        bounds_diameter = d.pop("boundsDiameter", UNSET)

        bt_type = d.pop("btType", UNSET)

        _closed_constituent_part_data = d.pop("closedConstituentPartData", UNSET)
        closed_constituent_part_data: BTClosedConstituentPartData2911 | Unset
        if isinstance(_closed_constituent_part_data, Unset):
            closed_constituent_part_data = UNSET
        else:
            closed_constituent_part_data = BTClosedConstituentPartData2911.from_dict(_closed_constituent_part_data)

        coarse_planar_face_triangle_count = d.pop("coarsePlanarFaceTriangleCount", UNSET)

        coarse_triangle_count = d.pop("coarseTriangleCount", UNSET)

        constituent_body_deterministic_ids = cast(list[str], d.pop("constituentBodyDeterministicIds", UNSET))

        _copy_without_entities = d.pop("copyWithoutEntities", UNSET)
        copy_without_entities: BTPartData16 | Unset
        if isinstance(_copy_without_entities, Unset):
            copy_without_entities = UNSET
        else:
            copy_without_entities = BTPartData16.from_dict(_copy_without_entities)

        entity_d_ids = cast(list[str], d.pop("entityDIds", UNSET))

        entity_deterministic_ids = cast(list[str], d.pop("entityDeterministicIds", UNSET))

        _flattened_to_unflattened_entities_mapping = d.pop("flattenedToUnflattenedEntitiesMapping", UNSET)
        flattened_to_unflattened_entities_mapping: BTPartData16FlattenedToUnflattenedEntitiesMapping | Unset
        if isinstance(_flattened_to_unflattened_entities_mapping, Unset):
            flattened_to_unflattened_entities_mapping = UNSET
        else:
            flattened_to_unflattened_entities_mapping = BTPartData16FlattenedToUnflattenedEntitiesMapping.from_dict(
                _flattened_to_unflattened_entities_mapping
            )

        _flattened_to_unflattened_mapping = d.pop("flattenedToUnflattenedMapping", UNSET)
        flattened_to_unflattened_mapping: BTPartData16FlattenedToUnflattenedMapping | Unset
        if isinstance(_flattened_to_unflattened_mapping, Unset):
            flattened_to_unflattened_mapping = UNSET
        else:
            flattened_to_unflattened_mapping = BTPartData16FlattenedToUnflattenedMapping.from_dict(
                _flattened_to_unflattened_mapping
            )

        _high_box_corner = d.pop("highBoxCorner", UNSET)
        high_box_corner: BTVector3D389 | Unset
        if isinstance(_high_box_corner, Unset):
            high_box_corner = UNSET
        else:
            high_box_corner = BTVector3D389.from_dict(_high_box_corner)

        is_a_copy_for_tessellation_settings = d.pop("isACopyForTessellationSettings", UNSET)

        is_associated_with_flat = d.pop("isAssociatedWithFlat", UNSET)

        is_bend_center_line_body = d.pop("isBendCenterLineBody", UNSET)

        is_closed_composite = d.pop("isClosedComposite", UNSET)

        is_composite = d.pop("isComposite", UNSET)

        is_deletion = d.pop("isDeletion", UNSET)

        is_entityless_part_data = d.pop("isEntitylessPartData", UNSET)

        is_flattened_sheet_metal_body = d.pop("isFlattenedSheetMetalBody", UNSET)

        is_open_composite = d.pop("isOpenComposite", UNSET)

        _low_box_corner = d.pop("lowBoxCorner", UNSET)
        low_box_corner: BTVector3D389 | Unset
        if isinstance(_low_box_corner, Unset):
            low_box_corner = UNSET
        else:
            low_box_corner = BTVector3D389.from_dict(_low_box_corner)

        owner_flattened_body_id = d.pop("ownerFlattenedBodyId", UNSET)

        sheet_metal_model_id = d.pop("sheetMetalModelId", UNSET)

        sheet_metal_order_id = d.pop("sheetMetalOrderId", UNSET)

        should_always_use_highest_quality_tessellation = d.pop("shouldAlwaysUseHighestQualityTessellation", UNSET)

        tessellation_settings = cast(list[int], d.pop("tessellationSettings", UNSET))

        total_entity_count = d.pop("totalEntityCount", UNSET)

        _user_tessellation_setting = d.pop("userTessellationSetting", UNSET)
        user_tessellation_setting: GBTTessellationSettingEnum | Unset
        if isinstance(_user_tessellation_setting, Unset):
            user_tessellation_setting = UNSET
        else:
            user_tessellation_setting = GBTTessellationSettingEnum(_user_tessellation_setting)

        bt_part_data_16 = cls(
            best_available_tessellation_setting=best_available_tessellation_setting,
            bounds_diameter=bounds_diameter,
            bt_type=bt_type,
            closed_constituent_part_data=closed_constituent_part_data,
            coarse_planar_face_triangle_count=coarse_planar_face_triangle_count,
            coarse_triangle_count=coarse_triangle_count,
            constituent_body_deterministic_ids=constituent_body_deterministic_ids,
            copy_without_entities=copy_without_entities,
            entity_d_ids=entity_d_ids,
            entity_deterministic_ids=entity_deterministic_ids,
            flattened_to_unflattened_entities_mapping=flattened_to_unflattened_entities_mapping,
            flattened_to_unflattened_mapping=flattened_to_unflattened_mapping,
            high_box_corner=high_box_corner,
            is_a_copy_for_tessellation_settings=is_a_copy_for_tessellation_settings,
            is_associated_with_flat=is_associated_with_flat,
            is_bend_center_line_body=is_bend_center_line_body,
            is_closed_composite=is_closed_composite,
            is_composite=is_composite,
            is_deletion=is_deletion,
            is_entityless_part_data=is_entityless_part_data,
            is_flattened_sheet_metal_body=is_flattened_sheet_metal_body,
            is_open_composite=is_open_composite,
            low_box_corner=low_box_corner,
            owner_flattened_body_id=owner_flattened_body_id,
            sheet_metal_model_id=sheet_metal_model_id,
            sheet_metal_order_id=sheet_metal_order_id,
            should_always_use_highest_quality_tessellation=should_always_use_highest_quality_tessellation,
            tessellation_settings=tessellation_settings,
            total_entity_count=total_entity_count,
            user_tessellation_setting=user_tessellation_setting,
        )

        bt_part_data_16.additional_properties = d
        return bt_part_data_16

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
