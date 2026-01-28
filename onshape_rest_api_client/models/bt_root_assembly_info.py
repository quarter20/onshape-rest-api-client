from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_assembly_feature_info import BTAssemblyFeatureInfo
    from ..models.bt_assembly_instance_info import BTAssemblyInstanceInfo
    from ..models.bt_assembly_occurrence_info import BTAssemblyOccurrenceInfo
    from ..models.bt_assembly_pattern_info import BTAssemblyPatternInfo


T = TypeVar("T", bound="BTRootAssemblyInfo")


@_attrs_define
class BTRootAssemblyInfo:
    """
    Attributes:
        configuration (str | Unset):
        document_id (str | Unset):
        document_microversion (str | Unset):
        document_version (str | Unset):
        element_id (str | Unset):
        features (list[BTAssemblyFeatureInfo] | Unset): List of Assembly features including those are created by
            replicates.
        full_configuration (str | Unset):
        instances (list[BTAssemblyInstanceInfo] | Unset): List of instances including those created by patterns and
            replicates.
        occurrences (list[BTAssemblyOccurrenceInfo] | Unset):
        part_number (str | Unset):
        patterns (list[BTAssemblyPatternInfo] | Unset): List of patterns.
        revision (str | Unset):
    """

    configuration: str | Unset = UNSET
    document_id: str | Unset = UNSET
    document_microversion: str | Unset = UNSET
    document_version: str | Unset = UNSET
    element_id: str | Unset = UNSET
    features: list[BTAssemblyFeatureInfo] | Unset = UNSET
    full_configuration: str | Unset = UNSET
    instances: list[BTAssemblyInstanceInfo] | Unset = UNSET
    occurrences: list[BTAssemblyOccurrenceInfo] | Unset = UNSET
    part_number: str | Unset = UNSET
    patterns: list[BTAssemblyPatternInfo] | Unset = UNSET
    revision: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration

        document_id = self.document_id

        document_microversion = self.document_microversion

        document_version = self.document_version

        element_id = self.element_id

        features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.to_dict()
                features.append(features_item)

        full_configuration = self.full_configuration

        instances: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.instances, Unset):
            instances = []
            for instances_item_data in self.instances:
                instances_item = instances_item_data.to_dict()
                instances.append(instances_item)

        occurrences: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.occurrences, Unset):
            occurrences = []
            for occurrences_item_data in self.occurrences:
                occurrences_item = occurrences_item_data.to_dict()
                occurrences.append(occurrences_item)

        part_number = self.part_number

        patterns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.patterns, Unset):
            patterns = []
            for patterns_item_data in self.patterns:
                patterns_item = patterns_item_data.to_dict()
                patterns.append(patterns_item)

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
        if features is not UNSET:
            field_dict["features"] = features
        if full_configuration is not UNSET:
            field_dict["fullConfiguration"] = full_configuration
        if instances is not UNSET:
            field_dict["instances"] = instances
        if occurrences is not UNSET:
            field_dict["occurrences"] = occurrences
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if patterns is not UNSET:
            field_dict["patterns"] = patterns
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_assembly_feature_info import BTAssemblyFeatureInfo
        from ..models.bt_assembly_instance_info import BTAssemblyInstanceInfo
        from ..models.bt_assembly_occurrence_info import BTAssemblyOccurrenceInfo
        from ..models.bt_assembly_pattern_info import BTAssemblyPatternInfo

        d = dict(src_dict)
        configuration = d.pop("configuration", UNSET)

        document_id = d.pop("documentId", UNSET)

        document_microversion = d.pop("documentMicroversion", UNSET)

        document_version = d.pop("documentVersion", UNSET)

        element_id = d.pop("elementId", UNSET)

        _features = d.pop("features", UNSET)
        features: list[BTAssemblyFeatureInfo] | Unset = UNSET
        if _features is not UNSET:
            features = []
            for features_item_data in _features:
                features_item = BTAssemblyFeatureInfo.from_dict(features_item_data)

                features.append(features_item)

        full_configuration = d.pop("fullConfiguration", UNSET)

        _instances = d.pop("instances", UNSET)
        instances: list[BTAssemblyInstanceInfo] | Unset = UNSET
        if _instances is not UNSET:
            instances = []
            for instances_item_data in _instances:
                instances_item = BTAssemblyInstanceInfo.from_dict(instances_item_data)

                instances.append(instances_item)

        _occurrences = d.pop("occurrences", UNSET)
        occurrences: list[BTAssemblyOccurrenceInfo] | Unset = UNSET
        if _occurrences is not UNSET:
            occurrences = []
            for occurrences_item_data in _occurrences:
                occurrences_item = BTAssemblyOccurrenceInfo.from_dict(occurrences_item_data)

                occurrences.append(occurrences_item)

        part_number = d.pop("partNumber", UNSET)

        _patterns = d.pop("patterns", UNSET)
        patterns: list[BTAssemblyPatternInfo] | Unset = UNSET
        if _patterns is not UNSET:
            patterns = []
            for patterns_item_data in _patterns:
                patterns_item = BTAssemblyPatternInfo.from_dict(patterns_item_data)

                patterns.append(patterns_item)

        revision = d.pop("revision", UNSET)

        bt_root_assembly_info = cls(
            configuration=configuration,
            document_id=document_id,
            document_microversion=document_microversion,
            document_version=document_version,
            element_id=element_id,
            features=features,
            full_configuration=full_configuration,
            instances=instances,
            occurrences=occurrences,
            part_number=part_number,
            patterns=patterns,
            revision=revision,
        )

        bt_root_assembly_info.additional_properties = d
        return bt_root_assembly_info

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
