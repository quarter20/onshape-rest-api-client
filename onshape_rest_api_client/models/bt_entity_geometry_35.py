from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTEntityGeometry35")


@_attrs_define
class BTEntityGeometry35:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        compressed (bool | Unset):
        decompressed (BTEntityGeometry35 | Unset):
        error_code (int | Unset):
        estimated_memory_usage_in_bytes (int | Unset):
        has_tessellation_error (bool | Unset):
        setting_index (int | Unset):
    """

    bt_type: str | Unset = UNSET
    compressed: bool | Unset = UNSET
    decompressed: BTEntityGeometry35 | Unset = UNSET
    error_code: int | Unset = UNSET
    estimated_memory_usage_in_bytes: int | Unset = UNSET
    has_tessellation_error: bool | Unset = UNSET
    setting_index: int | Unset = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        bt_entity_geometry_35 = cls(
            bt_type=bt_type,
            compressed=compressed,
            decompressed=decompressed,
            error_code=error_code,
            estimated_memory_usage_in_bytes=estimated_memory_usage_in_bytes,
            has_tessellation_error=has_tessellation_error,
            setting_index=setting_index,
        )

        bt_entity_geometry_35.additional_properties = d
        return bt_entity_geometry_35

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
