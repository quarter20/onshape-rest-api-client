from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_identity_info import BTIdentityInfo
    from ..models.bt_rbac_role_info import BTRbacRoleInfo


T = TypeVar("T", bound="RoleMapEntry")


@_attrs_define
class RoleMapEntry:
    """
    Attributes:
        identities (list[BTIdentityInfo] | Unset):
        role (BTRbacRoleInfo | Unset):
    """

    identities: list[BTIdentityInfo] | Unset = UNSET
    role: BTRbacRoleInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identities, Unset):
            identities = []
            for identities_item_data in self.identities:
                identities_item = identities_item_data.to_dict()
                identities.append(identities_item)

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identities is not UNSET:
            field_dict["identities"] = identities
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_identity_info import BTIdentityInfo
        from ..models.bt_rbac_role_info import BTRbacRoleInfo

        d = dict(src_dict)
        _identities = d.pop("identities", UNSET)
        identities: list[BTIdentityInfo] | Unset = UNSET
        if _identities is not UNSET:
            identities = []
            for identities_item_data in _identities:
                identities_item = BTIdentityInfo.from_dict(identities_item_data)

                identities.append(identities_item)

        _role = d.pop("role", UNSET)
        role: BTRbacRoleInfo | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = BTRbacRoleInfo.from_dict(_role)

        role_map_entry = cls(
            identities=identities,
            role=role,
        )

        role_map_entry.additional_properties = d
        return role_map_entry

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
