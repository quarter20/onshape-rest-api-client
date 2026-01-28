from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTInContextObjectFilter3810")


@_attrs_define
class BTInContextObjectFilter3810:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        is_in_context (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    is_in_context: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        is_in_context = self.is_in_context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if is_in_context is not UNSET:
            field_dict["isInContext"] = is_in_context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        is_in_context = d.pop("isInContext", UNSET)

        bt_in_context_object_filter_3810 = cls(
            bt_type=bt_type,
            is_in_context=is_in_context,
        )

        bt_in_context_object_filter_3810.additional_properties = d
        return bt_in_context_object_filter_3810

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
