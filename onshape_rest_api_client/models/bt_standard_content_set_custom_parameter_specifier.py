from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_standard_content_parameter_id_and_value import BTStandardContentParameterIdAndValue
    from ..models.bt_standard_content_property_id_and_value import BTStandardContentPropertyIdAndValue


T = TypeVar("T", bound="BTStandardContentSetCustomParameterSpecifier")


@_attrs_define
class BTStandardContentSetCustomParameterSpecifier:
    """Specifies a standard content component along with the custom properties whose values are to be set.

    Attributes:
        custom_parameters (list[BTStandardContentPropertyIdAndValue] | Unset): Non-driving custom parameters whose
            values are to be set.
        parameters (list[BTStandardContentParameterIdAndValue] | Unset): Parameters that drive configuration. Used to
            specify the standard content component to which the custom parameter values are associated.
    """

    custom_parameters: list[BTStandardContentPropertyIdAndValue] | Unset = UNSET
    parameters: list[BTStandardContentParameterIdAndValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_parameters, Unset):
            custom_parameters = []
            for custom_parameters_item_data in self.custom_parameters:
                custom_parameters_item = custom_parameters_item_data.to_dict()
                custom_parameters.append(custom_parameters_item)

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_parameters is not UNSET:
            field_dict["customParameters"] = custom_parameters
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_standard_content_parameter_id_and_value import BTStandardContentParameterIdAndValue
        from ..models.bt_standard_content_property_id_and_value import BTStandardContentPropertyIdAndValue

        d = dict(src_dict)
        _custom_parameters = d.pop("customParameters", UNSET)
        custom_parameters: list[BTStandardContentPropertyIdAndValue] | Unset = UNSET
        if _custom_parameters is not UNSET:
            custom_parameters = []
            for custom_parameters_item_data in _custom_parameters:
                custom_parameters_item = BTStandardContentPropertyIdAndValue.from_dict(custom_parameters_item_data)

                custom_parameters.append(custom_parameters_item)

        _parameters = d.pop("parameters", UNSET)
        parameters: list[BTStandardContentParameterIdAndValue] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = BTStandardContentParameterIdAndValue.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        bt_standard_content_set_custom_parameter_specifier = cls(
            custom_parameters=custom_parameters,
            parameters=parameters,
        )

        bt_standard_content_set_custom_parameter_specifier.additional_properties = d
        return bt_standard_content_set_custom_parameter_specifier

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
