from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.configuration_entry import ConfigurationEntry


T = TypeVar("T", bound="BTConfigurationParams")


@_attrs_define
class BTConfigurationParams:
    """
    Attributes:
        parameters (list[ConfigurationEntry] | Unset):
        standard_content_parameters_id (str | Unset):
    """

    parameters: list[ConfigurationEntry] | Unset = UNSET
    standard_content_parameters_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        standard_content_parameters_id = self.standard_content_parameters_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if standard_content_parameters_id is not UNSET:
            field_dict["standardContentParametersId"] = standard_content_parameters_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configuration_entry import ConfigurationEntry

        d = dict(src_dict)
        _parameters = d.pop("parameters", UNSET)
        parameters: list[ConfigurationEntry] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = ConfigurationEntry.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        standard_content_parameters_id = d.pop("standardContentParametersId", UNSET)

        bt_configuration_params = cls(
            parameters=parameters,
            standard_content_parameters_id=standard_content_parameters_id,
        )

        bt_configuration_params.additional_properties = d
        return bt_configuration_params

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
