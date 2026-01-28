from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btm_configuration_parameter_819 import BTMConfigurationParameter819
    from ..models.btm_parameter_1 import BTMParameter1


T = TypeVar("T", bound="BTConfigurationUpdateCall2933")


@_attrs_define
class BTConfigurationUpdateCall2933:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        configuration_parameters (list[BTMConfigurationParameter819] | Unset):
        current_configuration (list[BTMParameter1] | Unset):
        library_version (int | Unset): FeatureScript version used in the Part Studio. Do not modify.
        microversion_skew (bool | Unset): On output, `true` indicates a microversion mismatch was encountered.
        reject_microversion_skew (bool | Unset): If `true`, the call will refuse to make the addition if the current
            microversion for the document does not match the source microversion. If `false`, a best-effort attempt is made
            to re-interpret the feature addition in the context of a newer document microversion.
        serialization_version (str | Unset): Version of the structure serialization rules used to encode the output.
            This enables incompatibility detection during software updates.
        source_microversion (str | Unset): The state from which the result was extracted. Geometry ID interpretation is
            dependent on this document microversion.
    """

    bt_type: str | Unset = UNSET
    configuration_parameters: list[BTMConfigurationParameter819] | Unset = UNSET
    current_configuration: list[BTMParameter1] | Unset = UNSET
    library_version: int | Unset = UNSET
    microversion_skew: bool | Unset = UNSET
    reject_microversion_skew: bool | Unset = UNSET
    serialization_version: str | Unset = UNSET
    source_microversion: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        configuration_parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configuration_parameters, Unset):
            configuration_parameters = []
            for configuration_parameters_item_data in self.configuration_parameters:
                configuration_parameters_item = configuration_parameters_item_data.to_dict()
                configuration_parameters.append(configuration_parameters_item)

        current_configuration: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.current_configuration, Unset):
            current_configuration = []
            for current_configuration_item_data in self.current_configuration:
                current_configuration_item = current_configuration_item_data.to_dict()
                current_configuration.append(current_configuration_item)

        library_version = self.library_version

        microversion_skew = self.microversion_skew

        reject_microversion_skew = self.reject_microversion_skew

        serialization_version = self.serialization_version

        source_microversion = self.source_microversion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if configuration_parameters is not UNSET:
            field_dict["configurationParameters"] = configuration_parameters
        if current_configuration is not UNSET:
            field_dict["currentConfiguration"] = current_configuration
        if library_version is not UNSET:
            field_dict["libraryVersion"] = library_version
        if microversion_skew is not UNSET:
            field_dict["microversionSkew"] = microversion_skew
        if reject_microversion_skew is not UNSET:
            field_dict["rejectMicroversionSkew"] = reject_microversion_skew
        if serialization_version is not UNSET:
            field_dict["serializationVersion"] = serialization_version
        if source_microversion is not UNSET:
            field_dict["sourceMicroversion"] = source_microversion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btm_configuration_parameter_819 import BTMConfigurationParameter819
        from ..models.btm_parameter_1 import BTMParameter1

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _configuration_parameters = d.pop("configurationParameters", UNSET)
        configuration_parameters: list[BTMConfigurationParameter819] | Unset = UNSET
        if _configuration_parameters is not UNSET:
            configuration_parameters = []
            for configuration_parameters_item_data in _configuration_parameters:
                configuration_parameters_item = BTMConfigurationParameter819.from_dict(
                    configuration_parameters_item_data
                )

                configuration_parameters.append(configuration_parameters_item)

        _current_configuration = d.pop("currentConfiguration", UNSET)
        current_configuration: list[BTMParameter1] | Unset = UNSET
        if _current_configuration is not UNSET:
            current_configuration = []
            for current_configuration_item_data in _current_configuration:
                current_configuration_item = BTMParameter1.from_dict(current_configuration_item_data)

                current_configuration.append(current_configuration_item)

        library_version = d.pop("libraryVersion", UNSET)

        microversion_skew = d.pop("microversionSkew", UNSET)

        reject_microversion_skew = d.pop("rejectMicroversionSkew", UNSET)

        serialization_version = d.pop("serializationVersion", UNSET)

        source_microversion = d.pop("sourceMicroversion", UNSET)

        bt_configuration_update_call_2933 = cls(
            bt_type=bt_type,
            configuration_parameters=configuration_parameters,
            current_configuration=current_configuration,
            library_version=library_version,
            microversion_skew=microversion_skew,
            reject_microversion_skew=reject_microversion_skew,
            serialization_version=serialization_version,
            source_microversion=source_microversion,
        )

        bt_configuration_update_call_2933.additional_properties = d
        return bt_configuration_update_call_2933

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
