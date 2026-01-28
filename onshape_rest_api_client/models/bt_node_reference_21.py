from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_object_id import BTObjectId


T = TypeVar("T", bound="BTNodeReference21")


@_attrs_define
class BTNodeReference21:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        node_id (str | Unset):
        node_id_raw (BTObjectId | Unset):
    """

    bt_type: str | Unset = UNSET
    node_id: str | Unset = UNSET
    node_id_raw: BTObjectId | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        node_id = self.node_id

        node_id_raw: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node_id_raw, Unset):
            node_id_raw = self.node_id_raw.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if node_id_raw is not UNSET:
            field_dict["nodeIdRaw"] = node_id_raw

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_object_id import BTObjectId

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _node_id_raw = d.pop("nodeIdRaw", UNSET)
        node_id_raw: BTObjectId | Unset
        if isinstance(_node_id_raw, Unset):
            node_id_raw = UNSET
        else:
            node_id_raw = BTObjectId.from_dict(_node_id_raw)

        bt_node_reference_21 = cls(
            bt_type=bt_type,
            node_id=node_id,
            node_id_raw=node_id_raw,
        )

        bt_node_reference_21.additional_properties = d
        return bt_node_reference_21

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
