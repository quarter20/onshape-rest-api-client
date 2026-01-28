from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_coordinate_system_387 import BTCoordinateSystem387


T = TypeVar("T", bound="BTCosmeticThreadMetadata3248")


@_attrs_define
class BTCosmeticThreadMetadata3248:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        cylinder_radius (float | Unset):
        cylinder_system (BTCoordinateSystem387 | Unset):
        pitch (float | Unset):
        thread_length (float | Unset):
    """

    bt_type: str | Unset = UNSET
    cylinder_radius: float | Unset = UNSET
    cylinder_system: BTCoordinateSystem387 | Unset = UNSET
    pitch: float | Unset = UNSET
    thread_length: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        cylinder_radius = self.cylinder_radius

        cylinder_system: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cylinder_system, Unset):
            cylinder_system = self.cylinder_system.to_dict()

        pitch = self.pitch

        thread_length = self.thread_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if cylinder_radius is not UNSET:
            field_dict["cylinderRadius"] = cylinder_radius
        if cylinder_system is not UNSET:
            field_dict["cylinderSystem"] = cylinder_system
        if pitch is not UNSET:
            field_dict["pitch"] = pitch
        if thread_length is not UNSET:
            field_dict["threadLength"] = thread_length

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_coordinate_system_387 import BTCoordinateSystem387

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        cylinder_radius = d.pop("cylinderRadius", UNSET)

        _cylinder_system = d.pop("cylinderSystem", UNSET)
        cylinder_system: BTCoordinateSystem387 | Unset
        if isinstance(_cylinder_system, Unset):
            cylinder_system = UNSET
        else:
            cylinder_system = BTCoordinateSystem387.from_dict(_cylinder_system)

        pitch = d.pop("pitch", UNSET)

        thread_length = d.pop("threadLength", UNSET)

        bt_cosmetic_thread_metadata_3248 = cls(
            bt_type=bt_type,
            cylinder_radius=cylinder_radius,
            cylinder_system=cylinder_system,
            pitch=pitch,
            thread_length=thread_length,
        )

        bt_cosmetic_thread_metadata_3248.additional_properties = d
        return bt_cosmetic_thread_metadata_3248

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
