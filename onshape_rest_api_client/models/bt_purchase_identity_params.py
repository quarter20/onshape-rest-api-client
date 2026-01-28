from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTPurchaseIdentityParams")


@_attrs_define
class BTPurchaseIdentityParams:
    """
    Attributes:
        consumed_quantity (int | Unset):
        identity_id (str | Unset):
        identity_type (int | Unset):
        purchase_id (str | Unset):
    """

    consumed_quantity: int | Unset = UNSET
    identity_id: str | Unset = UNSET
    identity_type: int | Unset = UNSET
    purchase_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consumed_quantity = self.consumed_quantity

        identity_id = self.identity_id

        identity_type = self.identity_type

        purchase_id = self.purchase_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if consumed_quantity is not UNSET:
            field_dict["consumedQuantity"] = consumed_quantity
        if identity_id is not UNSET:
            field_dict["identityId"] = identity_id
        if identity_type is not UNSET:
            field_dict["identityType"] = identity_type
        if purchase_id is not UNSET:
            field_dict["purchaseId"] = purchase_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        consumed_quantity = d.pop("consumedQuantity", UNSET)

        identity_id = d.pop("identityId", UNSET)

        identity_type = d.pop("identityType", UNSET)

        purchase_id = d.pop("purchaseId", UNSET)

        bt_purchase_identity_params = cls(
            consumed_quantity=consumed_quantity,
            identity_id=identity_id,
            identity_type=identity_type,
            purchase_id=purchase_id,
        )

        bt_purchase_identity_params.additional_properties = d
        return bt_purchase_identity_params

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
