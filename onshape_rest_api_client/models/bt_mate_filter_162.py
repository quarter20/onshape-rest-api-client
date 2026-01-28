from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTMateFilter162")


@_attrs_define
class BTMateFilter162:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        require_mate_query_data (bool | Unset):
        top_level_mate_only (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    require_mate_query_data: bool | Unset = UNSET
    top_level_mate_only: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        require_mate_query_data = self.require_mate_query_data

        top_level_mate_only = self.top_level_mate_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if require_mate_query_data is not UNSET:
            field_dict["requireMateQueryData"] = require_mate_query_data
        if top_level_mate_only is not UNSET:
            field_dict["topLevelMateOnly"] = top_level_mate_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        require_mate_query_data = d.pop("requireMateQueryData", UNSET)

        top_level_mate_only = d.pop("topLevelMateOnly", UNSET)

        bt_mate_filter_162 = cls(
            bt_type=bt_type,
            require_mate_query_data=require_mate_query_data,
            top_level_mate_only=top_level_mate_only,
        )

        bt_mate_filter_162.additional_properties = d
        return bt_mate_filter_162

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
