from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_group_or_element_reference_2205 import BTGroupOrElementReference2205


T = TypeVar("T", bound="BTElementGroup1458")


@_attrs_define
class BTElementGroup1458:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        group_name (str | Unset): The name of the group (folder).
        groups (list[BTGroupOrElementReference2205] | Unset): List of folders or elements in this group (folder).
        node_id (str | Unset): A unique identifier for this folder.
    """

    bt_type: str | Unset = UNSET
    group_name: str | Unset = UNSET
    groups: list[BTGroupOrElementReference2205] | Unset = UNSET
    node_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        group_name = self.group_name

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        node_id = self.node_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if groups is not UNSET:
            field_dict["groups"] = groups
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_group_or_element_reference_2205 import BTGroupOrElementReference2205

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        group_name = d.pop("groupName", UNSET)

        _groups = d.pop("groups", UNSET)
        groups: list[BTGroupOrElementReference2205] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = BTGroupOrElementReference2205.from_dict(groups_item_data)

                groups.append(groups_item)

        node_id = d.pop("nodeId", UNSET)

        bt_element_group_1458 = cls(
            bt_type=bt_type,
            group_name=group_name,
            groups=groups,
            node_id=node_id,
        )

        bt_element_group_1458.additional_properties = d
        return bt_element_group_1458

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
