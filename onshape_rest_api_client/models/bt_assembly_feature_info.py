from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_assembly_feature_data_info import BTAssemblyFeatureDataInfo


T = TypeVar("T", bound="BTAssemblyFeatureInfo")


@_attrs_define
class BTAssemblyFeatureInfo:
    """List of Assembly features including those are created by replicates.

    Attributes:
        feature_data (BTAssemblyFeatureDataInfo | Unset):
        feature_type (str | Unset):
        id (str | Unset):
        suppressed (bool | Unset):
    """

    feature_data: BTAssemblyFeatureDataInfo | Unset = UNSET
    feature_type: str | Unset = UNSET
    id: str | Unset = UNSET
    suppressed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_data, Unset):
            feature_data = self.feature_data.to_dict()

        feature_type = self.feature_type

        id = self.id

        suppressed = self.suppressed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feature_data is not UNSET:
            field_dict["featureData"] = feature_data
        if feature_type is not UNSET:
            field_dict["featureType"] = feature_type
        if id is not UNSET:
            field_dict["id"] = id
        if suppressed is not UNSET:
            field_dict["suppressed"] = suppressed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_assembly_feature_data_info import BTAssemblyFeatureDataInfo

        d = dict(src_dict)
        _feature_data = d.pop("featureData", UNSET)
        feature_data: BTAssemblyFeatureDataInfo | Unset
        if isinstance(_feature_data, Unset):
            feature_data = UNSET
        else:
            feature_data = BTAssemblyFeatureDataInfo.from_dict(_feature_data)

        feature_type = d.pop("featureType", UNSET)

        id = d.pop("id", UNSET)

        suppressed = d.pop("suppressed", UNSET)

        bt_assembly_feature_info = cls(
            feature_data=feature_data,
            feature_type=feature_type,
            id=id,
            suppressed=suppressed,
        )

        bt_assembly_feature_info.additional_properties = d
        return bt_assembly_feature_info

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
