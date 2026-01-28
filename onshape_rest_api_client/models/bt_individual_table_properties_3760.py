from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_string_node_wrapper_4224 import BTStringNodeWrapper4224


T = TypeVar("T", bound="BTIndividualTableProperties3760")


@_attrs_define
class BTIndividualTableProperties3760:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        hidden_columns (list[BTStringNodeWrapper4224] | Unset):
        node_id (str | Unset):
        order (list[BTStringNodeWrapper4224] | Unset):
        table_node_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    hidden_columns: list[BTStringNodeWrapper4224] | Unset = UNSET
    node_id: str | Unset = UNSET
    order: list[BTStringNodeWrapper4224] | Unset = UNSET
    table_node_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        hidden_columns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hidden_columns, Unset):
            hidden_columns = []
            for hidden_columns_item_data in self.hidden_columns:
                hidden_columns_item = hidden_columns_item_data.to_dict()
                hidden_columns.append(hidden_columns_item)

        node_id = self.node_id

        order: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.order, Unset):
            order = []
            for order_item_data in self.order:
                order_item = order_item_data.to_dict()
                order.append(order_item)

        table_node_id = self.table_node_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if hidden_columns is not UNSET:
            field_dict["hiddenColumns"] = hidden_columns
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if order is not UNSET:
            field_dict["order"] = order
        if table_node_id is not UNSET:
            field_dict["tableNodeId"] = table_node_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_string_node_wrapper_4224 import BTStringNodeWrapper4224

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _hidden_columns = d.pop("hiddenColumns", UNSET)
        hidden_columns: list[BTStringNodeWrapper4224] | Unset = UNSET
        if _hidden_columns is not UNSET:
            hidden_columns = []
            for hidden_columns_item_data in _hidden_columns:
                hidden_columns_item = BTStringNodeWrapper4224.from_dict(hidden_columns_item_data)

                hidden_columns.append(hidden_columns_item)

        node_id = d.pop("nodeId", UNSET)

        _order = d.pop("order", UNSET)
        order: list[BTStringNodeWrapper4224] | Unset = UNSET
        if _order is not UNSET:
            order = []
            for order_item_data in _order:
                order_item = BTStringNodeWrapper4224.from_dict(order_item_data)

                order.append(order_item)

        table_node_id = d.pop("tableNodeId", UNSET)

        bt_individual_table_properties_3760 = cls(
            bt_type=bt_type,
            hidden_columns=hidden_columns,
            node_id=node_id,
            order=order,
            table_node_id=table_node_id,
        )

        bt_individual_table_properties_3760.additional_properties = d
        return bt_individual_table_properties_3760

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
