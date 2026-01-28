from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_locked_sub_assembly_4590 import BTLockedSubAssembly4590
    from ..models.bt_occurrence_74 import BTOccurrence74
    from ..models.bt_occurrence_data_75_feature_data import BTOccurrenceData75FeatureData
    from ..models.btbs_matrix_386 import BTBSMatrix386


T = TypeVar("T", bound="BTOccurrenceData75")


@_attrs_define
class BTOccurrenceData75:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        feature_data (BTOccurrenceData75FeatureData | Unset):
        force_highest_quality_tessellation (bool | Unset):
        hidden (bool | Unset):
        is_fixed (bool | Unset):
        is_hidden (bool | Unset):
        lock_info (BTLockedSubAssembly4590 | Unset):
        node_id (str | Unset):
        occurrence (BTOccurrence74 | Unset):
        transform (BTBSMatrix386 | Unset):
    """

    bt_type: str | Unset = UNSET
    feature_data: BTOccurrenceData75FeatureData | Unset = UNSET
    force_highest_quality_tessellation: bool | Unset = UNSET
    hidden: bool | Unset = UNSET
    is_fixed: bool | Unset = UNSET
    is_hidden: bool | Unset = UNSET
    lock_info: BTLockedSubAssembly4590 | Unset = UNSET
    node_id: str | Unset = UNSET
    occurrence: BTOccurrence74 | Unset = UNSET
    transform: BTBSMatrix386 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        feature_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_data, Unset):
            feature_data = self.feature_data.to_dict()

        force_highest_quality_tessellation = self.force_highest_quality_tessellation

        hidden = self.hidden

        is_fixed = self.is_fixed

        is_hidden = self.is_hidden

        lock_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lock_info, Unset):
            lock_info = self.lock_info.to_dict()

        node_id = self.node_id

        occurrence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.occurrence, Unset):
            occurrence = self.occurrence.to_dict()

        transform: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transform, Unset):
            transform = self.transform.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if feature_data is not UNSET:
            field_dict["featureData"] = feature_data
        if force_highest_quality_tessellation is not UNSET:
            field_dict["forceHighestQualityTessellation"] = force_highest_quality_tessellation
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if is_fixed is not UNSET:
            field_dict["isFixed"] = is_fixed
        if is_hidden is not UNSET:
            field_dict["isHidden"] = is_hidden
        if lock_info is not UNSET:
            field_dict["lockInfo"] = lock_info
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if occurrence is not UNSET:
            field_dict["occurrence"] = occurrence
        if transform is not UNSET:
            field_dict["transform"] = transform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_locked_sub_assembly_4590 import BTLockedSubAssembly4590
        from ..models.bt_occurrence_74 import BTOccurrence74
        from ..models.bt_occurrence_data_75_feature_data import BTOccurrenceData75FeatureData
        from ..models.btbs_matrix_386 import BTBSMatrix386

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _feature_data = d.pop("featureData", UNSET)
        feature_data: BTOccurrenceData75FeatureData | Unset
        if isinstance(_feature_data, Unset):
            feature_data = UNSET
        else:
            feature_data = BTOccurrenceData75FeatureData.from_dict(_feature_data)

        force_highest_quality_tessellation = d.pop("forceHighestQualityTessellation", UNSET)

        hidden = d.pop("hidden", UNSET)

        is_fixed = d.pop("isFixed", UNSET)

        is_hidden = d.pop("isHidden", UNSET)

        _lock_info = d.pop("lockInfo", UNSET)
        lock_info: BTLockedSubAssembly4590 | Unset
        if isinstance(_lock_info, Unset):
            lock_info = UNSET
        else:
            lock_info = BTLockedSubAssembly4590.from_dict(_lock_info)

        node_id = d.pop("nodeId", UNSET)

        _occurrence = d.pop("occurrence", UNSET)
        occurrence: BTOccurrence74 | Unset
        if isinstance(_occurrence, Unset):
            occurrence = UNSET
        else:
            occurrence = BTOccurrence74.from_dict(_occurrence)

        _transform = d.pop("transform", UNSET)
        transform: BTBSMatrix386 | Unset
        if isinstance(_transform, Unset):
            transform = UNSET
        else:
            transform = BTBSMatrix386.from_dict(_transform)

        bt_occurrence_data_75 = cls(
            bt_type=bt_type,
            feature_data=feature_data,
            force_highest_quality_tessellation=force_highest_quality_tessellation,
            hidden=hidden,
            is_fixed=is_fixed,
            is_hidden=is_hidden,
            lock_info=lock_info,
            node_id=node_id,
            occurrence=occurrence,
            transform=transform,
        )

        bt_occurrence_data_75.additional_properties = d
        return bt_occurrence_data_75

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
