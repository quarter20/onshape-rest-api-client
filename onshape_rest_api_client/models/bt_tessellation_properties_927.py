from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTTessellationProperties927")


@_attrs_define
class BTTessellationProperties927:
    """
    Attributes:
        angular_tolerance (float | Unset):
        bt_type (str | Unset): Type of JSON object.
        chordal_tolerance (float | Unset):
        node_id (str | Unset):
        tessellation_budget (int | Unset):
    """

    angular_tolerance: float | Unset = UNSET
    bt_type: str | Unset = UNSET
    chordal_tolerance: float | Unset = UNSET
    node_id: str | Unset = UNSET
    tessellation_budget: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        angular_tolerance = self.angular_tolerance

        bt_type = self.bt_type

        chordal_tolerance = self.chordal_tolerance

        node_id = self.node_id

        tessellation_budget = self.tessellation_budget

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if angular_tolerance is not UNSET:
            field_dict["angularTolerance"] = angular_tolerance
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if chordal_tolerance is not UNSET:
            field_dict["chordalTolerance"] = chordal_tolerance
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if tessellation_budget is not UNSET:
            field_dict["tessellationBudget"] = tessellation_budget

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        angular_tolerance = d.pop("angularTolerance", UNSET)

        bt_type = d.pop("btType", UNSET)

        chordal_tolerance = d.pop("chordalTolerance", UNSET)

        node_id = d.pop("nodeId", UNSET)

        tessellation_budget = d.pop("tessellationBudget", UNSET)

        bt_tessellation_properties_927 = cls(
            angular_tolerance=angular_tolerance,
            bt_type=bt_type,
            chordal_tolerance=chordal_tolerance,
            node_id=node_id,
            tessellation_budget=tessellation_budget,
        )

        bt_tessellation_properties_927.additional_properties = d
        return bt_tessellation_properties_927

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
