from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.configuration_info_entry import ConfigurationInfoEntry


T = TypeVar("T", bound="BTConfigurationInfo")


@_attrs_define
class BTConfigurationInfo:
    """
    Attributes:
        is_standard_content (bool | Unset):
        parameters (list[ConfigurationInfoEntry] | Unset):
    """

    is_standard_content: bool | Unset = UNSET
    parameters: list[ConfigurationInfoEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_standard_content = self.is_standard_content

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_standard_content is not UNSET:
            field_dict["isStandardContent"] = is_standard_content
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configuration_info_entry import ConfigurationInfoEntry

        d = dict(src_dict)
        is_standard_content = d.pop("isStandardContent", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: list[ConfigurationInfoEntry] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = ConfigurationInfoEntry.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        bt_configuration_info = cls(
            is_standard_content=is_standard_content,
            parameters=parameters,
        )

        bt_configuration_info.additional_properties = d
        return bt_configuration_info

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
