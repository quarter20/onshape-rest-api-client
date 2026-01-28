from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BufferViewModelBufferViewData")


@_attrs_define
class BufferViewModelBufferViewData:
    """
    Attributes:
        short (int | Unset):
        char (str | Unset):
        int_ (int | Unset):
        long (int | Unset):
        float_ (float | Unset):
        double (float | Unset):
        direct (bool | Unset):
        read_only (bool | Unset):
    """

    short: int | Unset = UNSET
    char: str | Unset = UNSET
    int_: int | Unset = UNSET
    long: int | Unset = UNSET
    float_: float | Unset = UNSET
    double: float | Unset = UNSET
    direct: bool | Unset = UNSET
    read_only: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        short = self.short

        char = self.char

        int_ = self.int_

        long = self.long

        float_ = self.float_

        double = self.double

        direct = self.direct

        read_only = self.read_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if short is not UNSET:
            field_dict["short"] = short
        if char is not UNSET:
            field_dict["char"] = char
        if int_ is not UNSET:
            field_dict["int"] = int_
        if long is not UNSET:
            field_dict["long"] = long
        if float_ is not UNSET:
            field_dict["float"] = float_
        if double is not UNSET:
            field_dict["double"] = double
        if direct is not UNSET:
            field_dict["direct"] = direct
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        short = d.pop("short", UNSET)

        char = d.pop("char", UNSET)

        int_ = d.pop("int", UNSET)

        long = d.pop("long", UNSET)

        float_ = d.pop("float", UNSET)

        double = d.pop("double", UNSET)

        direct = d.pop("direct", UNSET)

        read_only = d.pop("readOnly", UNSET)

        buffer_view_model_buffer_view_data = cls(
            short=short,
            char=char,
            int_=int_,
            long=long,
            float_=float_,
            double=double,
            direct=direct,
            read_only=read_only,
        )

        buffer_view_model_buffer_view_data.additional_properties = d
        return buffer_view_model_buffer_view_data

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
