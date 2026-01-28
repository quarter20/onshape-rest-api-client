from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_json_match_2290_node import BTJsonMatch2290Node


T = TypeVar("T", bound="BTJsonMatch2290")


@_attrs_define
class BTJsonMatch2290:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        definite_json_path (str | Unset):
        node (BTJsonMatch2290Node | Unset):
    """

    bt_type: str | Unset = UNSET
    definite_json_path: str | Unset = UNSET
    node: BTJsonMatch2290Node | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        definite_json_path = self.definite_json_path

        node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node, Unset):
            node = self.node.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if definite_json_path is not UNSET:
            field_dict["definiteJsonPath"] = definite_json_path
        if node is not UNSET:
            field_dict["node"] = node

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_json_match_2290_node import BTJsonMatch2290Node

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        definite_json_path = d.pop("definiteJsonPath", UNSET)

        _node = d.pop("node", UNSET)
        node: BTJsonMatch2290Node | Unset
        if isinstance(_node, Unset):
            node = UNSET
        else:
            node = BTJsonMatch2290Node.from_dict(_node)

        bt_json_match_2290 = cls(
            bt_type=bt_type,
            definite_json_path=definite_json_path,
            node=node,
        )

        bt_json_match_2290.additional_properties = d
        return bt_json_match_2290

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
