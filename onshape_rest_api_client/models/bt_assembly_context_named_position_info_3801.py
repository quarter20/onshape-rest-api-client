from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAssemblyContextNamedPositionInfo3801")


@_attrs_define
class BTAssemblyContextNamedPositionInfo3801:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        name (str | Unset):
        node_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    name: str | Unset = UNSET
    node_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        name = self.name

        node_id = self.node_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if name is not UNSET:
            field_dict["name"] = name
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        name = d.pop("name", UNSET)

        node_id = d.pop("nodeId", UNSET)

        bt_assembly_context_named_position_info_3801 = cls(
            bt_type=bt_type,
            name=name,
            node_id=node_id,
        )

        bt_assembly_context_named_position_info_3801.additional_properties = d
        return bt_assembly_context_named_position_info_3801

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
