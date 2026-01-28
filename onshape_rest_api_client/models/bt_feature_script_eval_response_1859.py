from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_notice_227 import BTNotice227
    from ..models.btfs_value_1888 import BTFSValue1888


T = TypeVar("T", bound="BTFeatureScriptEvalResponse1859")


@_attrs_define
class BTFeatureScriptEvalResponse1859:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        console (str | Unset):
        library_version (int | Unset): FeatureScript version used in the Part Studio. Do not modify.
        microversion_skew (bool | Unset): On output, `true` indicates a microversion mismatch was encountered.
        notices (list[BTNotice227] | Unset):
        reject_microversion_skew (bool | Unset): If `true`, the call will refuse to make the addition if the current
            microversion for the document does not match the source microversion. If `false`, a best-effort attempt is made
            to re-interpret the feature addition in the context of a newer document microversion.
        result (BTFSValue1888 | Unset):
        serialization_version (str | Unset): Version of the structure serialization rules used to encode the output.
            This enables incompatibility detection during software updates.
        source_microversion (str | Unset): The state from which the result was extracted. Geometry ID interpretation is
            dependent on this document microversion.
    """

    bt_type: str | Unset = UNSET
    console: str | Unset = UNSET
    library_version: int | Unset = UNSET
    microversion_skew: bool | Unset = UNSET
    notices: list[BTNotice227] | Unset = UNSET
    reject_microversion_skew: bool | Unset = UNSET
    result: BTFSValue1888 | Unset = UNSET
    serialization_version: str | Unset = UNSET
    source_microversion: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        console = self.console

        library_version = self.library_version

        microversion_skew = self.microversion_skew

        notices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.notices, Unset):
            notices = []
            for notices_item_data in self.notices:
                notices_item = notices_item_data.to_dict()
                notices.append(notices_item)

        reject_microversion_skew = self.reject_microversion_skew

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        serialization_version = self.serialization_version

        source_microversion = self.source_microversion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if console is not UNSET:
            field_dict["console"] = console
        if library_version is not UNSET:
            field_dict["libraryVersion"] = library_version
        if microversion_skew is not UNSET:
            field_dict["microversionSkew"] = microversion_skew
        if notices is not UNSET:
            field_dict["notices"] = notices
        if reject_microversion_skew is not UNSET:
            field_dict["rejectMicroversionSkew"] = reject_microversion_skew
        if result is not UNSET:
            field_dict["result"] = result
        if serialization_version is not UNSET:
            field_dict["serializationVersion"] = serialization_version
        if source_microversion is not UNSET:
            field_dict["sourceMicroversion"] = source_microversion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_notice_227 import BTNotice227
        from ..models.btfs_value_1888 import BTFSValue1888

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        console = d.pop("console", UNSET)

        library_version = d.pop("libraryVersion", UNSET)

        microversion_skew = d.pop("microversionSkew", UNSET)

        _notices = d.pop("notices", UNSET)
        notices: list[BTNotice227] | Unset = UNSET
        if _notices is not UNSET:
            notices = []
            for notices_item_data in _notices:
                notices_item = BTNotice227.from_dict(notices_item_data)

                notices.append(notices_item)

        reject_microversion_skew = d.pop("rejectMicroversionSkew", UNSET)

        _result = d.pop("result", UNSET)
        result: BTFSValue1888 | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = BTFSValue1888.from_dict(_result)

        serialization_version = d.pop("serializationVersion", UNSET)

        source_microversion = d.pop("sourceMicroversion", UNSET)

        bt_feature_script_eval_response_1859 = cls(
            bt_type=bt_type,
            console=console,
            library_version=library_version,
            microversion_skew=microversion_skew,
            notices=notices,
            reject_microversion_skew=reject_microversion_skew,
            result=result,
            serialization_version=serialization_version,
            source_microversion=source_microversion,
        )

        bt_feature_script_eval_response_1859.additional_properties = d
        return bt_feature_script_eval_response_1859

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
