from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTModelFormatInfo")


@_attrs_define
class BTModelFormatInfo:
    """
    Attributes:
        could_be_assembly (bool | Unset): Indicates if this format could be an assembly. Example: True.
        name (str | Unset): Name of the format. Example: STEP.
        translator_name (str | Unset): The name of the translator for the format. Example: step.
    """

    could_be_assembly: bool | Unset = UNSET
    name: str | Unset = UNSET
    translator_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        could_be_assembly = self.could_be_assembly

        name = self.name

        translator_name = self.translator_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if could_be_assembly is not UNSET:
            field_dict["couldBeAssembly"] = could_be_assembly
        if name is not UNSET:
            field_dict["name"] = name
        if translator_name is not UNSET:
            field_dict["translatorName"] = translator_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        could_be_assembly = d.pop("couldBeAssembly", UNSET)

        name = d.pop("name", UNSET)

        translator_name = d.pop("translatorName", UNSET)

        bt_model_format_info = cls(
            could_be_assembly=could_be_assembly,
            name=name,
            translator_name=translator_name,
        )

        bt_model_format_info.additional_properties = d
        return bt_model_format_info

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
