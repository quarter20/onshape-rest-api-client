from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_rbac_role_info import BTRbacRoleInfo


T = TypeVar("T", bound="Entry")


@_attrs_define
class Entry:
    """
    Attributes:
        permission_set (list[str] | Unset):
        role (BTRbacRoleInfo | Unset):
    """

    permission_set: list[str] | Unset = UNSET
    role: BTRbacRoleInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permission_set: list[str] | Unset = UNSET
        if not isinstance(self.permission_set, Unset):
            permission_set = self.permission_set

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permission_set is not UNSET:
            field_dict["permissionSet"] = permission_set
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_rbac_role_info import BTRbacRoleInfo

        d = dict(src_dict)
        permission_set = cast(list[str], d.pop("permissionSet", UNSET))

        _role = d.pop("role", UNSET)
        role: BTRbacRoleInfo | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = BTRbacRoleInfo.from_dict(_role)

        entry = cls(
            permission_set=permission_set,
            role=role,
        )

        entry.additional_properties = d
        return entry

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
