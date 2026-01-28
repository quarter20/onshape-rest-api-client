from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTStringMinimumLengthPattern895")


@_attrs_define
class BTStringMinimumLengthPattern895:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        error_message (str | Unset):
        should_reset_value_when_confirmed (bool | Unset):
        minimum_length (int | Unset):
    """

    bt_type: str | Unset = UNSET
    error_message: str | Unset = UNSET
    should_reset_value_when_confirmed: bool | Unset = UNSET
    minimum_length: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        error_message = self.error_message

        should_reset_value_when_confirmed = self.should_reset_value_when_confirmed

        minimum_length = self.minimum_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if should_reset_value_when_confirmed is not UNSET:
            field_dict["shouldResetValueWhenConfirmed"] = should_reset_value_when_confirmed
        if minimum_length is not UNSET:
            field_dict["minimumLength"] = minimum_length

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        should_reset_value_when_confirmed = d.pop("shouldResetValueWhenConfirmed", UNSET)

        minimum_length = d.pop("minimumLength", UNSET)

        bt_string_minimum_length_pattern_895 = cls(
            bt_type=bt_type,
            error_message=error_message,
            should_reset_value_when_confirmed=should_reset_value_when_confirmed,
            minimum_length=minimum_length,
        )

        bt_string_minimum_length_pattern_895.additional_properties = d
        return bt_string_minimum_length_pattern_895

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
