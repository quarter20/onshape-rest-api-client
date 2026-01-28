from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_one_configuration_part_properties_1661_configuration import (
        BTOneConfigurationPartProperties1661Configuration,
    )
    from ..models.bt_one_part_properties_230 import BTOnePartProperties230


T = TypeVar("T", bound="BTOneConfigurationPartProperties1661")


@_attrs_define
class BTOneConfigurationPartProperties1661:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        configuration (BTOneConfigurationPartProperties1661Configuration | Unset):
        merged (BTOnePartProperties230 | Unset):
        node_id (str | Unset):
        properties (list[BTOnePartProperties230] | Unset):
        property_ids (list[str] | Unset):
    """

    bt_type: str | Unset = UNSET
    configuration: BTOneConfigurationPartProperties1661Configuration | Unset = UNSET
    merged: BTOnePartProperties230 | Unset = UNSET
    node_id: str | Unset = UNSET
    properties: list[BTOnePartProperties230] | Unset = UNSET
    property_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        merged: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merged, Unset):
            merged = self.merged.to_dict()

        node_id = self.node_id

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        property_ids: list[str] | Unset = UNSET
        if not isinstance(self.property_ids, Unset):
            property_ids = self.property_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if merged is not UNSET:
            field_dict["merged"] = merged
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if properties is not UNSET:
            field_dict["properties"] = properties
        if property_ids is not UNSET:
            field_dict["propertyIds"] = property_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_one_configuration_part_properties_1661_configuration import (
            BTOneConfigurationPartProperties1661Configuration,
        )
        from ..models.bt_one_part_properties_230 import BTOnePartProperties230

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _configuration = d.pop("configuration", UNSET)
        configuration: BTOneConfigurationPartProperties1661Configuration | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = BTOneConfigurationPartProperties1661Configuration.from_dict(_configuration)

        _merged = d.pop("merged", UNSET)
        merged: BTOnePartProperties230 | Unset
        if isinstance(_merged, Unset):
            merged = UNSET
        else:
            merged = BTOnePartProperties230.from_dict(_merged)

        node_id = d.pop("nodeId", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: list[BTOnePartProperties230] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = BTOnePartProperties230.from_dict(properties_item_data)

                properties.append(properties_item)

        property_ids = cast(list[str], d.pop("propertyIds", UNSET))

        bt_one_configuration_part_properties_1661 = cls(
            bt_type=bt_type,
            configuration=configuration,
            merged=merged,
            node_id=node_id,
            properties=properties,
            property_ids=property_ids,
        )

        bt_one_configuration_part_properties_1661.additional_properties = d
        return bt_one_configuration_part_properties_1661

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
