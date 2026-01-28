from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAppElementCommitTransactionParams")


@_attrs_define
class BTAppElementCommitTransactionParams:
    """
    Attributes:
        allow_merge (bool | Unset):
        description (str | Unset): The label that will appear in the document's edit history for this operation. If
            blank, a value will be auto-generated.
        return_error (bool | Unset):
        transaction_ids (list[str] | Unset):
    """

    allow_merge: bool | Unset = UNSET
    description: str | Unset = UNSET
    return_error: bool | Unset = UNSET
    transaction_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_merge = self.allow_merge

        description = self.description

        return_error = self.return_error

        transaction_ids: list[str] | Unset = UNSET
        if not isinstance(self.transaction_ids, Unset):
            transaction_ids = self.transaction_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_merge is not UNSET:
            field_dict["allowMerge"] = allow_merge
        if description is not UNSET:
            field_dict["description"] = description
        if return_error is not UNSET:
            field_dict["returnError"] = return_error
        if transaction_ids is not UNSET:
            field_dict["transactionIds"] = transaction_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_merge = d.pop("allowMerge", UNSET)

        description = d.pop("description", UNSET)

        return_error = d.pop("returnError", UNSET)

        transaction_ids = cast(list[str], d.pop("transactionIds", UNSET))

        bt_app_element_commit_transaction_params = cls(
            allow_merge=allow_merge,
            description=description,
            return_error=return_error,
            transaction_ids=transaction_ids,
        )

        bt_app_element_commit_transaction_params.additional_properties = d
        return bt_app_element_commit_transaction_params

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
