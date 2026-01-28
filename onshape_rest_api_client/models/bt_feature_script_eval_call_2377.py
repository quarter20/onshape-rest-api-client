from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_feature_script_eval_call_2377_queries import BTFeatureScriptEvalCall2377Queries


T = TypeVar("T", bound="BTFeatureScriptEvalCall2377")


@_attrs_define
class BTFeatureScriptEvalCall2377:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        library_version (int | Unset): FeatureScript version used in the Part Studio. Do not modify.
        microversion_skew (bool | Unset): On output, `true` indicates a microversion mismatch was encountered.
        queries (BTFeatureScriptEvalCall2377Queries | Unset):
        reject_microversion_skew (bool | Unset): If `true`, the call will refuse to make the addition if the current
            microversion for the document does not match the source microversion. If `false`, a best-effort attempt is made
            to re-interpret the feature addition in the context of a newer document microversion.
        script (str | Unset):
        serialization_version (str | Unset): Version of the structure serialization rules used to encode the output.
            This enables incompatibility detection during software updates.
        source_microversion (str | Unset): The state from which the result was extracted. Geometry ID interpretation is
            dependent on this document microversion.
    """

    bt_type: str | Unset = UNSET
    library_version: int | Unset = UNSET
    microversion_skew: bool | Unset = UNSET
    queries: BTFeatureScriptEvalCall2377Queries | Unset = UNSET
    reject_microversion_skew: bool | Unset = UNSET
    script: str | Unset = UNSET
    serialization_version: str | Unset = UNSET
    source_microversion: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        library_version = self.library_version

        microversion_skew = self.microversion_skew

        queries: dict[str, Any] | Unset = UNSET
        if not isinstance(self.queries, Unset):
            queries = self.queries.to_dict()

        reject_microversion_skew = self.reject_microversion_skew

        script = self.script

        serialization_version = self.serialization_version

        source_microversion = self.source_microversion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if library_version is not UNSET:
            field_dict["libraryVersion"] = library_version
        if microversion_skew is not UNSET:
            field_dict["microversionSkew"] = microversion_skew
        if queries is not UNSET:
            field_dict["queries"] = queries
        if reject_microversion_skew is not UNSET:
            field_dict["rejectMicroversionSkew"] = reject_microversion_skew
        if script is not UNSET:
            field_dict["script"] = script
        if serialization_version is not UNSET:
            field_dict["serializationVersion"] = serialization_version
        if source_microversion is not UNSET:
            field_dict["sourceMicroversion"] = source_microversion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_feature_script_eval_call_2377_queries import BTFeatureScriptEvalCall2377Queries

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        library_version = d.pop("libraryVersion", UNSET)

        microversion_skew = d.pop("microversionSkew", UNSET)

        _queries = d.pop("queries", UNSET)
        queries: BTFeatureScriptEvalCall2377Queries | Unset
        if isinstance(_queries, Unset):
            queries = UNSET
        else:
            queries = BTFeatureScriptEvalCall2377Queries.from_dict(_queries)

        reject_microversion_skew = d.pop("rejectMicroversionSkew", UNSET)

        script = d.pop("script", UNSET)

        serialization_version = d.pop("serializationVersion", UNSET)

        source_microversion = d.pop("sourceMicroversion", UNSET)

        bt_feature_script_eval_call_2377 = cls(
            bt_type=bt_type,
            library_version=library_version,
            microversion_skew=microversion_skew,
            queries=queries,
            reject_microversion_skew=reject_microversion_skew,
            script=script,
            serialization_version=serialization_version,
            source_microversion=source_microversion,
        )

        bt_feature_script_eval_call_2377.additional_properties = d
        return bt_feature_script_eval_call_2377

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
