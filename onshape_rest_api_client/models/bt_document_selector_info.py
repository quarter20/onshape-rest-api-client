from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_document_selector_parameters_info import BTDocumentSelectorParametersInfo


T = TypeVar("T", bound="BTDocumentSelectorInfo")


@_attrs_define
class BTDocumentSelectorInfo:
    """
    Attributes:
        parameters (BTDocumentSelectorParametersInfo | Unset):
        selector_id (str | Unset):
    """

    parameters: BTDocumentSelectorParametersInfo | Unset = UNSET
    selector_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        selector_id = self.selector_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if selector_id is not UNSET:
            field_dict["selectorId"] = selector_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_document_selector_parameters_info import BTDocumentSelectorParametersInfo

        d = dict(src_dict)
        _parameters = d.pop("parameters", UNSET)
        parameters: BTDocumentSelectorParametersInfo | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = BTDocumentSelectorParametersInfo.from_dict(_parameters)

        selector_id = d.pop("selectorId", UNSET)

        bt_document_selector_info = cls(
            parameters=parameters,
            selector_id=selector_id,
        )

        bt_document_selector_info.additional_properties = d
        return bt_document_selector_info

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
