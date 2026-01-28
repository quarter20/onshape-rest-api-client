from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTMassPropertiesInfo")


@_attrs_define
class BTMassPropertiesInfo:
    """Mass properties information.

    Attributes:
        centroid (list[float] | Unset): Centroid, center of gravity, center of mass
        has_mass (bool | Unset): `true` if the part has mass.
        inertia (list[float] | Unset): Mass moments of inertia
        mass (list[float] | Unset): Mass
        mass_missing_count (int | Unset): Number of parts without mass.
        periphery (list[float] | Unset): Surface area
        principal_axes (list[BTVector3D389] | Unset): Vector coordinates of the principal axes. Use `BTVector3d-389` as
            the `btType`.
        principal_inertia (list[float] | Unset): Principal moments of inertia
        volume (list[float] | Unset): Volume
    """

    centroid: list[float] | Unset = UNSET
    has_mass: bool | Unset = UNSET
    inertia: list[float] | Unset = UNSET
    mass: list[float] | Unset = UNSET
    mass_missing_count: int | Unset = UNSET
    periphery: list[float] | Unset = UNSET
    principal_axes: list[BTVector3D389] | Unset = UNSET
    principal_inertia: list[float] | Unset = UNSET
    volume: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        centroid: list[float] | Unset = UNSET
        if not isinstance(self.centroid, Unset):
            centroid = self.centroid

        has_mass = self.has_mass

        inertia: list[float] | Unset = UNSET
        if not isinstance(self.inertia, Unset):
            inertia = self.inertia

        mass: list[float] | Unset = UNSET
        if not isinstance(self.mass, Unset):
            mass = self.mass

        mass_missing_count = self.mass_missing_count

        periphery: list[float] | Unset = UNSET
        if not isinstance(self.periphery, Unset):
            periphery = self.periphery

        principal_axes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.principal_axes, Unset):
            principal_axes = []
            for principal_axes_item_data in self.principal_axes:
                principal_axes_item = principal_axes_item_data.to_dict()
                principal_axes.append(principal_axes_item)

        principal_inertia: list[float] | Unset = UNSET
        if not isinstance(self.principal_inertia, Unset):
            principal_inertia = self.principal_inertia

        volume: list[float] | Unset = UNSET
        if not isinstance(self.volume, Unset):
            volume = self.volume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if centroid is not UNSET:
            field_dict["centroid"] = centroid
        if has_mass is not UNSET:
            field_dict["hasMass"] = has_mass
        if inertia is not UNSET:
            field_dict["inertia"] = inertia
        if mass is not UNSET:
            field_dict["mass"] = mass
        if mass_missing_count is not UNSET:
            field_dict["massMissingCount"] = mass_missing_count
        if periphery is not UNSET:
            field_dict["periphery"] = periphery
        if principal_axes is not UNSET:
            field_dict["principalAxes"] = principal_axes
        if principal_inertia is not UNSET:
            field_dict["principalInertia"] = principal_inertia
        if volume is not UNSET:
            field_dict["volume"] = volume

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_vector_3d389 import BTVector3D389

        d = dict(src_dict)
        centroid = cast(list[float], d.pop("centroid", UNSET))

        has_mass = d.pop("hasMass", UNSET)

        inertia = cast(list[float], d.pop("inertia", UNSET))

        mass = cast(list[float], d.pop("mass", UNSET))

        mass_missing_count = d.pop("massMissingCount", UNSET)

        periphery = cast(list[float], d.pop("periphery", UNSET))

        _principal_axes = d.pop("principalAxes", UNSET)
        principal_axes: list[BTVector3D389] | Unset = UNSET
        if _principal_axes is not UNSET:
            principal_axes = []
            for principal_axes_item_data in _principal_axes:
                principal_axes_item = BTVector3D389.from_dict(principal_axes_item_data)

                principal_axes.append(principal_axes_item)

        principal_inertia = cast(list[float], d.pop("principalInertia", UNSET))

        volume = cast(list[float], d.pop("volume", UNSET))

        bt_mass_properties_info = cls(
            centroid=centroid,
            has_mass=has_mass,
            inertia=inertia,
            mass=mass,
            mass_missing_count=mass_missing_count,
            periphery=periphery,
            principal_axes=principal_axes,
            principal_inertia=principal_inertia,
            volume=volume,
        )

        bt_mass_properties_info.additional_properties = d
        return bt_mass_properties_info

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
