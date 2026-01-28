from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_location_info_226 import BTLocationInfo226


T = TypeVar("T", bound="BTNullableQuantityRange1340")


@_attrs_define
class BTNullableQuantityRange1340:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        default_value (float | Unset):
        location (BTLocationInfo226 | Unset):
        max_value (float | Unset):
        min_value (float | Unset):
        units (str | Unset):
        has_default_value (bool | Unset):
        has_max_value (bool | Unset):
        has_min_value (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    default_value: float | Unset = UNSET
    location: BTLocationInfo226 | Unset = UNSET
    max_value: float | Unset = UNSET
    min_value: float | Unset = UNSET
    units: str | Unset = UNSET
    has_default_value: bool | Unset = UNSET
    has_max_value: bool | Unset = UNSET
    has_min_value: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        default_value = self.default_value

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        max_value = self.max_value

        min_value = self.min_value

        units = self.units

        has_default_value = self.has_default_value

        has_max_value = self.has_max_value

        has_min_value = self.has_min_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if location is not UNSET:
            field_dict["location"] = location
        if max_value is not UNSET:
            field_dict["maxValue"] = max_value
        if min_value is not UNSET:
            field_dict["minValue"] = min_value
        if units is not UNSET:
            field_dict["units"] = units
        if has_default_value is not UNSET:
            field_dict["hasDefaultValue"] = has_default_value
        if has_max_value is not UNSET:
            field_dict["hasMaxValue"] = has_max_value
        if has_min_value is not UNSET:
            field_dict["hasMinValue"] = has_min_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_location_info_226 import BTLocationInfo226

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        _location = d.pop("location", UNSET)
        location: BTLocationInfo226 | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = BTLocationInfo226.from_dict(_location)

        max_value = d.pop("maxValue", UNSET)

        min_value = d.pop("minValue", UNSET)

        units = d.pop("units", UNSET)

        has_default_value = d.pop("hasDefaultValue", UNSET)

        has_max_value = d.pop("hasMaxValue", UNSET)

        has_min_value = d.pop("hasMinValue", UNSET)

        bt_nullable_quantity_range_1340 = cls(
            bt_type=bt_type,
            default_value=default_value,
            location=location,
            max_value=max_value,
            min_value=min_value,
            units=units,
            has_default_value=has_default_value,
            has_max_value=has_max_value,
            has_min_value=has_min_value,
        )

        bt_nullable_quantity_range_1340.additional_properties = d
        return bt_nullable_quantity_range_1340

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
