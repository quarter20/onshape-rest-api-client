from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_one_part_properties_230 import BTOnePartProperties230


T = TypeVar("T", bound="BTModelProperties1258")


@_attrs_define
class BTModelProperties1258:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        node_id (str | Unset):
        sub_part_properties (list[BTOnePartProperties230] | Unset):
    """

    bt_type: str | Unset = UNSET
    node_id: str | Unset = UNSET
    sub_part_properties: list[BTOnePartProperties230] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        node_id = self.node_id

        sub_part_properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sub_part_properties, Unset):
            sub_part_properties = []
            for sub_part_properties_item_data in self.sub_part_properties:
                sub_part_properties_item = sub_part_properties_item_data.to_dict()
                sub_part_properties.append(sub_part_properties_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if sub_part_properties is not UNSET:
            field_dict["subPartProperties"] = sub_part_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_one_part_properties_230 import BTOnePartProperties230

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _sub_part_properties = d.pop("subPartProperties", UNSET)
        sub_part_properties: list[BTOnePartProperties230] | Unset = UNSET
        if _sub_part_properties is not UNSET:
            sub_part_properties = []
            for sub_part_properties_item_data in _sub_part_properties:
                sub_part_properties_item = BTOnePartProperties230.from_dict(sub_part_properties_item_data)

                sub_part_properties.append(sub_part_properties_item)

        bt_model_properties_1258 = cls(
            bt_type=bt_type,
            node_id=node_id,
            sub_part_properties=sub_part_properties,
        )

        bt_model_properties_1258.additional_properties = d
        return bt_model_properties_1258

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
