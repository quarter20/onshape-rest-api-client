from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_sub_assembly_lock_type import GBTSubAssemblyLockType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_rigid_or_locked_sub_assembly_output_info_3860 import BTRigidOrLockedSubAssemblyOutputInfo3860


T = TypeVar("T", bound="BTLockedAtCurrentPosition4006")


@_attrs_define
class BTLockedAtCurrentPosition4006:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        lock_type (GBTSubAssemblyLockType | Unset):
        locked_sub_assembly_output_info (BTRigidOrLockedSubAssemblyOutputInfo3860 | Unset):
    """

    bt_type: str | Unset = UNSET
    lock_type: GBTSubAssemblyLockType | Unset = UNSET
    locked_sub_assembly_output_info: BTRigidOrLockedSubAssemblyOutputInfo3860 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        lock_type: str | Unset = UNSET
        if not isinstance(self.lock_type, Unset):
            lock_type = self.lock_type.value

        locked_sub_assembly_output_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.locked_sub_assembly_output_info, Unset):
            locked_sub_assembly_output_info = self.locked_sub_assembly_output_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if lock_type is not UNSET:
            field_dict["lockType"] = lock_type
        if locked_sub_assembly_output_info is not UNSET:
            field_dict["lockedSubAssemblyOutputInfo"] = locked_sub_assembly_output_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_rigid_or_locked_sub_assembly_output_info_3860 import BTRigidOrLockedSubAssemblyOutputInfo3860

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        _lock_type = d.pop("lockType", UNSET)
        lock_type: GBTSubAssemblyLockType | Unset
        if isinstance(_lock_type, Unset):
            lock_type = UNSET
        else:
            lock_type = GBTSubAssemblyLockType(_lock_type)

        _locked_sub_assembly_output_info = d.pop("lockedSubAssemblyOutputInfo", UNSET)
        locked_sub_assembly_output_info: BTRigidOrLockedSubAssemblyOutputInfo3860 | Unset
        if isinstance(_locked_sub_assembly_output_info, Unset):
            locked_sub_assembly_output_info = UNSET
        else:
            locked_sub_assembly_output_info = BTRigidOrLockedSubAssemblyOutputInfo3860.from_dict(
                _locked_sub_assembly_output_info
            )

        bt_locked_at_current_position_4006 = cls(
            bt_type=bt_type,
            lock_type=lock_type,
            locked_sub_assembly_output_info=locked_sub_assembly_output_info,
        )

        bt_locked_at_current_position_4006.additional_properties = d
        return bt_locked_at_current_position_4006

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
