from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAppElementStartTransactionParams")


@_attrs_define
class BTAppElementStartTransactionParams:
    """
    Attributes:
        description (str | Unset): The label that will appear in the document's edit history for this operation. If
            blank, a value will be auto-generated.
        parent_change_id (str | Unset):
        return_error (bool | Unset):
    """

    description: str | Unset = UNSET
    parent_change_id: str | Unset = UNSET
    return_error: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        parent_change_id = self.parent_change_id

        return_error = self.return_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if parent_change_id is not UNSET:
            field_dict["parentChangeId"] = parent_change_id
        if return_error is not UNSET:
            field_dict["returnError"] = return_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        parent_change_id = d.pop("parentChangeId", UNSET)

        return_error = d.pop("returnError", UNSET)

        bt_app_element_start_transaction_params = cls(
            description=description,
            parent_change_id=parent_change_id,
            return_error=return_error,
        )

        bt_app_element_start_transaction_params.additional_properties = d
        return bt_app_element_start_transaction_params

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
