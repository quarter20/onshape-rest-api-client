from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_one_configuration_part_properties_1661 import BTOneConfigurationPartProperties1661
    from ..models.btp_function_declaration_246 import BTPFunctionDeclaration246


T = TypeVar("T", bound="BTPartWithConfiguredProperties2163")


@_attrs_define
class BTPartWithConfiguredProperties2163:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        configuration_properties (list[BTOneConfigurationPartProperties1661] | Unset):
        for_sub_part_properties (bool | Unset):
        node_id (str | Unset):
        parsed_query (BTPFunctionDeclaration246 | Unset):
        property_node_id (str | Unset):
        query (str | Unset):
    """

    bt_type: str | Unset = UNSET
    configuration_properties: list[BTOneConfigurationPartProperties1661] | Unset = UNSET
    for_sub_part_properties: bool | Unset = UNSET
    node_id: str | Unset = UNSET
    parsed_query: BTPFunctionDeclaration246 | Unset = UNSET
    property_node_id: str | Unset = UNSET
    query: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        configuration_properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configuration_properties, Unset):
            configuration_properties = []
            for configuration_properties_item_data in self.configuration_properties:
                configuration_properties_item = configuration_properties_item_data.to_dict()
                configuration_properties.append(configuration_properties_item)

        for_sub_part_properties = self.for_sub_part_properties

        node_id = self.node_id

        parsed_query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parsed_query, Unset):
            parsed_query = self.parsed_query.to_dict()

        property_node_id = self.property_node_id

        query = self.query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if configuration_properties is not UNSET:
            field_dict["configurationProperties"] = configuration_properties
        if for_sub_part_properties is not UNSET:
            field_dict["forSubPartProperties"] = for_sub_part_properties
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if parsed_query is not UNSET:
            field_dict["parsedQuery"] = parsed_query
        if property_node_id is not UNSET:
            field_dict["propertyNodeId"] = property_node_id
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_one_configuration_part_properties_1661 import BTOneConfigurationPartProperties1661
        from ..models.btp_function_declaration_246 import BTPFunctionDeclaration246

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _configuration_properties = d.pop("configurationProperties", UNSET)
        configuration_properties: list[BTOneConfigurationPartProperties1661] | Unset = UNSET
        if _configuration_properties is not UNSET:
            configuration_properties = []
            for configuration_properties_item_data in _configuration_properties:
                configuration_properties_item = BTOneConfigurationPartProperties1661.from_dict(
                    configuration_properties_item_data
                )

                configuration_properties.append(configuration_properties_item)

        for_sub_part_properties = d.pop("forSubPartProperties", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _parsed_query = d.pop("parsedQuery", UNSET)
        parsed_query: BTPFunctionDeclaration246 | Unset
        if isinstance(_parsed_query, Unset):
            parsed_query = UNSET
        else:
            parsed_query = BTPFunctionDeclaration246.from_dict(_parsed_query)

        property_node_id = d.pop("propertyNodeId", UNSET)

        query = d.pop("query", UNSET)

        bt_part_with_configured_properties_2163 = cls(
            bt_type=bt_type,
            configuration_properties=configuration_properties,
            for_sub_part_properties=for_sub_part_properties,
            node_id=node_id,
            parsed_query=parsed_query,
            property_node_id=property_node_id,
            query=query,
        )

        bt_part_with_configured_properties_2163.additional_properties = d
        return bt_part_with_configured_properties_2163

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
