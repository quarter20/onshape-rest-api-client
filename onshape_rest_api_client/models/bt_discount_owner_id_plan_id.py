from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTDiscountOwnerIdPlanId")


@_attrs_define
class BTDiscountOwnerIdPlanId:
    """
    Attributes:
        owner_id (str | Unset):
        plan_id (str | Unset):
    """

    owner_id: str | Unset = UNSET
    plan_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner_id = self.owner_id

        plan_id = self.plan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if plan_id is not UNSET:
            field_dict["planId"] = plan_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        owner_id = d.pop("ownerId", UNSET)

        plan_id = d.pop("planId", UNSET)

        bt_discount_owner_id_plan_id = cls(
            owner_id=owner_id,
            plan_id=plan_id,
        )

        bt_discount_owner_id_plan_id.additional_properties = d
        return bt_discount_owner_id_plan_id

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
