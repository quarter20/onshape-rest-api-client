from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_body_type import GBTBodyType
from ..models.gbt_mesh_state import GBTMeshState
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTClosedConstituentPartData2911")


@_attrs_define
class BTClosedConstituentPartData2911:
    """
    Attributes:
        body_type (GBTBodyType | Unset):
        bt_type (str | Unset): Type of JSON object.
        is_active_sheet_metal (bool | Unset):
        is_mesh (bool | Unset):
        mesh_state (GBTMeshState | Unset):
    """

    body_type: GBTBodyType | Unset = UNSET
    bt_type: str | Unset = UNSET
    is_active_sheet_metal: bool | Unset = UNSET
    is_mesh: bool | Unset = UNSET
    mesh_state: GBTMeshState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body_type: str | Unset = UNSET
        if not isinstance(self.body_type, Unset):
            body_type = self.body_type.value

        bt_type = self.bt_type

        is_active_sheet_metal = self.is_active_sheet_metal

        is_mesh = self.is_mesh

        mesh_state: str | Unset = UNSET
        if not isinstance(self.mesh_state, Unset):
            mesh_state = self.mesh_state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body_type is not UNSET:
            field_dict["bodyType"] = body_type
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if is_active_sheet_metal is not UNSET:
            field_dict["isActiveSheetMetal"] = is_active_sheet_metal
        if is_mesh is not UNSET:
            field_dict["isMesh"] = is_mesh
        if mesh_state is not UNSET:
            field_dict["meshState"] = mesh_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _body_type = d.pop("bodyType", UNSET)
        body_type: GBTBodyType | Unset
        if isinstance(_body_type, Unset):
            body_type = UNSET
        else:
            body_type = GBTBodyType(_body_type)

        bt_type = d.pop("btType", UNSET)

        is_active_sheet_metal = d.pop("isActiveSheetMetal", UNSET)

        is_mesh = d.pop("isMesh", UNSET)

        _mesh_state = d.pop("meshState", UNSET)
        mesh_state: GBTMeshState | Unset
        if isinstance(_mesh_state, Unset):
            mesh_state = UNSET
        else:
            mesh_state = GBTMeshState(_mesh_state)

        bt_closed_constituent_part_data_2911 = cls(
            body_type=body_type,
            bt_type=bt_type,
            is_active_sheet_metal=is_active_sheet_metal,
            is_mesh=is_mesh,
            mesh_state=mesh_state,
        )

        bt_closed_constituent_part_data_2911.additional_properties = d
        return bt_closed_constituent_part_data_2911

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
