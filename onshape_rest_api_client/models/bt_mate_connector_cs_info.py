from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTMateConnectorCSInfo")


@_attrs_define
class BTMateConnectorCSInfo:
    """
    Attributes:
        getx_axis (list[float] | Unset):
        gety_axis (list[float] | Unset):
        getz_axis (list[float] | Unset):
        origin (list[float] | Unset):
    """

    getx_axis: list[float] | Unset = UNSET
    gety_axis: list[float] | Unset = UNSET
    getz_axis: list[float] | Unset = UNSET
    origin: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        getx_axis: list[float] | Unset = UNSET
        if not isinstance(self.getx_axis, Unset):
            getx_axis = self.getx_axis

        gety_axis: list[float] | Unset = UNSET
        if not isinstance(self.gety_axis, Unset):
            gety_axis = self.gety_axis

        getz_axis: list[float] | Unset = UNSET
        if not isinstance(self.getz_axis, Unset):
            getz_axis = self.getz_axis

        origin: list[float] | Unset = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if getx_axis is not UNSET:
            field_dict["getxAxis"] = getx_axis
        if gety_axis is not UNSET:
            field_dict["getyAxis"] = gety_axis
        if getz_axis is not UNSET:
            field_dict["getzAxis"] = getz_axis
        if origin is not UNSET:
            field_dict["origin"] = origin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        getx_axis = cast(list[float], d.pop("getxAxis", UNSET))

        gety_axis = cast(list[float], d.pop("getyAxis", UNSET))

        getz_axis = cast(list[float], d.pop("getzAxis", UNSET))

        origin = cast(list[float], d.pop("origin", UNSET))

        bt_mate_connector_cs_info = cls(
            getx_axis=getx_axis,
            gety_axis=gety_axis,
            getz_axis=getz_axis,
            origin=origin,
        )

        bt_mate_connector_cs_info.additional_properties = d
        return bt_mate_connector_cs_info

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
