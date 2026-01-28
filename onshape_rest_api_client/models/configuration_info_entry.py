from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigurationInfoEntry")


@_attrs_define
class ConfigurationInfoEntry:
    """
    Attributes:
        explicit (bool | Unset):
        is_cosmetic (bool | Unset):
        is_visible (bool | Unset):
        parameter_abbreviated_display_value (str | Unset):
        parameter_display_value (str | Unset):
        parameter_id (str | Unset):
        parameter_name (str | Unset):
        parameter_type (int | Unset):
        parameter_value (str | Unset):
    """

    explicit: bool | Unset = UNSET
    is_cosmetic: bool | Unset = UNSET
    is_visible: bool | Unset = UNSET
    parameter_abbreviated_display_value: str | Unset = UNSET
    parameter_display_value: str | Unset = UNSET
    parameter_id: str | Unset = UNSET
    parameter_name: str | Unset = UNSET
    parameter_type: int | Unset = UNSET
    parameter_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        explicit = self.explicit

        is_cosmetic = self.is_cosmetic

        is_visible = self.is_visible

        parameter_abbreviated_display_value = self.parameter_abbreviated_display_value

        parameter_display_value = self.parameter_display_value

        parameter_id = self.parameter_id

        parameter_name = self.parameter_name

        parameter_type = self.parameter_type

        parameter_value = self.parameter_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if explicit is not UNSET:
            field_dict["explicit"] = explicit
        if is_cosmetic is not UNSET:
            field_dict["isCosmetic"] = is_cosmetic
        if is_visible is not UNSET:
            field_dict["isVisible"] = is_visible
        if parameter_abbreviated_display_value is not UNSET:
            field_dict["parameterAbbreviatedDisplayValue"] = parameter_abbreviated_display_value
        if parameter_display_value is not UNSET:
            field_dict["parameterDisplayValue"] = parameter_display_value
        if parameter_id is not UNSET:
            field_dict["parameterId"] = parameter_id
        if parameter_name is not UNSET:
            field_dict["parameterName"] = parameter_name
        if parameter_type is not UNSET:
            field_dict["parameterType"] = parameter_type
        if parameter_value is not UNSET:
            field_dict["parameterValue"] = parameter_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        explicit = d.pop("explicit", UNSET)

        is_cosmetic = d.pop("isCosmetic", UNSET)

        is_visible = d.pop("isVisible", UNSET)

        parameter_abbreviated_display_value = d.pop("parameterAbbreviatedDisplayValue", UNSET)

        parameter_display_value = d.pop("parameterDisplayValue", UNSET)

        parameter_id = d.pop("parameterId", UNSET)

        parameter_name = d.pop("parameterName", UNSET)

        parameter_type = d.pop("parameterType", UNSET)

        parameter_value = d.pop("parameterValue", UNSET)

        configuration_info_entry = cls(
            explicit=explicit,
            is_cosmetic=is_cosmetic,
            is_visible=is_visible,
            parameter_abbreviated_display_value=parameter_abbreviated_display_value,
            parameter_display_value=parameter_display_value,
            parameter_id=parameter_id,
            parameter_name=parameter_name,
            parameter_type=parameter_type,
            parameter_value=parameter_value,
        )

        configuration_info_entry.additional_properties = d
        return configuration_info_entry

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
