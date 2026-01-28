from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbtp_type import GBTPType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTFSValueOther1124")


@_attrs_define
class BTFSValueOther1124:
    """
    Attributes:
        bt_type (str): Type of JSON object.
        type_tag (str | Unset):
        type_ (GBTPType | Unset):
    """

    bt_type: str
    type_tag: str | Unset = UNSET
    type_: GBTPType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        type_tag = self.type_tag

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "btType": bt_type,
            }
        )
        if type_tag is not UNSET:
            field_dict["typeTag"] = type_tag
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType")

        type_tag = d.pop("typeTag", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: GBTPType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GBTPType(_type_)

        btfs_value_other_1124 = cls(
            bt_type=bt_type,
            type_tag=type_tag,
            type_=type_,
        )

        btfs_value_other_1124.additional_properties = d
        return btfs_value_other_1124

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
