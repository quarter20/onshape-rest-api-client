from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_type import EditType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_tree_node_20 import BTTreeNode20


T = TypeVar("T", bound="BTTreeEdit13")


@_attrs_define
class BTTreeEdit13:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        edit_type (EditType | Unset):
        new_nodes (list[BTTreeNode20] | Unset):
        nothing (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    edit_type: EditType | Unset = UNSET
    new_nodes: list[BTTreeNode20] | Unset = UNSET
    nothing: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        edit_type: str | Unset = UNSET
        if not isinstance(self.edit_type, Unset):
            edit_type = self.edit_type.value

        new_nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.new_nodes, Unset):
            new_nodes = []
            for new_nodes_item_data in self.new_nodes:
                new_nodes_item = new_nodes_item_data.to_dict()
                new_nodes.append(new_nodes_item)

        nothing = self.nothing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if edit_type is not UNSET:
            field_dict["editType"] = edit_type
        if new_nodes is not UNSET:
            field_dict["newNodes"] = new_nodes
        if nothing is not UNSET:
            field_dict["nothing"] = nothing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_tree_node_20 import BTTreeNode20

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _edit_type = d.pop("editType", UNSET)
        edit_type: EditType | Unset
        if isinstance(_edit_type, Unset):
            edit_type = UNSET
        else:
            edit_type = EditType(_edit_type)

        _new_nodes = d.pop("newNodes", UNSET)
        new_nodes: list[BTTreeNode20] | Unset = UNSET
        if _new_nodes is not UNSET:
            new_nodes = []
            for new_nodes_item_data in _new_nodes:
                new_nodes_item = BTTreeNode20.from_dict(new_nodes_item_data)

                new_nodes.append(new_nodes_item)

        nothing = d.pop("nothing", UNSET)

        bt_tree_edit_13 = cls(
            bt_type=bt_type,
            edit_type=edit_type,
            new_nodes=new_nodes,
            nothing=nothing,
        )

        bt_tree_edit_13.additional_properties = d
        return bt_tree_edit_13

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
