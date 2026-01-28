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
    from ..models.btp_module_id_235 import BTPModuleId235
    from ..models.btp_space_10 import BTPSpace10


T = TypeVar("T", bound="BTPTopLevelImport285")


@_attrs_define
class BTPTopLevelImport285:
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
        arguments_to_document (list[BTPArgumentDeclaration232] | Unset):
        deprecated (bool | Unset):
        deprecated_explanation (str | Unset):
        for_export (bool | Unset):
        space_after_export (BTPSpace10 | Unset):
        symbol_name (BTPIdentifier8 | Unset):
        combined_namespace_path_and_version (str | Unset):
        import_microversion (str | Unset): Element microversion that is being imported.
        module_id (BTPModuleId235 | Unset):
        namespace (list[BTPIdentifier8] | Unset):
        namespace_string (str | Unset):
        space_before_import (BTPSpace10 | Unset):
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
    arguments_to_document: list[BTPArgumentDeclaration232] | Unset = UNSET
    deprecated: bool | Unset = UNSET
    deprecated_explanation: str | Unset = UNSET
    for_export: bool | Unset = UNSET
    space_after_export: BTPSpace10 | Unset = UNSET
    symbol_name: BTPIdentifier8 | Unset = UNSET
    combined_namespace_path_and_version: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    module_id: BTPModuleId235 | Unset = UNSET
    namespace: list[BTPIdentifier8] | Unset = UNSET
    namespace_string: str | Unset = UNSET
    space_before_import: BTPSpace10 | Unset = UNSET
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

        arguments_to_document: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.arguments_to_document, Unset):
            arguments_to_document = []
            for arguments_to_document_item_data in self.arguments_to_document:
                arguments_to_document_item = arguments_to_document_item_data.to_dict()
                arguments_to_document.append(arguments_to_document_item)

        deprecated = self.deprecated

        deprecated_explanation = self.deprecated_explanation

        for_export = self.for_export

        space_after_export: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_after_export, Unset):
            space_after_export = self.space_after_export.to_dict()

        symbol_name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.symbol_name, Unset):
            symbol_name = self.symbol_name.to_dict()

        combined_namespace_path_and_version = self.combined_namespace_path_and_version

        import_microversion = self.import_microversion

        module_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.module_id, Unset):
            module_id = self.module_id.to_dict()

        namespace: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.namespace, Unset):
            namespace = []
            for namespace_item_data in self.namespace:
                namespace_item = namespace_item_data.to_dict()
                namespace.append(namespace_item)

        namespace_string = self.namespace_string

        space_before_import: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_before_import, Unset):
            space_before_import = self.space_before_import.to_dict()

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
        if arguments_to_document is not UNSET:
            field_dict["argumentsToDocument"] = arguments_to_document
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated
        if deprecated_explanation is not UNSET:
            field_dict["deprecatedExplanation"] = deprecated_explanation
        if for_export is not UNSET:
            field_dict["forExport"] = for_export
        if space_after_export is not UNSET:
            field_dict["spaceAfterExport"] = space_after_export
        if symbol_name is not UNSET:
            field_dict["symbolName"] = symbol_name
        if combined_namespace_path_and_version is not UNSET:
            field_dict["combinedNamespacePathAndVersion"] = combined_namespace_path_and_version
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if module_id is not UNSET:
            field_dict["moduleId"] = module_id
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if namespace_string is not UNSET:
            field_dict["namespaceString"] = namespace_string
        if space_before_import is not UNSET:
            field_dict["spaceBeforeImport"] = space_before_import

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btp_annotation_231 import BTPAnnotation231
        from ..models.btp_argument_declaration_232 import BTPArgumentDeclaration232
        from ..models.btp_identifier_8 import BTPIdentifier8
        from ..models.btp_module_id_235 import BTPModuleId235
        from ..models.btp_space_10 import BTPSpace10

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

        _arguments_to_document = d.pop("argumentsToDocument", UNSET)
        arguments_to_document: list[BTPArgumentDeclaration232] | Unset = UNSET
        if _arguments_to_document is not UNSET:
            arguments_to_document = []
            for arguments_to_document_item_data in _arguments_to_document:
                arguments_to_document_item = BTPArgumentDeclaration232.from_dict(arguments_to_document_item_data)

                arguments_to_document.append(arguments_to_document_item)

        deprecated = d.pop("deprecated", UNSET)

        deprecated_explanation = d.pop("deprecatedExplanation", UNSET)

        for_export = d.pop("forExport", UNSET)

        _space_after_export = d.pop("spaceAfterExport", UNSET)
        space_after_export: BTPSpace10 | Unset
        if isinstance(_space_after_export, Unset):
            space_after_export = UNSET
        else:
            space_after_export = BTPSpace10.from_dict(_space_after_export)

        _symbol_name = d.pop("symbolName", UNSET)
        symbol_name: BTPIdentifier8 | Unset
        if isinstance(_symbol_name, Unset):
            symbol_name = UNSET
        else:
            symbol_name = BTPIdentifier8.from_dict(_symbol_name)

        combined_namespace_path_and_version = d.pop("combinedNamespacePathAndVersion", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        _module_id = d.pop("moduleId", UNSET)
        module_id: BTPModuleId235 | Unset
        if isinstance(_module_id, Unset):
            module_id = UNSET
        else:
            module_id = BTPModuleId235.from_dict(_module_id)

        _namespace = d.pop("namespace", UNSET)
        namespace: list[BTPIdentifier8] | Unset = UNSET
        if _namespace is not UNSET:
            namespace = []
            for namespace_item_data in _namespace:
                namespace_item = BTPIdentifier8.from_dict(namespace_item_data)

                namespace.append(namespace_item)

        namespace_string = d.pop("namespaceString", UNSET)

        _space_before_import = d.pop("spaceBeforeImport", UNSET)
        space_before_import: BTPSpace10 | Unset
        if isinstance(_space_before_import, Unset):
            space_before_import = UNSET
        else:
            space_before_import = BTPSpace10.from_dict(_space_before_import)

        btp_top_level_import_285 = cls(
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
            arguments_to_document=arguments_to_document,
            deprecated=deprecated,
            deprecated_explanation=deprecated_explanation,
            for_export=for_export,
            space_after_export=space_after_export,
            symbol_name=symbol_name,
            combined_namespace_path_and_version=combined_namespace_path_and_version,
            import_microversion=import_microversion,
            module_id=module_id,
            namespace=namespace,
            namespace_string=namespace_string,
            space_before_import=space_before_import,
        )

        btp_top_level_import_285.additional_properties = d
        return btp_top_level_import_285

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
