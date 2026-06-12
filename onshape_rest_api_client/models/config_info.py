from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigInfo")


@_attrs_define
class ConfigInfo:
    """The configuration parameters of the referring element.

    Attributes:
        display_value (str | Unset): The formatted display value of the configuration parameter.
        display_value_abbr_unit (str | Unset): The abbreviated display value with unit for the configuration parameter.
        id (str | Unset): The configuration parameter ID.
        name (str | Unset): The configuration parameter name.
        type_ (int | Unset): The configuration parameter type. `0: ENUM | 1: BOOLEAN | 2: STRING | 3: QUANTITY`
        value (str | Unset): The raw value of the configuration parameter.
    """

    display_value: str | Unset = UNSET
    display_value_abbr_unit: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: int | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_value = self.display_value

        display_value_abbr_unit = self.display_value_abbr_unit

        id = self.id

        name = self.name

        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value
        if display_value_abbr_unit is not UNSET:
            field_dict["displayValueAbbrUnit"] = display_value_abbr_unit
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_value = d.pop("displayValue", UNSET)

        display_value_abbr_unit = d.pop("displayValueAbbrUnit", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        config_info = cls(
            display_value=display_value,
            display_value_abbr_unit=display_value_abbr_unit,
            id=id,
            name=name,
            type_=type_,
            value=value,
        )

        config_info.additional_properties = d
        return config_info

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
