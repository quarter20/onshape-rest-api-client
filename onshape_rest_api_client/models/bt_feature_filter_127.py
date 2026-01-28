from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_feature_filter_exclusion import GBTFeatureFilterExclusion
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTFeatureFilter127")


@_attrs_define
class BTFeatureFilter127:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        exclusion (GBTFeatureFilterExclusion | Unset):
        feature_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    exclusion: GBTFeatureFilterExclusion | Unset = UNSET
    feature_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        exclusion: str | Unset = UNSET
        if not isinstance(self.exclusion, Unset):
            exclusion = self.exclusion.value

        feature_id = self.feature_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if exclusion is not UNSET:
            field_dict["exclusion"] = exclusion
        if feature_id is not UNSET:
            field_dict["featureId"] = feature_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _exclusion = d.pop("exclusion", UNSET)
        exclusion: GBTFeatureFilterExclusion | Unset
        if isinstance(_exclusion, Unset):
            exclusion = UNSET
        else:
            exclusion = GBTFeatureFilterExclusion(_exclusion)

        feature_id = d.pop("featureId", UNSET)

        bt_feature_filter_127 = cls(
            bt_type=bt_type,
            exclusion=exclusion,
            feature_id=feature_id,
        )

        bt_feature_filter_127.additional_properties = d
        return bt_feature_filter_127

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
