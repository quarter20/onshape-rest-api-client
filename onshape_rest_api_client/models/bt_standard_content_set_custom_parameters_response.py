from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_standard_content_set_custom_parameters_error import BTStandardContentSetCustomParametersError
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTStandardContentSetCustomParametersResponse")


@_attrs_define
class BTStandardContentSetCustomParametersResponse:
    """Reports the status of an individual request to set custom parameter values.

    Attributes:
        error (BTStandardContentSetCustomParametersError | Unset): Indicates whether or not the individual request had
            an error.
        error_message (str | Unset): If there was an error, this provides a more detailed description of the problem.
    """

    error: BTStandardContentSetCustomParametersError | Unset = UNSET
    error_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: str | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.value

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: BTStandardContentSetCustomParametersError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = BTStandardContentSetCustomParametersError(_error)

        error_message = d.pop("errorMessage", UNSET)

        bt_standard_content_set_custom_parameters_response = cls(
            error=error,
            error_message=error_message,
        )

        bt_standard_content_set_custom_parameters_response.additional_properties = d
        return bt_standard_content_set_custom_parameters_response

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
