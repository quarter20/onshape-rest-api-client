from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_owner_info import BTOwnerInfo
    from ..models.bt_rbac_permission_scheme_info import BTRbacPermissionSchemeInfo
    from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo
    from ..models.role_map_entry import RoleMapEntry


T = TypeVar("T", bound="BTProjectInfo")


@_attrs_define
class BTProjectInfo:
    """
    Attributes:
        json_type (str):
        can_move (bool | Unset):
        connection_name (str | Unset):
        connection_names (list[str] | Unset):
        created_at (datetime.datetime | Unset):
        created_by (BTUserBasicSummaryInfo | Unset):
        description (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        is_container (bool | Unset):
        is_enterprise_owned (bool | Unset):
        is_external_connection_resource (bool | Unset):
        is_mutable (bool | Unset):
        modified_at (datetime.datetime | Unset):
        modified_by (BTUserBasicSummaryInfo | Unset):
        name (str | Unset): Name of the resource.
        owner (BTOwnerInfo | Unset):
        parent_id (str | Unset):
        project_id (str | Unset):
        resource_type (str | Unset):
        tree_href (str | Unset):
        unparent_href (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        permission_scheme (BTRbacPermissionSchemeInfo | Unset):
        permission_set (list[str] | Unset):
        role_map_entries (list[RoleMapEntry] | Unset):
        trash (bool | Unset):
    """

    json_type: str
    can_move: bool | Unset = UNSET
    connection_name: str | Unset = UNSET
    connection_names: list[str] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by: BTUserBasicSummaryInfo | Unset = UNSET
    description: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    is_container: bool | Unset = UNSET
    is_enterprise_owned: bool | Unset = UNSET
    is_external_connection_resource: bool | Unset = UNSET
    is_mutable: bool | Unset = UNSET
    modified_at: datetime.datetime | Unset = UNSET
    modified_by: BTUserBasicSummaryInfo | Unset = UNSET
    name: str | Unset = UNSET
    owner: BTOwnerInfo | Unset = UNSET
    parent_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    resource_type: str | Unset = UNSET
    tree_href: str | Unset = UNSET
    unparent_href: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    permission_scheme: BTRbacPermissionSchemeInfo | Unset = UNSET
    permission_set: list[str] | Unset = UNSET
    role_map_entries: list[RoleMapEntry] | Unset = UNSET
    trash: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        json_type = self.json_type

        can_move = self.can_move

        connection_name = self.connection_name

        connection_names: list[str] | Unset = UNSET
        if not isinstance(self.connection_names, Unset):
            connection_names = self.connection_names

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        description = self.description

        href = self.href

        id = self.id

        is_container = self.is_container

        is_enterprise_owned = self.is_enterprise_owned

        is_external_connection_resource = self.is_external_connection_resource

        is_mutable = self.is_mutable

        modified_at: str | Unset = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        modified_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.modified_by, Unset):
            modified_by = self.modified_by.to_dict()

        name = self.name

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        parent_id = self.parent_id

        project_id = self.project_id

        resource_type = self.resource_type

        tree_href = self.tree_href

        unparent_href = self.unparent_href

        view_ref = self.view_ref

        permission_scheme: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permission_scheme, Unset):
            permission_scheme = self.permission_scheme.to_dict()

        permission_set: list[str] | Unset = UNSET
        if not isinstance(self.permission_set, Unset):
            permission_set = self.permission_set

        role_map_entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.role_map_entries, Unset):
            role_map_entries = []
            for role_map_entries_item_data in self.role_map_entries:
                role_map_entries_item = role_map_entries_item_data.to_dict()
                role_map_entries.append(role_map_entries_item)

        trash = self.trash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jsonType": json_type,
            }
        )
        if can_move is not UNSET:
            field_dict["canMove"] = can_move
        if connection_name is not UNSET:
            field_dict["connectionName"] = connection_name
        if connection_names is not UNSET:
            field_dict["connectionNames"] = connection_names
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if is_container is not UNSET:
            field_dict["isContainer"] = is_container
        if is_enterprise_owned is not UNSET:
            field_dict["isEnterpriseOwned"] = is_enterprise_owned
        if is_external_connection_resource is not UNSET:
            field_dict["isExternalConnectionResource"] = is_external_connection_resource
        if is_mutable is not UNSET:
            field_dict["isMutable"] = is_mutable
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if name is not UNSET:
            field_dict["name"] = name
        if owner is not UNSET:
            field_dict["owner"] = owner
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if tree_href is not UNSET:
            field_dict["treeHref"] = tree_href
        if unparent_href is not UNSET:
            field_dict["unparentHref"] = unparent_href
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if permission_scheme is not UNSET:
            field_dict["permissionScheme"] = permission_scheme
        if permission_set is not UNSET:
            field_dict["permissionSet"] = permission_set
        if role_map_entries is not UNSET:
            field_dict["roleMapEntries"] = role_map_entries
        if trash is not UNSET:
            field_dict["trash"] = trash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_owner_info import BTOwnerInfo
        from ..models.bt_rbac_permission_scheme_info import BTRbacPermissionSchemeInfo
        from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo
        from ..models.role_map_entry import RoleMapEntry

        d = dict(src_dict)
        json_type = d.pop("jsonType")

        can_move = d.pop("canMove", UNSET)

        connection_name = d.pop("connectionName", UNSET)

        connection_names = cast(list[str], d.pop("connectionNames", UNSET))

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _created_by = d.pop("createdBy", UNSET)
        created_by: BTUserBasicSummaryInfo | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = BTUserBasicSummaryInfo.from_dict(_created_by)

        description = d.pop("description", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        is_container = d.pop("isContainer", UNSET)

        is_enterprise_owned = d.pop("isEnterpriseOwned", UNSET)

        is_external_connection_resource = d.pop("isExternalConnectionResource", UNSET)

        is_mutable = d.pop("isMutable", UNSET)

        _modified_at = d.pop("modifiedAt", UNSET)
        modified_at: datetime.datetime | Unset
        if isinstance(_modified_at, Unset):
            modified_at = UNSET
        else:
            modified_at = isoparse(_modified_at)

        _modified_by = d.pop("modifiedBy", UNSET)
        modified_by: BTUserBasicSummaryInfo | Unset
        if isinstance(_modified_by, Unset):
            modified_by = UNSET
        else:
            modified_by = BTUserBasicSummaryInfo.from_dict(_modified_by)

        name = d.pop("name", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: BTOwnerInfo | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = BTOwnerInfo.from_dict(_owner)

        parent_id = d.pop("parentId", UNSET)

        project_id = d.pop("projectId", UNSET)

        resource_type = d.pop("resourceType", UNSET)

        tree_href = d.pop("treeHref", UNSET)

        unparent_href = d.pop("unparentHref", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        _permission_scheme = d.pop("permissionScheme", UNSET)
        permission_scheme: BTRbacPermissionSchemeInfo | Unset
        if isinstance(_permission_scheme, Unset):
            permission_scheme = UNSET
        else:
            permission_scheme = BTRbacPermissionSchemeInfo.from_dict(_permission_scheme)

        permission_set = cast(list[str], d.pop("permissionSet", UNSET))

        _role_map_entries = d.pop("roleMapEntries", UNSET)
        role_map_entries: list[RoleMapEntry] | Unset = UNSET
        if _role_map_entries is not UNSET:
            role_map_entries = []
            for role_map_entries_item_data in _role_map_entries:
                role_map_entries_item = RoleMapEntry.from_dict(role_map_entries_item_data)

                role_map_entries.append(role_map_entries_item)

        trash = d.pop("trash", UNSET)

        bt_project_info = cls(
            json_type=json_type,
            can_move=can_move,
            connection_name=connection_name,
            connection_names=connection_names,
            created_at=created_at,
            created_by=created_by,
            description=description,
            href=href,
            id=id,
            is_container=is_container,
            is_enterprise_owned=is_enterprise_owned,
            is_external_connection_resource=is_external_connection_resource,
            is_mutable=is_mutable,
            modified_at=modified_at,
            modified_by=modified_by,
            name=name,
            owner=owner,
            parent_id=parent_id,
            project_id=project_id,
            resource_type=resource_type,
            tree_href=tree_href,
            unparent_href=unparent_href,
            view_ref=view_ref,
            permission_scheme=permission_scheme,
            permission_set=permission_set,
            role_map_entries=role_map_entries,
            trash=trash,
        )

        bt_project_info.additional_properties = d
        return bt_project_info

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
