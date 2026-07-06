from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_instance_properties_4828_property_values import BTInstanceProperties4828PropertyValues
    from ..models.bt_one_configuration_properties_1900 import BTOneConfigurationProperties1900


T = TypeVar("T", bound="BTInstanceProperties4828")


@_attrs_define
class BTInstanceProperties4828:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        configuration_properties (list[BTOneConfigurationProperties1900] | Unset):
        configured_property_ids (list[str] | Unset):
        is_in_microversion (bool | Unset):
        node_id (str | Unset):
        property_values (BTInstanceProperties4828PropertyValues | Unset):
    """

    bt_type: str | Unset = UNSET
    configuration_properties: list[BTOneConfigurationProperties1900] | Unset = UNSET
    configured_property_ids: list[str] | Unset = UNSET
    is_in_microversion: bool | Unset = UNSET
    node_id: str | Unset = UNSET
    property_values: BTInstanceProperties4828PropertyValues | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        configuration_properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configuration_properties, Unset):
            configuration_properties = []
            for configuration_properties_item_data in self.configuration_properties:
                configuration_properties_item = configuration_properties_item_data.to_dict()
                configuration_properties.append(configuration_properties_item)

        configured_property_ids: list[str] | Unset = UNSET
        if not isinstance(self.configured_property_ids, Unset):
            configured_property_ids = self.configured_property_ids

        is_in_microversion = self.is_in_microversion

        node_id = self.node_id

        property_values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.property_values, Unset):
            property_values = self.property_values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if configuration_properties is not UNSET:
            field_dict["configurationProperties"] = configuration_properties
        if configured_property_ids is not UNSET:
            field_dict["configuredPropertyIds"] = configured_property_ids
        if is_in_microversion is not UNSET:
            field_dict["isInMicroversion"] = is_in_microversion
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if property_values is not UNSET:
            field_dict["propertyValues"] = property_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_instance_properties_4828_property_values import BTInstanceProperties4828PropertyValues
        from ..models.bt_one_configuration_properties_1900 import BTOneConfigurationProperties1900

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _configuration_properties = d.pop("configurationProperties", UNSET)
        configuration_properties: list[BTOneConfigurationProperties1900] | Unset = UNSET
        if _configuration_properties is not UNSET:
            configuration_properties = []
            for configuration_properties_item_data in _configuration_properties:
                configuration_properties_item = BTOneConfigurationProperties1900.from_dict(
                    configuration_properties_item_data
                )

                configuration_properties.append(configuration_properties_item)

        configured_property_ids = cast(list[str], d.pop("configuredPropertyIds", UNSET))

        is_in_microversion = d.pop("isInMicroversion", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _property_values = d.pop("propertyValues", UNSET)
        property_values: BTInstanceProperties4828PropertyValues | Unset
        if isinstance(_property_values, Unset):
            property_values = UNSET
        else:
            property_values = BTInstanceProperties4828PropertyValues.from_dict(_property_values)

        bt_instance_properties_4828 = cls(
            bt_type=bt_type,
            configuration_properties=configuration_properties,
            configured_property_ids=configured_property_ids,
            is_in_microversion=is_in_microversion,
            node_id=node_id,
            property_values=property_values,
        )

        bt_instance_properties_4828.additional_properties = d
        return bt_instance_properties_4828

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
