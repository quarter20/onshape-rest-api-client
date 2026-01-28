from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_user_state import BTUserState
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAclEntryInfo")


@_attrs_define
class BTAclEntryInfo:
    """
    Attributes:
        accept_owner_transfer (bool | Unset):
        can_connection_user_edit (bool | Unset):
        company_name (str | Unset):
        connection_id (str | Unset):
        connection_name (str | Unset):
        connection_user (bool | Unset):
        email (str | Unset):
        enterprise_member (bool | Unset):
        entry_id (str | Unset):
        entry_state (BTUserState | Unset):
        entry_type (int | Unset):
        image (str | Unset):
        name (str | Unset):
        object_id (str | Unset):
        pending_owner_transfer (bool | Unset):
        permission (int | Unset):
        permission_set (list[str] | Unset):
        pro_company_subtype (int | Unset):
        team_name (str | Unset):
    """

    accept_owner_transfer: bool | Unset = UNSET
    can_connection_user_edit: bool | Unset = UNSET
    company_name: str | Unset = UNSET
    connection_id: str | Unset = UNSET
    connection_name: str | Unset = UNSET
    connection_user: bool | Unset = UNSET
    email: str | Unset = UNSET
    enterprise_member: bool | Unset = UNSET
    entry_id: str | Unset = UNSET
    entry_state: BTUserState | Unset = UNSET
    entry_type: int | Unset = UNSET
    image: str | Unset = UNSET
    name: str | Unset = UNSET
    object_id: str | Unset = UNSET
    pending_owner_transfer: bool | Unset = UNSET
    permission: int | Unset = UNSET
    permission_set: list[str] | Unset = UNSET
    pro_company_subtype: int | Unset = UNSET
    team_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accept_owner_transfer = self.accept_owner_transfer

        can_connection_user_edit = self.can_connection_user_edit

        company_name = self.company_name

        connection_id = self.connection_id

        connection_name = self.connection_name

        connection_user = self.connection_user

        email = self.email

        enterprise_member = self.enterprise_member

        entry_id = self.entry_id

        entry_state: str | Unset = UNSET
        if not isinstance(self.entry_state, Unset):
            entry_state = self.entry_state.value

        entry_type = self.entry_type

        image = self.image

        name = self.name

        object_id = self.object_id

        pending_owner_transfer = self.pending_owner_transfer

        permission = self.permission

        permission_set: list[str] | Unset = UNSET
        if not isinstance(self.permission_set, Unset):
            permission_set = self.permission_set

        pro_company_subtype = self.pro_company_subtype

        team_name = self.team_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accept_owner_transfer is not UNSET:
            field_dict["acceptOwnerTransfer"] = accept_owner_transfer
        if can_connection_user_edit is not UNSET:
            field_dict["canConnectionUserEdit"] = can_connection_user_edit
        if company_name is not UNSET:
            field_dict["companyName"] = company_name
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if connection_name is not UNSET:
            field_dict["connectionName"] = connection_name
        if connection_user is not UNSET:
            field_dict["connectionUser"] = connection_user
        if email is not UNSET:
            field_dict["email"] = email
        if enterprise_member is not UNSET:
            field_dict["enterpriseMember"] = enterprise_member
        if entry_id is not UNSET:
            field_dict["entryId"] = entry_id
        if entry_state is not UNSET:
            field_dict["entryState"] = entry_state
        if entry_type is not UNSET:
            field_dict["entryType"] = entry_type
        if image is not UNSET:
            field_dict["image"] = image
        if name is not UNSET:
            field_dict["name"] = name
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if pending_owner_transfer is not UNSET:
            field_dict["pendingOwnerTransfer"] = pending_owner_transfer
        if permission is not UNSET:
            field_dict["permission"] = permission
        if permission_set is not UNSET:
            field_dict["permissionSet"] = permission_set
        if pro_company_subtype is not UNSET:
            field_dict["proCompanySubtype"] = pro_company_subtype
        if team_name is not UNSET:
            field_dict["teamName"] = team_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accept_owner_transfer = d.pop("acceptOwnerTransfer", UNSET)

        can_connection_user_edit = d.pop("canConnectionUserEdit", UNSET)

        company_name = d.pop("companyName", UNSET)

        connection_id = d.pop("connectionId", UNSET)

        connection_name = d.pop("connectionName", UNSET)

        connection_user = d.pop("connectionUser", UNSET)

        email = d.pop("email", UNSET)

        enterprise_member = d.pop("enterpriseMember", UNSET)

        entry_id = d.pop("entryId", UNSET)

        _entry_state = d.pop("entryState", UNSET)
        entry_state: BTUserState | Unset
        if isinstance(_entry_state, Unset):
            entry_state = UNSET
        else:
            entry_state = BTUserState(_entry_state)

        entry_type = d.pop("entryType", UNSET)

        image = d.pop("image", UNSET)

        name = d.pop("name", UNSET)

        object_id = d.pop("objectId", UNSET)

        pending_owner_transfer = d.pop("pendingOwnerTransfer", UNSET)

        permission = d.pop("permission", UNSET)

        permission_set = cast(list[str], d.pop("permissionSet", UNSET))

        pro_company_subtype = d.pop("proCompanySubtype", UNSET)

        team_name = d.pop("teamName", UNSET)

        bt_acl_entry_info = cls(
            accept_owner_transfer=accept_owner_transfer,
            can_connection_user_edit=can_connection_user_edit,
            company_name=company_name,
            connection_id=connection_id,
            connection_name=connection_name,
            connection_user=connection_user,
            email=email,
            enterprise_member=enterprise_member,
            entry_id=entry_id,
            entry_state=entry_state,
            entry_type=entry_type,
            image=image,
            name=name,
            object_id=object_id,
            pending_owner_transfer=pending_owner_transfer,
            permission=permission,
            permission_set=permission_set,
            pro_company_subtype=pro_company_subtype,
            team_name=team_name,
        )

        bt_acl_entry_info.additional_properties = d
        return bt_acl_entry_info

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
