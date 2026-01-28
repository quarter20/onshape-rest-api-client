from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTModifiableEntityOnlyFilter1593")


@_attrs_define
class BTModifiableEntityOnlyFilter1593:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        modifiable_only (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    modifiable_only: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        modifiable_only = self.modifiable_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if modifiable_only is not UNSET:
            field_dict["modifiableOnly"] = modifiable_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        modifiable_only = d.pop("modifiableOnly", UNSET)

        bt_modifiable_entity_only_filter_1593 = cls(
            bt_type=bt_type,
            modifiable_only=modifiable_only,
        )

        bt_modifiable_entity_only_filter_1593.additional_properties = d
        return bt_modifiable_entity_only_filter_1593

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
