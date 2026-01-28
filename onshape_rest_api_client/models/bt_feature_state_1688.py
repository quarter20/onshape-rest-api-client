from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_node_status_type import GBTNodeStatusType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTFeatureState1688")


@_attrs_define
class BTFeatureState1688:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        feature_status (GBTNodeStatusType | Unset):
        inactive (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    feature_status: GBTNodeStatusType | Unset = UNSET
    inactive: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        feature_status: str | Unset = UNSET
        if not isinstance(self.feature_status, Unset):
            feature_status = self.feature_status.value

        inactive = self.inactive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if feature_status is not UNSET:
            field_dict["featureStatus"] = feature_status
        if inactive is not UNSET:
            field_dict["inactive"] = inactive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _feature_status = d.pop("featureStatus", UNSET)
        feature_status: GBTNodeStatusType | Unset
        if isinstance(_feature_status, Unset):
            feature_status = UNSET
        else:
            feature_status = GBTNodeStatusType(_feature_status)

        inactive = d.pop("inactive", UNSET)

        bt_feature_state_1688 = cls(
            bt_type=bt_type,
            feature_status=feature_status,
            inactive=inactive,
        )

        bt_feature_state_1688.additional_properties = d
        return bt_feature_state_1688

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
