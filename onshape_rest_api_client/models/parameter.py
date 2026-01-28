from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.style_enum import StyleEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parameter_content import ParameterContent
    from ..models.parameter_example import ParameterExample
    from ..models.parameter_examples import ParameterExamples
    from ..models.parameter_extensions import ParameterExtensions
    from ..models.schema import Schema


T = TypeVar("T", bound="Parameter")


@_attrs_define
class Parameter:
    """
    Attributes:
        allow_empty_value (bool | Unset):
        allow_reserved (bool | Unset):
        content (ParameterContent | Unset):
        deprecated (bool | Unset):
        description (str | Unset):
        example (ParameterExample | Unset):
        examples (ParameterExamples | Unset):
        explode (bool | Unset):
        extensions (ParameterExtensions | Unset):
        getref (str | Unset):
        in_ (str | Unset):
        name (str | Unset):
        required (bool | Unset):
        schema (Schema | Unset):
        style (StyleEnum | Unset):
    """

    allow_empty_value: bool | Unset = UNSET
    allow_reserved: bool | Unset = UNSET
    content: ParameterContent | Unset = UNSET
    deprecated: bool | Unset = UNSET
    description: str | Unset = UNSET
    example: ParameterExample | Unset = UNSET
    examples: ParameterExamples | Unset = UNSET
    explode: bool | Unset = UNSET
    extensions: ParameterExtensions | Unset = UNSET
    getref: str | Unset = UNSET
    in_: str | Unset = UNSET
    name: str | Unset = UNSET
    required: bool | Unset = UNSET
    schema: Schema | Unset = UNSET
    style: StyleEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_empty_value = self.allow_empty_value

        allow_reserved = self.allow_reserved

        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

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

        in_ = self.in_

        name = self.name

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
        if allow_empty_value is not UNSET:
            field_dict["allowEmptyValue"] = allow_empty_value
        if allow_reserved is not UNSET:
            field_dict["allowReserved"] = allow_reserved
        if content is not UNSET:
            field_dict["content"] = content
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
        if in_ is not UNSET:
            field_dict["in"] = in_
        if name is not UNSET:
            field_dict["name"] = name
        if required is not UNSET:
            field_dict["required"] = required
        if schema is not UNSET:
            field_dict["schema"] = schema
        if style is not UNSET:
            field_dict["style"] = style

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parameter_content import ParameterContent
        from ..models.parameter_example import ParameterExample
        from ..models.parameter_examples import ParameterExamples
        from ..models.parameter_extensions import ParameterExtensions
        from ..models.schema import Schema

        d = dict(src_dict)
        allow_empty_value = d.pop("allowEmptyValue", UNSET)

        allow_reserved = d.pop("allowReserved", UNSET)

        _content = d.pop("content", UNSET)
        content: ParameterContent | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = ParameterContent.from_dict(_content)

        deprecated = d.pop("deprecated", UNSET)

        description = d.pop("description", UNSET)

        _example = d.pop("example", UNSET)
        example: ParameterExample | Unset
        if isinstance(_example, Unset):
            example = UNSET
        else:
            example = ParameterExample.from_dict(_example)

        _examples = d.pop("examples", UNSET)
        examples: ParameterExamples | Unset
        if isinstance(_examples, Unset):
            examples = UNSET
        else:
            examples = ParameterExamples.from_dict(_examples)

        explode = d.pop("explode", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: ParameterExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = ParameterExtensions.from_dict(_extensions)

        getref = d.pop("get$ref", UNSET)

        in_ = d.pop("in", UNSET)

        name = d.pop("name", UNSET)

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

        parameter = cls(
            allow_empty_value=allow_empty_value,
            allow_reserved=allow_reserved,
            content=content,
            deprecated=deprecated,
            description=description,
            example=example,
            examples=examples,
            explode=explode,
            extensions=extensions,
            getref=getref,
            in_=in_,
            name=name,
            required=required,
            schema=schema,
            style=style,
        )

        parameter.additional_properties = d
        return parameter

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
