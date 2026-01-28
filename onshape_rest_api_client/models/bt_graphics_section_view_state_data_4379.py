from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_graphics_section_plane_data_1429 import BTGraphicsSectionPlaneData1429
    from ..models.bt_ui_selection_1185 import BTUiSelection1185


T = TypeVar("T", bound="BTGraphicsSectionViewStateData4379")


@_attrs_define
class BTGraphicsSectionViewStateData4379:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        element_id (str | Unset):
        is_excluding (bool | Unset):
        section_planes (list[BTGraphicsSectionPlaneData1429] | Unset):
        selections_to_exclude (list[BTUiSelection1185] | Unset):
        selections_to_include (list[BTUiSelection1185] | Unset):
    """

    bt_type: str | Unset = UNSET
    element_id: str | Unset = UNSET
    is_excluding: bool | Unset = UNSET
    section_planes: list[BTGraphicsSectionPlaneData1429] | Unset = UNSET
    selections_to_exclude: list[BTUiSelection1185] | Unset = UNSET
    selections_to_include: list[BTUiSelection1185] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        element_id = self.element_id

        is_excluding = self.is_excluding

        section_planes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.section_planes, Unset):
            section_planes = []
            for section_planes_item_data in self.section_planes:
                section_planes_item = section_planes_item_data.to_dict()
                section_planes.append(section_planes_item)

        selections_to_exclude: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.selections_to_exclude, Unset):
            selections_to_exclude = []
            for selections_to_exclude_item_data in self.selections_to_exclude:
                selections_to_exclude_item = selections_to_exclude_item_data.to_dict()
                selections_to_exclude.append(selections_to_exclude_item)

        selections_to_include: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.selections_to_include, Unset):
            selections_to_include = []
            for selections_to_include_item_data in self.selections_to_include:
                selections_to_include_item = selections_to_include_item_data.to_dict()
                selections_to_include.append(selections_to_include_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if is_excluding is not UNSET:
            field_dict["isExcluding"] = is_excluding
        if section_planes is not UNSET:
            field_dict["sectionPlanes"] = section_planes
        if selections_to_exclude is not UNSET:
            field_dict["selectionsToExclude"] = selections_to_exclude
        if selections_to_include is not UNSET:
            field_dict["selectionsToInclude"] = selections_to_include

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_graphics_section_plane_data_1429 import BTGraphicsSectionPlaneData1429
        from ..models.bt_ui_selection_1185 import BTUiSelection1185

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        element_id = d.pop("elementId", UNSET)

        is_excluding = d.pop("isExcluding", UNSET)

        _section_planes = d.pop("sectionPlanes", UNSET)
        section_planes: list[BTGraphicsSectionPlaneData1429] | Unset = UNSET
        if _section_planes is not UNSET:
            section_planes = []
            for section_planes_item_data in _section_planes:
                section_planes_item = BTGraphicsSectionPlaneData1429.from_dict(section_planes_item_data)

                section_planes.append(section_planes_item)

        _selections_to_exclude = d.pop("selectionsToExclude", UNSET)
        selections_to_exclude: list[BTUiSelection1185] | Unset = UNSET
        if _selections_to_exclude is not UNSET:
            selections_to_exclude = []
            for selections_to_exclude_item_data in _selections_to_exclude:
                selections_to_exclude_item = BTUiSelection1185.from_dict(selections_to_exclude_item_data)

                selections_to_exclude.append(selections_to_exclude_item)

        _selections_to_include = d.pop("selectionsToInclude", UNSET)
        selections_to_include: list[BTUiSelection1185] | Unset = UNSET
        if _selections_to_include is not UNSET:
            selections_to_include = []
            for selections_to_include_item_data in _selections_to_include:
                selections_to_include_item = BTUiSelection1185.from_dict(selections_to_include_item_data)

                selections_to_include.append(selections_to_include_item)

        bt_graphics_section_view_state_data_4379 = cls(
            bt_type=bt_type,
            element_id=element_id,
            is_excluding=is_excluding,
            section_planes=section_planes,
            selections_to_exclude=selections_to_exclude,
            selections_to_include=selections_to_include,
        )

        bt_graphics_section_view_state_data_4379.additional_properties = d
        return bt_graphics_section_view_state_data_4379

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
