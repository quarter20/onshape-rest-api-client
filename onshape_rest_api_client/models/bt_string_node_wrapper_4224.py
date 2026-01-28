from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTStringNodeWrapper4224")


@_attrs_define
class BTStringNodeWrapper4224:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        node_id (str | Unset):
        string (str | Unset):
    """

    bt_type: str | Unset = UNSET
    node_id: str | Unset = UNSET
    string: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        node_id = self.node_id

        string = self.string

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if string is not UNSET:
            field_dict["string"] = string

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        node_id = d.pop("nodeId", UNSET)

        string = d.pop("string", UNSET)

        bt_string_node_wrapper_4224 = cls(
            bt_type=bt_type,
            node_id=node_id,
            string=string,
        )

        bt_string_node_wrapper_4224.additional_properties = d
        return bt_string_node_wrapper_4224

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
