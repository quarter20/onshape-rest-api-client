from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_coordinate_system_387 import BTCoordinateSystem387
    from ..models.bt_matrix_3x3340 import BTMatrix3X3340


T = TypeVar("T", bound="BTPlanarImageMapping4398")


@_attrs_define
class BTPlanarImageMapping4398:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        deterministic_ids (list[str] | Unset):
        uv_transform (BTMatrix3X3340 | Unset):
        plane_system (BTCoordinateSystem387 | Unset):
    """

    bt_type: str | Unset = UNSET
    deterministic_ids: list[str] | Unset = UNSET
    uv_transform: BTMatrix3X3340 | Unset = UNSET
    plane_system: BTCoordinateSystem387 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        deterministic_ids: list[str] | Unset = UNSET
        if not isinstance(self.deterministic_ids, Unset):
            deterministic_ids = self.deterministic_ids

        uv_transform: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uv_transform, Unset):
            uv_transform = self.uv_transform.to_dict()

        plane_system: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plane_system, Unset):
            plane_system = self.plane_system.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if deterministic_ids is not UNSET:
            field_dict["deterministicIds"] = deterministic_ids
        if uv_transform is not UNSET:
            field_dict["uvTransform"] = uv_transform
        if plane_system is not UNSET:
            field_dict["planeSystem"] = plane_system

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_coordinate_system_387 import BTCoordinateSystem387
        from ..models.bt_matrix_3x3340 import BTMatrix3X3340

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        deterministic_ids = cast(list[str], d.pop("deterministicIds", UNSET))

        _uv_transform = d.pop("uvTransform", UNSET)
        uv_transform: BTMatrix3X3340 | Unset
        if isinstance(_uv_transform, Unset):
            uv_transform = UNSET
        else:
            uv_transform = BTMatrix3X3340.from_dict(_uv_transform)

        _plane_system = d.pop("planeSystem", UNSET)
        plane_system: BTCoordinateSystem387 | Unset
        if isinstance(_plane_system, Unset):
            plane_system = UNSET
        else:
            plane_system = BTCoordinateSystem387.from_dict(_plane_system)

        bt_planar_image_mapping_4398 = cls(
            bt_type=bt_type,
            deterministic_ids=deterministic_ids,
            uv_transform=uv_transform,
            plane_system=plane_system,
        )

        bt_planar_image_mapping_4398.additional_properties = d
        return bt_planar_image_mapping_4398

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
