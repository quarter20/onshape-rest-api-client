from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btm_configured_value_1341 import BTMConfiguredValue1341


T = TypeVar("T", bound="BTMSuppressionStateConfigured2598")


@_attrs_define
class BTMSuppressionStateConfigured2598:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Microversion that resulted from the import.
        node_id (str | Unset):
        suppression_configured (bool | Unset):
        configuration_parameter_id (str | Unset):
        configuration_parameter_id_field_index (int | Unset):
        values (list[BTMConfiguredValue1341] | Unset):
        values_field_index (int | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    node_id: str | Unset = UNSET
    suppression_configured: bool | Unset = UNSET
    configuration_parameter_id: str | Unset = UNSET
    configuration_parameter_id_field_index: int | Unset = UNSET
    values: list[BTMConfiguredValue1341] | Unset = UNSET
    values_field_index: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        node_id = self.node_id

        suppression_configured = self.suppression_configured

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
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if suppression_configured is not UNSET:
            field_dict["suppressionConfigured"] = suppression_configured
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

        node_id = d.pop("nodeId", UNSET)

        suppression_configured = d.pop("suppressionConfigured", UNSET)

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

        btm_suppression_state_configured_2598 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            node_id=node_id,
            suppression_configured=suppression_configured,
            configuration_parameter_id=configuration_parameter_id,
            configuration_parameter_id_field_index=configuration_parameter_id_field_index,
            values=values,
            values_field_index=values_field_index,
        )

        btm_suppression_state_configured_2598.additional_properties = d
        return btm_suppression_state_configured_2598

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
