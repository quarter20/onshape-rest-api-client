from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTItemParams")


@_attrs_define
class BTItemParams:
    """
    Attributes:
        company_id (str | Unset): ID of the company, classroom, or enterprise that owns this item.
        name (str | Unset): Item name.
        publish_state (int | Unset): `0: PENDING | 1: ACTIVE | 2: INACTIVE`
    """

    company_id: str | Unset = UNSET
    name: str | Unset = UNSET
    publish_state: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        name = self.name

        publish_state = self.publish_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if name is not UNSET:
            field_dict["name"] = name
        if publish_state is not UNSET:
            field_dict["publishState"] = publish_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("companyId", UNSET)

        name = d.pop("name", UNSET)

        publish_state = d.pop("publishState", UNSET)

        bt_item_params = cls(
            company_id=company_id,
            name=name,
            publish_state=publish_state,
        )

        bt_item_params.additional_properties = d
        return bt_item_params

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
