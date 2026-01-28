from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_entity_geometry_35 import BTEntityGeometry35


T = TypeVar("T", bound="BTBaseEntityData33")


@_attrs_define
class BTBaseEntityData33:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        construction_plane (bool | Unset):
        copy_without_geometry (BTBaseEntityData33 | Unset):
        decompressed (BTBaseEntityData33 | Unset):
        default_pane (bool | Unset):
        deletion (bool | Unset):
        feature_ids (list[str] | Unset):
        from_sketch (bool | Unset):
        geometries (list[BTEntityGeometry35] | Unset):
        origin (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    construction_plane: bool | Unset = UNSET
    copy_without_geometry: BTBaseEntityData33 | Unset = UNSET
    decompressed: BTBaseEntityData33 | Unset = UNSET
    default_pane: bool | Unset = UNSET
    deletion: bool | Unset = UNSET
    feature_ids: list[str] | Unset = UNSET
    from_sketch: bool | Unset = UNSET
    geometries: list[BTEntityGeometry35] | Unset = UNSET
    origin: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        construction_plane = self.construction_plane

        copy_without_geometry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.copy_without_geometry, Unset):
            copy_without_geometry = self.copy_without_geometry.to_dict()

        decompressed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.decompressed, Unset):
            decompressed = self.decompressed.to_dict()

        default_pane = self.default_pane

        deletion = self.deletion

        feature_ids: list[str] | Unset = UNSET
        if not isinstance(self.feature_ids, Unset):
            feature_ids = self.feature_ids

        from_sketch = self.from_sketch

        geometries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.geometries, Unset):
            geometries = []
            for geometries_item_data in self.geometries:
                geometries_item = geometries_item_data.to_dict()
                geometries.append(geometries_item)

        origin = self.origin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if construction_plane is not UNSET:
            field_dict["constructionPlane"] = construction_plane
        if copy_without_geometry is not UNSET:
            field_dict["copyWithoutGeometry"] = copy_without_geometry
        if decompressed is not UNSET:
            field_dict["decompressed"] = decompressed
        if default_pane is not UNSET:
            field_dict["defaultPane"] = default_pane
        if deletion is not UNSET:
            field_dict["deletion"] = deletion
        if feature_ids is not UNSET:
            field_dict["featureIds"] = feature_ids
        if from_sketch is not UNSET:
            field_dict["fromSketch"] = from_sketch
        if geometries is not UNSET:
            field_dict["geometries"] = geometries
        if origin is not UNSET:
            field_dict["origin"] = origin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_entity_geometry_35 import BTEntityGeometry35

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        construction_plane = d.pop("constructionPlane", UNSET)

        _copy_without_geometry = d.pop("copyWithoutGeometry", UNSET)
        copy_without_geometry: BTBaseEntityData33 | Unset
        if isinstance(_copy_without_geometry, Unset):
            copy_without_geometry = UNSET
        else:
            copy_without_geometry = BTBaseEntityData33.from_dict(_copy_without_geometry)

        _decompressed = d.pop("decompressed", UNSET)
        decompressed: BTBaseEntityData33 | Unset
        if isinstance(_decompressed, Unset):
            decompressed = UNSET
        else:
            decompressed = BTBaseEntityData33.from_dict(_decompressed)

        default_pane = d.pop("defaultPane", UNSET)

        deletion = d.pop("deletion", UNSET)

        feature_ids = cast(list[str], d.pop("featureIds", UNSET))

        from_sketch = d.pop("fromSketch", UNSET)

        _geometries = d.pop("geometries", UNSET)
        geometries: list[BTEntityGeometry35] | Unset = UNSET
        if _geometries is not UNSET:
            geometries = []
            for geometries_item_data in _geometries:
                geometries_item = BTEntityGeometry35.from_dict(geometries_item_data)

                geometries.append(geometries_item)

        origin = d.pop("origin", UNSET)

        bt_base_entity_data_33 = cls(
            bt_type=bt_type,
            construction_plane=construction_plane,
            copy_without_geometry=copy_without_geometry,
            decompressed=decompressed,
            default_pane=default_pane,
            deletion=deletion,
            feature_ids=feature_ids,
            from_sketch=from_sketch,
            geometries=geometries,
            origin=origin,
        )

        bt_base_entity_data_33.additional_properties = d
        return bt_base_entity_data_33

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
