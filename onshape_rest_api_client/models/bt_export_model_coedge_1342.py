from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTExportModelCoedge1342")


@_attrs_define
class BTExportModelCoedge1342:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        edge_id (str | Unset):
        orientation (bool | Unset):
    """

    bt_type: str | Unset = UNSET
    edge_id: str | Unset = UNSET
    orientation: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        edge_id = self.edge_id

        orientation = self.orientation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if edge_id is not UNSET:
            field_dict["edgeId"] = edge_id
        if orientation is not UNSET:
            field_dict["orientation"] = orientation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        edge_id = d.pop("edgeId", UNSET)

        orientation = d.pop("orientation", UNSET)

        bt_export_model_coedge_1342 = cls(
            bt_type=bt_type,
            edge_id=edge_id,
            orientation=orientation,
        )

        bt_export_model_coedge_1342.additional_properties = d
        return bt_export_model_coedge_1342

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
