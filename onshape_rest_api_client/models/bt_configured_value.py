from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_configured_value_configuration_to_value import BTConfiguredValueConfigurationToValue


T = TypeVar("T", bound="BTConfiguredValue")


@_attrs_define
class BTConfiguredValue:
    """Configured variable description, if configured

    Attributes:
        configuration_parameter_id (str | Unset): The configuration parameter configuring this value, if configured
        configuration_to_value (BTConfiguredValueConfigurationToValue | Unset): Configuration to value, required if
            configuration parameter id is specified
    """

    configuration_parameter_id: str | Unset = UNSET
    configuration_to_value: BTConfiguredValueConfigurationToValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration_parameter_id = self.configuration_parameter_id

        configuration_to_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration_to_value, Unset):
            configuration_to_value = self.configuration_to_value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration_parameter_id is not UNSET:
            field_dict["configurationParameterId"] = configuration_parameter_id
        if configuration_to_value is not UNSET:
            field_dict["configurationToValue"] = configuration_to_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_configured_value_configuration_to_value import BTConfiguredValueConfigurationToValue

        d = dict(src_dict)
        configuration_parameter_id = d.pop("configurationParameterId", UNSET)

        _configuration_to_value = d.pop("configurationToValue", UNSET)
        configuration_to_value: BTConfiguredValueConfigurationToValue | Unset
        if isinstance(_configuration_to_value, Unset):
            configuration_to_value = UNSET
        else:
            configuration_to_value = BTConfiguredValueConfigurationToValue.from_dict(_configuration_to_value)

        bt_configured_value = cls(
            configuration_parameter_id=configuration_parameter_id,
            configuration_to_value=configuration_to_value,
        )

        bt_configured_value.additional_properties = d
        return bt_configured_value

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
