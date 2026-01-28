from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.style_enum import StyleEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.header_example import HeaderExample
    from ..models.header_examples import HeaderExamples
    from ..models.header_extensions import HeaderExtensions
    from ..models.schema import Schema


T = TypeVar("T", bound="Header")


@_attrs_define
class Header:
    """
    Attributes:
        deprecated (bool | Unset):
        description (str | Unset):
        example (HeaderExample | Unset):
        examples (HeaderExamples | Unset):
        explode (bool | Unset):
        extensions (HeaderExtensions | Unset):
        getref (str | Unset):
        required (bool | Unset):
        schema (Schema | Unset):
        style (StyleEnum | Unset):
    """

    deprecated: bool | Unset = UNSET
    description: str | Unset = UNSET
    example: HeaderExample | Unset = UNSET
    examples: HeaderExamples | Unset = UNSET
    explode: bool | Unset = UNSET
    extensions: HeaderExtensions | Unset = UNSET
    getref: str | Unset = UNSET
    required: bool | Unset = UNSET
    schema: Schema | Unset = UNSET
    style: StyleEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deprecated = self.deprecated

        description = self.description

        example: dict[str, Any] | Unset = UNSET
        if not isinstance(self.example, Unset):
            example = self.example.to_dict()

        examples: dict[str, Any] | Unset = UNSET
        if not isinstance(self.examples, Unset):
            examples = self.examples.to_dict()

        explode = self.explode

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        getref = self.getref

        required = self.required

        schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        style: str | Unset = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated
        if description is not UNSET:
            field_dict["description"] = description
        if example is not UNSET:
            field_dict["example"] = example
        if examples is not UNSET:
            field_dict["examples"] = examples
        if explode is not UNSET:
            field_dict["explode"] = explode
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if getref is not UNSET:
            field_dict["get$ref"] = getref
        if required is not UNSET:
            field_dict["required"] = required
        if schema is not UNSET:
            field_dict["schema"] = schema
        if style is not UNSET:
            field_dict["style"] = style

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.header_example import HeaderExample
        from ..models.header_examples import HeaderExamples
        from ..models.header_extensions import HeaderExtensions
        from ..models.schema import Schema

        d = dict(src_dict)
        deprecated = d.pop("deprecated", UNSET)

        description = d.pop("description", UNSET)

        _example = d.pop("example", UNSET)
        example: HeaderExample | Unset
        if isinstance(_example, Unset):
            example = UNSET
        else:
            example = HeaderExample.from_dict(_example)

        _examples = d.pop("examples", UNSET)
        examples: HeaderExamples | Unset
        if isinstance(_examples, Unset):
            examples = UNSET
        else:
            examples = HeaderExamples.from_dict(_examples)

        explode = d.pop("explode", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: HeaderExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = HeaderExtensions.from_dict(_extensions)

        getref = d.pop("get$ref", UNSET)

        required = d.pop("required", UNSET)

        _schema = d.pop("schema", UNSET)
        schema: Schema | Unset
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = Schema.from_dict(_schema)

        _style = d.pop("style", UNSET)
        style: StyleEnum | Unset
        if isinstance(_style, Unset):
            style = UNSET
        else:
            style = StyleEnum(_style)

        header = cls(
            deprecated=deprecated,
            description=description,
            example=example,
            examples=examples,
            explode=explode,
            extensions=extensions,
            getref=getref,
            required=required,
            schema=schema,
            style=style,
        )

        header.additional_properties = d
        return header

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
