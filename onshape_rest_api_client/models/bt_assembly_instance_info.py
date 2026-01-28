from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_assembly_instance_status import BTAssemblyInstanceStatus
from ..models.bt_assembly_instance_type import BTAssemblyInstanceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAssemblyInstanceInfo")


@_attrs_define
class BTAssemblyInstanceInfo:
    """List of instances including those created by patterns and replicates.

    Attributes:
        configuration (str | Unset):
        document_id (str | Unset):
        document_microversion (str | Unset):
        document_version (str | Unset):
        element_id (str | Unset):
        feature_id (str | Unset):
        full_configuration (str | Unset):
        id (str | Unset):
        is_standard_content (bool | Unset):
        name (str | Unset):
        part_id (str | Unset):
        part_number (str | Unset):
        revision (str | Unset):
        status (BTAssemblyInstanceStatus | Unset):
        suppressed (bool | Unset):
        type_ (BTAssemblyInstanceType | Unset):
    """

    configuration: str | Unset = UNSET
    document_id: str | Unset = UNSET
    document_microversion: str | Unset = UNSET
    document_version: str | Unset = UNSET
    element_id: str | Unset = UNSET
    feature_id: str | Unset = UNSET
    full_configuration: str | Unset = UNSET
    id: str | Unset = UNSET
    is_standard_content: bool | Unset = UNSET
    name: str | Unset = UNSET
    part_id: str | Unset = UNSET
    part_number: str | Unset = UNSET
    revision: str | Unset = UNSET
    status: BTAssemblyInstanceStatus | Unset = UNSET
    suppressed: bool | Unset = UNSET
    type_: BTAssemblyInstanceType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration

        document_id = self.document_id

        document_microversion = self.document_microversion

        document_version = self.document_version

        element_id = self.element_id

        feature_id = self.feature_id

        full_configuration = self.full_configuration

        id = self.id

        is_standard_content = self.is_standard_content

        name = self.name

        part_id = self.part_id

        part_number = self.part_number

        revision = self.revision

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        suppressed = self.suppressed

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

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
        if full_configuration is not UNSET:
            field_dict["fullConfiguration"] = full_configuration
        if id is not UNSET:
            field_dict["id"] = id
        if is_standard_content is not UNSET:
            field_dict["isStandardContent"] = is_standard_content
        if name is not UNSET:
            field_dict["name"] = name
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if revision is not UNSET:
            field_dict["revision"] = revision
        if status is not UNSET:
            field_dict["status"] = status
        if suppressed is not UNSET:
            field_dict["suppressed"] = suppressed
        if type_ is not UNSET:
            field_dict["type"] = type_

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

        full_configuration = d.pop("fullConfiguration", UNSET)

        id = d.pop("id", UNSET)

        is_standard_content = d.pop("isStandardContent", UNSET)

        name = d.pop("name", UNSET)

        part_id = d.pop("partId", UNSET)

        part_number = d.pop("partNumber", UNSET)

        revision = d.pop("revision", UNSET)

        _status = d.pop("status", UNSET)
        status: BTAssemblyInstanceStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BTAssemblyInstanceStatus(_status)

        suppressed = d.pop("suppressed", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: BTAssemblyInstanceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BTAssemblyInstanceType(_type_)

        bt_assembly_instance_info = cls(
            configuration=configuration,
            document_id=document_id,
            document_microversion=document_microversion,
            document_version=document_version,
            element_id=element_id,
            feature_id=feature_id,
            full_configuration=full_configuration,
            id=id,
            is_standard_content=is_standard_content,
            name=name,
            part_id=part_id,
            part_number=part_number,
            revision=revision,
            status=status,
            suppressed=suppressed,
            type_=type_,
        )

        bt_assembly_instance_info.additional_properties = d
        return bt_assembly_instance_info

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
