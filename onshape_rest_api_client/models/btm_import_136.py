from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTMImport136")


@_attrs_define
class BTMImport136:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Element microversion that is being imported.
        node_id (str | Unset):
        element_import (bool | Unset):
        imported_external_document_id (str | Unset):
        namespace (str | Unset):
        path (str | Unset):
        version (str | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    node_id: str | Unset = UNSET
    element_import: bool | Unset = UNSET
    imported_external_document_id: str | Unset = UNSET
    namespace: str | Unset = UNSET
    path: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        node_id = self.node_id

        element_import = self.element_import

        imported_external_document_id = self.imported_external_document_id

        namespace = self.namespace

        path = self.path

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if element_import is not UNSET:
            field_dict["elementImport"] = element_import
        if imported_external_document_id is not UNSET:
            field_dict["importedExternalDocumentId"] = imported_external_document_id
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if path is not UNSET:
            field_dict["path"] = path
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        node_id = d.pop("nodeId", UNSET)

        element_import = d.pop("elementImport", UNSET)

        imported_external_document_id = d.pop("importedExternalDocumentId", UNSET)

        namespace = d.pop("namespace", UNSET)

        path = d.pop("path", UNSET)

        version = d.pop("version", UNSET)

        btm_import_136 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            node_id=node_id,
            element_import=element_import,
            imported_external_document_id=imported_external_document_id,
            namespace=namespace,
            path=path,
            version=version,
        )

        btm_import_136.additional_properties = d
        return btm_import_136

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
