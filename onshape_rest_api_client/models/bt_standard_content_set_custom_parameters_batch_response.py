from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_standard_content_set_custom_parameters_response import BTStandardContentSetCustomParametersResponse


T = TypeVar("T", bound="BTStandardContentSetCustomParametersBatchResponse")


@_attrs_define
class BTStandardContentSetCustomParametersBatchResponse:
    """
    Attributes:
        responses (list[BTStandardContentSetCustomParametersResponse] | Unset):
    """

    responses: list[BTStandardContentSetCustomParametersResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        responses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.responses, Unset):
            responses = []
            for responses_item_data in self.responses:
                responses_item = responses_item_data.to_dict()
                responses.append(responses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if responses is not UNSET:
            field_dict["responses"] = responses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_standard_content_set_custom_parameters_response import (
            BTStandardContentSetCustomParametersResponse,
        )

        d = dict(src_dict)
        _responses = d.pop("responses", UNSET)
        responses: list[BTStandardContentSetCustomParametersResponse] | Unset = UNSET
        if _responses is not UNSET:
            responses = []
            for responses_item_data in _responses:
                responses_item = BTStandardContentSetCustomParametersResponse.from_dict(responses_item_data)

                responses.append(responses_item)

        bt_standard_content_set_custom_parameters_batch_response = cls(
            responses=responses,
        )

        bt_standard_content_set_custom_parameters_batch_response.additional_properties = d
        return bt_standard_content_set_custom_parameters_batch_response

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
