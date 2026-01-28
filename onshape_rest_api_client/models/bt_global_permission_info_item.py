from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_identity_info import BTIdentityInfo


T = TypeVar("T", bound="BTGlobalPermissionInfoItem")


@_attrs_define
class BTGlobalPermissionInfoItem:
    """
    Attributes:
        code (int | Unset):
        identities (list[BTIdentityInfo] | Unset):
    """

    code: int | Unset = UNSET
    identities: list[BTIdentityInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        identities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identities, Unset):
            identities = []
            for identities_item_data in self.identities:
                identities_item = identities_item_data.to_dict()
                identities.append(identities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if identities is not UNSET:
            field_dict["identities"] = identities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_identity_info import BTIdentityInfo

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        _identities = d.pop("identities", UNSET)
        identities: list[BTIdentityInfo] | Unset = UNSET
        if _identities is not UNSET:
            identities = []
            for identities_item_data in _identities:
                identities_item = BTIdentityInfo.from_dict(identities_item_data)

                identities.append(identities_item)

        bt_global_permission_info_item = cls(
            code=code,
            identities=identities,
        )

        bt_global_permission_info_item.additional_properties = d
        return bt_global_permission_info_item

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
