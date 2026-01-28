from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btm_assembly_feature_887 import BTMAssemblyFeature887
    from ..models.btm_parameter_array_2025 import BTMParameterArray2025


T = TypeVar("T", bound="BTAssemblyMirrorFeatureInterface")


@_attrs_define
class BTAssemblyMirrorFeatureInterface:
    """
    Attributes:
        array_parameter_from_feature (BTMParameterArray2025 | Unset):
        feature (BTMAssemblyFeature887 | Unset):
        node_id (str | Unset):
    """

    array_parameter_from_feature: BTMParameterArray2025 | Unset = UNSET
    feature: BTMAssemblyFeature887 | Unset = UNSET
    node_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        array_parameter_from_feature: dict[str, Any] | Unset = UNSET
        if not isinstance(self.array_parameter_from_feature, Unset):
            array_parameter_from_feature = self.array_parameter_from_feature.to_dict()

        feature: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature, Unset):
            feature = self.feature.to_dict()

        node_id = self.node_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if array_parameter_from_feature is not UNSET:
            field_dict["arrayParameterFromFeature"] = array_parameter_from_feature
        if feature is not UNSET:
            field_dict["feature"] = feature
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btm_assembly_feature_887 import BTMAssemblyFeature887
        from ..models.btm_parameter_array_2025 import BTMParameterArray2025

        d = dict(src_dict)
        _array_parameter_from_feature = d.pop("arrayParameterFromFeature", UNSET)
        array_parameter_from_feature: BTMParameterArray2025 | Unset
        if isinstance(_array_parameter_from_feature, Unset):
            array_parameter_from_feature = UNSET
        else:
            array_parameter_from_feature = BTMParameterArray2025.from_dict(_array_parameter_from_feature)

        _feature = d.pop("feature", UNSET)
        feature: BTMAssemblyFeature887 | Unset
        if isinstance(_feature, Unset):
            feature = UNSET
        else:
            feature = BTMAssemblyFeature887.from_dict(_feature)

        node_id = d.pop("nodeId", UNSET)

        bt_assembly_mirror_feature_interface = cls(
            array_parameter_from_feature=array_parameter_from_feature,
            feature=feature,
            node_id=node_id,
        )

        bt_assembly_mirror_feature_interface.additional_properties = d
        return bt_assembly_mirror_feature_interface

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
