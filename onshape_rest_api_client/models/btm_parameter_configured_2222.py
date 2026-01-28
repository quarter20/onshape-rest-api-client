from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_parameter_library_relation_type import GBTParameterLibraryRelationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btm_configured_value_1341 import BTMConfiguredValue1341


T = TypeVar("T", bound="BTMParameterConfigured2222")


@_attrs_define
class BTMParameterConfigured2222:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Microversion that resulted from the import.
        library_relation_type (GBTParameterLibraryRelationType | Unset):
        node_id (str | Unset): ID of the parameter's node.
        parameter_id (str | Unset): Unique ID of the parameter.
        parameter_name (str | Unset):
        value_string (str | Unset):
        configuration_parameter_id (str | Unset):
        configuration_parameter_id_field_index (int | Unset):
        values (list[BTMConfiguredValue1341] | Unset):
        values_field_index (int | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    library_relation_type: GBTParameterLibraryRelationType | Unset = UNSET
    node_id: str | Unset = UNSET
    parameter_id: str | Unset = UNSET
    parameter_name: str | Unset = UNSET
    value_string: str | Unset = UNSET
    configuration_parameter_id: str | Unset = UNSET
    configuration_parameter_id_field_index: int | Unset = UNSET
    values: list[BTMConfiguredValue1341] | Unset = UNSET
    values_field_index: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        library_relation_type: str | Unset = UNSET
        if not isinstance(self.library_relation_type, Unset):
            library_relation_type = self.library_relation_type.value

        node_id = self.node_id

        parameter_id = self.parameter_id

        parameter_name = self.parameter_name

        value_string = self.value_string

        configuration_parameter_id = self.configuration_parameter_id

        configuration_parameter_id_field_index = self.configuration_parameter_id_field_index

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        values_field_index = self.values_field_index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if library_relation_type is not UNSET:
            field_dict["libraryRelationType"] = library_relation_type
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if parameter_id is not UNSET:
            field_dict["parameterId"] = parameter_id
        if parameter_name is not UNSET:
            field_dict["parameterName"] = parameter_name
        if value_string is not UNSET:
            field_dict["valueString"] = value_string
        if configuration_parameter_id is not UNSET:
            field_dict["configurationParameterId"] = configuration_parameter_id
        if configuration_parameter_id_field_index is not UNSET:
            field_dict["configurationParameterIdFieldIndex"] = configuration_parameter_id_field_index
        if values is not UNSET:
            field_dict["values"] = values
        if values_field_index is not UNSET:
            field_dict["valuesFieldIndex"] = values_field_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btm_configured_value_1341 import BTMConfiguredValue1341

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        _library_relation_type = d.pop("libraryRelationType", UNSET)
        library_relation_type: GBTParameterLibraryRelationType | Unset
        if isinstance(_library_relation_type, Unset):
            library_relation_type = UNSET
        else:
            library_relation_type = GBTParameterLibraryRelationType(_library_relation_type)

        node_id = d.pop("nodeId", UNSET)

        parameter_id = d.pop("parameterId", UNSET)

        parameter_name = d.pop("parameterName", UNSET)

        value_string = d.pop("valueString", UNSET)

        configuration_parameter_id = d.pop("configurationParameterId", UNSET)

        configuration_parameter_id_field_index = d.pop("configurationParameterIdFieldIndex", UNSET)

        _values = d.pop("values", UNSET)
        values: list[BTMConfiguredValue1341] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = BTMConfiguredValue1341.from_dict(values_item_data)

                values.append(values_item)

        values_field_index = d.pop("valuesFieldIndex", UNSET)

        btm_parameter_configured_2222 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            library_relation_type=library_relation_type,
            node_id=node_id,
            parameter_id=parameter_id,
            parameter_name=parameter_name,
            value_string=value_string,
            configuration_parameter_id=configuration_parameter_id,
            configuration_parameter_id_field_index=configuration_parameter_id_field_index,
            values=values,
            values_field_index=values_field_index,
        )

        btm_parameter_configured_2222.additional_properties = d
        return btm_parameter_configured_2222

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
