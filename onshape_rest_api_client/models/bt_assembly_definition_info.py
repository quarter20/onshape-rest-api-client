from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_assembly_part_info import BTAssemblyPartInfo
    from ..models.bt_assembly_ps_feature_info import BTAssemblyPsFeatureInfo
    from ..models.bt_root_assembly_info import BTRootAssemblyInfo
    from ..models.bt_sub_assembly_info import BTSubAssemblyInfo


T = TypeVar("T", bound="BTAssemblyDefinitionInfo")


@_attrs_define
class BTAssemblyDefinitionInfo:
    """
    Attributes:
        part_studio_features (list[BTAssemblyPsFeatureInfo] | Unset):
        parts (list[BTAssemblyPartInfo] | Unset):
        root_assembly (BTRootAssemblyInfo | Unset):
        sub_assemblies (list[BTSubAssemblyInfo] | Unset):
    """

    part_studio_features: list[BTAssemblyPsFeatureInfo] | Unset = UNSET
    parts: list[BTAssemblyPartInfo] | Unset = UNSET
    root_assembly: BTRootAssemblyInfo | Unset = UNSET
    sub_assemblies: list[BTSubAssemblyInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        part_studio_features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.part_studio_features, Unset):
            part_studio_features = []
            for part_studio_features_item_data in self.part_studio_features:
                part_studio_features_item = part_studio_features_item_data.to_dict()
                part_studio_features.append(part_studio_features_item)

        parts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parts, Unset):
            parts = []
            for parts_item_data in self.parts:
                parts_item = parts_item_data.to_dict()
                parts.append(parts_item)

        root_assembly: dict[str, Any] | Unset = UNSET
        if not isinstance(self.root_assembly, Unset):
            root_assembly = self.root_assembly.to_dict()

        sub_assemblies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sub_assemblies, Unset):
            sub_assemblies = []
            for sub_assemblies_item_data in self.sub_assemblies:
                sub_assemblies_item = sub_assemblies_item_data.to_dict()
                sub_assemblies.append(sub_assemblies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if part_studio_features is not UNSET:
            field_dict["partStudioFeatures"] = part_studio_features
        if parts is not UNSET:
            field_dict["parts"] = parts
        if root_assembly is not UNSET:
            field_dict["rootAssembly"] = root_assembly
        if sub_assemblies is not UNSET:
            field_dict["subAssemblies"] = sub_assemblies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_assembly_part_info import BTAssemblyPartInfo
        from ..models.bt_assembly_ps_feature_info import BTAssemblyPsFeatureInfo
        from ..models.bt_root_assembly_info import BTRootAssemblyInfo
        from ..models.bt_sub_assembly_info import BTSubAssemblyInfo

        d = dict(src_dict)
        _part_studio_features = d.pop("partStudioFeatures", UNSET)
        part_studio_features: list[BTAssemblyPsFeatureInfo] | Unset = UNSET
        if _part_studio_features is not UNSET:
            part_studio_features = []
            for part_studio_features_item_data in _part_studio_features:
                part_studio_features_item = BTAssemblyPsFeatureInfo.from_dict(part_studio_features_item_data)

                part_studio_features.append(part_studio_features_item)

        _parts = d.pop("parts", UNSET)
        parts: list[BTAssemblyPartInfo] | Unset = UNSET
        if _parts is not UNSET:
            parts = []
            for parts_item_data in _parts:
                parts_item = BTAssemblyPartInfo.from_dict(parts_item_data)

                parts.append(parts_item)

        _root_assembly = d.pop("rootAssembly", UNSET)
        root_assembly: BTRootAssemblyInfo | Unset
        if isinstance(_root_assembly, Unset):
            root_assembly = UNSET
        else:
            root_assembly = BTRootAssemblyInfo.from_dict(_root_assembly)

        _sub_assemblies = d.pop("subAssemblies", UNSET)
        sub_assemblies: list[BTSubAssemblyInfo] | Unset = UNSET
        if _sub_assemblies is not UNSET:
            sub_assemblies = []
            for sub_assemblies_item_data in _sub_assemblies:
                sub_assemblies_item = BTSubAssemblyInfo.from_dict(sub_assemblies_item_data)

                sub_assemblies.append(sub_assemblies_item)

        bt_assembly_definition_info = cls(
            part_studio_features=part_studio_features,
            parts=parts,
            root_assembly=root_assembly,
            sub_assemblies=sub_assemblies,
        )

        bt_assembly_definition_info.additional_properties = d
        return bt_assembly_definition_info

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
