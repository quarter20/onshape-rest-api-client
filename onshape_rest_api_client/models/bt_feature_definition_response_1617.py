from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_feature_state_1688 import BTFeatureState1688
    from ..models.btm_feature_134 import BTMFeature134


T = TypeVar("T", bound="BTFeatureDefinitionResponse1617")


@_attrs_define
class BTFeatureDefinitionResponse1617:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        feature (BTMFeature134 | Unset):
        feature_state (BTFeatureState1688 | Unset):
        library_version (int | Unset): FeatureScript version used in the Part Studio. Do not modify.
        microversion_skew (bool | Unset): On output, `true` indicates a microversion mismatch was encountered.
        reject_microversion_skew (bool | Unset): If `true`, the call will refuse to make the addition if the current
            microversion for the document does not match the source microversion. If `false`, a best-effort attempt is made
            to re-interpret the feature addition in the context of a newer document microversion.
        serialization_version (str | Unset): Version of the structure serialization rules used to encode the output.
            This enables incompatibility detection during software updates.
        source_microversion (str | Unset): The state from which the result was extracted. Geometry ID interpretation is
            dependent on this document microversion.
    """

    bt_type: str | Unset = UNSET
    feature: BTMFeature134 | Unset = UNSET
    feature_state: BTFeatureState1688 | Unset = UNSET
    library_version: int | Unset = UNSET
    microversion_skew: bool | Unset = UNSET
    reject_microversion_skew: bool | Unset = UNSET
    serialization_version: str | Unset = UNSET
    source_microversion: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        feature: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature, Unset):
            feature = self.feature.to_dict()

        feature_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_state, Unset):
            feature_state = self.feature_state.to_dict()

        library_version = self.library_version

        microversion_skew = self.microversion_skew

        reject_microversion_skew = self.reject_microversion_skew

        serialization_version = self.serialization_version

        source_microversion = self.source_microversion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if feature is not UNSET:
            field_dict["feature"] = feature
        if feature_state is not UNSET:
            field_dict["featureState"] = feature_state
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_feature_state_1688 import BTFeatureState1688
        from ..models.btm_feature_134 import BTMFeature134

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _feature = d.pop("feature", UNSET)
        feature: BTMFeature134 | Unset
        if isinstance(_feature, Unset):
            feature = UNSET
        else:
            feature = BTMFeature134.from_dict(_feature)

        _feature_state = d.pop("featureState", UNSET)
        feature_state: BTFeatureState1688 | Unset
        if isinstance(_feature_state, Unset):
            feature_state = UNSET
        else:
            feature_state = BTFeatureState1688.from_dict(_feature_state)

        library_version = d.pop("libraryVersion", UNSET)

        microversion_skew = d.pop("microversionSkew", UNSET)

        reject_microversion_skew = d.pop("rejectMicroversionSkew", UNSET)

        serialization_version = d.pop("serializationVersion", UNSET)

        source_microversion = d.pop("sourceMicroversion", UNSET)

        bt_feature_definition_response_1617 = cls(
            bt_type=bt_type,
            feature=feature,
            feature_state=feature_state,
            library_version=library_version,
            microversion_skew=microversion_skew,
            reject_microversion_skew=reject_microversion_skew,
            serialization_version=serialization_version,
            source_microversion=source_microversion,
        )

        bt_feature_definition_response_1617.additional_properties = d
        return bt_feature_definition_response_1617

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
