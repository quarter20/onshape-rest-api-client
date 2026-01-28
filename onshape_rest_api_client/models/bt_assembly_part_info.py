from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_assembly_part_body_type import BTAssemblyPartBodyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_assembly_mate_connector_info import BTAssemblyMateConnectorInfo


T = TypeVar("T", bound="BTAssemblyPartInfo")


@_attrs_define
class BTAssemblyPartInfo:
    """
    Attributes:
        body_type (BTAssemblyPartBodyType | Unset):
        configuration (str | Unset):
        document_id (str | Unset):
        document_microversion (str | Unset):
        document_version (str | Unset):
        element_id (str | Unset):
        full_configuration (str | Unset):
        is_standard_content (bool | Unset):
        mate_connectors (list[BTAssemblyMateConnectorInfo] | Unset):
        part_id (str | Unset):
        part_number (str | Unset):
        revision (str | Unset):
    """

    body_type: BTAssemblyPartBodyType | Unset = UNSET
    configuration: str | Unset = UNSET
    document_id: str | Unset = UNSET
    document_microversion: str | Unset = UNSET
    document_version: str | Unset = UNSET
    element_id: str | Unset = UNSET
    full_configuration: str | Unset = UNSET
    is_standard_content: bool | Unset = UNSET
    mate_connectors: list[BTAssemblyMateConnectorInfo] | Unset = UNSET
    part_id: str | Unset = UNSET
    part_number: str | Unset = UNSET
    revision: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body_type: str | Unset = UNSET
        if not isinstance(self.body_type, Unset):
            body_type = self.body_type.value

        configuration = self.configuration

        document_id = self.document_id

        document_microversion = self.document_microversion

        document_version = self.document_version

        element_id = self.element_id

        full_configuration = self.full_configuration

        is_standard_content = self.is_standard_content

        mate_connectors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mate_connectors, Unset):
            mate_connectors = []
            for mate_connectors_item_data in self.mate_connectors:
                mate_connectors_item = mate_connectors_item_data.to_dict()
                mate_connectors.append(mate_connectors_item)

        part_id = self.part_id

        part_number = self.part_number

        revision = self.revision

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body_type is not UNSET:
            field_dict["bodyType"] = body_type
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if document_microversion is not UNSET:
            field_dict["documentMicroversion"] = document_microversion
        if document_version is not UNSET:
            field_dict["documentVersion"] = document_version
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if full_configuration is not UNSET:
            field_dict["fullConfiguration"] = full_configuration
        if is_standard_content is not UNSET:
            field_dict["isStandardContent"] = is_standard_content
        if mate_connectors is not UNSET:
            field_dict["mateConnectors"] = mate_connectors
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_assembly_mate_connector_info import BTAssemblyMateConnectorInfo

        d = dict(src_dict)
        _body_type = d.pop("bodyType", UNSET)
        body_type: BTAssemblyPartBodyType | Unset
        if isinstance(_body_type, Unset):
            body_type = UNSET
        else:
            body_type = BTAssemblyPartBodyType(_body_type)

        configuration = d.pop("configuration", UNSET)

        document_id = d.pop("documentId", UNSET)

        document_microversion = d.pop("documentMicroversion", UNSET)

        document_version = d.pop("documentVersion", UNSET)

        element_id = d.pop("elementId", UNSET)

        full_configuration = d.pop("fullConfiguration", UNSET)

        is_standard_content = d.pop("isStandardContent", UNSET)

        _mate_connectors = d.pop("mateConnectors", UNSET)
        mate_connectors: list[BTAssemblyMateConnectorInfo] | Unset = UNSET
        if _mate_connectors is not UNSET:
            mate_connectors = []
            for mate_connectors_item_data in _mate_connectors:
                mate_connectors_item = BTAssemblyMateConnectorInfo.from_dict(mate_connectors_item_data)

                mate_connectors.append(mate_connectors_item)

        part_id = d.pop("partId", UNSET)

        part_number = d.pop("partNumber", UNSET)

        revision = d.pop("revision", UNSET)

        bt_assembly_part_info = cls(
            body_type=body_type,
            configuration=configuration,
            document_id=document_id,
            document_microversion=document_microversion,
            document_version=document_version,
            element_id=element_id,
            full_configuration=full_configuration,
            is_standard_content=is_standard_content,
            mate_connectors=mate_connectors,
            part_id=part_id,
            part_number=part_number,
            revision=revision,
        )

        bt_assembly_part_info.additional_properties = d
        return bt_assembly_part_info

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
