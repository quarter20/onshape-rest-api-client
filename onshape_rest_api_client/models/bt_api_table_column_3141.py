from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_table_text_alignment import GBTTableTextAlignment
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTApiTableColumn3141")


@_attrs_define
class BTApiTableColumn3141:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        header (str | Unset):
        id (str | Unset):
        text_alignment (GBTTableTextAlignment | Unset):
    """

    bt_type: str | Unset = UNSET
    header: str | Unset = UNSET
    id: str | Unset = UNSET
    text_alignment: GBTTableTextAlignment | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        header = self.header

        id = self.id

        text_alignment: str | Unset = UNSET
        if not isinstance(self.text_alignment, Unset):
            text_alignment = self.text_alignment.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if header is not UNSET:
            field_dict["header"] = header
        if id is not UNSET:
            field_dict["id"] = id
        if text_alignment is not UNSET:
            field_dict["textAlignment"] = text_alignment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        header = d.pop("header", UNSET)

        id = d.pop("id", UNSET)

        _text_alignment = d.pop("textAlignment", UNSET)
        text_alignment: GBTTableTextAlignment | Unset
        if isinstance(_text_alignment, Unset):
            text_alignment = UNSET
        else:
            text_alignment = GBTTableTextAlignment(_text_alignment)

        bt_api_table_column_3141 = cls(
            bt_type=bt_type,
            header=header,
            id=id,
            text_alignment=text_alignment,
        )

        bt_api_table_column_3141.additional_properties = d
        return bt_api_table_column_3141

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
