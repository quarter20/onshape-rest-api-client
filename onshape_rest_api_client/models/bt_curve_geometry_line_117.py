from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_sketch_entity_type import GBTSketchEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTCurveGeometryLine117")


@_attrs_define
class BTCurveGeometryLine117:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        entity_type (GBTSketchEntityType | Unset):
        dir_x (float | Unset):
        dir_y (float | Unset):
        pnt_x (float | Unset):
        pnt_y (float | Unset):
    """

    bt_type: str | Unset = UNSET
    entity_type: GBTSketchEntityType | Unset = UNSET
    dir_x: float | Unset = UNSET
    dir_y: float | Unset = UNSET
    pnt_x: float | Unset = UNSET
    pnt_y: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        entity_type: str | Unset = UNSET
        if not isinstance(self.entity_type, Unset):
            entity_type = self.entity_type.value

        dir_x = self.dir_x

        dir_y = self.dir_y

        pnt_x = self.pnt_x

        pnt_y = self.pnt_y

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if dir_x is not UNSET:
            field_dict["dirX"] = dir_x
        if dir_y is not UNSET:
            field_dict["dirY"] = dir_y
        if pnt_x is not UNSET:
            field_dict["pntX"] = pnt_x
        if pnt_y is not UNSET:
            field_dict["pntY"] = pnt_y

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _entity_type = d.pop("entityType", UNSET)
        entity_type: GBTSketchEntityType | Unset
        if isinstance(_entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = GBTSketchEntityType(_entity_type)

        dir_x = d.pop("dirX", UNSET)

        dir_y = d.pop("dirY", UNSET)

        pnt_x = d.pop("pntX", UNSET)

        pnt_y = d.pop("pntY", UNSET)

        bt_curve_geometry_line_117 = cls(
            bt_type=bt_type,
            entity_type=entity_type,
            dir_x=dir_x,
            dir_y=dir_y,
            pnt_x=pnt_x,
            pnt_y=pnt_y,
        )

        bt_curve_geometry_line_117.additional_properties = d
        return bt_curve_geometry_line_117

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
