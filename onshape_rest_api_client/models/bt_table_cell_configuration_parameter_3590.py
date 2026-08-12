from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_parameter_spec_6 import BTParameterSpec6
    from ..models.bt_table_cell_configuration_parameter_3590_configuration_parameter_id_to_value import (
        BTTableCellConfigurationParameter3590ConfigurationParameterIdToValue,
    )
    from ..models.bt_table_cell_modifier_4883 import BTTableCellModifier4883
    from ..models.btm_configuration_parameter_819 import BTMConfigurationParameter819
    from ..models.btm_parameter_1 import BTMParameter1


T = TypeVar("T", bound="BTTableCellConfigurationParameter3590")


@_attrs_define
class BTTableCellConfigurationParameter3590:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        is_ever_visible (bool | Unset):
        is_read_only (bool | Unset):
        modifiers (list[BTTableCellModifier4883] | Unset):
        error (str | Unset):
        info (str | Unset):
        override_spec (BTParameterSpec6 | Unset):
        parameter (BTMParameter1 | Unset): A list of parameter values for instantiation of the feature spec. Parameters
            are present for all defined parameters, even if not used in a specific instantiation.
        warning (str | Unset):
        configuration_parameter_id_to_value (BTTableCellConfigurationParameter3590ConfigurationParameterIdToValue |
            Unset):
        configuration_parameters (list[BTMConfigurationParameter819] | Unset):
    """

    bt_type: str | Unset = UNSET
    is_ever_visible: bool | Unset = UNSET
    is_read_only: bool | Unset = UNSET
    modifiers: list[BTTableCellModifier4883] | Unset = UNSET
    error: str | Unset = UNSET
    info: str | Unset = UNSET
    override_spec: BTParameterSpec6 | Unset = UNSET
    parameter: BTMParameter1 | Unset = UNSET
    warning: str | Unset = UNSET
    configuration_parameter_id_to_value: (
        BTTableCellConfigurationParameter3590ConfigurationParameterIdToValue | Unset
    ) = UNSET
    configuration_parameters: list[BTMConfigurationParameter819] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        is_ever_visible = self.is_ever_visible

        is_read_only = self.is_read_only

        modifiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.modifiers, Unset):
            modifiers = []
            for modifiers_item_data in self.modifiers:
                modifiers_item = modifiers_item_data.to_dict()
                modifiers.append(modifiers_item)

        error = self.error

        info = self.info

        override_spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.override_spec, Unset):
            override_spec = self.override_spec.to_dict()

        parameter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameter, Unset):
            parameter = self.parameter.to_dict()

        warning = self.warning

        configuration_parameter_id_to_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration_parameter_id_to_value, Unset):
            configuration_parameter_id_to_value = self.configuration_parameter_id_to_value.to_dict()

        configuration_parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configuration_parameters, Unset):
            configuration_parameters = []
            for configuration_parameters_item_data in self.configuration_parameters:
                configuration_parameters_item = configuration_parameters_item_data.to_dict()
                configuration_parameters.append(configuration_parameters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if is_ever_visible is not UNSET:
            field_dict["isEverVisible"] = is_ever_visible
        if is_read_only is not UNSET:
            field_dict["isReadOnly"] = is_read_only
        if modifiers is not UNSET:
            field_dict["modifiers"] = modifiers
        if error is not UNSET:
            field_dict["error"] = error
        if info is not UNSET:
            field_dict["info"] = info
        if override_spec is not UNSET:
            field_dict["overrideSpec"] = override_spec
        if parameter is not UNSET:
            field_dict["parameter"] = parameter
        if warning is not UNSET:
            field_dict["warning"] = warning
        if configuration_parameter_id_to_value is not UNSET:
            field_dict["configurationParameterIdToValue"] = configuration_parameter_id_to_value
        if configuration_parameters is not UNSET:
            field_dict["configurationParameters"] = configuration_parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_parameter_spec_6 import BTParameterSpec6
        from ..models.bt_table_cell_configuration_parameter_3590_configuration_parameter_id_to_value import (
            BTTableCellConfigurationParameter3590ConfigurationParameterIdToValue,
        )
        from ..models.bt_table_cell_modifier_4883 import BTTableCellModifier4883
        from ..models.btm_configuration_parameter_819 import BTMConfigurationParameter819
        from ..models.btm_parameter_1 import BTMParameter1

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        is_ever_visible = d.pop("isEverVisible", UNSET)

        is_read_only = d.pop("isReadOnly", UNSET)

        _modifiers = d.pop("modifiers", UNSET)
        modifiers: list[BTTableCellModifier4883] | Unset = UNSET
        if _modifiers is not UNSET:
            modifiers = []
            for modifiers_item_data in _modifiers:
                modifiers_item = BTTableCellModifier4883.from_dict(modifiers_item_data)

                modifiers.append(modifiers_item)

        error = d.pop("error", UNSET)

        info = d.pop("info", UNSET)

        _override_spec = d.pop("overrideSpec", UNSET)
        override_spec: BTParameterSpec6 | Unset
        if isinstance(_override_spec, Unset):
            override_spec = UNSET
        else:
            override_spec = BTParameterSpec6.from_dict(_override_spec)

        _parameter = d.pop("parameter", UNSET)
        parameter: BTMParameter1 | Unset
        if isinstance(_parameter, Unset):
            parameter = UNSET
        else:
            parameter = BTMParameter1.from_dict(_parameter)

        warning = d.pop("warning", UNSET)

        _configuration_parameter_id_to_value = d.pop("configurationParameterIdToValue", UNSET)
        configuration_parameter_id_to_value: (
            BTTableCellConfigurationParameter3590ConfigurationParameterIdToValue | Unset
        )
        if isinstance(_configuration_parameter_id_to_value, Unset):
            configuration_parameter_id_to_value = UNSET
        else:
            configuration_parameter_id_to_value = (
                BTTableCellConfigurationParameter3590ConfigurationParameterIdToValue.from_dict(
                    _configuration_parameter_id_to_value
                )
            )

        _configuration_parameters = d.pop("configurationParameters", UNSET)
        configuration_parameters: list[BTMConfigurationParameter819] | Unset = UNSET
        if _configuration_parameters is not UNSET:
            configuration_parameters = []
            for configuration_parameters_item_data in _configuration_parameters:
                configuration_parameters_item = BTMConfigurationParameter819.from_dict(
                    configuration_parameters_item_data
                )

                configuration_parameters.append(configuration_parameters_item)

        bt_table_cell_configuration_parameter_3590 = cls(
            bt_type=bt_type,
            is_ever_visible=is_ever_visible,
            is_read_only=is_read_only,
            modifiers=modifiers,
            error=error,
            info=info,
            override_spec=override_spec,
            parameter=parameter,
            warning=warning,
            configuration_parameter_id_to_value=configuration_parameter_id_to_value,
            configuration_parameters=configuration_parameters,
        )

        bt_table_cell_configuration_parameter_3590.additional_properties = d
        return bt_table_cell_configuration_parameter_3590

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
