from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_sketch_entity_display_data_354 import BTSketchEntityDisplayData354
    from ..models.bt_vector_3d389 import BTVector3D389


T = TypeVar("T", bound="BTSketchImageDisplayData1379")


@_attrs_define
class BTSketchImageDisplayData1379:
    """
    Attributes:
        bottom_left_corner (BTVector3D389 | Unset):
        bottom_right_corner (BTVector3D389 | Unset):
        bt_type (str | Unset): Type of JSON object.
        entities (list[BTSketchEntityDisplayData354] | Unset):
        feature_id (str | Unset):
        is_on_flat (bool | Unset):
        points (list[float] | Unset):
        source_id (str | Unset):
        top_left_corner (BTVector3D389 | Unset):
    """

    bottom_left_corner: BTVector3D389 | Unset = UNSET
    bottom_right_corner: BTVector3D389 | Unset = UNSET
    bt_type: str | Unset = UNSET
    entities: list[BTSketchEntityDisplayData354] | Unset = UNSET
    feature_id: str | Unset = UNSET
    is_on_flat: bool | Unset = UNSET
    points: list[float] | Unset = UNSET
    source_id: str | Unset = UNSET
    top_left_corner: BTVector3D389 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bottom_left_corner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bottom_left_corner, Unset):
            bottom_left_corner = self.bottom_left_corner.to_dict()

        bottom_right_corner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bottom_right_corner, Unset):
            bottom_right_corner = self.bottom_right_corner.to_dict()

        bt_type = self.bt_type

        entities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entities, Unset):
            entities = []
            for entities_item_data in self.entities:
                entities_item = entities_item_data.to_dict()
                entities.append(entities_item)

        feature_id = self.feature_id

        is_on_flat = self.is_on_flat

        points: list[float] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = self.points

        source_id = self.source_id

        top_left_corner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top_left_corner, Unset):
            top_left_corner = self.top_left_corner.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bottom_left_corner is not UNSET:
            field_dict["bottomLeftCorner"] = bottom_left_corner
        if bottom_right_corner is not UNSET:
            field_dict["bottomRightCorner"] = bottom_right_corner
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if entities is not UNSET:
            field_dict["entities"] = entities
        if feature_id is not UNSET:
            field_dict["featureId"] = feature_id
        if is_on_flat is not UNSET:
            field_dict["isOnFlat"] = is_on_flat
        if points is not UNSET:
            field_dict["points"] = points
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if top_left_corner is not UNSET:
            field_dict["topLeftCorner"] = top_left_corner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_sketch_entity_display_data_354 import BTSketchEntityDisplayData354
        from ..models.bt_vector_3d389 import BTVector3D389

        d = dict(src_dict)
        _bottom_left_corner = d.pop("bottomLeftCorner", UNSET)
        bottom_left_corner: BTVector3D389 | Unset
        if isinstance(_bottom_left_corner, Unset):
            bottom_left_corner = UNSET
        else:
            bottom_left_corner = BTVector3D389.from_dict(_bottom_left_corner)

        _bottom_right_corner = d.pop("bottomRightCorner", UNSET)
        bottom_right_corner: BTVector3D389 | Unset
        if isinstance(_bottom_right_corner, Unset):
            bottom_right_corner = UNSET
        else:
            bottom_right_corner = BTVector3D389.from_dict(_bottom_right_corner)

        bt_type = d.pop("btType", UNSET)

        _entities = d.pop("entities", UNSET)
        entities: list[BTSketchEntityDisplayData354] | Unset = UNSET
        if _entities is not UNSET:
            entities = []
            for entities_item_data in _entities:
                entities_item = BTSketchEntityDisplayData354.from_dict(entities_item_data)

                entities.append(entities_item)

        feature_id = d.pop("featureId", UNSET)

        is_on_flat = d.pop("isOnFlat", UNSET)

        points = cast(list[float], d.pop("points", UNSET))

        source_id = d.pop("sourceId", UNSET)

        _top_left_corner = d.pop("topLeftCorner", UNSET)
        top_left_corner: BTVector3D389 | Unset
        if isinstance(_top_left_corner, Unset):
            top_left_corner = UNSET
        else:
            top_left_corner = BTVector3D389.from_dict(_top_left_corner)

        bt_sketch_image_display_data_1379 = cls(
            bottom_left_corner=bottom_left_corner,
            bottom_right_corner=bottom_right_corner,
            bt_type=bt_type,
            entities=entities,
            feature_id=feature_id,
            is_on_flat=is_on_flat,
            points=points,
            source_id=source_id,
            top_left_corner=top_left_corner,
        )

        bt_sketch_image_display_data_1379.additional_properties = d
        return bt_sketch_image_display_data_1379

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
