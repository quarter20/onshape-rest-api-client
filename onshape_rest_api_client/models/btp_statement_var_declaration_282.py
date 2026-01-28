from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbtp_definition_type import GBTPDefinitionType
from ..models.gbtp_type import GBTPType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btp_annotation_231 import BTPAnnotation231
    from ..models.btp_expression_9 import BTPExpression9
    from ..models.btp_identifier_8 import BTPIdentifier8
    from ..models.btp_space_10 import BTPSpace10
    from ..models.btp_type_name_290 import BTPTypeName290


T = TypeVar("T", bound="BTPStatementVarDeclaration282")


@_attrs_define
class BTPStatementVarDeclaration282:
    """
    Attributes:
        atomic (bool | Unset):
        bt_type (str | Unset): Type of JSON object.
        documentation_type (GBTPDefinitionType | Unset):
        end_source_location (int | Unset):
        node_id (str | Unset):
        short_descriptor (str | Unset):
        space_after (BTPSpace10 | Unset):
        space_before (BTPSpace10 | Unset):
        space_default (bool | Unset):
        start_source_location (int | Unset):
        annotation (BTPAnnotation231 | Unset):
        identifier (BTPIdentifier8 | Unset):
        name (BTPIdentifier8 | Unset):
        standard_type (GBTPType | Unset):
        type_ (BTPTypeName290 | Unset):
        type_name (str | Unset):
        value (BTPExpression9 | Unset):
    """

    atomic: bool | Unset = UNSET
    bt_type: str | Unset = UNSET
    documentation_type: GBTPDefinitionType | Unset = UNSET
    end_source_location: int | Unset = UNSET
    node_id: str | Unset = UNSET
    short_descriptor: str | Unset = UNSET
    space_after: BTPSpace10 | Unset = UNSET
    space_before: BTPSpace10 | Unset = UNSET
    space_default: bool | Unset = UNSET
    start_source_location: int | Unset = UNSET
    annotation: BTPAnnotation231 | Unset = UNSET
    identifier: BTPIdentifier8 | Unset = UNSET
    name: BTPIdentifier8 | Unset = UNSET
    standard_type: GBTPType | Unset = UNSET
    type_: BTPTypeName290 | Unset = UNSET
    type_name: str | Unset = UNSET
    value: BTPExpression9 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        atomic = self.atomic

        bt_type = self.bt_type

        documentation_type: str | Unset = UNSET
        if not isinstance(self.documentation_type, Unset):
            documentation_type = self.documentation_type.value

        end_source_location = self.end_source_location

        node_id = self.node_id

        short_descriptor = self.short_descriptor

        space_after: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_after, Unset):
            space_after = self.space_after.to_dict()

        space_before: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_before, Unset):
            space_before = self.space_before.to_dict()

        space_default = self.space_default

        start_source_location = self.start_source_location

        annotation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotation, Unset):
            annotation = self.annotation.to_dict()

        identifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = self.identifier.to_dict()

        name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        standard_type: str | Unset = UNSET
        if not isinstance(self.standard_type, Unset):
            standard_type = self.standard_type.value

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        type_name = self.type_name

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if atomic is not UNSET:
            field_dict["atomic"] = atomic
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if documentation_type is not UNSET:
            field_dict["documentationType"] = documentation_type
        if end_source_location is not UNSET:
            field_dict["endSourceLocation"] = end_source_location
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if short_descriptor is not UNSET:
            field_dict["shortDescriptor"] = short_descriptor
        if space_after is not UNSET:
            field_dict["spaceAfter"] = space_after
        if space_before is not UNSET:
            field_dict["spaceBefore"] = space_before
        if space_default is not UNSET:
            field_dict["spaceDefault"] = space_default
        if start_source_location is not UNSET:
            field_dict["startSourceLocation"] = start_source_location
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name
        if standard_type is not UNSET:
            field_dict["standardType"] = standard_type
        if type_ is not UNSET:
            field_dict["type"] = type_
        if type_name is not UNSET:
            field_dict["typeName"] = type_name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btp_annotation_231 import BTPAnnotation231
        from ..models.btp_expression_9 import BTPExpression9
        from ..models.btp_identifier_8 import BTPIdentifier8
        from ..models.btp_space_10 import BTPSpace10
        from ..models.btp_type_name_290 import BTPTypeName290

        d = dict(src_dict)
        atomic = d.pop("atomic", UNSET)

        bt_type = d.pop("btType", UNSET)

        _documentation_type = d.pop("documentationType", UNSET)
        documentation_type: GBTPDefinitionType | Unset
        if isinstance(_documentation_type, Unset):
            documentation_type = UNSET
        else:
            documentation_type = GBTPDefinitionType(_documentation_type)

        end_source_location = d.pop("endSourceLocation", UNSET)

        node_id = d.pop("nodeId", UNSET)

        short_descriptor = d.pop("shortDescriptor", UNSET)

        _space_after = d.pop("spaceAfter", UNSET)
        space_after: BTPSpace10 | Unset
        if isinstance(_space_after, Unset):
            space_after = UNSET
        else:
            space_after = BTPSpace10.from_dict(_space_after)

        _space_before = d.pop("spaceBefore", UNSET)
        space_before: BTPSpace10 | Unset
        if isinstance(_space_before, Unset):
            space_before = UNSET
        else:
            space_before = BTPSpace10.from_dict(_space_before)

        space_default = d.pop("spaceDefault", UNSET)

        start_source_location = d.pop("startSourceLocation", UNSET)

        _annotation = d.pop("annotation", UNSET)
        annotation: BTPAnnotation231 | Unset
        if isinstance(_annotation, Unset):
            annotation = UNSET
        else:
            annotation = BTPAnnotation231.from_dict(_annotation)

        _identifier = d.pop("identifier", UNSET)
        identifier: BTPIdentifier8 | Unset
        if isinstance(_identifier, Unset):
            identifier = UNSET
        else:
            identifier = BTPIdentifier8.from_dict(_identifier)

        _name = d.pop("name", UNSET)
        name: BTPIdentifier8 | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = BTPIdentifier8.from_dict(_name)

        _standard_type = d.pop("standardType", UNSET)
        standard_type: GBTPType | Unset
        if isinstance(_standard_type, Unset):
            standard_type = UNSET
        else:
            standard_type = GBTPType(_standard_type)

        _type_ = d.pop("type", UNSET)
        type_: BTPTypeName290 | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BTPTypeName290.from_dict(_type_)

        type_name = d.pop("typeName", UNSET)

        _value = d.pop("value", UNSET)
        value: BTPExpression9 | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = BTPExpression9.from_dict(_value)

        btp_statement_var_declaration_282 = cls(
            atomic=atomic,
            bt_type=bt_type,
            documentation_type=documentation_type,
            end_source_location=end_source_location,
            node_id=node_id,
            short_descriptor=short_descriptor,
            space_after=space_after,
            space_before=space_before,
            space_default=space_default,
            start_source_location=start_source_location,
            annotation=annotation,
            identifier=identifier,
            name=name,
            standard_type=standard_type,
            type_=type_,
            type_name=type_name,
            value=value,
        )

        btp_statement_var_declaration_282.additional_properties = d
        return btp_statement_var_declaration_282

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
