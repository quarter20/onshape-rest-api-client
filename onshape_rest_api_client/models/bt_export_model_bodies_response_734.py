from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_error_string_enum import GBTErrorStringEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_export_model_bodies_response_734_node_id_to_referenced_property import (
        BTExportModelBodiesResponse734NodeIdToReferencedProperty,
    )
    from ..models.bt_export_model_body_1272 import BTExportModelBody1272
    from ..models.bt_microversion_id_366 import BTMicroversionId366


T = TypeVar("T", bound="BTExportModelBodiesResponse734")


@_attrs_define
class BTExportModelBodiesResponse734:
    """
    Attributes:
        bodies (list[BTExportModelBody1272] | Unset):
        bt_type (str | Unset): Type of JSON object.
        error_enum (GBTErrorStringEnum | Unset):
        microversion_id (BTMicroversionId366 | Unset):
        node_id_to_referenced_property (BTExportModelBodiesResponse734NodeIdToReferencedProperty | Unset):
    """

    bodies: list[BTExportModelBody1272] | Unset = UNSET
    bt_type: str | Unset = UNSET
    error_enum: GBTErrorStringEnum | Unset = UNSET
    microversion_id: BTMicroversionId366 | Unset = UNSET
    node_id_to_referenced_property: BTExportModelBodiesResponse734NodeIdToReferencedProperty | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bodies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bodies, Unset):
            bodies = []
            for bodies_item_data in self.bodies:
                bodies_item = bodies_item_data.to_dict()
                bodies.append(bodies_item)

        bt_type = self.bt_type

        error_enum: str | Unset = UNSET
        if not isinstance(self.error_enum, Unset):
            error_enum = self.error_enum.value

        microversion_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_id, Unset):
            microversion_id = self.microversion_id.to_dict()

        node_id_to_referenced_property: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node_id_to_referenced_property, Unset):
            node_id_to_referenced_property = self.node_id_to_referenced_property.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bodies is not UNSET:
            field_dict["bodies"] = bodies
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if error_enum is not UNSET:
            field_dict["errorEnum"] = error_enum
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id
        if node_id_to_referenced_property is not UNSET:
            field_dict["nodeIdToReferencedProperty"] = node_id_to_referenced_property

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_export_model_bodies_response_734_node_id_to_referenced_property import (
            BTExportModelBodiesResponse734NodeIdToReferencedProperty,
        )
        from ..models.bt_export_model_body_1272 import BTExportModelBody1272
        from ..models.bt_microversion_id_366 import BTMicroversionId366

        d = dict(src_dict)
        _bodies = d.pop("bodies", UNSET)
        bodies: list[BTExportModelBody1272] | Unset = UNSET
        if _bodies is not UNSET:
            bodies = []
            for bodies_item_data in _bodies:
                bodies_item = BTExportModelBody1272.from_dict(bodies_item_data)

                bodies.append(bodies_item)

        bt_type = d.pop("btType", UNSET)

        _error_enum = d.pop("errorEnum", UNSET)
        error_enum: GBTErrorStringEnum | Unset
        if isinstance(_error_enum, Unset):
            error_enum = UNSET
        else:
            error_enum = GBTErrorStringEnum(_error_enum)

        _microversion_id = d.pop("microversionId", UNSET)
        microversion_id: BTMicroversionId366 | Unset
        if isinstance(_microversion_id, Unset):
            microversion_id = UNSET
        else:
            microversion_id = BTMicroversionId366.from_dict(_microversion_id)

        _node_id_to_referenced_property = d.pop("nodeIdToReferencedProperty", UNSET)
        node_id_to_referenced_property: BTExportModelBodiesResponse734NodeIdToReferencedProperty | Unset
        if isinstance(_node_id_to_referenced_property, Unset):
            node_id_to_referenced_property = UNSET
        else:
            node_id_to_referenced_property = BTExportModelBodiesResponse734NodeIdToReferencedProperty.from_dict(
                _node_id_to_referenced_property
            )

        bt_export_model_bodies_response_734 = cls(
            bodies=bodies,
            bt_type=bt_type,
            error_enum=error_enum,
            microversion_id=microversion_id,
            node_id_to_referenced_property=node_id_to_referenced_property,
        )

        bt_export_model_bodies_response_734.additional_properties = d
        return bt_export_model_bodies_response_734

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
