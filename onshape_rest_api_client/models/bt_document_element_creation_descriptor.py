from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_app_element_params import BTAppElementParams


T = TypeVar("T", bound="BTDocumentElementCreationDescriptor")


@_attrs_define
class BTDocumentElementCreationDescriptor:
    """List of element IDs to include in the document.

    Attributes:
        element_params (BTAppElementParams | Unset):
        element_type (int | Unset):
    """

    element_params: BTAppElementParams | Unset = UNSET
    element_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        element_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.element_params, Unset):
            element_params = self.element_params.to_dict()

        element_type = self.element_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if element_params is not UNSET:
            field_dict["elementParams"] = element_params
        if element_type is not UNSET:
            field_dict["elementType"] = element_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_app_element_params import BTAppElementParams

        d = dict(src_dict)
        _element_params = d.pop("elementParams", UNSET)
        element_params: BTAppElementParams | Unset
        if isinstance(_element_params, Unset):
            element_params = UNSET
        else:
            element_params = BTAppElementParams.from_dict(_element_params)

        element_type = d.pop("elementType", UNSET)

        bt_document_element_creation_descriptor = cls(
            element_params=element_params,
            element_type=element_type,
        )

        bt_document_element_creation_descriptor.additional_properties = d
        return bt_document_element_creation_descriptor

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
