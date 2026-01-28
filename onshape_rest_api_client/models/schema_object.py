from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discriminator import Discriminator
    from ..models.external_documentation import ExternalDocumentation
    from ..models.schema import Schema
    from ..models.schema_object_additional_properties import SchemaObjectAdditionalProperties
    from ..models.schema_object_const import SchemaObjectConst
    from ..models.schema_object_default import SchemaObjectDefault
    from ..models.schema_object_dependent_required import SchemaObjectDependentRequired
    from ..models.schema_object_enum_item import SchemaObjectEnumItem
    from ..models.schema_object_example import SchemaObjectExample
    from ..models.schema_object_examples_item import SchemaObjectExamplesItem
    from ..models.schema_object_extensions import SchemaObjectExtensions
    from ..models.schema_object_json_schema import SchemaObjectJsonSchema
    from ..models.schema_object_json_schema_impl import SchemaObjectJsonSchemaImpl
    from ..models.xml import XML


T = TypeVar("T", bound="SchemaObject")


@_attrs_define
class SchemaObject:
    """
    Attributes:
        additional_items (Schema | Unset):
        additional_properties (SchemaObjectAdditionalProperties | Unset):
        all_of (list[Schema] | Unset):
        any_of (list[Schema] | Unset):
        boolean_schema_value (bool | Unset):
        const (SchemaObjectConst | Unset):
        contains (Schema | Unset):
        content_encoding (str | Unset):
        content_media_type (str | Unset):
        content_schema (Schema | Unset):
        default (SchemaObjectDefault | Unset):
        dependent_required (SchemaObjectDependentRequired | Unset):
        deprecated (bool | Unset):
        description (str | Unset):
        discriminator (Discriminator | Unset):
        else_ (Schema | Unset):
        enum (list[SchemaObjectEnumItem] | Unset):
        example (SchemaObjectExample | Unset):
        example_set_flag (bool | Unset):
        examples (list[SchemaObjectExamplesItem] | Unset):
        exclusive_maximum (bool | Unset):
        exclusive_maximum_value (float | Unset):
        exclusive_minimum (bool | Unset):
        exclusive_minimum_value (float | Unset):
        extensions (SchemaObjectExtensions | Unset):
        external_docs (ExternalDocumentation | Unset):
        format_ (str | Unset):
        getanchor (str | Unset):
        getcomment (str | Unset):
        getid (str | Unset):
        getref (str | Unset):
        getschema (str | Unset):
        if_ (Schema | Unset):
        items (SchemaObject | Unset):
        json_schema (SchemaObjectJsonSchema | Unset):
        json_schema_impl (SchemaObjectJsonSchemaImpl | Unset):
        max_contains (int | Unset):
        max_items (int | Unset):
        max_length (int | Unset):
        max_properties (int | Unset):
        maximum (float | Unset):
        min_contains (int | Unset):
        min_items (int | Unset):
        min_length (int | Unset):
        min_properties (int | Unset):
        minimum (float | Unset):
        multiple_of (float | Unset):
        not_ (Schema | Unset):
        nullable (bool | Unset):
        one_of (list[Schema] | Unset):
        pattern (str | Unset):
        prefix_items (list[Schema] | Unset):
        property_names (Schema | Unset):
        read_only (bool | Unset):
        required (list[str] | Unset):
        then (Schema | Unset):
        title (str | Unset):
        type_ (str | Unset):
        types (list[str] | Unset):
        unevaluated_items (Schema | Unset):
        unevaluated_properties (Schema | Unset):
        unique_items (bool | Unset):
        write_only (bool | Unset):
        xml (XML | Unset):
    """

    additional_items: Schema | Unset = UNSET
    additional_properties: SchemaObjectAdditionalProperties | Unset = UNSET
    all_of: list[Schema] | Unset = UNSET
    any_of: list[Schema] | Unset = UNSET
    boolean_schema_value: bool | Unset = UNSET
    const: SchemaObjectConst | Unset = UNSET
    contains: Schema | Unset = UNSET
    content_encoding: str | Unset = UNSET
    content_media_type: str | Unset = UNSET
    content_schema: Schema | Unset = UNSET
    default: SchemaObjectDefault | Unset = UNSET
    dependent_required: SchemaObjectDependentRequired | Unset = UNSET
    deprecated: bool | Unset = UNSET
    description: str | Unset = UNSET
    discriminator: Discriminator | Unset = UNSET
    else_: Schema | Unset = UNSET
    enum: list[SchemaObjectEnumItem] | Unset = UNSET
    example: SchemaObjectExample | Unset = UNSET
    example_set_flag: bool | Unset = UNSET
    examples: list[SchemaObjectExamplesItem] | Unset = UNSET
    exclusive_maximum: bool | Unset = UNSET
    exclusive_maximum_value: float | Unset = UNSET
    exclusive_minimum: bool | Unset = UNSET
    exclusive_minimum_value: float | Unset = UNSET
    extensions: SchemaObjectExtensions | Unset = UNSET
    external_docs: ExternalDocumentation | Unset = UNSET
    format_: str | Unset = UNSET
    getanchor: str | Unset = UNSET
    getcomment: str | Unset = UNSET
    getid: str | Unset = UNSET
    getref: str | Unset = UNSET
    getschema: str | Unset = UNSET
    if_: Schema | Unset = UNSET
    items: SchemaObject | Unset = UNSET
    json_schema: SchemaObjectJsonSchema | Unset = UNSET
    json_schema_impl: SchemaObjectJsonSchemaImpl | Unset = UNSET
    max_contains: int | Unset = UNSET
    max_items: int | Unset = UNSET
    max_length: int | Unset = UNSET
    max_properties: int | Unset = UNSET
    maximum: float | Unset = UNSET
    min_contains: int | Unset = UNSET
    min_items: int | Unset = UNSET
    min_length: int | Unset = UNSET
    min_properties: int | Unset = UNSET
    minimum: float | Unset = UNSET
    multiple_of: float | Unset = UNSET
    not_: Schema | Unset = UNSET
    nullable: bool | Unset = UNSET
    one_of: list[Schema] | Unset = UNSET
    pattern: str | Unset = UNSET
    prefix_items: list[Schema] | Unset = UNSET
    property_names: Schema | Unset = UNSET
    read_only: bool | Unset = UNSET
    required: list[str] | Unset = UNSET
    then: Schema | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    types: list[str] | Unset = UNSET
    unevaluated_items: Schema | Unset = UNSET
    unevaluated_properties: Schema | Unset = UNSET
    unique_items: bool | Unset = UNSET
    write_only: bool | Unset = UNSET
    xml: XML | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_items, Unset):
            additional_items = self.additional_items.to_dict()

        additional_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_properties, Unset):
            additional_properties = self.additional_properties.to_dict()

        all_of: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_of, Unset):
            all_of = []
            for all_of_item_data in self.all_of:
                all_of_item = all_of_item_data.to_dict()
                all_of.append(all_of_item)

        any_of: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.any_of, Unset):
            any_of = []
            for any_of_item_data in self.any_of:
                any_of_item = any_of_item_data.to_dict()
                any_of.append(any_of_item)

        boolean_schema_value = self.boolean_schema_value

        const: dict[str, Any] | Unset = UNSET
        if not isinstance(self.const, Unset):
            const = self.const.to_dict()

        contains: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contains, Unset):
            contains = self.contains.to_dict()

        content_encoding = self.content_encoding

        content_media_type = self.content_media_type

        content_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_schema, Unset):
            content_schema = self.content_schema.to_dict()

        default: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default, Unset):
            default = self.default.to_dict()

        dependent_required: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dependent_required, Unset):
            dependent_required = self.dependent_required.to_dict()

        deprecated = self.deprecated

        description = self.description

        discriminator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.discriminator, Unset):
            discriminator = self.discriminator.to_dict()

        else_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.else_, Unset):
            else_ = self.else_.to_dict()

        enum: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.enum, Unset):
            enum = []
            for enum_item_data in self.enum:
                enum_item = enum_item_data.to_dict()
                enum.append(enum_item)

        example: dict[str, Any] | Unset = UNSET
        if not isinstance(self.example, Unset):
            example = self.example.to_dict()

        example_set_flag = self.example_set_flag

        examples: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.examples, Unset):
            examples = []
            for examples_item_data in self.examples:
                examples_item = examples_item_data.to_dict()
                examples.append(examples_item)

        exclusive_maximum = self.exclusive_maximum

        exclusive_maximum_value = self.exclusive_maximum_value

        exclusive_minimum = self.exclusive_minimum

        exclusive_minimum_value = self.exclusive_minimum_value

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        external_docs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_docs, Unset):
            external_docs = self.external_docs.to_dict()

        format_ = self.format_

        getanchor = self.getanchor

        getcomment = self.getcomment

        getid = self.getid

        getref = self.getref

        getschema = self.getschema

        if_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.if_, Unset):
            if_ = self.if_.to_dict()

        items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = self.items.to_dict()

        json_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.json_schema, Unset):
            json_schema = self.json_schema.to_dict()

        json_schema_impl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.json_schema_impl, Unset):
            json_schema_impl = self.json_schema_impl.to_dict()

        max_contains = self.max_contains

        max_items = self.max_items

        max_length = self.max_length

        max_properties = self.max_properties

        maximum = self.maximum

        min_contains = self.min_contains

        min_items = self.min_items

        min_length = self.min_length

        min_properties = self.min_properties

        minimum = self.minimum

        multiple_of = self.multiple_of

        not_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.not_, Unset):
            not_ = self.not_.to_dict()

        nullable = self.nullable

        one_of: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.one_of, Unset):
            one_of = []
            for one_of_item_data in self.one_of:
                one_of_item = one_of_item_data.to_dict()
                one_of.append(one_of_item)

        pattern = self.pattern

        prefix_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.prefix_items, Unset):
            prefix_items = []
            for prefix_items_item_data in self.prefix_items:
                prefix_items_item = prefix_items_item_data.to_dict()
                prefix_items.append(prefix_items_item)

        property_names: dict[str, Any] | Unset = UNSET
        if not isinstance(self.property_names, Unset):
            property_names = self.property_names.to_dict()

        read_only = self.read_only

        required: list[str] | Unset = UNSET
        if not isinstance(self.required, Unset):
            required = self.required

        then: dict[str, Any] | Unset = UNSET
        if not isinstance(self.then, Unset):
            then = self.then.to_dict()

        title = self.title

        type_ = self.type_

        types: list[str] | Unset = UNSET
        if not isinstance(self.types, Unset):
            types = self.types

        unevaluated_items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unevaluated_items, Unset):
            unevaluated_items = self.unevaluated_items.to_dict()

        unevaluated_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unevaluated_properties, Unset):
            unevaluated_properties = self.unevaluated_properties.to_dict()

        unique_items = self.unique_items

        write_only = self.write_only

        xml: dict[str, Any] | Unset = UNSET
        if not isinstance(self.xml, Unset):
            xml = self.xml.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_items is not UNSET:
            field_dict["additionalItems"] = additional_items
        if additional_properties is not UNSET:
            field_dict["additionalProperties"] = additional_properties
        if all_of is not UNSET:
            field_dict["allOf"] = all_of
        if any_of is not UNSET:
            field_dict["anyOf"] = any_of
        if boolean_schema_value is not UNSET:
            field_dict["booleanSchemaValue"] = boolean_schema_value
        if const is not UNSET:
            field_dict["const"] = const
        if contains is not UNSET:
            field_dict["contains"] = contains
        if content_encoding is not UNSET:
            field_dict["contentEncoding"] = content_encoding
        if content_media_type is not UNSET:
            field_dict["contentMediaType"] = content_media_type
        if content_schema is not UNSET:
            field_dict["contentSchema"] = content_schema
        if default is not UNSET:
            field_dict["default"] = default
        if dependent_required is not UNSET:
            field_dict["dependentRequired"] = dependent_required
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated
        if description is not UNSET:
            field_dict["description"] = description
        if discriminator is not UNSET:
            field_dict["discriminator"] = discriminator
        if else_ is not UNSET:
            field_dict["else"] = else_
        if enum is not UNSET:
            field_dict["enum"] = enum
        if example is not UNSET:
            field_dict["example"] = example
        if example_set_flag is not UNSET:
            field_dict["exampleSetFlag"] = example_set_flag
        if examples is not UNSET:
            field_dict["examples"] = examples
        if exclusive_maximum is not UNSET:
            field_dict["exclusiveMaximum"] = exclusive_maximum
        if exclusive_maximum_value is not UNSET:
            field_dict["exclusiveMaximumValue"] = exclusive_maximum_value
        if exclusive_minimum is not UNSET:
            field_dict["exclusiveMinimum"] = exclusive_minimum
        if exclusive_minimum_value is not UNSET:
            field_dict["exclusiveMinimumValue"] = exclusive_minimum_value
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if external_docs is not UNSET:
            field_dict["externalDocs"] = external_docs
        if format_ is not UNSET:
            field_dict["format"] = format_
        if getanchor is not UNSET:
            field_dict["get$anchor"] = getanchor
        if getcomment is not UNSET:
            field_dict["get$comment"] = getcomment
        if getid is not UNSET:
            field_dict["get$id"] = getid
        if getref is not UNSET:
            field_dict["get$ref"] = getref
        if getschema is not UNSET:
            field_dict["get$schema"] = getschema
        if if_ is not UNSET:
            field_dict["if"] = if_
        if items is not UNSET:
            field_dict["items"] = items
        if json_schema is not UNSET:
            field_dict["jsonSchema"] = json_schema
        if json_schema_impl is not UNSET:
            field_dict["jsonSchemaImpl"] = json_schema_impl
        if max_contains is not UNSET:
            field_dict["maxContains"] = max_contains
        if max_items is not UNSET:
            field_dict["maxItems"] = max_items
        if max_length is not UNSET:
            field_dict["maxLength"] = max_length
        if max_properties is not UNSET:
            field_dict["maxProperties"] = max_properties
        if maximum is not UNSET:
            field_dict["maximum"] = maximum
        if min_contains is not UNSET:
            field_dict["minContains"] = min_contains
        if min_items is not UNSET:
            field_dict["minItems"] = min_items
        if min_length is not UNSET:
            field_dict["minLength"] = min_length
        if min_properties is not UNSET:
            field_dict["minProperties"] = min_properties
        if minimum is not UNSET:
            field_dict["minimum"] = minimum
        if multiple_of is not UNSET:
            field_dict["multipleOf"] = multiple_of
        if not_ is not UNSET:
            field_dict["not"] = not_
        if nullable is not UNSET:
            field_dict["nullable"] = nullable
        if one_of is not UNSET:
            field_dict["oneOf"] = one_of
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if prefix_items is not UNSET:
            field_dict["prefixItems"] = prefix_items
        if property_names is not UNSET:
            field_dict["propertyNames"] = property_names
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if required is not UNSET:
            field_dict["required"] = required
        if then is not UNSET:
            field_dict["then"] = then
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if types is not UNSET:
            field_dict["types"] = types
        if unevaluated_items is not UNSET:
            field_dict["unevaluatedItems"] = unevaluated_items
        if unevaluated_properties is not UNSET:
            field_dict["unevaluatedProperties"] = unevaluated_properties
        if unique_items is not UNSET:
            field_dict["uniqueItems"] = unique_items
        if write_only is not UNSET:
            field_dict["writeOnly"] = write_only
        if xml is not UNSET:
            field_dict["xml"] = xml

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discriminator import Discriminator
        from ..models.external_documentation import ExternalDocumentation
        from ..models.schema import Schema
        from ..models.schema_object_additional_properties import SchemaObjectAdditionalProperties
        from ..models.schema_object_const import SchemaObjectConst
        from ..models.schema_object_default import SchemaObjectDefault
        from ..models.schema_object_dependent_required import SchemaObjectDependentRequired
        from ..models.schema_object_enum_item import SchemaObjectEnumItem
        from ..models.schema_object_example import SchemaObjectExample
        from ..models.schema_object_examples_item import SchemaObjectExamplesItem
        from ..models.schema_object_extensions import SchemaObjectExtensions
        from ..models.schema_object_json_schema import SchemaObjectJsonSchema
        from ..models.schema_object_json_schema_impl import SchemaObjectJsonSchemaImpl
        from ..models.xml import XML

        d = dict(src_dict)
        _additional_items = d.pop("additionalItems", UNSET)
        additional_items: Schema | Unset
        if isinstance(_additional_items, Unset):
            additional_items = UNSET
        else:
            additional_items = Schema.from_dict(_additional_items)

        _additional_properties = d.pop("additionalProperties", UNSET)
        additional_properties: SchemaObjectAdditionalProperties | Unset
        if isinstance(_additional_properties, Unset):
            additional_properties = UNSET
        else:
            additional_properties = SchemaObjectAdditionalProperties.from_dict(_additional_properties)

        _all_of = d.pop("allOf", UNSET)
        all_of: list[Schema] | Unset = UNSET
        if _all_of is not UNSET:
            all_of = []
            for all_of_item_data in _all_of:
                all_of_item = Schema.from_dict(all_of_item_data)

                all_of.append(all_of_item)

        _any_of = d.pop("anyOf", UNSET)
        any_of: list[Schema] | Unset = UNSET
        if _any_of is not UNSET:
            any_of = []
            for any_of_item_data in _any_of:
                any_of_item = Schema.from_dict(any_of_item_data)

                any_of.append(any_of_item)

        boolean_schema_value = d.pop("booleanSchemaValue", UNSET)

        _const = d.pop("const", UNSET)
        const: SchemaObjectConst | Unset
        if isinstance(_const, Unset):
            const = UNSET
        else:
            const = SchemaObjectConst.from_dict(_const)

        _contains = d.pop("contains", UNSET)
        contains: Schema | Unset
        if isinstance(_contains, Unset):
            contains = UNSET
        else:
            contains = Schema.from_dict(_contains)

        content_encoding = d.pop("contentEncoding", UNSET)

        content_media_type = d.pop("contentMediaType", UNSET)

        _content_schema = d.pop("contentSchema", UNSET)
        content_schema: Schema | Unset
        if isinstance(_content_schema, Unset):
            content_schema = UNSET
        else:
            content_schema = Schema.from_dict(_content_schema)

        _default = d.pop("default", UNSET)
        default: SchemaObjectDefault | Unset
        if isinstance(_default, Unset):
            default = UNSET
        else:
            default = SchemaObjectDefault.from_dict(_default)

        _dependent_required = d.pop("dependentRequired", UNSET)
        dependent_required: SchemaObjectDependentRequired | Unset
        if isinstance(_dependent_required, Unset):
            dependent_required = UNSET
        else:
            dependent_required = SchemaObjectDependentRequired.from_dict(_dependent_required)

        deprecated = d.pop("deprecated", UNSET)

        description = d.pop("description", UNSET)

        _discriminator = d.pop("discriminator", UNSET)
        discriminator: Discriminator | Unset
        if isinstance(_discriminator, Unset):
            discriminator = UNSET
        else:
            discriminator = Discriminator.from_dict(_discriminator)

        _else_ = d.pop("else", UNSET)
        else_: Schema | Unset
        if isinstance(_else_, Unset):
            else_ = UNSET
        else:
            else_ = Schema.from_dict(_else_)

        _enum = d.pop("enum", UNSET)
        enum: list[SchemaObjectEnumItem] | Unset = UNSET
        if _enum is not UNSET:
            enum = []
            for enum_item_data in _enum:
                enum_item = SchemaObjectEnumItem.from_dict(enum_item_data)

                enum.append(enum_item)

        _example = d.pop("example", UNSET)
        example: SchemaObjectExample | Unset
        if isinstance(_example, Unset):
            example = UNSET
        else:
            example = SchemaObjectExample.from_dict(_example)

        example_set_flag = d.pop("exampleSetFlag", UNSET)

        _examples = d.pop("examples", UNSET)
        examples: list[SchemaObjectExamplesItem] | Unset = UNSET
        if _examples is not UNSET:
            examples = []
            for examples_item_data in _examples:
                examples_item = SchemaObjectExamplesItem.from_dict(examples_item_data)

                examples.append(examples_item)

        exclusive_maximum = d.pop("exclusiveMaximum", UNSET)

        exclusive_maximum_value = d.pop("exclusiveMaximumValue", UNSET)

        exclusive_minimum = d.pop("exclusiveMinimum", UNSET)

        exclusive_minimum_value = d.pop("exclusiveMinimumValue", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: SchemaObjectExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = SchemaObjectExtensions.from_dict(_extensions)

        _external_docs = d.pop("externalDocs", UNSET)
        external_docs: ExternalDocumentation | Unset
        if isinstance(_external_docs, Unset):
            external_docs = UNSET
        else:
            external_docs = ExternalDocumentation.from_dict(_external_docs)

        format_ = d.pop("format", UNSET)

        getanchor = d.pop("get$anchor", UNSET)

        getcomment = d.pop("get$comment", UNSET)

        getid = d.pop("get$id", UNSET)

        getref = d.pop("get$ref", UNSET)

        getschema = d.pop("get$schema", UNSET)

        _if_ = d.pop("if", UNSET)
        if_: Schema | Unset
        if isinstance(_if_, Unset):
            if_ = UNSET
        else:
            if_ = Schema.from_dict(_if_)

        _items = d.pop("items", UNSET)
        items: SchemaObject | Unset
        if isinstance(_items, Unset):
            items = UNSET
        else:
            items = SchemaObject.from_dict(_items)

        _json_schema = d.pop("jsonSchema", UNSET)
        json_schema: SchemaObjectJsonSchema | Unset
        if isinstance(_json_schema, Unset):
            json_schema = UNSET
        else:
            json_schema = SchemaObjectJsonSchema.from_dict(_json_schema)

        _json_schema_impl = d.pop("jsonSchemaImpl", UNSET)
        json_schema_impl: SchemaObjectJsonSchemaImpl | Unset
        if isinstance(_json_schema_impl, Unset):
            json_schema_impl = UNSET
        else:
            json_schema_impl = SchemaObjectJsonSchemaImpl.from_dict(_json_schema_impl)

        max_contains = d.pop("maxContains", UNSET)

        max_items = d.pop("maxItems", UNSET)

        max_length = d.pop("maxLength", UNSET)

        max_properties = d.pop("maxProperties", UNSET)

        maximum = d.pop("maximum", UNSET)

        min_contains = d.pop("minContains", UNSET)

        min_items = d.pop("minItems", UNSET)

        min_length = d.pop("minLength", UNSET)

        min_properties = d.pop("minProperties", UNSET)

        minimum = d.pop("minimum", UNSET)

        multiple_of = d.pop("multipleOf", UNSET)

        _not_ = d.pop("not", UNSET)
        not_: Schema | Unset
        if isinstance(_not_, Unset):
            not_ = UNSET
        else:
            not_ = Schema.from_dict(_not_)

        nullable = d.pop("nullable", UNSET)

        _one_of = d.pop("oneOf", UNSET)
        one_of: list[Schema] | Unset = UNSET
        if _one_of is not UNSET:
            one_of = []
            for one_of_item_data in _one_of:
                one_of_item = Schema.from_dict(one_of_item_data)

                one_of.append(one_of_item)

        pattern = d.pop("pattern", UNSET)

        _prefix_items = d.pop("prefixItems", UNSET)
        prefix_items: list[Schema] | Unset = UNSET
        if _prefix_items is not UNSET:
            prefix_items = []
            for prefix_items_item_data in _prefix_items:
                prefix_items_item = Schema.from_dict(prefix_items_item_data)

                prefix_items.append(prefix_items_item)

        _property_names = d.pop("propertyNames", UNSET)
        property_names: Schema | Unset
        if isinstance(_property_names, Unset):
            property_names = UNSET
        else:
            property_names = Schema.from_dict(_property_names)

        read_only = d.pop("readOnly", UNSET)

        required = cast(list[str], d.pop("required", UNSET))

        _then = d.pop("then", UNSET)
        then: Schema | Unset
        if isinstance(_then, Unset):
            then = UNSET
        else:
            then = Schema.from_dict(_then)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        types = cast(list[str], d.pop("types", UNSET))

        _unevaluated_items = d.pop("unevaluatedItems", UNSET)
        unevaluated_items: Schema | Unset
        if isinstance(_unevaluated_items, Unset):
            unevaluated_items = UNSET
        else:
            unevaluated_items = Schema.from_dict(_unevaluated_items)

        _unevaluated_properties = d.pop("unevaluatedProperties", UNSET)
        unevaluated_properties: Schema | Unset
        if isinstance(_unevaluated_properties, Unset):
            unevaluated_properties = UNSET
        else:
            unevaluated_properties = Schema.from_dict(_unevaluated_properties)

        unique_items = d.pop("uniqueItems", UNSET)

        write_only = d.pop("writeOnly", UNSET)

        _xml = d.pop("xml", UNSET)
        xml: XML | Unset
        if isinstance(_xml, Unset):
            xml = UNSET
        else:
            xml = XML.from_dict(_xml)

        schema_object = cls(
            additional_items=additional_items,
            additional_properties=additional_properties,
            all_of=all_of,
            any_of=any_of,
            boolean_schema_value=boolean_schema_value,
            const=const,
            contains=contains,
            content_encoding=content_encoding,
            content_media_type=content_media_type,
            content_schema=content_schema,
            default=default,
            dependent_required=dependent_required,
            deprecated=deprecated,
            description=description,
            discriminator=discriminator,
            else_=else_,
            enum=enum,
            example=example,
            example_set_flag=example_set_flag,
            examples=examples,
            exclusive_maximum=exclusive_maximum,
            exclusive_maximum_value=exclusive_maximum_value,
            exclusive_minimum=exclusive_minimum,
            exclusive_minimum_value=exclusive_minimum_value,
            extensions=extensions,
            external_docs=external_docs,
            format_=format_,
            getanchor=getanchor,
            getcomment=getcomment,
            getid=getid,
            getref=getref,
            getschema=getschema,
            if_=if_,
            items=items,
            json_schema=json_schema,
            json_schema_impl=json_schema_impl,
            max_contains=max_contains,
            max_items=max_items,
            max_length=max_length,
            max_properties=max_properties,
            maximum=maximum,
            min_contains=min_contains,
            min_items=min_items,
            min_length=min_length,
            min_properties=min_properties,
            minimum=minimum,
            multiple_of=multiple_of,
            not_=not_,
            nullable=nullable,
            one_of=one_of,
            pattern=pattern,
            prefix_items=prefix_items,
            property_names=property_names,
            read_only=read_only,
            required=required,
            then=then,
            title=title,
            type_=type_,
            types=types,
            unevaluated_items=unevaluated_items,
            unevaluated_properties=unevaluated_properties,
            unique_items=unique_items,
            write_only=write_only,
            xml=xml,
        )

        schema_object.additional_properties = d
        return schema_object

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
