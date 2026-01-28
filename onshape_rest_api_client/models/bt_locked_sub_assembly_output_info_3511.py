from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_error_string_enum import GBTErrorStringEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_locked_sub_assembly_4590 import BTLockedSubAssembly4590
    from ..models.bt_microversion_id_366 import BTMicroversionId366


T = TypeVar("T", bound="BTLockedSubAssemblyOutputInfo3511")


@_attrs_define
class BTLockedSubAssemblyOutputInfo3511:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        locked (bool | Unset):
        rigid (bool | Unset):
        synced_output_mvid (BTMicroversionId366 | Unset):
        lock_info (BTLockedSubAssembly4590 | Unset):
        sync_error (GBTErrorStringEnum | Unset):
    """

    bt_type: str | Unset = UNSET
    locked: bool | Unset = UNSET
    rigid: bool | Unset = UNSET
    synced_output_mvid: BTMicroversionId366 | Unset = UNSET
    lock_info: BTLockedSubAssembly4590 | Unset = UNSET
    sync_error: GBTErrorStringEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        locked = self.locked

        rigid = self.rigid

        synced_output_mvid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.synced_output_mvid, Unset):
            synced_output_mvid = self.synced_output_mvid.to_dict()

        lock_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lock_info, Unset):
            lock_info = self.lock_info.to_dict()

        sync_error: str | Unset = UNSET
        if not isinstance(self.sync_error, Unset):
            sync_error = self.sync_error.value

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
        if lock_info is not UNSET:
            field_dict["lockInfo"] = lock_info
        if sync_error is not UNSET:
            field_dict["syncError"] = sync_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_locked_sub_assembly_4590 import BTLockedSubAssembly4590
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

        _lock_info = d.pop("lockInfo", UNSET)
        lock_info: BTLockedSubAssembly4590 | Unset
        if isinstance(_lock_info, Unset):
            lock_info = UNSET
        else:
            lock_info = BTLockedSubAssembly4590.from_dict(_lock_info)

        _sync_error = d.pop("syncError", UNSET)
        sync_error: GBTErrorStringEnum | Unset
        if isinstance(_sync_error, Unset):
            sync_error = UNSET
        else:
            sync_error = GBTErrorStringEnum(_sync_error)

        bt_locked_sub_assembly_output_info_3511 = cls(
            bt_type=bt_type,
            locked=locked,
            rigid=rigid,
            synced_output_mvid=synced_output_mvid,
            lock_info=lock_info,
            sync_error=sync_error,
        )

        bt_locked_sub_assembly_output_info_3511.additional_properties = d
        return bt_locked_sub_assembly_output_info_3511

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
