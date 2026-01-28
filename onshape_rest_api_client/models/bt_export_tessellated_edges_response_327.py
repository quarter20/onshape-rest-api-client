from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_error_string_enum import GBTErrorStringEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_export_tessellated_body_3398 import BTExportTessellatedBody3398


T = TypeVar("T", bound="BTExportTessellatedEdgesResponse327")


@_attrs_define
class BTExportTessellatedEdgesResponse327:
    """
    Attributes:
        bodies (list[BTExportTessellatedBody3398] | Unset):
        bt_type (str | Unset): Type of JSON object.
        error_enum (GBTErrorStringEnum | Unset):
    """

    bodies: list[BTExportTessellatedBody3398] | Unset = UNSET
    bt_type: str | Unset = UNSET
    error_enum: GBTErrorStringEnum | Unset = UNSET
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bodies is not UNSET:
            field_dict["bodies"] = bodies
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if error_enum is not UNSET:
            field_dict["errorEnum"] = error_enum

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_export_tessellated_body_3398 import BTExportTessellatedBody3398

        d = dict(src_dict)
        _bodies = d.pop("bodies", UNSET)
        bodies: list[BTExportTessellatedBody3398] | Unset = UNSET
        if _bodies is not UNSET:
            bodies = []
            for bodies_item_data in _bodies:
                bodies_item = BTExportTessellatedBody3398.from_dict(bodies_item_data)

                bodies.append(bodies_item)

        bt_type = d.pop("btType", UNSET)

        _error_enum = d.pop("errorEnum", UNSET)
        error_enum: GBTErrorStringEnum | Unset
        if isinstance(_error_enum, Unset):
            error_enum = UNSET
        else:
            error_enum = GBTErrorStringEnum(_error_enum)

        bt_export_tessellated_edges_response_327 = cls(
            bodies=bodies,
            bt_type=bt_type,
            error_enum=error_enum,
        )

        bt_export_tessellated_edges_response_327.additional_properties = d
        return bt_export_tessellated_edges_response_327

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
