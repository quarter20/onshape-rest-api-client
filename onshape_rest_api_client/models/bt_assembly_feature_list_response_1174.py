from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_assembly_feature_list_response_1174_feature_states import (
        BTAssemblyFeatureListResponse1174FeatureStates,
    )
    from ..models.btm_assembly_feature_887 import BTMAssemblyFeature887


T = TypeVar("T", bound="BTAssemblyFeatureListResponse1174")


@_attrs_define
class BTAssemblyFeatureListResponse1174:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        library_version (int | Unset): FeatureScript version used in the Part Studio. Do not modify.
        microversion_skew (bool | Unset): On output, `true` indicates a microversion mismatch was encountered.
        reject_microversion_skew (bool | Unset): If `true`, the call will refuse to make the addition if the current
            microversion for the document does not match the source microversion. If `false`, a best-effort attempt is made
            to re-interpret the feature addition in the context of a newer document microversion.
        serialization_version (str | Unset): Version of the structure serialization rules used to encode the output.
            This enables incompatibility detection during software updates.
        source_microversion (str | Unset): The state from which the result was extracted. Geometry ID interpretation is
            dependent on this document microversion.
        feature_states (BTAssemblyFeatureListResponse1174FeatureStates | Unset):
        features (list[BTMAssemblyFeature887] | Unset):
        is_complete (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    library_version: int | Unset = UNSET
    microversion_skew: bool | Unset = UNSET
    reject_microversion_skew: bool | Unset = UNSET
    serialization_version: str | Unset = UNSET
    source_microversion: str | Unset = UNSET
    feature_states: BTAssemblyFeatureListResponse1174FeatureStates | Unset = UNSET
    features: list[BTMAssemblyFeature887] | Unset = UNSET
    is_complete: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        library_version = self.library_version

        microversion_skew = self.microversion_skew

        reject_microversion_skew = self.reject_microversion_skew

        serialization_version = self.serialization_version

        source_microversion = self.source_microversion

        feature_states: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_states, Unset):
            feature_states = self.feature_states.to_dict()

        features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.to_dict()
                features.append(features_item)

        is_complete = self.is_complete

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if library_version is not UNSET:
            field_dict["libraryVersion"] = library_version
        if microversion_skew is not UNSET:
            field_dict["microversionSkew"] = microversion_skew
        if reject_microversion_skew is not UNSET:
            field_dict["rejectMicroversionSkew"] = reject_microversion_skew
        if serialization_version is not UNSET:
            field_dict["serializationVersion"] = serialization_version
        if source_microversion is not UNSET:
            field_dict["sourceMicroversion"] = source_microversion
        if feature_states is not UNSET:
            field_dict["featureStates"] = feature_states
        if features is not UNSET:
            field_dict["features"] = features
        if is_complete is not UNSET:
            field_dict["isComplete"] = is_complete

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_assembly_feature_list_response_1174_feature_states import (
            BTAssemblyFeatureListResponse1174FeatureStates,
        )
        from ..models.btm_assembly_feature_887 import BTMAssemblyFeature887

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        library_version = d.pop("libraryVersion", UNSET)

        microversion_skew = d.pop("microversionSkew", UNSET)

        reject_microversion_skew = d.pop("rejectMicroversionSkew", UNSET)

        serialization_version = d.pop("serializationVersion", UNSET)

        source_microversion = d.pop("sourceMicroversion", UNSET)

        _feature_states = d.pop("featureStates", UNSET)
        feature_states: BTAssemblyFeatureListResponse1174FeatureStates | Unset
        if isinstance(_feature_states, Unset):
            feature_states = UNSET
        else:
            feature_states = BTAssemblyFeatureListResponse1174FeatureStates.from_dict(_feature_states)

        _features = d.pop("features", UNSET)
        features: list[BTMAssemblyFeature887] | Unset = UNSET
        if _features is not UNSET:
            features = []
            for features_item_data in _features:
                features_item = BTMAssemblyFeature887.from_dict(features_item_data)

                features.append(features_item)

        is_complete = d.pop("isComplete", UNSET)

        bt_assembly_feature_list_response_1174 = cls(
            bt_type=bt_type,
            library_version=library_version,
            microversion_skew=microversion_skew,
            reject_microversion_skew=reject_microversion_skew,
            serialization_version=serialization_version,
            source_microversion=source_microversion,
            feature_states=feature_states,
            features=features,
            is_complete=is_complete,
        )

        bt_assembly_feature_list_response_1174.additional_properties = d
        return bt_assembly_feature_list_response_1174

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
