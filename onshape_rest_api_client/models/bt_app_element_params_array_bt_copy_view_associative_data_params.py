from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_copy_view_associative_data_params import BTCopyViewAssociativeDataParams


T = TypeVar("T", bound="BTAppElementParamsArrayBTCopyViewAssociativeDataParams")


@_attrs_define
class BTAppElementParamsArrayBTCopyViewAssociativeDataParams:
    """
    Attributes:
        description (str | Unset):
        items (list[BTCopyViewAssociativeDataParams] | Unset):
        parent_change_id (str | Unset):
        transaction_id (str | Unset):
    """

    description: str | Unset = UNSET
    items: list[BTCopyViewAssociativeDataParams] | Unset = UNSET
    parent_change_id: str | Unset = UNSET
    transaction_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        parent_change_id = self.parent_change_id

        transaction_id = self.transaction_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if items is not UNSET:
            field_dict["items"] = items
        if parent_change_id is not UNSET:
            field_dict["parentChangeId"] = parent_change_id
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_copy_view_associative_data_params import BTCopyViewAssociativeDataParams

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _items = d.pop("items", UNSET)
        items: list[BTCopyViewAssociativeDataParams] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = BTCopyViewAssociativeDataParams.from_dict(items_item_data)

                items.append(items_item)

        parent_change_id = d.pop("parentChangeId", UNSET)

        transaction_id = d.pop("transactionId", UNSET)

        bt_app_element_params_array_bt_copy_view_associative_data_params = cls(
            description=description,
            items=items,
            parent_change_id=parent_change_id,
            transaction_id=transaction_id,
        )

        bt_app_element_params_array_bt_copy_view_associative_data_params.additional_properties = d
        return bt_app_element_params_array_bt_copy_view_associative_data_params

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
