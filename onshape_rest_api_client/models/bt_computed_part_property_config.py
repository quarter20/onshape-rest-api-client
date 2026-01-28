from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTComputedPartPropertyConfig")


@_attrs_define
class BTComputedPartPropertyConfig:
    """
    Attributes:
        computed_part_property_spec_function (str | Unset):
        computed_part_property_spec_namespace (str | Unset):
        computed_property_function_return_type (int | Unset):
        property_function_document_id (str | Unset):
    """

    computed_part_property_spec_function: str | Unset = UNSET
    computed_part_property_spec_namespace: str | Unset = UNSET
    computed_property_function_return_type: int | Unset = UNSET
    property_function_document_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        computed_part_property_spec_function = self.computed_part_property_spec_function

        computed_part_property_spec_namespace = self.computed_part_property_spec_namespace

        computed_property_function_return_type = self.computed_property_function_return_type

        property_function_document_id = self.property_function_document_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if computed_part_property_spec_function is not UNSET:
            field_dict["computedPartPropertySpecFunction"] = computed_part_property_spec_function
        if computed_part_property_spec_namespace is not UNSET:
            field_dict["computedPartPropertySpecNamespace"] = computed_part_property_spec_namespace
        if computed_property_function_return_type is not UNSET:
            field_dict["computedPropertyFunctionReturnType"] = computed_property_function_return_type
        if property_function_document_id is not UNSET:
            field_dict["propertyFunctionDocumentId"] = property_function_document_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        computed_part_property_spec_function = d.pop("computedPartPropertySpecFunction", UNSET)

        computed_part_property_spec_namespace = d.pop("computedPartPropertySpecNamespace", UNSET)

        computed_property_function_return_type = d.pop("computedPropertyFunctionReturnType", UNSET)

        property_function_document_id = d.pop("propertyFunctionDocumentId", UNSET)

        bt_computed_part_property_config = cls(
            computed_part_property_spec_function=computed_part_property_spec_function,
            computed_part_property_spec_namespace=computed_part_property_spec_namespace,
            computed_property_function_return_type=computed_property_function_return_type,
            property_function_document_id=property_function_document_id,
        )

        bt_computed_part_property_config.additional_properties = d
        return bt_computed_part_property_config

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
