from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTModelFormatFullInfo")


@_attrs_define
class BTModelFormatFullInfo:
    """
    Attributes:
        content_type (str | Unset): Content-Type for this file format. Example: text/csv.
        could_be_assembly (bool | Unset): Indicates if this format could be an assembly. Example: True.
        file_extensions (list[str] | Unset): Supported file extensions for this format. Example: ['x_t', 'x_b',
            'xmt_txt', 'xmt_bin'].
        name (str | Unset): Name of the format. Example: STEP.
        translator_name (str | Unset): The name of the translator for the format. Example: step.
        valid_destination_format (bool | Unset): Indicates if this format is a valid destination format for translation.
            Example: True.
        valid_source_format (bool | Unset): Indicates if this format is a valid source format for translation. Example:
            True.
    """

    content_type: str | Unset = UNSET
    could_be_assembly: bool | Unset = UNSET
    file_extensions: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    translator_name: str | Unset = UNSET
    valid_destination_format: bool | Unset = UNSET
    valid_source_format: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        could_be_assembly = self.could_be_assembly

        file_extensions: list[str] | Unset = UNSET
        if not isinstance(self.file_extensions, Unset):
            file_extensions = self.file_extensions

        name = self.name

        translator_name = self.translator_name

        valid_destination_format = self.valid_destination_format

        valid_source_format = self.valid_source_format

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if could_be_assembly is not UNSET:
            field_dict["couldBeAssembly"] = could_be_assembly
        if file_extensions is not UNSET:
            field_dict["fileExtensions"] = file_extensions
        if name is not UNSET:
            field_dict["name"] = name
        if translator_name is not UNSET:
            field_dict["translatorName"] = translator_name
        if valid_destination_format is not UNSET:
            field_dict["validDestinationFormat"] = valid_destination_format
        if valid_source_format is not UNSET:
            field_dict["validSourceFormat"] = valid_source_format

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_type = d.pop("contentType", UNSET)

        could_be_assembly = d.pop("couldBeAssembly", UNSET)

        file_extensions = cast(list[str], d.pop("fileExtensions", UNSET))

        name = d.pop("name", UNSET)

        translator_name = d.pop("translatorName", UNSET)

        valid_destination_format = d.pop("validDestinationFormat", UNSET)

        valid_source_format = d.pop("validSourceFormat", UNSET)

        bt_model_format_full_info = cls(
            content_type=content_type,
            could_be_assembly=could_be_assembly,
            file_extensions=file_extensions,
            name=name,
            translator_name=translator_name,
            valid_destination_format=valid_destination_format,
            valid_source_format=valid_source_format,
        )

        bt_model_format_full_info.additional_properties = d
        return bt_model_format_full_info

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
