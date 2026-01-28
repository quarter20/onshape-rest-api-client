from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTTableCrossHighlightData1753")


@_attrs_define
class BTTableCrossHighlightData1753:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        deterministic_id_list (list[str] | Unset):
        feature_id_list (list[str] | Unset):
    """

    bt_type: str | Unset = UNSET
    deterministic_id_list: list[str] | Unset = UNSET
    feature_id_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        deterministic_id_list: list[str] | Unset = UNSET
        if not isinstance(self.deterministic_id_list, Unset):
            deterministic_id_list = self.deterministic_id_list

        feature_id_list: list[str] | Unset = UNSET
        if not isinstance(self.feature_id_list, Unset):
            feature_id_list = self.feature_id_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if deterministic_id_list is not UNSET:
            field_dict["deterministicIdList"] = deterministic_id_list
        if feature_id_list is not UNSET:
            field_dict["featureIdList"] = feature_id_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        deterministic_id_list = cast(list[str], d.pop("deterministicIdList", UNSET))

        feature_id_list = cast(list[str], d.pop("featureIdList", UNSET))

        bt_table_cross_highlight_data_1753 = cls(
            bt_type=bt_type,
            deterministic_id_list=deterministic_id_list,
            feature_id_list=feature_id_list,
        )

        bt_table_cross_highlight_data_1753.additional_properties = d
        return bt_table_cross_highlight_data_1753

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
