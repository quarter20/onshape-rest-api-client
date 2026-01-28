from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.example_extensions import ExampleExtensions
    from ..models.example_value import ExampleValue


T = TypeVar("T", bound="Example")


@_attrs_define
class Example:
    """
    Attributes:
        description (str | Unset):
        extensions (ExampleExtensions | Unset):
        external_value (str | Unset):
        getref (str | Unset):
        summary (str | Unset):
        value (ExampleValue | Unset):
        value_set_flag (bool | Unset):
    """

    description: str | Unset = UNSET
    extensions: ExampleExtensions | Unset = UNSET
    external_value: str | Unset = UNSET
    getref: str | Unset = UNSET
    summary: str | Unset = UNSET
    value: ExampleValue | Unset = UNSET
    value_set_flag: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        external_value = self.external_value

        getref = self.getref

        summary = self.summary

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        value_set_flag = self.value_set_flag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if external_value is not UNSET:
            field_dict["externalValue"] = external_value
        if getref is not UNSET:
            field_dict["get$ref"] = getref
        if summary is not UNSET:
            field_dict["summary"] = summary
        if value is not UNSET:
            field_dict["value"] = value
        if value_set_flag is not UNSET:
            field_dict["valueSetFlag"] = value_set_flag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.example_extensions import ExampleExtensions
        from ..models.example_value import ExampleValue

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: ExampleExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = ExampleExtensions.from_dict(_extensions)

        external_value = d.pop("externalValue", UNSET)

        getref = d.pop("get$ref", UNSET)

        summary = d.pop("summary", UNSET)

        _value = d.pop("value", UNSET)
        value: ExampleValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = ExampleValue.from_dict(_value)

        value_set_flag = d.pop("valueSetFlag", UNSET)

        example = cls(
            description=description,
            extensions=extensions,
            external_value=external_value,
            getref=getref,
            summary=summary,
            value=value,
            value_set_flag=value_set_flag,
        )

        example.additional_properties = d
        return example

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
