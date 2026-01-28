from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_response import ApiResponse
    from ..models.operation_responses_extensions import OperationResponsesExtensions


T = TypeVar("T", bound="OperationResponses")


@_attrs_define
class OperationResponses:
    """
    Attributes:
        extensions (OperationResponsesExtensions | Unset):
        default (ApiResponse | Unset):
        empty (bool | Unset):
    """

    extensions: OperationResponsesExtensions | Unset = UNSET
    default: ApiResponse | Unset = UNSET
    empty: bool | Unset = UNSET
    additional_properties: dict[str, ApiResponse] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        default: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default, Unset):
            default = self.default.to_dict()

        empty = self.empty

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if default is not UNSET:
            field_dict["default"] = default
        if empty is not UNSET:
            field_dict["empty"] = empty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_response import ApiResponse
        from ..models.operation_responses_extensions import OperationResponsesExtensions

        d = dict(src_dict)
        _extensions = d.pop("extensions", UNSET)
        extensions: OperationResponsesExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = OperationResponsesExtensions.from_dict(_extensions)

        _default = d.pop("default", UNSET)
        default: ApiResponse | Unset
        if isinstance(_default, Unset):
            default = UNSET
        else:
            default = ApiResponse.from_dict(_default)

        empty = d.pop("empty", UNSET)

        operation_responses = cls(
            extensions=extensions,
            default=default,
            empty=empty,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ApiResponse.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        operation_responses.additional_properties = additional_properties
        return operation_responses

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ApiResponse:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ApiResponse) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
