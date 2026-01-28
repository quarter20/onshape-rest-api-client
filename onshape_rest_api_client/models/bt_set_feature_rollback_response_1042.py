from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_microversion_id_366 import BTMicroversionId366


T = TypeVar("T", bound="BTSetFeatureRollbackResponse1042")


@_attrs_define
class BTSetFeatureRollbackResponse1042:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        library_version (int | Unset): FeatureScript version used in the Part Studio. Do not modify.
        microversion_id (BTMicroversionId366 | Unset):
        microversion_skew (bool | Unset): On output, `true` indicates a microversion mismatch was encountered.
        reject_microversion_skew (bool | Unset): If `true`, the call will refuse to make the addition if the current
            microversion for the document does not match the source microversion. If `false`, a best-effort attempt is made
            to re-interpret the feature addition in the context of a newer document microversion.
        rollback_index (int | Unset):
        serialization_version (str | Unset): Version of the structure serialization rules used to encode the output.
            This enables incompatibility detection during software updates.
        source_microversion (str | Unset): The state from which the result was extracted. Geometry ID interpretation is
            dependent on this document microversion.
    """

    bt_type: str | Unset = UNSET
    library_version: int | Unset = UNSET
    microversion_id: BTMicroversionId366 | Unset = UNSET
    microversion_skew: bool | Unset = UNSET
    reject_microversion_skew: bool | Unset = UNSET
    rollback_index: int | Unset = UNSET
    serialization_version: str | Unset = UNSET
    source_microversion: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        library_version = self.library_version

        microversion_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_id, Unset):
            microversion_id = self.microversion_id.to_dict()

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
        if library_version is not UNSET:
            field_dict["libraryVersion"] = library_version
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id
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
        from ..models.bt_microversion_id_366 import BTMicroversionId366

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        library_version = d.pop("libraryVersion", UNSET)

        _microversion_id = d.pop("microversionId", UNSET)
        microversion_id: BTMicroversionId366 | Unset
        if isinstance(_microversion_id, Unset):
            microversion_id = UNSET
        else:
            microversion_id = BTMicroversionId366.from_dict(_microversion_id)

        microversion_skew = d.pop("microversionSkew", UNSET)

        reject_microversion_skew = d.pop("rejectMicroversionSkew", UNSET)

        rollback_index = d.pop("rollbackIndex", UNSET)

        serialization_version = d.pop("serializationVersion", UNSET)

        source_microversion = d.pop("sourceMicroversion", UNSET)

        bt_set_feature_rollback_response_1042 = cls(
            bt_type=bt_type,
            library_version=library_version,
            microversion_id=microversion_id,
            microversion_skew=microversion_skew,
            reject_microversion_skew=reject_microversion_skew,
            rollback_index=rollback_index,
            serialization_version=serialization_version,
            source_microversion=source_microversion,
        )

        bt_set_feature_rollback_response_1042.additional_properties = d
        return bt_set_feature_rollback_response_1042

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
