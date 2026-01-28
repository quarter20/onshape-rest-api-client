from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTViewDataInfo")


@_attrs_define
class BTViewDataInfo:
    """
    Attributes:
        angle (float | Unset):
        camera_viewport (list[float] | Unset):
        is_perspective (bool | Unset):
        view_matrix (list[float] | Unset):
    """

    angle: float | Unset = UNSET
    camera_viewport: list[float] | Unset = UNSET
    is_perspective: bool | Unset = UNSET
    view_matrix: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        angle = self.angle

        camera_viewport: list[float] | Unset = UNSET
        if not isinstance(self.camera_viewport, Unset):
            camera_viewport = self.camera_viewport

        is_perspective = self.is_perspective

        view_matrix: list[float] | Unset = UNSET
        if not isinstance(self.view_matrix, Unset):
            view_matrix = self.view_matrix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if angle is not UNSET:
            field_dict["angle"] = angle
        if camera_viewport is not UNSET:
            field_dict["cameraViewport"] = camera_viewport
        if is_perspective is not UNSET:
            field_dict["isPerspective"] = is_perspective
        if view_matrix is not UNSET:
            field_dict["viewMatrix"] = view_matrix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        angle = d.pop("angle", UNSET)

        camera_viewport = cast(list[float], d.pop("cameraViewport", UNSET))

        is_perspective = d.pop("isPerspective", UNSET)

        view_matrix = cast(list[float], d.pop("viewMatrix", UNSET))

        bt_view_data_info = cls(
            angle=angle,
            camera_viewport=camera_viewport,
            is_perspective=is_perspective,
            view_matrix=view_matrix,
        )

        bt_view_data_info.additional_properties = d
        return bt_view_data_info

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
