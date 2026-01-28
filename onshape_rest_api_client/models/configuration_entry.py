from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigurationEntry")


@_attrs_define
class ConfigurationEntry:
    """
    Attributes:
        parameter_id (str | Unset):
        parameter_value (str | Unset):
    """

    parameter_id: str | Unset = UNSET
    parameter_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameter_id = self.parameter_id

        parameter_value = self.parameter_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parameter_id is not UNSET:
            field_dict["parameterId"] = parameter_id
        if parameter_value is not UNSET:
            field_dict["parameterValue"] = parameter_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parameter_id = d.pop("parameterId", UNSET)

        parameter_value = d.pop("parameterValue", UNSET)

        configuration_entry = cls(
            parameter_id=parameter_id,
            parameter_value=parameter_value,
        )

        configuration_entry.additional_properties = d
        return configuration_entry

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
