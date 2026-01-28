from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTFeatureStudioContents2239")


@_attrs_define
class BTFeatureStudioContents2239:
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
        contents (str | Unset):
    """

    bt_type: str | Unset = UNSET
    library_version: int | Unset = UNSET
    microversion_skew: bool | Unset = UNSET
    reject_microversion_skew: bool | Unset = UNSET
    serialization_version: str | Unset = UNSET
    source_microversion: str | Unset = UNSET
    contents: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        library_version = self.library_version

        microversion_skew = self.microversion_skew

        reject_microversion_skew = self.reject_microversion_skew

        serialization_version = self.serialization_version

        source_microversion = self.source_microversion

        contents = self.contents

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
        if contents is not UNSET:
            field_dict["contents"] = contents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        library_version = d.pop("libraryVersion", UNSET)

        microversion_skew = d.pop("microversionSkew", UNSET)

        reject_microversion_skew = d.pop("rejectMicroversionSkew", UNSET)

        serialization_version = d.pop("serializationVersion", UNSET)

        source_microversion = d.pop("sourceMicroversion", UNSET)

        contents = d.pop("contents", UNSET)

        bt_feature_studio_contents_2239 = cls(
            bt_type=bt_type,
            library_version=library_version,
            microversion_skew=microversion_skew,
            reject_microversion_skew=reject_microversion_skew,
            serialization_version=serialization_version,
            source_microversion=source_microversion,
            contents=contents,
        )

        bt_feature_studio_contents_2239.additional_properties = d
        return bt_feature_studio_contents_2239

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
