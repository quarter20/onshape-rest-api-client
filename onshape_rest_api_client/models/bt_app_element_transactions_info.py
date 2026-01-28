from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_app_element_error_code import BTAppElementErrorCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_element_transaction import BTElementTransaction


T = TypeVar("T", bound="BTAppElementTransactionsInfo")


@_attrs_define
class BTAppElementTransactionsInfo:
    """
    Attributes:
        element_transactions (list[BTElementTransaction] | Unset):
        error_code (int | Unset): `0: OK (healthy) | 1: INFO | 2: WARNING | 3: ERROR (dangling or view generation call
            failed) | 4: UNKNOWN`
        error_description (str | Unset): A human-readable value for the error that occurred, if one occurred.
        error_value (BTAppElementErrorCode | Unset):
    """

    element_transactions: list[BTElementTransaction] | Unset = UNSET
    error_code: int | Unset = UNSET
    error_description: str | Unset = UNSET
    error_value: BTAppElementErrorCode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        element_transactions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.element_transactions, Unset):
            element_transactions = []
            for element_transactions_item_data in self.element_transactions:
                element_transactions_item = element_transactions_item_data.to_dict()
                element_transactions.append(element_transactions_item)

        error_code = self.error_code

        error_description = self.error_description

        error_value: str | Unset = UNSET
        if not isinstance(self.error_value, Unset):
            error_value = self.error_value.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if element_transactions is not UNSET:
            field_dict["elementTransactions"] = element_transactions
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if error_description is not UNSET:
            field_dict["errorDescription"] = error_description
        if error_value is not UNSET:
            field_dict["errorValue"] = error_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_element_transaction import BTElementTransaction

        d = dict(src_dict)
        _element_transactions = d.pop("elementTransactions", UNSET)
        element_transactions: list[BTElementTransaction] | Unset = UNSET
        if _element_transactions is not UNSET:
            element_transactions = []
            for element_transactions_item_data in _element_transactions:
                element_transactions_item = BTElementTransaction.from_dict(element_transactions_item_data)

                element_transactions.append(element_transactions_item)

        error_code = d.pop("errorCode", UNSET)

        error_description = d.pop("errorDescription", UNSET)

        _error_value = d.pop("errorValue", UNSET)
        error_value: BTAppElementErrorCode | Unset
        if isinstance(_error_value, Unset):
            error_value = UNSET
        else:
            error_value = BTAppElementErrorCode(_error_value)

        bt_app_element_transactions_info = cls(
            element_transactions=element_transactions,
            error_code=error_code,
            error_description=error_description,
            error_value=error_value,
        )

        bt_app_element_transactions_info.additional_properties = d
        return bt_app_element_transactions_info

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
