from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bt_bounding_box_1052 import BTBoundingBox1052


T = TypeVar("T", bound="BTAppDrawingViewInfoBrokenOutBBoxes")


@_attrs_define
class BTAppDrawingViewInfoBrokenOutBBoxes:
    """ """

    additional_properties: dict[str, BTBoundingBox1052] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_bounding_box_1052 import BTBoundingBox1052

        d = dict(src_dict)
        bt_app_drawing_view_info_broken_out_b_boxes = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = BTBoundingBox1052.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        bt_app_drawing_view_info_broken_out_b_boxes.additional_properties = additional_properties
        return bt_app_drawing_view_info_broken_out_b_boxes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> BTBoundingBox1052:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: BTBoundingBox1052) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
