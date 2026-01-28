from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTExportTessellatedBody3398")


@_attrs_define
class BTExportTessellatedBody3398:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        constituents (list[str] | Unset):
        id (str | Unset):
        name (str | Unset):
    """

    bt_type: str | Unset = UNSET
    constituents: list[str] | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        constituents: list[str] | Unset = UNSET
        if not isinstance(self.constituents, Unset):
            constituents = self.constituents

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if constituents is not UNSET:
            field_dict["constituents"] = constituents
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        constituents = cast(list[str], d.pop("constituents", UNSET))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        bt_export_tessellated_body_3398 = cls(
            bt_type=bt_type,
            constituents=constituents,
            id=id,
            name=name,
        )

        bt_export_tessellated_body_3398.additional_properties = d
        return bt_export_tessellated_body_3398

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
