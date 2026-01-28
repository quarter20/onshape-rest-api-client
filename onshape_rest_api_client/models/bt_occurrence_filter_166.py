from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTOccurrenceFilter166")


@_attrs_define
class BTOccurrenceFilter166:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        exclude_flattened_parts (bool | Unset):
        exclude_mirrored_or_derive_mirrored_instance (bool | Unset):
        exclude_parametric_part_studio_child_instance (bool | Unset):
        exclude_parametric_part_studio_instance (bool | Unset):
        exclude_pattern_instances (bool | Unset):
        exclude_replicated_instances (bool | Unset):
        exclude_sketch (bool | Unset):
        exclude_standard_content (bool | Unset):
        exclude_studio_inserts (bool | Unset):
        exclude_sub_assemblies (bool | Unset):
        exclude_suppressed (bool | Unset):
        include_assembly_root (bool | Unset):
        include_parametric_instance (bool | Unset):
        include_pattern_occurrence (bool | Unset):
        solid_or_composite_body_only (bool | Unset):
        top_level_only (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    exclude_flattened_parts: bool | Unset = UNSET
    exclude_mirrored_or_derive_mirrored_instance: bool | Unset = UNSET
    exclude_parametric_part_studio_child_instance: bool | Unset = UNSET
    exclude_parametric_part_studio_instance: bool | Unset = UNSET
    exclude_pattern_instances: bool | Unset = UNSET
    exclude_replicated_instances: bool | Unset = UNSET
    exclude_sketch: bool | Unset = UNSET
    exclude_standard_content: bool | Unset = UNSET
    exclude_studio_inserts: bool | Unset = UNSET
    exclude_sub_assemblies: bool | Unset = UNSET
    exclude_suppressed: bool | Unset = UNSET
    include_assembly_root: bool | Unset = UNSET
    include_parametric_instance: bool | Unset = UNSET
    include_pattern_occurrence: bool | Unset = UNSET
    solid_or_composite_body_only: bool | Unset = UNSET
    top_level_only: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        exclude_flattened_parts = self.exclude_flattened_parts

        exclude_mirrored_or_derive_mirrored_instance = self.exclude_mirrored_or_derive_mirrored_instance

        exclude_parametric_part_studio_child_instance = self.exclude_parametric_part_studio_child_instance

        exclude_parametric_part_studio_instance = self.exclude_parametric_part_studio_instance

        exclude_pattern_instances = self.exclude_pattern_instances

        exclude_replicated_instances = self.exclude_replicated_instances

        exclude_sketch = self.exclude_sketch

        exclude_standard_content = self.exclude_standard_content

        exclude_studio_inserts = self.exclude_studio_inserts

        exclude_sub_assemblies = self.exclude_sub_assemblies

        exclude_suppressed = self.exclude_suppressed

        include_assembly_root = self.include_assembly_root

        include_parametric_instance = self.include_parametric_instance

        include_pattern_occurrence = self.include_pattern_occurrence

        solid_or_composite_body_only = self.solid_or_composite_body_only

        top_level_only = self.top_level_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if exclude_flattened_parts is not UNSET:
            field_dict["excludeFlattenedParts"] = exclude_flattened_parts
        if exclude_mirrored_or_derive_mirrored_instance is not UNSET:
            field_dict["excludeMirroredOrDeriveMirroredInstance"] = exclude_mirrored_or_derive_mirrored_instance
        if exclude_parametric_part_studio_child_instance is not UNSET:
            field_dict["excludeParametricPartStudioChildInstance"] = exclude_parametric_part_studio_child_instance
        if exclude_parametric_part_studio_instance is not UNSET:
            field_dict["excludeParametricPartStudioInstance"] = exclude_parametric_part_studio_instance
        if exclude_pattern_instances is not UNSET:
            field_dict["excludePatternInstances"] = exclude_pattern_instances
        if exclude_replicated_instances is not UNSET:
            field_dict["excludeReplicatedInstances"] = exclude_replicated_instances
        if exclude_sketch is not UNSET:
            field_dict["excludeSketch"] = exclude_sketch
        if exclude_standard_content is not UNSET:
            field_dict["excludeStandardContent"] = exclude_standard_content
        if exclude_studio_inserts is not UNSET:
            field_dict["excludeStudioInserts"] = exclude_studio_inserts
        if exclude_sub_assemblies is not UNSET:
            field_dict["excludeSubAssemblies"] = exclude_sub_assemblies
        if exclude_suppressed is not UNSET:
            field_dict["excludeSuppressed"] = exclude_suppressed
        if include_assembly_root is not UNSET:
            field_dict["includeAssemblyRoot"] = include_assembly_root
        if include_parametric_instance is not UNSET:
            field_dict["includeParametricInstance"] = include_parametric_instance
        if include_pattern_occurrence is not UNSET:
            field_dict["includePatternOccurrence"] = include_pattern_occurrence
        if solid_or_composite_body_only is not UNSET:
            field_dict["solidOrCompositeBodyOnly"] = solid_or_composite_body_only
        if top_level_only is not UNSET:
            field_dict["topLevelOnly"] = top_level_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        exclude_flattened_parts = d.pop("excludeFlattenedParts", UNSET)

        exclude_mirrored_or_derive_mirrored_instance = d.pop("excludeMirroredOrDeriveMirroredInstance", UNSET)

        exclude_parametric_part_studio_child_instance = d.pop("excludeParametricPartStudioChildInstance", UNSET)

        exclude_parametric_part_studio_instance = d.pop("excludeParametricPartStudioInstance", UNSET)

        exclude_pattern_instances = d.pop("excludePatternInstances", UNSET)

        exclude_replicated_instances = d.pop("excludeReplicatedInstances", UNSET)

        exclude_sketch = d.pop("excludeSketch", UNSET)

        exclude_standard_content = d.pop("excludeStandardContent", UNSET)

        exclude_studio_inserts = d.pop("excludeStudioInserts", UNSET)

        exclude_sub_assemblies = d.pop("excludeSubAssemblies", UNSET)

        exclude_suppressed = d.pop("excludeSuppressed", UNSET)

        include_assembly_root = d.pop("includeAssemblyRoot", UNSET)

        include_parametric_instance = d.pop("includeParametricInstance", UNSET)

        include_pattern_occurrence = d.pop("includePatternOccurrence", UNSET)

        solid_or_composite_body_only = d.pop("solidOrCompositeBodyOnly", UNSET)

        top_level_only = d.pop("topLevelOnly", UNSET)

        bt_occurrence_filter_166 = cls(
            bt_type=bt_type,
            exclude_flattened_parts=exclude_flattened_parts,
            exclude_mirrored_or_derive_mirrored_instance=exclude_mirrored_or_derive_mirrored_instance,
            exclude_parametric_part_studio_child_instance=exclude_parametric_part_studio_child_instance,
            exclude_parametric_part_studio_instance=exclude_parametric_part_studio_instance,
            exclude_pattern_instances=exclude_pattern_instances,
            exclude_replicated_instances=exclude_replicated_instances,
            exclude_sketch=exclude_sketch,
            exclude_standard_content=exclude_standard_content,
            exclude_studio_inserts=exclude_studio_inserts,
            exclude_sub_assemblies=exclude_sub_assemblies,
            exclude_suppressed=exclude_suppressed,
            include_assembly_root=include_assembly_root,
            include_parametric_instance=include_parametric_instance,
            include_pattern_occurrence=include_pattern_occurrence,
            solid_or_composite_body_only=solid_or_composite_body_only,
            top_level_only=top_level_only,
        )

        bt_occurrence_filter_166.additional_properties = d
        return bt_occurrence_filter_166

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
