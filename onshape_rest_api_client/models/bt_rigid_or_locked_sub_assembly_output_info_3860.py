from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_microversion_id_366 import BTMicroversionId366


T = TypeVar("T", bound="BTRigidOrLockedSubAssemblyOutputInfo3860")


@_attrs_define
class BTRigidOrLockedSubAssemblyOutputInfo3860:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        locked (bool | Unset):
        rigid (bool | Unset):
        synced_output_mvid (BTMicroversionId366 | Unset):
    """

    bt_type: str | Unset = UNSET
    locked: bool | Unset = UNSET
    rigid: bool | Unset = UNSET
    synced_output_mvid: BTMicroversionId366 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        locked = self.locked

        rigid = self.rigid

        synced_output_mvid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.synced_output_mvid, Unset):
            synced_output_mvid = self.synced_output_mvid.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if locked is not UNSET:
            field_dict["locked"] = locked
        if rigid is not UNSET:
            field_dict["rigid"] = rigid
        if synced_output_mvid is not UNSET:
            field_dict["syncedOutputMVID"] = synced_output_mvid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_microversion_id_366 import BTMicroversionId366

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        locked = d.pop("locked", UNSET)

        rigid = d.pop("rigid", UNSET)

        _synced_output_mvid = d.pop("syncedOutputMVID", UNSET)
        synced_output_mvid: BTMicroversionId366 | Unset
        if isinstance(_synced_output_mvid, Unset):
            synced_output_mvid = UNSET
        else:
            synced_output_mvid = BTMicroversionId366.from_dict(_synced_output_mvid)

        bt_rigid_or_locked_sub_assembly_output_info_3860 = cls(
            bt_type=bt_type,
            locked=locked,
            rigid=rigid,
            synced_output_mvid=synced_output_mvid,
        )

        bt_rigid_or_locked_sub_assembly_output_info_3860.additional_properties = d
        return bt_rigid_or_locked_sub_assembly_output_info_3860

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
