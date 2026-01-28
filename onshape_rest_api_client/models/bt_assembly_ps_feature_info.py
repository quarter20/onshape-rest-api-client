from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAssemblyPsFeatureInfo")


@_attrs_define
class BTAssemblyPsFeatureInfo:
    """
    Attributes:
        configuration (str | Unset):
        document_id (str | Unset):
        document_microversion (str | Unset):
        document_version (str | Unset):
        element_id (str | Unset):
        feature_id (str | Unset):
        feature_type (str | Unset):
        full_configuration (str | Unset):
        part_number (str | Unset):
        revision (str | Unset):
    """

    configuration: str | Unset = UNSET
    document_id: str | Unset = UNSET
    document_microversion: str | Unset = UNSET
    document_version: str | Unset = UNSET
    element_id: str | Unset = UNSET
    feature_id: str | Unset = UNSET
    feature_type: str | Unset = UNSET
    full_configuration: str | Unset = UNSET
    part_number: str | Unset = UNSET
    revision: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration

        document_id = self.document_id

        document_microversion = self.document_microversion

        document_version = self.document_version

        element_id = self.element_id

        feature_id = self.feature_id

        feature_type = self.feature_type

        full_configuration = self.full_configuration

        part_number = self.part_number

        revision = self.revision

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if feature_id is not UNSET:
            field_dict["featureId"] = feature_id
        if feature_type is not UNSET:
            field_dict["featureType"] = feature_type
        if full_configuration is not UNSET:
            field_dict["fullConfiguration"] = full_configuration
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        configuration = d.pop("configuration", UNSET)

        document_id = d.pop("documentId", UNSET)

        document_microversion = d.pop("documentMicroversion", UNSET)

        document_version = d.pop("documentVersion", UNSET)

        element_id = d.pop("elementId", UNSET)

        feature_id = d.pop("featureId", UNSET)

        feature_type = d.pop("featureType", UNSET)

        full_configuration = d.pop("fullConfiguration", UNSET)

        part_number = d.pop("partNumber", UNSET)

        revision = d.pop("revision", UNSET)

        bt_assembly_ps_feature_info = cls(
            configuration=configuration,
            document_id=document_id,
            document_microversion=document_microversion,
            document_version=document_version,
            element_id=element_id,
            feature_id=feature_id,
            feature_type=feature_type,
            full_configuration=full_configuration,
            part_number=part_number,
            revision=revision,
        )

        bt_assembly_ps_feature_info.additional_properties = d
        return bt_assembly_ps_feature_info

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
