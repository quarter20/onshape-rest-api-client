from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessorData")


@_attrs_define
class AccessorData:
    """
    Attributes:
        num_components_per_element (int | Unset):
        num_elements (int | Unset):
        total_num_components (int | Unset):
    """

    num_components_per_element: int | Unset = UNSET
    num_elements: int | Unset = UNSET
    total_num_components: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_components_per_element = self.num_components_per_element

        num_elements = self.num_elements

        total_num_components = self.total_num_components

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_components_per_element is not UNSET:
            field_dict["numComponentsPerElement"] = num_components_per_element
        if num_elements is not UNSET:
            field_dict["numElements"] = num_elements
        if total_num_components is not UNSET:
            field_dict["totalNumComponents"] = total_num_components

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        num_components_per_element = d.pop("numComponentsPerElement", UNSET)

        num_elements = d.pop("numElements", UNSET)

        total_num_components = d.pop("totalNumComponents", UNSET)

        accessor_data = cls(
            num_components_per_element=num_components_per_element,
            num_elements=num_elements,
            total_num_components=total_num_components,
        )

        accessor_data.additional_properties = d
        return accessor_data

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
