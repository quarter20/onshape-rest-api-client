from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_insertable_type import GBTInsertableType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAssemblyInstanceDefinitionParams")


@_attrs_define
class BTAssemblyInstanceDefinitionParams:
    """
    Attributes:
        document_id (str):
        configuration (str | Unset):
        element_id (str | Unset):
        feature_id (str | Unset):
        include_part_types (list[GBTInsertableType] | Unset):
        is_assembly (bool | Unset):
        is_hidden (bool | Unset):
        is_suppressed (bool | Unset):
        is_whole_part_studio (bool | Unset):
        microversion_id (str | Unset):
        part_id (str | Unset):
        part_number (str | Unset):
        revision (str | Unset):
        version_id (str | Unset):
    """

    document_id: str
    configuration: str | Unset = UNSET
    element_id: str | Unset = UNSET
    feature_id: str | Unset = UNSET
    include_part_types: list[GBTInsertableType] | Unset = UNSET
    is_assembly: bool | Unset = UNSET
    is_hidden: bool | Unset = UNSET
    is_suppressed: bool | Unset = UNSET
    is_whole_part_studio: bool | Unset = UNSET
    microversion_id: str | Unset = UNSET
    part_id: str | Unset = UNSET
    part_number: str | Unset = UNSET
    revision: str | Unset = UNSET
    version_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        configuration = self.configuration

        element_id = self.element_id

        feature_id = self.feature_id

        include_part_types: list[str] | Unset = UNSET
        if not isinstance(self.include_part_types, Unset):
            include_part_types = []
            for include_part_types_item_data in self.include_part_types:
                include_part_types_item = include_part_types_item_data.value
                include_part_types.append(include_part_types_item)

        is_assembly = self.is_assembly

        is_hidden = self.is_hidden

        is_suppressed = self.is_suppressed

        is_whole_part_studio = self.is_whole_part_studio

        microversion_id = self.microversion_id

        part_id = self.part_id

        part_number = self.part_number

        revision = self.revision

        version_id = self.version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentId": document_id,
            }
        )
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if feature_id is not UNSET:
            field_dict["featureId"] = feature_id
        if include_part_types is not UNSET:
            field_dict["includePartTypes"] = include_part_types
        if is_assembly is not UNSET:
            field_dict["isAssembly"] = is_assembly
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden
        if is_suppressed is not UNSET:
            field_dict["isSuppressed"] = is_suppressed
        if is_whole_part_studio is not UNSET:
            field_dict["isWholePartStudio"] = is_whole_part_studio
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if revision is not UNSET:
            field_dict["revision"] = revision
        if version_id is not UNSET:
            field_dict["versionId"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_id = d.pop("documentId")

        configuration = d.pop("configuration", UNSET)

        element_id = d.pop("elementId", UNSET)

        feature_id = d.pop("featureId", UNSET)

        _include_part_types = d.pop("includePartTypes", UNSET)
        include_part_types: list[GBTInsertableType] | Unset = UNSET
        if _include_part_types is not UNSET:
            include_part_types = []
            for include_part_types_item_data in _include_part_types:
                include_part_types_item = GBTInsertableType(include_part_types_item_data)

                include_part_types.append(include_part_types_item)

        is_assembly = d.pop("isAssembly", UNSET)

        is_hidden = d.pop("isHidden", UNSET)

        is_suppressed = d.pop("isSuppressed", UNSET)

        is_whole_part_studio = d.pop("isWholePartStudio", UNSET)

        microversion_id = d.pop("microversionId", UNSET)

        part_id = d.pop("partId", UNSET)

        part_number = d.pop("partNumber", UNSET)

        revision = d.pop("revision", UNSET)

        version_id = d.pop("versionId", UNSET)

        bt_assembly_instance_definition_params = cls(
            document_id=document_id,
            configuration=configuration,
            element_id=element_id,
            feature_id=feature_id,
            include_part_types=include_part_types,
            is_assembly=is_assembly,
            is_hidden=is_hidden,
            is_suppressed=is_suppressed,
            is_whole_part_studio=is_whole_part_studio,
            microversion_id=microversion_id,
            part_id=part_id,
            part_number=part_number,
            revision=revision,
            version_id=version_id,
        )

        bt_assembly_instance_definition_params.additional_properties = d
        return bt_assembly_instance_definition_params

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
