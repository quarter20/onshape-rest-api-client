from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_key_mouse_values_info import BTKeyMouseValuesInfo


T = TypeVar("T", bound="BTViewManipulationMouseKeyMappingInfo")


@_attrs_define
class BTViewManipulationMouseKeyMappingInfo:
    """
    Attributes:
        axis_rotate_3d_mapping (list[BTKeyMouseValuesInfo] | Unset):
        pan_2d_mapping (list[BTKeyMouseValuesInfo] | Unset):
        pan_3d_mapping (list[BTKeyMouseValuesInfo] | Unset):
        rotate_3d_mapping (list[BTKeyMouseValuesInfo] | Unset):
        zoom_2d_mapping (list[BTKeyMouseValuesInfo] | Unset):
        zoom_3d_mapping (list[BTKeyMouseValuesInfo] | Unset):
    """

    axis_rotate_3d_mapping: list[BTKeyMouseValuesInfo] | Unset = UNSET
    pan_2d_mapping: list[BTKeyMouseValuesInfo] | Unset = UNSET
    pan_3d_mapping: list[BTKeyMouseValuesInfo] | Unset = UNSET
    rotate_3d_mapping: list[BTKeyMouseValuesInfo] | Unset = UNSET
    zoom_2d_mapping: list[BTKeyMouseValuesInfo] | Unset = UNSET
    zoom_3d_mapping: list[BTKeyMouseValuesInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        axis_rotate_3d_mapping: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.axis_rotate_3d_mapping, Unset):
            axis_rotate_3d_mapping = []
            for axis_rotate_3d_mapping_item_data in self.axis_rotate_3d_mapping:
                axis_rotate_3d_mapping_item = axis_rotate_3d_mapping_item_data.to_dict()
                axis_rotate_3d_mapping.append(axis_rotate_3d_mapping_item)

        pan_2d_mapping: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pan_2d_mapping, Unset):
            pan_2d_mapping = []
            for pan_2d_mapping_item_data in self.pan_2d_mapping:
                pan_2d_mapping_item = pan_2d_mapping_item_data.to_dict()
                pan_2d_mapping.append(pan_2d_mapping_item)

        pan_3d_mapping: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pan_3d_mapping, Unset):
            pan_3d_mapping = []
            for pan_3d_mapping_item_data in self.pan_3d_mapping:
                pan_3d_mapping_item = pan_3d_mapping_item_data.to_dict()
                pan_3d_mapping.append(pan_3d_mapping_item)

        rotate_3d_mapping: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rotate_3d_mapping, Unset):
            rotate_3d_mapping = []
            for rotate_3d_mapping_item_data in self.rotate_3d_mapping:
                rotate_3d_mapping_item = rotate_3d_mapping_item_data.to_dict()
                rotate_3d_mapping.append(rotate_3d_mapping_item)

        zoom_2d_mapping: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.zoom_2d_mapping, Unset):
            zoom_2d_mapping = []
            for zoom_2d_mapping_item_data in self.zoom_2d_mapping:
                zoom_2d_mapping_item = zoom_2d_mapping_item_data.to_dict()
                zoom_2d_mapping.append(zoom_2d_mapping_item)

        zoom_3d_mapping: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.zoom_3d_mapping, Unset):
            zoom_3d_mapping = []
            for zoom_3d_mapping_item_data in self.zoom_3d_mapping:
                zoom_3d_mapping_item = zoom_3d_mapping_item_data.to_dict()
                zoom_3d_mapping.append(zoom_3d_mapping_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if axis_rotate_3d_mapping is not UNSET:
            field_dict["axisRotate3DMapping"] = axis_rotate_3d_mapping
        if pan_2d_mapping is not UNSET:
            field_dict["pan2DMapping"] = pan_2d_mapping
        if pan_3d_mapping is not UNSET:
            field_dict["pan3DMapping"] = pan_3d_mapping
        if rotate_3d_mapping is not UNSET:
            field_dict["rotate3DMapping"] = rotate_3d_mapping
        if zoom_2d_mapping is not UNSET:
            field_dict["zoom2DMapping"] = zoom_2d_mapping
        if zoom_3d_mapping is not UNSET:
            field_dict["zoom3DMapping"] = zoom_3d_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_key_mouse_values_info import BTKeyMouseValuesInfo

        d = dict(src_dict)
        _axis_rotate_3d_mapping = d.pop("axisRotate3DMapping", UNSET)
        axis_rotate_3d_mapping: list[BTKeyMouseValuesInfo] | Unset = UNSET
        if _axis_rotate_3d_mapping is not UNSET:
            axis_rotate_3d_mapping = []
            for axis_rotate_3d_mapping_item_data in _axis_rotate_3d_mapping:
                axis_rotate_3d_mapping_item = BTKeyMouseValuesInfo.from_dict(axis_rotate_3d_mapping_item_data)

                axis_rotate_3d_mapping.append(axis_rotate_3d_mapping_item)

        _pan_2d_mapping = d.pop("pan2DMapping", UNSET)
        pan_2d_mapping: list[BTKeyMouseValuesInfo] | Unset = UNSET
        if _pan_2d_mapping is not UNSET:
            pan_2d_mapping = []
            for pan_2d_mapping_item_data in _pan_2d_mapping:
                pan_2d_mapping_item = BTKeyMouseValuesInfo.from_dict(pan_2d_mapping_item_data)

                pan_2d_mapping.append(pan_2d_mapping_item)

        _pan_3d_mapping = d.pop("pan3DMapping", UNSET)
        pan_3d_mapping: list[BTKeyMouseValuesInfo] | Unset = UNSET
        if _pan_3d_mapping is not UNSET:
            pan_3d_mapping = []
            for pan_3d_mapping_item_data in _pan_3d_mapping:
                pan_3d_mapping_item = BTKeyMouseValuesInfo.from_dict(pan_3d_mapping_item_data)

                pan_3d_mapping.append(pan_3d_mapping_item)

        _rotate_3d_mapping = d.pop("rotate3DMapping", UNSET)
        rotate_3d_mapping: list[BTKeyMouseValuesInfo] | Unset = UNSET
        if _rotate_3d_mapping is not UNSET:
            rotate_3d_mapping = []
            for rotate_3d_mapping_item_data in _rotate_3d_mapping:
                rotate_3d_mapping_item = BTKeyMouseValuesInfo.from_dict(rotate_3d_mapping_item_data)

                rotate_3d_mapping.append(rotate_3d_mapping_item)

        _zoom_2d_mapping = d.pop("zoom2DMapping", UNSET)
        zoom_2d_mapping: list[BTKeyMouseValuesInfo] | Unset = UNSET
        if _zoom_2d_mapping is not UNSET:
            zoom_2d_mapping = []
            for zoom_2d_mapping_item_data in _zoom_2d_mapping:
                zoom_2d_mapping_item = BTKeyMouseValuesInfo.from_dict(zoom_2d_mapping_item_data)

                zoom_2d_mapping.append(zoom_2d_mapping_item)

        _zoom_3d_mapping = d.pop("zoom3DMapping", UNSET)
        zoom_3d_mapping: list[BTKeyMouseValuesInfo] | Unset = UNSET
        if _zoom_3d_mapping is not UNSET:
            zoom_3d_mapping = []
            for zoom_3d_mapping_item_data in _zoom_3d_mapping:
                zoom_3d_mapping_item = BTKeyMouseValuesInfo.from_dict(zoom_3d_mapping_item_data)

                zoom_3d_mapping.append(zoom_3d_mapping_item)

        bt_view_manipulation_mouse_key_mapping_info = cls(
            axis_rotate_3d_mapping=axis_rotate_3d_mapping,
            pan_2d_mapping=pan_2d_mapping,
            pan_3d_mapping=pan_3d_mapping,
            rotate_3d_mapping=rotate_3d_mapping,
            zoom_2d_mapping=zoom_2d_mapping,
            zoom_3d_mapping=zoom_3d_mapping,
        )

        bt_view_manipulation_mouse_key_mapping_info.additional_properties = d
        return bt_view_manipulation_mouse_key_mapping_info

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
