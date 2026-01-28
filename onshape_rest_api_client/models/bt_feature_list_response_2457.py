from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_feature_list_response_2457_feature_states import BTFeatureListResponse2457FeatureStates
    from ..models.btm_feature_134 import BTMFeature134
    from ..models.btm_import_136 import BTMImport136


T = TypeVar("T", bound="BTFeatureListResponse2457")


@_attrs_define
class BTFeatureListResponse2457:
    """List of features instantiated within the Part Studio.

    Attributes:
        bt_type (str | Unset): Type of JSON object.
        default_features (list[BTMFeature134] | Unset): List of Onshape-defined features instantiated within the Part
            Studio.
        feature_states (BTFeatureListResponse2457FeatureStates | Unset): State of each feature, indicating if the
            feature is valid. Incorrectly defined features will still appear in the Feature list.
        features (list[BTMFeature134] | Unset): List of user-defined features instantiated within the Part Studio.
        imports (list[BTMImport136] | Unset): Internal only. Do not modify.
        is_complete (bool | Unset): `true` if the features represent the entire part studio or `false` for a filtered
            subset.
        library_version (int | Unset): FeatureScript version used in the Part Studio. Do not modify.
        microversion_skew (bool | Unset): On output, `true` indicates a microversion mismatch was encountered.
        reject_microversion_skew (bool | Unset): If `true`, the call will refuse to make the addition if the current
            microversion for the document does not match the source microversion. If `false`, a best-effort attempt is made
            to re-interpret the feature addition in the context of a newer document microversion.
        rollback_index (int | Unset): Index of the rollback bar location. `-1` indicates the bar is at the end of the
            Feature List.
        serialization_version (str | Unset): Version of the structure serialization rules used to encode the output.
            This enables incompatibility detection during software updates.
        source_microversion (str | Unset): The document microversion from which the result was extracted. Part, face,
            edge, and vertex IDs are only valid for the same microversion.
    """

    bt_type: str | Unset = UNSET
    default_features: list[BTMFeature134] | Unset = UNSET
    feature_states: BTFeatureListResponse2457FeatureStates | Unset = UNSET
    features: list[BTMFeature134] | Unset = UNSET
    imports: list[BTMImport136] | Unset = UNSET
    is_complete: bool | Unset = UNSET
    library_version: int | Unset = UNSET
    microversion_skew: bool | Unset = UNSET
    reject_microversion_skew: bool | Unset = UNSET
    rollback_index: int | Unset = UNSET
    serialization_version: str | Unset = UNSET
    source_microversion: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        default_features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.default_features, Unset):
            default_features = []
            for default_features_item_data in self.default_features:
                default_features_item = default_features_item_data.to_dict()
                default_features.append(default_features_item)

        feature_states: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_states, Unset):
            feature_states = self.feature_states.to_dict()

        features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.to_dict()
                features.append(features_item)

        imports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.imports, Unset):
            imports = []
            for imports_item_data in self.imports:
                imports_item = imports_item_data.to_dict()
                imports.append(imports_item)

        is_complete = self.is_complete

        library_version = self.library_version

        microversion_skew = self.microversion_skew

        reject_microversion_skew = self.reject_microversion_skew

        rollback_index = self.rollback_index

        serialization_version = self.serialization_version

        source_microversion = self.source_microversion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if default_features is not UNSET:
            field_dict["defaultFeatures"] = default_features
        if feature_states is not UNSET:
            field_dict["featureStates"] = feature_states
        if features is not UNSET:
            field_dict["features"] = features
        if imports is not UNSET:
            field_dict["imports"] = imports
        if is_complete is not UNSET:
            field_dict["isComplete"] = is_complete
        if library_version is not UNSET:
            field_dict["libraryVersion"] = library_version
        if microversion_skew is not UNSET:
            field_dict["microversionSkew"] = microversion_skew
        if reject_microversion_skew is not UNSET:
            field_dict["rejectMicroversionSkew"] = reject_microversion_skew
        if rollback_index is not UNSET:
            field_dict["rollbackIndex"] = rollback_index
        if serialization_version is not UNSET:
            field_dict["serializationVersion"] = serialization_version
        if source_microversion is not UNSET:
            field_dict["sourceMicroversion"] = source_microversion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_feature_list_response_2457_feature_states import BTFeatureListResponse2457FeatureStates
        from ..models.btm_feature_134 import BTMFeature134
        from ..models.btm_import_136 import BTMImport136

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _default_features = d.pop("defaultFeatures", UNSET)
        default_features: list[BTMFeature134] | Unset = UNSET
        if _default_features is not UNSET:
            default_features = []
            for default_features_item_data in _default_features:
                default_features_item = BTMFeature134.from_dict(default_features_item_data)

                default_features.append(default_features_item)

        _feature_states = d.pop("featureStates", UNSET)
        feature_states: BTFeatureListResponse2457FeatureStates | Unset
        if isinstance(_feature_states, Unset):
            feature_states = UNSET
        else:
            feature_states = BTFeatureListResponse2457FeatureStates.from_dict(_feature_states)

        _features = d.pop("features", UNSET)
        features: list[BTMFeature134] | Unset = UNSET
        if _features is not UNSET:
            features = []
            for features_item_data in _features:
                features_item = BTMFeature134.from_dict(features_item_data)

                features.append(features_item)

        _imports = d.pop("imports", UNSET)
        imports: list[BTMImport136] | Unset = UNSET
        if _imports is not UNSET:
            imports = []
            for imports_item_data in _imports:
                imports_item = BTMImport136.from_dict(imports_item_data)

                imports.append(imports_item)

        is_complete = d.pop("isComplete", UNSET)

        library_version = d.pop("libraryVersion", UNSET)

        microversion_skew = d.pop("microversionSkew", UNSET)

        reject_microversion_skew = d.pop("rejectMicroversionSkew", UNSET)

        rollback_index = d.pop("rollbackIndex", UNSET)

        serialization_version = d.pop("serializationVersion", UNSET)

        source_microversion = d.pop("sourceMicroversion", UNSET)

        bt_feature_list_response_2457 = cls(
            bt_type=bt_type,
            default_features=default_features,
            feature_states=feature_states,
            features=features,
            imports=imports,
            is_complete=is_complete,
            library_version=library_version,
            microversion_skew=microversion_skew,
            reject_microversion_skew=reject_microversion_skew,
            rollback_index=rollback_index,
            serialization_version=serialization_version,
            source_microversion=source_microversion,
        )

        bt_feature_list_response_2457.additional_properties = d
        return bt_feature_list_response_2457

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
