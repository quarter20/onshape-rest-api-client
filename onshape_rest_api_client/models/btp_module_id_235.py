from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbtp_definition_type import GBTPDefinitionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_document_with_version_and_element_id import BTDocumentWithVersionAndElementId
    from ..models.bt_document_with_version_id import BTDocumentWithVersionId
    from ..models.btp_literal_string_259 import BTPLiteralString259
    from ..models.btp_space_10 import BTPSpace10


T = TypeVar("T", bound="BTPModuleId235")


@_attrs_define
class BTPModuleId235:
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
        dbimport_string (str | Unset):
        element_import (bool | Unset):
        external_document_with_version (BTDocumentWithVersionId | Unset):
        external_document_with_version_and_element_id (BTDocumentWithVersionAndElementId | Unset):
        external_import (bool | Unset):
        imported_document_id (str | Unset):
        imported_element_id (str | Unset):
        imported_version_id (str | Unset):
        legacy (bool | Unset):
        legacy_element_name (str | Unset):
        legacy_version_number (int | Unset):
        microversion (str | Unset):
        path (BTPLiteralString259 | Unset):
        path_potentially_valid (bool | Unset):
        path_version (str | Unset):
        potentially_valid (bool | Unset):
        space_after_path (BTPSpace10 | Unset):
        space_after_version (BTPSpace10 | Unset):
        space_before_path (BTPSpace10 | Unset):
        space_before_version (BTPSpace10 | Unset):
        standard_library (bool | Unset):
        standard_library_common (bool | Unset):
        valid_legacy_version (bool | Unset):
        version (BTPLiteralString259 | Unset):
        version_and_microversion (str | Unset):
        version_potentially_valid (bool | Unset):
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
    dbimport_string: str | Unset = UNSET
    element_import: bool | Unset = UNSET
    external_document_with_version: BTDocumentWithVersionId | Unset = UNSET
    external_document_with_version_and_element_id: BTDocumentWithVersionAndElementId | Unset = UNSET
    external_import: bool | Unset = UNSET
    imported_document_id: str | Unset = UNSET
    imported_element_id: str | Unset = UNSET
    imported_version_id: str | Unset = UNSET
    legacy: bool | Unset = UNSET
    legacy_element_name: str | Unset = UNSET
    legacy_version_number: int | Unset = UNSET
    microversion: str | Unset = UNSET
    path: BTPLiteralString259 | Unset = UNSET
    path_potentially_valid: bool | Unset = UNSET
    path_version: str | Unset = UNSET
    potentially_valid: bool | Unset = UNSET
    space_after_path: BTPSpace10 | Unset = UNSET
    space_after_version: BTPSpace10 | Unset = UNSET
    space_before_path: BTPSpace10 | Unset = UNSET
    space_before_version: BTPSpace10 | Unset = UNSET
    standard_library: bool | Unset = UNSET
    standard_library_common: bool | Unset = UNSET
    valid_legacy_version: bool | Unset = UNSET
    version: BTPLiteralString259 | Unset = UNSET
    version_and_microversion: str | Unset = UNSET
    version_potentially_valid: bool | Unset = UNSET
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

        dbimport_string = self.dbimport_string

        element_import = self.element_import

        external_document_with_version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_document_with_version, Unset):
            external_document_with_version = self.external_document_with_version.to_dict()

        external_document_with_version_and_element_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_document_with_version_and_element_id, Unset):
            external_document_with_version_and_element_id = self.external_document_with_version_and_element_id.to_dict()

        external_import = self.external_import

        imported_document_id = self.imported_document_id

        imported_element_id = self.imported_element_id

        imported_version_id = self.imported_version_id

        legacy = self.legacy

        legacy_element_name = self.legacy_element_name

        legacy_version_number = self.legacy_version_number

        microversion = self.microversion

        path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = self.path.to_dict()

        path_potentially_valid = self.path_potentially_valid

        path_version = self.path_version

        potentially_valid = self.potentially_valid

        space_after_path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_after_path, Unset):
            space_after_path = self.space_after_path.to_dict()

        space_after_version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_after_version, Unset):
            space_after_version = self.space_after_version.to_dict()

        space_before_path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_before_path, Unset):
            space_before_path = self.space_before_path.to_dict()

        space_before_version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.space_before_version, Unset):
            space_before_version = self.space_before_version.to_dict()

        standard_library = self.standard_library

        standard_library_common = self.standard_library_common

        valid_legacy_version = self.valid_legacy_version

        version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        version_and_microversion = self.version_and_microversion

        version_potentially_valid = self.version_potentially_valid

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
        if dbimport_string is not UNSET:
            field_dict["dbimportString"] = dbimport_string
        if element_import is not UNSET:
            field_dict["elementImport"] = element_import
        if external_document_with_version is not UNSET:
            field_dict["externalDocumentWithVersion"] = external_document_with_version
        if external_document_with_version_and_element_id is not UNSET:
            field_dict["externalDocumentWithVersionAndElementId"] = external_document_with_version_and_element_id
        if external_import is not UNSET:
            field_dict["externalImport"] = external_import
        if imported_document_id is not UNSET:
            field_dict["importedDocumentId"] = imported_document_id
        if imported_element_id is not UNSET:
            field_dict["importedElementId"] = imported_element_id
        if imported_version_id is not UNSET:
            field_dict["importedVersionId"] = imported_version_id
        if legacy is not UNSET:
            field_dict["legacy"] = legacy
        if legacy_element_name is not UNSET:
            field_dict["legacyElementName"] = legacy_element_name
        if legacy_version_number is not UNSET:
            field_dict["legacyVersionNumber"] = legacy_version_number
        if microversion is not UNSET:
            field_dict["microversion"] = microversion
        if path is not UNSET:
            field_dict["path"] = path
        if path_potentially_valid is not UNSET:
            field_dict["pathPotentiallyValid"] = path_potentially_valid
        if path_version is not UNSET:
            field_dict["pathVersion"] = path_version
        if potentially_valid is not UNSET:
            field_dict["potentiallyValid"] = potentially_valid
        if space_after_path is not UNSET:
            field_dict["spaceAfterPath"] = space_after_path
        if space_after_version is not UNSET:
            field_dict["spaceAfterVersion"] = space_after_version
        if space_before_path is not UNSET:
            field_dict["spaceBeforePath"] = space_before_path
        if space_before_version is not UNSET:
            field_dict["spaceBeforeVersion"] = space_before_version
        if standard_library is not UNSET:
            field_dict["standardLibrary"] = standard_library
        if standard_library_common is not UNSET:
            field_dict["standardLibraryCommon"] = standard_library_common
        if valid_legacy_version is not UNSET:
            field_dict["validLegacyVersion"] = valid_legacy_version
        if version is not UNSET:
            field_dict["version"] = version
        if version_and_microversion is not UNSET:
            field_dict["versionAndMicroversion"] = version_and_microversion
        if version_potentially_valid is not UNSET:
            field_dict["versionPotentiallyValid"] = version_potentially_valid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_document_with_version_and_element_id import BTDocumentWithVersionAndElementId
        from ..models.bt_document_with_version_id import BTDocumentWithVersionId
        from ..models.btp_literal_string_259 import BTPLiteralString259
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

        dbimport_string = d.pop("dbimportString", UNSET)

        element_import = d.pop("elementImport", UNSET)

        _external_document_with_version = d.pop("externalDocumentWithVersion", UNSET)
        external_document_with_version: BTDocumentWithVersionId | Unset
        if isinstance(_external_document_with_version, Unset):
            external_document_with_version = UNSET
        else:
            external_document_with_version = BTDocumentWithVersionId.from_dict(_external_document_with_version)

        _external_document_with_version_and_element_id = d.pop("externalDocumentWithVersionAndElementId", UNSET)
        external_document_with_version_and_element_id: BTDocumentWithVersionAndElementId | Unset
        if isinstance(_external_document_with_version_and_element_id, Unset):
            external_document_with_version_and_element_id = UNSET
        else:
            external_document_with_version_and_element_id = BTDocumentWithVersionAndElementId.from_dict(
                _external_document_with_version_and_element_id
            )

        external_import = d.pop("externalImport", UNSET)

        imported_document_id = d.pop("importedDocumentId", UNSET)

        imported_element_id = d.pop("importedElementId", UNSET)

        imported_version_id = d.pop("importedVersionId", UNSET)

        legacy = d.pop("legacy", UNSET)

        legacy_element_name = d.pop("legacyElementName", UNSET)

        legacy_version_number = d.pop("legacyVersionNumber", UNSET)

        microversion = d.pop("microversion", UNSET)

        _path = d.pop("path", UNSET)
        path: BTPLiteralString259 | Unset
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = BTPLiteralString259.from_dict(_path)

        path_potentially_valid = d.pop("pathPotentiallyValid", UNSET)

        path_version = d.pop("pathVersion", UNSET)

        potentially_valid = d.pop("potentiallyValid", UNSET)

        _space_after_path = d.pop("spaceAfterPath", UNSET)
        space_after_path: BTPSpace10 | Unset
        if isinstance(_space_after_path, Unset):
            space_after_path = UNSET
        else:
            space_after_path = BTPSpace10.from_dict(_space_after_path)

        _space_after_version = d.pop("spaceAfterVersion", UNSET)
        space_after_version: BTPSpace10 | Unset
        if isinstance(_space_after_version, Unset):
            space_after_version = UNSET
        else:
            space_after_version = BTPSpace10.from_dict(_space_after_version)

        _space_before_path = d.pop("spaceBeforePath", UNSET)
        space_before_path: BTPSpace10 | Unset
        if isinstance(_space_before_path, Unset):
            space_before_path = UNSET
        else:
            space_before_path = BTPSpace10.from_dict(_space_before_path)

        _space_before_version = d.pop("spaceBeforeVersion", UNSET)
        space_before_version: BTPSpace10 | Unset
        if isinstance(_space_before_version, Unset):
            space_before_version = UNSET
        else:
            space_before_version = BTPSpace10.from_dict(_space_before_version)

        standard_library = d.pop("standardLibrary", UNSET)

        standard_library_common = d.pop("standardLibraryCommon", UNSET)

        valid_legacy_version = d.pop("validLegacyVersion", UNSET)

        _version = d.pop("version", UNSET)
        version: BTPLiteralString259 | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = BTPLiteralString259.from_dict(_version)

        version_and_microversion = d.pop("versionAndMicroversion", UNSET)

        version_potentially_valid = d.pop("versionPotentiallyValid", UNSET)

        btp_module_id_235 = cls(
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
            dbimport_string=dbimport_string,
            element_import=element_import,
            external_document_with_version=external_document_with_version,
            external_document_with_version_and_element_id=external_document_with_version_and_element_id,
            external_import=external_import,
            imported_document_id=imported_document_id,
            imported_element_id=imported_element_id,
            imported_version_id=imported_version_id,
            legacy=legacy,
            legacy_element_name=legacy_element_name,
            legacy_version_number=legacy_version_number,
            microversion=microversion,
            path=path,
            path_potentially_valid=path_potentially_valid,
            path_version=path_version,
            potentially_valid=potentially_valid,
            space_after_path=space_after_path,
            space_after_version=space_after_version,
            space_before_path=space_before_path,
            space_before_version=space_before_version,
            standard_library=standard_library,
            standard_library_common=standard_library_common,
            valid_legacy_version=valid_legacy_version,
            version=version,
            version_and_microversion=version_and_microversion,
            version_potentially_valid=version_potentially_valid,
        )

        btp_module_id_235.additional_properties = d
        return btp_module_id_235

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
