from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_get_json_response_2137_tree import BTGetJsonResponse2137Tree


T = TypeVar("T", bound="BTGetJsonResponse2137")


@_attrs_define
class BTGetJsonResponse2137:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        change_id (str | Unset):
        tree (BTGetJsonResponse2137Tree | Unset):
    """

    bt_type: str | Unset = UNSET
    change_id: str | Unset = UNSET
    tree: BTGetJsonResponse2137Tree | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        change_id = self.change_id

        tree: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tree, Unset):
            tree = self.tree.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if change_id is not UNSET:
            field_dict["changeId"] = change_id
        if tree is not UNSET:
            field_dict["tree"] = tree

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_get_json_response_2137_tree import BTGetJsonResponse2137Tree

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        change_id = d.pop("changeId", UNSET)

        _tree = d.pop("tree", UNSET)
        tree: BTGetJsonResponse2137Tree | Unset
        if isinstance(_tree, Unset):
            tree = UNSET
        else:
            tree = BTGetJsonResponse2137Tree.from_dict(_tree)

        bt_get_json_response_2137 = cls(
            bt_type=bt_type,
            change_id=change_id,
            tree=tree,
        )

        bt_get_json_response_2137.additional_properties = d
        return bt_get_json_response_2137

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
