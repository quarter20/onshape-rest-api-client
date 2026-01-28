from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_body_type import GBTBodyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTBodyTypeFilter112")


@_attrs_define
class BTBodyTypeFilter112:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        body_type (GBTBodyType | Unset):
    """

    bt_type: str | Unset = UNSET
    body_type: GBTBodyType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        body_type: str | Unset = UNSET
        if not isinstance(self.body_type, Unset):
            body_type = self.body_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if body_type is not UNSET:
            field_dict["bodyType"] = body_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _body_type = d.pop("bodyType", UNSET)
        body_type: GBTBodyType | Unset
        if isinstance(_body_type, Unset):
            body_type = UNSET
        else:
            body_type = GBTBodyType(_body_type)

        bt_body_type_filter_112 = cls(
            bt_type=bt_type,
            body_type=body_type,
        )

        bt_body_type_filter_112.additional_properties = d
        return bt_body_type_filter_112

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
