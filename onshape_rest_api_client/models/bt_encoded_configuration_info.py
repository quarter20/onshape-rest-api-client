from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTEncodedConfigurationInfo")


@_attrs_define
class BTEncodedConfigurationInfo:
    """
    Attributes:
        encoded_id (str | Unset):
        query_param (str | Unset):
    """

    encoded_id: str | Unset = UNSET
    query_param: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        encoded_id = self.encoded_id

        query_param = self.query_param

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encoded_id is not UNSET:
            field_dict["encodedId"] = encoded_id
        if query_param is not UNSET:
            field_dict["queryParam"] = query_param

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        encoded_id = d.pop("encodedId", UNSET)

        query_param = d.pop("queryParam", UNSET)

        bt_encoded_configuration_info = cls(
            encoded_id=encoded_id,
            query_param=query_param,
        )

        bt_encoded_configuration_info.additional_properties = d
        return bt_encoded_configuration_info

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
