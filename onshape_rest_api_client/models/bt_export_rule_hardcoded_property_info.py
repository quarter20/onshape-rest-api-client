from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTExportRuleHardcodedPropertyInfo")


@_attrs_define
class BTExportRuleHardcodedPropertyInfo:
    """
    Attributes:
        context (int | Unset):
        id (str | Unset):
        name (str | Unset):
        object_types (list[int] | Unset):
    """

    context: int | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    object_types: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context = self.context

        id = self.id

        name = self.name

        object_types: list[int] | Unset = UNSET
        if not isinstance(self.object_types, Unset):
            object_types = self.object_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context is not UNSET:
            field_dict["context"] = context
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if object_types is not UNSET:
            field_dict["objectTypes"] = object_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        context = d.pop("context", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        object_types = cast(list[int], d.pop("objectTypes", UNSET))

        bt_export_rule_hardcoded_property_info = cls(
            context=context,
            id=id,
            name=name,
            object_types=object_types,
        )

        bt_export_rule_hardcoded_property_info.additional_properties = d
        return bt_export_rule_hardcoded_property_info

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
