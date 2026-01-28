from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_graphics_section_view_state_data_4379 import BTGraphicsSectionViewStateData4379
    from ..models.bt_section_plane_info import BTSectionPlaneInfo


T = TypeVar("T", bound="BTNamedViewInfo")


@_attrs_define
class BTNamedViewInfo:
    """
    Attributes:
        angle (float | Unset):
        camera_viewport (list[float] | Unset):
        perspective (bool | Unset):
        section_planes (list[BTSectionPlaneInfo] | Unset):
        section_view_data (BTGraphicsSectionViewStateData4379 | Unset):
        view_matrix (list[float] | Unset):
    """

    angle: float | Unset = UNSET
    camera_viewport: list[float] | Unset = UNSET
    perspective: bool | Unset = UNSET
    section_planes: list[BTSectionPlaneInfo] | Unset = UNSET
    section_view_data: BTGraphicsSectionViewStateData4379 | Unset = UNSET
    view_matrix: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        angle = self.angle

        camera_viewport: list[float] | Unset = UNSET
        if not isinstance(self.camera_viewport, Unset):
            camera_viewport = self.camera_viewport

        perspective = self.perspective

        section_planes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.section_planes, Unset):
            section_planes = []
            for section_planes_item_data in self.section_planes:
                section_planes_item = section_planes_item_data.to_dict()
                section_planes.append(section_planes_item)

        section_view_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.section_view_data, Unset):
            section_view_data = self.section_view_data.to_dict()

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
        if perspective is not UNSET:
            field_dict["perspective"] = perspective
        if section_planes is not UNSET:
            field_dict["sectionPlanes"] = section_planes
        if section_view_data is not UNSET:
            field_dict["sectionViewData"] = section_view_data
        if view_matrix is not UNSET:
            field_dict["viewMatrix"] = view_matrix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_graphics_section_view_state_data_4379 import BTGraphicsSectionViewStateData4379
        from ..models.bt_section_plane_info import BTSectionPlaneInfo

        d = dict(src_dict)
        angle = d.pop("angle", UNSET)

        camera_viewport = cast(list[float], d.pop("cameraViewport", UNSET))

        perspective = d.pop("perspective", UNSET)

        _section_planes = d.pop("sectionPlanes", UNSET)
        section_planes: list[BTSectionPlaneInfo] | Unset = UNSET
        if _section_planes is not UNSET:
            section_planes = []
            for section_planes_item_data in _section_planes:
                section_planes_item = BTSectionPlaneInfo.from_dict(section_planes_item_data)

                section_planes.append(section_planes_item)

        _section_view_data = d.pop("sectionViewData", UNSET)
        section_view_data: BTGraphicsSectionViewStateData4379 | Unset
        if isinstance(_section_view_data, Unset):
            section_view_data = UNSET
        else:
            section_view_data = BTGraphicsSectionViewStateData4379.from_dict(_section_view_data)

        view_matrix = cast(list[float], d.pop("viewMatrix", UNSET))

        bt_named_view_info = cls(
            angle=angle,
            camera_viewport=camera_viewport,
            perspective=perspective,
            section_planes=section_planes,
            section_view_data=section_view_data,
            view_matrix=view_matrix,
        )

        bt_named_view_info.additional_properties = d
        return bt_named_view_info

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
