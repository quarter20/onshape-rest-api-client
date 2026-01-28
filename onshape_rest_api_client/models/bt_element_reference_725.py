from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_document_with_version_and_element_id import BTDocumentWithVersionAndElementId
    from ..models.bt_document_with_version_id import BTDocumentWithVersionId
    from ..models.bt_full_element_id_756 import BTFullElementId756
    from ..models.bt_microversion_id_and_configuration_2338 import BTMicroversionIdAndConfiguration2338


T = TypeVar("T", bound="BTElementReference725")


@_attrs_define
class BTElementReference725:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        configured (bool | Unset):
        document_version_id (str | Unset):
        element_id (str | Unset):
        external_document_with_version (BTDocumentWithVersionId | Unset):
        external_document_with_version_and_element_id (BTDocumentWithVersionAndElementId | Unset):
        external_reference (bool | Unset):
        full_element_id (BTFullElementId756 | Unset):
        microversion_id_and_configuration (BTMicroversionIdAndConfiguration2338 | Unset):
        node_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    configured: bool | Unset = UNSET
    document_version_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    external_document_with_version: BTDocumentWithVersionId | Unset = UNSET
    external_document_with_version_and_element_id: BTDocumentWithVersionAndElementId | Unset = UNSET
    external_reference: bool | Unset = UNSET
    full_element_id: BTFullElementId756 | Unset = UNSET
    microversion_id_and_configuration: BTMicroversionIdAndConfiguration2338 | Unset = UNSET
    node_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        configured = self.configured

        document_version_id = self.document_version_id

        element_id = self.element_id

        external_document_with_version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_document_with_version, Unset):
            external_document_with_version = self.external_document_with_version.to_dict()

        external_document_with_version_and_element_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_document_with_version_and_element_id, Unset):
            external_document_with_version_and_element_id = self.external_document_with_version_and_element_id.to_dict()

        external_reference = self.external_reference

        full_element_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.full_element_id, Unset):
            full_element_id = self.full_element_id.to_dict()

        microversion_id_and_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_id_and_configuration, Unset):
            microversion_id_and_configuration = self.microversion_id_and_configuration.to_dict()

        node_id = self.node_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if configured is not UNSET:
            field_dict["configured"] = configured
        if document_version_id is not UNSET:
            field_dict["documentVersionId"] = document_version_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if external_document_with_version is not UNSET:
            field_dict["externalDocumentWithVersion"] = external_document_with_version
        if external_document_with_version_and_element_id is not UNSET:
            field_dict["externalDocumentWithVersionAndElementId"] = external_document_with_version_and_element_id
        if external_reference is not UNSET:
            field_dict["externalReference"] = external_reference
        if full_element_id is not UNSET:
            field_dict["fullElementId"] = full_element_id
        if microversion_id_and_configuration is not UNSET:
            field_dict["microversionIdAndConfiguration"] = microversion_id_and_configuration
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_document_with_version_and_element_id import BTDocumentWithVersionAndElementId
        from ..models.bt_document_with_version_id import BTDocumentWithVersionId
        from ..models.bt_full_element_id_756 import BTFullElementId756
        from ..models.bt_microversion_id_and_configuration_2338 import BTMicroversionIdAndConfiguration2338

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        configured = d.pop("configured", UNSET)

        document_version_id = d.pop("documentVersionId", UNSET)

        element_id = d.pop("elementId", UNSET)

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

        external_reference = d.pop("externalReference", UNSET)

        _full_element_id = d.pop("fullElementId", UNSET)
        full_element_id: BTFullElementId756 | Unset
        if isinstance(_full_element_id, Unset):
            full_element_id = UNSET
        else:
            full_element_id = BTFullElementId756.from_dict(_full_element_id)

        _microversion_id_and_configuration = d.pop("microversionIdAndConfiguration", UNSET)
        microversion_id_and_configuration: BTMicroversionIdAndConfiguration2338 | Unset
        if isinstance(_microversion_id_and_configuration, Unset):
            microversion_id_and_configuration = UNSET
        else:
            microversion_id_and_configuration = BTMicroversionIdAndConfiguration2338.from_dict(
                _microversion_id_and_configuration
            )

        node_id = d.pop("nodeId", UNSET)

        bt_element_reference_725 = cls(
            bt_type=bt_type,
            configured=configured,
            document_version_id=document_version_id,
            element_id=element_id,
            external_document_with_version=external_document_with_version,
            external_document_with_version_and_element_id=external_document_with_version_and_element_id,
            external_reference=external_reference,
            full_element_id=full_element_id,
            microversion_id_and_configuration=microversion_id_and_configuration,
            node_id=node_id,
        )

        bt_element_reference_725.additional_properties = d
        return bt_element_reference_725

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
