from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTPartsExportFilter4308")


@_attrs_define
class BTPartsExportFilter4308:
    """Skip mesh/curve foreign data creation in individual parts export

    Attributes:
        bt_type (str | Unset): Type of JSON object.
        skip_all_mesh (bool | Unset):
        skip_curves (bool | Unset):
        skip_partial_mesh (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    skip_all_mesh: bool | Unset = UNSET
    skip_curves: bool | Unset = UNSET
    skip_partial_mesh: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        skip_all_mesh = self.skip_all_mesh

        skip_curves = self.skip_curves

        skip_partial_mesh = self.skip_partial_mesh

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if skip_all_mesh is not UNSET:
            field_dict["skipAllMesh"] = skip_all_mesh
        if skip_curves is not UNSET:
            field_dict["skipCurves"] = skip_curves
        if skip_partial_mesh is not UNSET:
            field_dict["skipPartialMesh"] = skip_partial_mesh

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        skip_all_mesh = d.pop("skipAllMesh", UNSET)

        skip_curves = d.pop("skipCurves", UNSET)

        skip_partial_mesh = d.pop("skipPartialMesh", UNSET)

        bt_parts_export_filter_4308 = cls(
            bt_type=bt_type,
            skip_all_mesh=skip_all_mesh,
            skip_curves=skip_curves,
            skip_partial_mesh=skip_partial_mesh,
        )

        bt_parts_export_filter_4308.additional_properties = d
        return bt_parts_export_filter_4308

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
