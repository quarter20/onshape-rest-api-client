from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_debug_entity_color import GBTDebugEntityColor
from ..models.gbt_debug_entity_style import GBTDebugEntityStyle
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_entity_geometry_35 import BTEntityGeometry35
    from ..models.bt_graphics_appearance_1152 import BTGraphicsAppearance1152
    from ..models.bt_tessellated_geometry_2576 import BTTessellatedGeometry2576


T = TypeVar("T", bound="BTDebugGeometry2059")


@_attrs_define
class BTDebugGeometry2059:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        compressed (bool | Unset):
        decompressed (BTEntityGeometry35 | Unset):
        error_code (int | Unset):
        estimated_memory_usage_in_bytes (int | Unset):
        has_tessellation_error (bool | Unset):
        setting_index (int | Unset):
        appearance (BTGraphicsAppearance1152 | Unset):
        belongs_to_flattened_sheet_metal_body (bool | Unset):
        body_id (str | Unset):
        color (GBTDebugEntityColor | Unset):
        deterministic_id (str | Unset):
        sheet_metal_model_id (str | Unset):
        style (GBTDebugEntityStyle | Unset):
        tessellation (BTTessellatedGeometry2576 | Unset):
    """

    bt_type: str | Unset = UNSET
    compressed: bool | Unset = UNSET
    decompressed: BTEntityGeometry35 | Unset = UNSET
    error_code: int | Unset = UNSET
    estimated_memory_usage_in_bytes: int | Unset = UNSET
    has_tessellation_error: bool | Unset = UNSET
    setting_index: int | Unset = UNSET
    appearance: BTGraphicsAppearance1152 | Unset = UNSET
    belongs_to_flattened_sheet_metal_body: bool | Unset = UNSET
    body_id: str | Unset = UNSET
    color: GBTDebugEntityColor | Unset = UNSET
    deterministic_id: str | Unset = UNSET
    sheet_metal_model_id: str | Unset = UNSET
    style: GBTDebugEntityStyle | Unset = UNSET
    tessellation: BTTessellatedGeometry2576 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        compressed = self.compressed

        decompressed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.decompressed, Unset):
            decompressed = self.decompressed.to_dict()

        error_code = self.error_code

        estimated_memory_usage_in_bytes = self.estimated_memory_usage_in_bytes

        has_tessellation_error = self.has_tessellation_error

        setting_index = self.setting_index

        appearance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.appearance, Unset):
            appearance = self.appearance.to_dict()

        belongs_to_flattened_sheet_metal_body = self.belongs_to_flattened_sheet_metal_body

        body_id = self.body_id

        color: str | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.value

        deterministic_id = self.deterministic_id

        sheet_metal_model_id = self.sheet_metal_model_id

        style: str | Unset = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.value

        tessellation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tessellation, Unset):
            tessellation = self.tessellation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if compressed is not UNSET:
            field_dict["compressed"] = compressed
        if decompressed is not UNSET:
            field_dict["decompressed"] = decompressed
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if estimated_memory_usage_in_bytes is not UNSET:
            field_dict["estimatedMemoryUsageInBytes"] = estimated_memory_usage_in_bytes
        if has_tessellation_error is not UNSET:
            field_dict["hasTessellationError"] = has_tessellation_error
        if setting_index is not UNSET:
            field_dict["settingIndex"] = setting_index
        if appearance is not UNSET:
            field_dict["appearance"] = appearance
        if belongs_to_flattened_sheet_metal_body is not UNSET:
            field_dict["belongsToFlattenedSheetMetalBody"] = belongs_to_flattened_sheet_metal_body
        if body_id is not UNSET:
            field_dict["bodyId"] = body_id
        if color is not UNSET:
            field_dict["color"] = color
        if deterministic_id is not UNSET:
            field_dict["deterministicId"] = deterministic_id
        if sheet_metal_model_id is not UNSET:
            field_dict["sheetMetalModelId"] = sheet_metal_model_id
        if style is not UNSET:
            field_dict["style"] = style
        if tessellation is not UNSET:
            field_dict["tessellation"] = tessellation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_entity_geometry_35 import BTEntityGeometry35
        from ..models.bt_graphics_appearance_1152 import BTGraphicsAppearance1152
        from ..models.bt_tessellated_geometry_2576 import BTTessellatedGeometry2576

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        compressed = d.pop("compressed", UNSET)

        _decompressed = d.pop("decompressed", UNSET)
        decompressed: BTEntityGeometry35 | Unset
        if isinstance(_decompressed, Unset):
            decompressed = UNSET
        else:
            decompressed = BTEntityGeometry35.from_dict(_decompressed)

        error_code = d.pop("errorCode", UNSET)

        estimated_memory_usage_in_bytes = d.pop("estimatedMemoryUsageInBytes", UNSET)

        has_tessellation_error = d.pop("hasTessellationError", UNSET)

        setting_index = d.pop("settingIndex", UNSET)

        _appearance = d.pop("appearance", UNSET)
        appearance: BTGraphicsAppearance1152 | Unset
        if isinstance(_appearance, Unset):
            appearance = UNSET
        else:
            appearance = BTGraphicsAppearance1152.from_dict(_appearance)

        belongs_to_flattened_sheet_metal_body = d.pop("belongsToFlattenedSheetMetalBody", UNSET)

        body_id = d.pop("bodyId", UNSET)

        _color = d.pop("color", UNSET)
        color: GBTDebugEntityColor | Unset
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = GBTDebugEntityColor(_color)

        deterministic_id = d.pop("deterministicId", UNSET)

        sheet_metal_model_id = d.pop("sheetMetalModelId", UNSET)

        _style = d.pop("style", UNSET)
        style: GBTDebugEntityStyle | Unset
        if isinstance(_style, Unset):
            style = UNSET
        else:
            style = GBTDebugEntityStyle(_style)

        _tessellation = d.pop("tessellation", UNSET)
        tessellation: BTTessellatedGeometry2576 | Unset
        if isinstance(_tessellation, Unset):
            tessellation = UNSET
        else:
            tessellation = BTTessellatedGeometry2576.from_dict(_tessellation)

        bt_debug_geometry_2059 = cls(
            bt_type=bt_type,
            compressed=compressed,
            decompressed=decompressed,
            error_code=error_code,
            estimated_memory_usage_in_bytes=estimated_memory_usage_in_bytes,
            has_tessellation_error=has_tessellation_error,
            setting_index=setting_index,
            appearance=appearance,
            belongs_to_flattened_sheet_metal_body=belongs_to_flattened_sheet_metal_body,
            body_id=body_id,
            color=color,
            deterministic_id=deterministic_id,
            sheet_metal_model_id=sheet_metal_model_id,
            style=style,
            tessellation=tessellation,
        )

        bt_debug_geometry_2059.additional_properties = d
        return bt_debug_geometry_2059

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
