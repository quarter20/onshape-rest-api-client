from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_get_json_response_2137_tree_additional_property import BTGetJsonResponse2137TreeAdditionalProperty


T = TypeVar("T", bound="BTGetJsonResponse2137Tree")


@_attrs_define
class BTGetJsonResponse2137Tree:
    """
    Attributes:
        bt_type (str | Unset):
    """

    bt_type: str | Unset = UNSET
    additional_properties: dict[str, BTGetJsonResponse2137TreeAdditionalProperty] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_get_json_response_2137_tree_additional_property import (
            BTGetJsonResponse2137TreeAdditionalProperty,
        )

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        bt_get_json_response_2137_tree = cls(
            bt_type=bt_type,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = BTGetJsonResponse2137TreeAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        bt_get_json_response_2137_tree.additional_properties = additional_properties
        return bt_get_json_response_2137_tree

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> BTGetJsonResponse2137TreeAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: BTGetJsonResponse2137TreeAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
