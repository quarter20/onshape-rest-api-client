from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTGraphicsSectionPlaneData1429")


@_attrs_define
class BTGraphicsSectionPlaneData1429:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        center (BTVector3D389 | Unset):
        normal (BTVector3D389 | Unset):
        tangent (BTVector3D389 | Unset):
    """

    bt_type: str | Unset = UNSET
    center: BTVector3D389 | Unset = UNSET
    normal: BTVector3D389 | Unset = UNSET
    tangent: BTVector3D389 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        center: dict[str, Any] | Unset = UNSET
        if not isinstance(self.center, Unset):
            center = self.center.to_dict()

        normal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.normal, Unset):
            normal = self.normal.to_dict()

        tangent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tangent, Unset):
            tangent = self.tangent.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if center is not UNSET:
            field_dict["center"] = center
        if normal is not UNSET:
            field_dict["normal"] = normal
        if tangent is not UNSET:
            field_dict["tangent"] = tangent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_vector_3d389 import BTVector3D389

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _center = d.pop("center", UNSET)
        center: BTVector3D389 | Unset
        if isinstance(_center, Unset):
            center = UNSET
        else:
            center = BTVector3D389.from_dict(_center)

        _normal = d.pop("normal", UNSET)
        normal: BTVector3D389 | Unset
        if isinstance(_normal, Unset):
            normal = UNSET
        else:
            normal = BTVector3D389.from_dict(_normal)

        _tangent = d.pop("tangent", UNSET)
        tangent: BTVector3D389 | Unset
        if isinstance(_tangent, Unset):
            tangent = UNSET
        else:
            tangent = BTVector3D389.from_dict(_tangent)

        bt_graphics_section_plane_data_1429 = cls(
            bt_type=bt_type,
            center=center,
            normal=normal,
            tangent=tangent,
        )

        bt_graphics_section_plane_data_1429.additional_properties = d
        return bt_graphics_section_plane_data_1429

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
