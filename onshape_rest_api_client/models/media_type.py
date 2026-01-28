from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_type_encoding import MediaTypeEncoding
    from ..models.media_type_example import MediaTypeExample
    from ..models.media_type_examples import MediaTypeExamples
    from ..models.media_type_extensions import MediaTypeExtensions
    from ..models.schema import Schema


T = TypeVar("T", bound="MediaType")


@_attrs_define
class MediaType:
    """
    Attributes:
        encoding (MediaTypeEncoding | Unset):
        example (MediaTypeExample | Unset):
        example_set_flag (bool | Unset):
        examples (MediaTypeExamples | Unset):
        extensions (MediaTypeExtensions | Unset):
        schema (Schema | Unset):
    """

    encoding: MediaTypeEncoding | Unset = UNSET
    example: MediaTypeExample | Unset = UNSET
    example_set_flag: bool | Unset = UNSET
    examples: MediaTypeExamples | Unset = UNSET
    extensions: MediaTypeExtensions | Unset = UNSET
    schema: Schema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        encoding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.encoding, Unset):
            encoding = self.encoding.to_dict()

        example: dict[str, Any] | Unset = UNSET
        if not isinstance(self.example, Unset):
            example = self.example.to_dict()

        example_set_flag = self.example_set_flag

        examples: dict[str, Any] | Unset = UNSET
        if not isinstance(self.examples, Unset):
            examples = self.examples.to_dict()

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encoding is not UNSET:
            field_dict["encoding"] = encoding
        if example is not UNSET:
            field_dict["example"] = example
        if example_set_flag is not UNSET:
            field_dict["exampleSetFlag"] = example_set_flag
        if examples is not UNSET:
            field_dict["examples"] = examples
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_type_encoding import MediaTypeEncoding
        from ..models.media_type_example import MediaTypeExample
        from ..models.media_type_examples import MediaTypeExamples
        from ..models.media_type_extensions import MediaTypeExtensions
        from ..models.schema import Schema

        d = dict(src_dict)
        _encoding = d.pop("encoding", UNSET)
        encoding: MediaTypeEncoding | Unset
        if isinstance(_encoding, Unset):
            encoding = UNSET
        else:
            encoding = MediaTypeEncoding.from_dict(_encoding)

        _example = d.pop("example", UNSET)
        example: MediaTypeExample | Unset
        if isinstance(_example, Unset):
            example = UNSET
        else:
            example = MediaTypeExample.from_dict(_example)

        example_set_flag = d.pop("exampleSetFlag", UNSET)

        _examples = d.pop("examples", UNSET)
        examples: MediaTypeExamples | Unset
        if isinstance(_examples, Unset):
            examples = UNSET
        else:
            examples = MediaTypeExamples.from_dict(_examples)

        _extensions = d.pop("extensions", UNSET)
        extensions: MediaTypeExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = MediaTypeExtensions.from_dict(_extensions)

        _schema = d.pop("schema", UNSET)
        schema: Schema | Unset
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = Schema.from_dict(_schema)

        media_type = cls(
            encoding=encoding,
            example=example,
            example_set_flag=example_set_flag,
            examples=examples,
            extensions=extensions,
            schema=schema,
        )

        media_type.additional_properties = d
        return media_type

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
