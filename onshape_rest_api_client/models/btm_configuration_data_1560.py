from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btm_configuration_data_1560_current_fs_values import BTMConfigurationData1560CurrentFSValues
    from ..models.btm_configuration_data_1560_default_configuration_values import (
        BTMConfigurationData1560DefaultConfigurationValues,
    )
    from ..models.btm_configuration_parameter_819 import BTMConfigurationParameter819
    from ..models.btm_parameter_1 import BTMParameter1


T = TypeVar("T", bound="BTMConfigurationData1560")


@_attrs_define
class BTMConfigurationData1560:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Microversion that resulted from the import.
        node_id (str | Unset):
        configuration_parameters (list[BTMConfigurationParameter819] | Unset):
        cosmetic_parameter_ids (list[str] | Unset):
        current_configuration (list[BTMParameter1] | Unset):
        current_fs_values (BTMConfigurationData1560CurrentFSValues | Unset):
        default_configuration_values (BTMConfigurationData1560DefaultConfigurationValues | Unset):
        sync_and_passthrough_reference_node_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    node_id: str | Unset = UNSET
    configuration_parameters: list[BTMConfigurationParameter819] | Unset = UNSET
    cosmetic_parameter_ids: list[str] | Unset = UNSET
    current_configuration: list[BTMParameter1] | Unset = UNSET
    current_fs_values: BTMConfigurationData1560CurrentFSValues | Unset = UNSET
    default_configuration_values: BTMConfigurationData1560DefaultConfigurationValues | Unset = UNSET
    sync_and_passthrough_reference_node_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        node_id = self.node_id

        configuration_parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configuration_parameters, Unset):
            configuration_parameters = []
            for configuration_parameters_item_data in self.configuration_parameters:
                configuration_parameters_item = configuration_parameters_item_data.to_dict()
                configuration_parameters.append(configuration_parameters_item)

        cosmetic_parameter_ids: list[str] | Unset = UNSET
        if not isinstance(self.cosmetic_parameter_ids, Unset):
            cosmetic_parameter_ids = self.cosmetic_parameter_ids

        current_configuration: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.current_configuration, Unset):
            current_configuration = []
            for current_configuration_item_data in self.current_configuration:
                current_configuration_item = current_configuration_item_data.to_dict()
                current_configuration.append(current_configuration_item)

        current_fs_values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_fs_values, Unset):
            current_fs_values = self.current_fs_values.to_dict()

        default_configuration_values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_configuration_values, Unset):
            default_configuration_values = self.default_configuration_values.to_dict()

        sync_and_passthrough_reference_node_id = self.sync_and_passthrough_reference_node_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if configuration_parameters is not UNSET:
            field_dict["configurationParameters"] = configuration_parameters
        if cosmetic_parameter_ids is not UNSET:
            field_dict["cosmeticParameterIds"] = cosmetic_parameter_ids
        if current_configuration is not UNSET:
            field_dict["currentConfiguration"] = current_configuration
        if current_fs_values is not UNSET:
            field_dict["currentFSValues"] = current_fs_values
        if default_configuration_values is not UNSET:
            field_dict["defaultConfigurationValues"] = default_configuration_values
        if sync_and_passthrough_reference_node_id is not UNSET:
            field_dict["syncAndPassthroughReferenceNodeId"] = sync_and_passthrough_reference_node_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btm_configuration_data_1560_current_fs_values import BTMConfigurationData1560CurrentFSValues
        from ..models.btm_configuration_data_1560_default_configuration_values import (
            BTMConfigurationData1560DefaultConfigurationValues,
        )
        from ..models.btm_configuration_parameter_819 import BTMConfigurationParameter819
        from ..models.btm_parameter_1 import BTMParameter1

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _configuration_parameters = d.pop("configurationParameters", UNSET)
        configuration_parameters: list[BTMConfigurationParameter819] | Unset = UNSET
        if _configuration_parameters is not UNSET:
            configuration_parameters = []
            for configuration_parameters_item_data in _configuration_parameters:
                configuration_parameters_item = BTMConfigurationParameter819.from_dict(
                    configuration_parameters_item_data
                )

                configuration_parameters.append(configuration_parameters_item)

        cosmetic_parameter_ids = cast(list[str], d.pop("cosmeticParameterIds", UNSET))

        _current_configuration = d.pop("currentConfiguration", UNSET)
        current_configuration: list[BTMParameter1] | Unset = UNSET
        if _current_configuration is not UNSET:
            current_configuration = []
            for current_configuration_item_data in _current_configuration:
                current_configuration_item = BTMParameter1.from_dict(current_configuration_item_data)

                current_configuration.append(current_configuration_item)

        _current_fs_values = d.pop("currentFSValues", UNSET)
        current_fs_values: BTMConfigurationData1560CurrentFSValues | Unset
        if isinstance(_current_fs_values, Unset):
            current_fs_values = UNSET
        else:
            current_fs_values = BTMConfigurationData1560CurrentFSValues.from_dict(_current_fs_values)

        _default_configuration_values = d.pop("defaultConfigurationValues", UNSET)
        default_configuration_values: BTMConfigurationData1560DefaultConfigurationValues | Unset
        if isinstance(_default_configuration_values, Unset):
            default_configuration_values = UNSET
        else:
            default_configuration_values = BTMConfigurationData1560DefaultConfigurationValues.from_dict(
                _default_configuration_values
            )

        sync_and_passthrough_reference_node_id = d.pop("syncAndPassthroughReferenceNodeId", UNSET)

        btm_configuration_data_1560 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            node_id=node_id,
            configuration_parameters=configuration_parameters,
            cosmetic_parameter_ids=cosmetic_parameter_ids,
            current_configuration=current_configuration,
            current_fs_values=current_fs_values,
            default_configuration_values=default_configuration_values,
            sync_and_passthrough_reference_node_id=sync_and_passthrough_reference_node_id,
        )

        btm_configuration_data_1560.additional_properties = d
        return btm_configuration_data_1560

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
