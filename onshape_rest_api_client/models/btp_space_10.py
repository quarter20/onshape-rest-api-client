from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTPSpace10")


@_attrs_define
class BTPSpace10:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        lines (list[str] | Unset):
        node_id (str | Unset):
        text (str | Unset):
    """

    bt_type: str | Unset = UNSET
    lines: list[str] | Unset = UNSET
    node_id: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        lines: list[str] | Unset = UNSET
        if not isinstance(self.lines, Unset):
            lines = self.lines

        node_id = self.node_id

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if lines is not UNSET:
            field_dict["lines"] = lines
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        lines = cast(list[str], d.pop("lines", UNSET))

        node_id = d.pop("nodeId", UNSET)

        text = d.pop("text", UNSET)

        btp_space_10 = cls(
            bt_type=bt_type,
            lines=lines,
            node_id=node_id,
            text=text,
        )

        btp_space_10.additional_properties = d
        return btp_space_10

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
