from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_standard_content_set_custom_parameter_specifier import BTStandardContentSetCustomParameterSpecifier


T = TypeVar("T", bound="BTStandardContentSetCustomParametersBatchRequest")


@_attrs_define
class BTStandardContentSetCustomParametersBatchRequest:
    """
    Attributes:
        specifiers (list[BTStandardContentSetCustomParameterSpecifier] | Unset):
    """

    specifiers: list[BTStandardContentSetCustomParameterSpecifier] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        specifiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.specifiers, Unset):
            specifiers = []
            for specifiers_item_data in self.specifiers:
                specifiers_item = specifiers_item_data.to_dict()
                specifiers.append(specifiers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if specifiers is not UNSET:
            field_dict["specifiers"] = specifiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_standard_content_set_custom_parameter_specifier import (
            BTStandardContentSetCustomParameterSpecifier,
        )

        d = dict(src_dict)
        _specifiers = d.pop("specifiers", UNSET)
        specifiers: list[BTStandardContentSetCustomParameterSpecifier] | Unset = UNSET
        if _specifiers is not UNSET:
            specifiers = []
            for specifiers_item_data in _specifiers:
                specifiers_item = BTStandardContentSetCustomParameterSpecifier.from_dict(specifiers_item_data)

                specifiers.append(specifiers_item)

        bt_standard_content_set_custom_parameters_batch_request = cls(
            specifiers=specifiers,
        )

        bt_standard_content_set_custom_parameters_batch_request.additional_properties = d
        return bt_standard_content_set_custom_parameters_batch_request

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
