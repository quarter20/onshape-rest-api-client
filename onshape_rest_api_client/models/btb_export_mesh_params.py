from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_export_resolution import GBTExportResolution
from ..models.gbt_export_unit import GBTExportUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTBExportMeshParams")


@_attrs_define
class BTBExportMeshParams:
    """Options for an element export to mesh format.

    Attributes:
        angular_tolerance (float | Unset): Determines the maximum angular deviation, between the analytical surface and
            its triangulation. Lower values result in a finer geometry and higher values result in coarser geometry.
            Default: 0.001.
        distance_tolerance (float | Unset): Determines the maximum distance deviation, between the analytical surface
            and its triangulation. Lower values result in a finer geometry and higher values result in coarser geometry.
            Default: 0.001.
        maximum_chord_length (float | Unset): Determines the maximum of a triangle edge length. Lower values result in a
            finer geometry and higher values result in coarser geometry. Default: 0.01.
        resolution (GBTExportResolution | Unset): Determines export resolution of fine, medium, or coarse
        unit (GBTExportUnit | Unset): Units to export the model with.
    """

    angular_tolerance: float | Unset = 0.001
    distance_tolerance: float | Unset = 0.001
    maximum_chord_length: float | Unset = 0.01
    resolution: GBTExportResolution | Unset = UNSET
    unit: GBTExportUnit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        angular_tolerance = self.angular_tolerance

        distance_tolerance = self.distance_tolerance

        maximum_chord_length = self.maximum_chord_length

        resolution: str | Unset = UNSET
        if not isinstance(self.resolution, Unset):
            resolution = self.resolution.value

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if angular_tolerance is not UNSET:
            field_dict["angularTolerance"] = angular_tolerance
        if distance_tolerance is not UNSET:
            field_dict["distanceTolerance"] = distance_tolerance
        if maximum_chord_length is not UNSET:
            field_dict["maximumChordLength"] = maximum_chord_length
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        angular_tolerance = d.pop("angularTolerance", UNSET)

        distance_tolerance = d.pop("distanceTolerance", UNSET)

        maximum_chord_length = d.pop("maximumChordLength", UNSET)

        _resolution = d.pop("resolution", UNSET)
        resolution: GBTExportResolution | Unset
        if isinstance(_resolution, Unset):
            resolution = UNSET
        else:
            resolution = GBTExportResolution(_resolution)

        _unit = d.pop("unit", UNSET)
        unit: GBTExportUnit | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = GBTExportUnit(_unit)

        btb_export_mesh_params = cls(
            angular_tolerance=angular_tolerance,
            distance_tolerance=distance_tolerance,
            maximum_chord_length=maximum_chord_length,
            resolution=resolution,
            unit=unit,
        )

        btb_export_mesh_params.additional_properties = d
        return btb_export_mesh_params

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
