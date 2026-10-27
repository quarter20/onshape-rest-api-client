from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_vector_3d389 import BTVector3D389
    from ..models.btm_parameter_1 import BTMParameter1


T = TypeVar("T", bound="BTMSketch3DPoint5367")


@_attrs_define
class BTMSketch3DPoint5367:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Microversion that resulted from the import.
        node_id (str | Unset):
        entity_id (str | Unset):
        parameters (list[BTMParameter1] | Unset):
        is_construction (bool | Unset):
        is_user_point (bool | Unset):
        position (BTVector3D389 | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    node_id: str | Unset = UNSET
    entity_id: str | Unset = UNSET
    parameters: list[BTMParameter1] | Unset = UNSET
    is_construction: bool | Unset = UNSET
    is_user_point: bool | Unset = UNSET
    position: BTVector3D389 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        node_id = self.node_id

        entity_id = self.entity_id

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        is_construction = self.is_construction

        is_user_point = self.is_user_point

        position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if is_construction is not UNSET:
            field_dict["isConstruction"] = is_construction
        if is_user_point is not UNSET:
            field_dict["isUserPoint"] = is_user_point
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_vector_3d389 import BTVector3D389  # noqa: PLC0415
        from ..models.btm_parameter_1 import BTMParameter1  # noqa: PLC0415

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        node_id = d.pop("nodeId", UNSET)

        entity_id = d.pop("entityId", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: list[BTMParameter1] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = BTMParameter1.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        is_construction = d.pop("isConstruction", UNSET)

        is_user_point = d.pop("isUserPoint", UNSET)

        _position = d.pop("position", UNSET)
        position: BTVector3D389 | Unset
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = BTVector3D389.from_dict(_position)

        btm_sketch_3d_point_5367 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            node_id=node_id,
            entity_id=entity_id,
            parameters=parameters,
            is_construction=is_construction,
            is_user_point=is_user_point,
            position=position,
        )

        btm_sketch_3d_point_5367.additional_properties = d
        return btm_sketch_3d_point_5367

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
