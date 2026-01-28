from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbtp_definition_type import GBTPDefinitionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btp_annotation_231 import BTPAnnotation231
    from ..models.btp_argument_declaration_232 import BTPArgumentDeclaration232
    from ..models.btp_identifier_8 import BTPIdentifier8
    from ..models.btp_space_10 import BTPSpace10
    from ..models.btp_statement_269 import BTPStatement269
    from ..models.btp_statement_block_271 import BTPStatementBlock271
    from ..models.btp_type_name_290 import BTPTypeName290


T = TypeVar("T", bound="BTPFunctionDeclaration246")


@_attrs_define
class BTPFunctionDeclaration246:
    """
    Attributes:
        annotation (BTPAnnotation231 | Unset):
        arguments (list[BTPArgumentDeclaration232] | Unset):
        arguments_to_document (list[BTPArgumentDeclaration232] | Unset):
        atomic (bool | Unset):
        body (BTPStatementBlock271 | Unset):
        bt_type (str | Unset): Type of JSON object.
        deprecated (bool | Unset):
        deprecated_explanation (str | Unset):
        documentation_type (GBTPDefinitionType | Unset):
        end_source_location (int | Unset):
        for_export (bool | Unset):
        name (BTPIdentifier8 | Unset):
        node_id (str | Unset):
        precondition (BTPStatement269 | Unset):
        return_type (BTPTypeName290 | Unset):
        short_descriptor (str | Unset):
        space_after (BTPSpace10 | Unset):
        space_after_arglist (BTPSpace10 | Unset):
        space_after_export (BTPSpace10 | Unset):
        space_before (BTPSpace10 | Unset):
        space_default (bool | Unset):
        space_in_empty_list (BTPSpace10 | Unset):
        start_source_location (int | Unset):
        symbol_name (BTPIdentifier8 | Unset):
    """

    annotation: BTPAnnotation231 | Unset = UNSET
    arguments: list[BTPArgumentDeclaration232] | Unset = UNSET
    arguments_to_document: list[BTPArgumentDeclaration232] | Unset = UNSET
    atomic: bool | Unset = UNSET
    body: BTPStatementBlock271 | Unset = UNSET
    bt_type: str | Unset = UNSET
    deprecated: bool | Unset = UNSET
    deprecated_explanation: str | Unset = UNSET
    documentation_type: GBTPDefinitionType | Unset = UNSET
    end_source_location: int | Unset = UNSET
    for_export: bool | Unset = UNSET
    name: BTPIdentifier8 | Unset = UNSET
    node_id: str | Unset = UNSET
    precondition: BTPStatement269 | Unset = UNSET
    return_type: BTPTypeName290 | Unset = UNSET
    short_descriptor: str | Unset = UNSET
    space_after: BTPSpace10 | Unset = UNSET
    space_after_arglist: BTPSpace10 | Unset = UNSET
    space_after_export: BTPSpace10 | Unset = UNSET
    space_before: BTPSpace10 | Unset = UNSET
    space_default: bool | Unset = UNSET
    space_in_empty_list: BTPSpace10 | Unset = UNSET
    start_source_location: int | Unset = UNSET
    symbol_name: BTPIdentifier8 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotation, Unset):
            annotation = self.annotation.to_dict()

        arguments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.arguments, Unset):
            arguments = []
            for arguments_item_data in self.arguments:
                arguments_item = arguments_item_data.to_dict()
                arguments.append(arguments_item)

        arguments_to_document: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.arguments_to_document, Unset):
            arguments_to_document = []
            for arguments_to_document_item_data in self.arguments_to_document:
                arguments_to_document_item = arguments_to_document_item_data.to_dict()
                arguments_to_document.append(arguments_to_document_item)

        atomic = self.atomic

        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        bt_type = self.bt_type

        deprecated = self.deprecated

        deprecated_explanation = self.deprecated_explanation

        documentation_type: str | Unset = UNSET
        if not isinstance(self.documentation_type, Unset):
            documentation_type = self.documentation_type.value

        end_source_location = self.end_source_location

        for_export = self.for_export

        name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        node_id = self.node_id

        precondition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.precondition, Unset):
            precondition = self.precondition.to_dict()

        return_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.return_type, Unset):
            return_type = self.return_type.to_dict()

        short_descriptor = self.short_descriptor

        space_after: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_after, Unset):
            space_after = self.space_after.to_dict()

        space_after_arglist: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_after_arglist, Unset):
            space_after_arglist = self.space_after_arglist.to_dict()

        space_after_export: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_after_export, Unset):
            space_after_export = self.space_after_export.to_dict()

        space_before: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_before, Unset):
            space_before = self.space_before.to_dict()

        space_default = self.space_default

        space_in_empty_list: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_in_empty_list, Unset):
            space_in_empty_list = self.space_in_empty_list.to_dict()

        start_source_location = self.start_source_location

        symbol_name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.symbol_name, Unset):
            symbol_name = self.symbol_name.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if arguments is not UNSET:
            field_dict["arguments"] = arguments
        if arguments_to_document is not UNSET:
            field_dict["argumentsToDocument"] = arguments_to_document
        if atomic is not UNSET:
            field_dict["atomic"] = atomic
        if body is not UNSET:
            field_dict["body"] = body
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated
        if deprecated_explanation is not UNSET:
            field_dict["deprecatedExplanation"] = deprecated_explanation
        if documentation_type is not UNSET:
            field_dict["documentationType"] = documentation_type
        if end_source_location is not UNSET:
            field_dict["endSourceLocation"] = end_source_location
        if for_export is not UNSET:
            field_dict["forExport"] = for_export
        if name is not UNSET:
            field_dict["name"] = name
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if precondition is not UNSET:
            field_dict["precondition"] = precondition
        if return_type is not UNSET:
            field_dict["returnType"] = return_type
        if short_descriptor is not UNSET:
            field_dict["shortDescriptor"] = short_descriptor
        if space_after is not UNSET:
            field_dict["spaceAfter"] = space_after
        if space_after_arglist is not UNSET:
            field_dict["spaceAfterArglist"] = space_after_arglist
        if space_after_export is not UNSET:
            field_dict["spaceAfterExport"] = space_after_export
        if space_before is not UNSET:
            field_dict["spaceBefore"] = space_before
        if space_default is not UNSET:
            field_dict["spaceDefault"] = space_default
        if space_in_empty_list is not UNSET:
            field_dict["spaceInEmptyList"] = space_in_empty_list
        if start_source_location is not UNSET:
            field_dict["startSourceLocation"] = start_source_location
        if symbol_name is not UNSET:
            field_dict["symbolName"] = symbol_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btp_annotation_231 import BTPAnnotation231
        from ..models.btp_argument_declaration_232 import BTPArgumentDeclaration232
        from ..models.btp_identifier_8 import BTPIdentifier8
        from ..models.btp_space_10 import BTPSpace10
        from ..models.btp_statement_269 import BTPStatement269
        from ..models.btp_statement_block_271 import BTPStatementBlock271
        from ..models.btp_type_name_290 import BTPTypeName290

        d = dict(src_dict)
        _annotation = d.pop("annotation", UNSET)
        annotation: BTPAnnotation231 | Unset
        if isinstance(_annotation, Unset):
            annotation = UNSET
        else:
            annotation = BTPAnnotation231.from_dict(_annotation)

        _arguments = d.pop("arguments", UNSET)
        arguments: list[BTPArgumentDeclaration232] | Unset = UNSET
        if _arguments is not UNSET:
            arguments = []
            for arguments_item_data in _arguments:
                arguments_item = BTPArgumentDeclaration232.from_dict(arguments_item_data)

                arguments.append(arguments_item)

        _arguments_to_document = d.pop("argumentsToDocument", UNSET)
        arguments_to_document: list[BTPArgumentDeclaration232] | Unset = UNSET
        if _arguments_to_document is not UNSET:
            arguments_to_document = []
            for arguments_to_document_item_data in _arguments_to_document:
                arguments_to_document_item = BTPArgumentDeclaration232.from_dict(arguments_to_document_item_data)

                arguments_to_document.append(arguments_to_document_item)

        atomic = d.pop("atomic", UNSET)

        _body = d.pop("body", UNSET)
        body: BTPStatementBlock271 | Unset
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = BTPStatementBlock271.from_dict(_body)

        bt_type = d.pop("btType", UNSET)

        deprecated = d.pop("deprecated", UNSET)

        deprecated_explanation = d.pop("deprecatedExplanation", UNSET)

        _documentation_type = d.pop("documentationType", UNSET)
        documentation_type: GBTPDefinitionType | Unset
        if isinstance(_documentation_type, Unset):
            documentation_type = UNSET
        else:
            documentation_type = GBTPDefinitionType(_documentation_type)

        end_source_location = d.pop("endSourceLocation", UNSET)

        for_export = d.pop("forExport", UNSET)

        _name = d.pop("name", UNSET)
        name: BTPIdentifier8 | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = BTPIdentifier8.from_dict(_name)

        node_id = d.pop("nodeId", UNSET)

        _precondition = d.pop("precondition", UNSET)
        precondition: BTPStatement269 | Unset
        if isinstance(_precondition, Unset):
            precondition = UNSET
        else:
            precondition = BTPStatement269.from_dict(_precondition)

        _return_type = d.pop("returnType", UNSET)
        return_type: BTPTypeName290 | Unset
        if isinstance(_return_type, Unset):
            return_type = UNSET
        else:
            return_type = BTPTypeName290.from_dict(_return_type)

        short_descriptor = d.pop("shortDescriptor", UNSET)

        _space_after = d.pop("spaceAfter", UNSET)
        space_after: BTPSpace10 | Unset
        if isinstance(_space_after, Unset):
            space_after = UNSET
        else:
            space_after = BTPSpace10.from_dict(_space_after)

        _space_after_arglist = d.pop("spaceAfterArglist", UNSET)
        space_after_arglist: BTPSpace10 | Unset
        if isinstance(_space_after_arglist, Unset):
            space_after_arglist = UNSET
        else:
            space_after_arglist = BTPSpace10.from_dict(_space_after_arglist)

        _space_after_export = d.pop("spaceAfterExport", UNSET)
        space_after_export: BTPSpace10 | Unset
        if isinstance(_space_after_export, Unset):
            space_after_export = UNSET
        else:
            space_after_export = BTPSpace10.from_dict(_space_after_export)

        _space_before = d.pop("spaceBefore", UNSET)
        space_before: BTPSpace10 | Unset
        if isinstance(_space_before, Unset):
            space_before = UNSET
        else:
            space_before = BTPSpace10.from_dict(_space_before)

        space_default = d.pop("spaceDefault", UNSET)

        _space_in_empty_list = d.pop("spaceInEmptyList", UNSET)
        space_in_empty_list: BTPSpace10 | Unset
        if isinstance(_space_in_empty_list, Unset):
            space_in_empty_list = UNSET
        else:
            space_in_empty_list = BTPSpace10.from_dict(_space_in_empty_list)

        start_source_location = d.pop("startSourceLocation", UNSET)

        _symbol_name = d.pop("symbolName", UNSET)
        symbol_name: BTPIdentifier8 | Unset
        if isinstance(_symbol_name, Unset):
            symbol_name = UNSET
        else:
            symbol_name = BTPIdentifier8.from_dict(_symbol_name)

        btp_function_declaration_246 = cls(
            annotation=annotation,
            arguments=arguments,
            arguments_to_document=arguments_to_document,
            atomic=atomic,
            body=body,
            bt_type=bt_type,
            deprecated=deprecated,
            deprecated_explanation=deprecated_explanation,
            documentation_type=documentation_type,
            end_source_location=end_source_location,
            for_export=for_export,
            name=name,
            node_id=node_id,
            precondition=precondition,
            return_type=return_type,
            short_descriptor=short_descriptor,
            space_after=space_after,
            space_after_arglist=space_after_arglist,
            space_after_export=space_after_export,
            space_before=space_before,
            space_default=space_default,
            space_in_empty_list=space_in_empty_list,
            start_source_location=start_source_location,
            symbol_name=symbol_name,
        )

        btp_function_declaration_246.additional_properties = d
        return btp_function_declaration_246

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
