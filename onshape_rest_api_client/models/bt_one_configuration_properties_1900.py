from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_one_configuration_properties_1900_configuration import (
        BTOneConfigurationProperties1900Configuration,
    )
    from ..models.bt_one_configuration_properties_1900_property_values import (
        BTOneConfigurationProperties1900PropertyValues,
    )


T = TypeVar("T", bound="BTOneConfigurationProperties1900")


@_attrs_define
class BTOneConfigurationProperties1900:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        configuration (BTOneConfigurationProperties1900Configuration | Unset):
        node_id (str | Unset):
        property_ids (list[str] | Unset):
        property_values (BTOneConfigurationProperties1900PropertyValues | Unset):
    """

    bt_type: str | Unset = UNSET
    configuration: BTOneConfigurationProperties1900Configuration | Unset = UNSET
    node_id: str | Unset = UNSET
    property_ids: list[str] | Unset = UNSET
    property_values: BTOneConfigurationProperties1900PropertyValues | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        node_id = self.node_id

        property_ids: list[str] | Unset = UNSET
        if not isinstance(self.property_ids, Unset):
            property_ids = self.property_ids

        property_values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.property_values, Unset):
            property_values = self.property_values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if property_ids is not UNSET:
            field_dict["propertyIds"] = property_ids
        if property_values is not UNSET:
            field_dict["propertyValues"] = property_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_one_configuration_properties_1900_configuration import (
            BTOneConfigurationProperties1900Configuration,
        )
        from ..models.bt_one_configuration_properties_1900_property_values import (
            BTOneConfigurationProperties1900PropertyValues,
        )

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _configuration = d.pop("configuration", UNSET)
        configuration: BTOneConfigurationProperties1900Configuration | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = BTOneConfigurationProperties1900Configuration.from_dict(_configuration)

        node_id = d.pop("nodeId", UNSET)

        property_ids = cast(list[str], d.pop("propertyIds", UNSET))

        _property_values = d.pop("propertyValues", UNSET)
        property_values: BTOneConfigurationProperties1900PropertyValues | Unset
        if isinstance(_property_values, Unset):
            property_values = UNSET
        else:
            property_values = BTOneConfigurationProperties1900PropertyValues.from_dict(_property_values)

        bt_one_configuration_properties_1900 = cls(
            bt_type=bt_type,
            configuration=configuration,
            node_id=node_id,
            property_ids=property_ids,
            property_values=property_values,
        )

        bt_one_configuration_properties_1900.additional_properties = d
        return bt_one_configuration_properties_1900

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
