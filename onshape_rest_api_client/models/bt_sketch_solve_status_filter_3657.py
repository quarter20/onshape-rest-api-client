from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbtm_geom_status import GBTMGeomStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTSketchSolveStatusFilter3657")


@_attrs_define
class BTSketchSolveStatusFilter3657:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        solve_status (GBTMGeomStatus | Unset):
    """

    bt_type: str | Unset = UNSET
    solve_status: GBTMGeomStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        solve_status: str | Unset = UNSET
        if not isinstance(self.solve_status, Unset):
            solve_status = self.solve_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if solve_status is not UNSET:
            field_dict["solveStatus"] = solve_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _solve_status = d.pop("solveStatus", UNSET)
        solve_status: GBTMGeomStatus | Unset
        if isinstance(_solve_status, Unset):
            solve_status = UNSET
        else:
            solve_status = GBTMGeomStatus(_solve_status)

        bt_sketch_solve_status_filter_3657 = cls(
            bt_type=bt_type,
            solve_status=solve_status,
        )

        bt_sketch_solve_status_filter_3657.additional_properties = d
        return bt_sketch_solve_status_filter_3657

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
