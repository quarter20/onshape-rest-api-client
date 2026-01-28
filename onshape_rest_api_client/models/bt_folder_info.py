from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_element_library_summary_info import BTElementLibrarySummaryInfo
    from ..models.bt_owner_info import BTOwnerInfo
    from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo


T = TypeVar("T", bound="BTFolderInfo")


@_attrs_define
class BTFolderInfo:
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
        active (bool | Unset):
        can_unshare (bool | Unset):
        element_library_summary_info (list[BTElementLibrarySummaryInfo] | Unset):
        is_orphaned (bool | Unset):
        permission_set (list[str] | Unset):
        trash (bool | Unset):
        trashed_at (datetime.datetime | Unset):
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
    active: bool | Unset = UNSET
    can_unshare: bool | Unset = UNSET
    element_library_summary_info: list[BTElementLibrarySummaryInfo] | Unset = UNSET
    is_orphaned: bool | Unset = UNSET
    permission_set: list[str] | Unset = UNSET
    trash: bool | Unset = UNSET
    trashed_at: datetime.datetime | Unset = UNSET
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

        active = self.active

        can_unshare = self.can_unshare

        element_library_summary_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.element_library_summary_info, Unset):
            element_library_summary_info = []
            for element_library_summary_info_item_data in self.element_library_summary_info:
                element_library_summary_info_item = element_library_summary_info_item_data.to_dict()
                element_library_summary_info.append(element_library_summary_info_item)

        is_orphaned = self.is_orphaned

        permission_set: list[str] | Unset = UNSET
        if not isinstance(self.permission_set, Unset):
            permission_set = self.permission_set

        trash = self.trash

        trashed_at: str | Unset = UNSET
        if not isinstance(self.trashed_at, Unset):
            trashed_at = self.trashed_at.isoformat()

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
        if active is not UNSET:
            field_dict["active"] = active
        if can_unshare is not UNSET:
            field_dict["canUnshare"] = can_unshare
        if element_library_summary_info is not UNSET:
            field_dict["elementLibrarySummaryInfo"] = element_library_summary_info
        if is_orphaned is not UNSET:
            field_dict["isOrphaned"] = is_orphaned
        if permission_set is not UNSET:
            field_dict["permissionSet"] = permission_set
        if trash is not UNSET:
            field_dict["trash"] = trash
        if trashed_at is not UNSET:
            field_dict["trashedAt"] = trashed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_element_library_summary_info import BTElementLibrarySummaryInfo
        from ..models.bt_owner_info import BTOwnerInfo
        from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo

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

        active = d.pop("active", UNSET)

        can_unshare = d.pop("canUnshare", UNSET)

        _element_library_summary_info = d.pop("elementLibrarySummaryInfo", UNSET)
        element_library_summary_info: list[BTElementLibrarySummaryInfo] | Unset = UNSET
        if _element_library_summary_info is not UNSET:
            element_library_summary_info = []
            for element_library_summary_info_item_data in _element_library_summary_info:
                element_library_summary_info_item = BTElementLibrarySummaryInfo.from_dict(
                    element_library_summary_info_item_data
                )

                element_library_summary_info.append(element_library_summary_info_item)

        is_orphaned = d.pop("isOrphaned", UNSET)

        permission_set = cast(list[str], d.pop("permissionSet", UNSET))

        trash = d.pop("trash", UNSET)

        _trashed_at = d.pop("trashedAt", UNSET)
        trashed_at: datetime.datetime | Unset
        if isinstance(_trashed_at, Unset):
            trashed_at = UNSET
        else:
            trashed_at = isoparse(_trashed_at)

        bt_folder_info = cls(
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
            active=active,
            can_unshare=can_unshare,
            element_library_summary_info=element_library_summary_info,
            is_orphaned=is_orphaned,
            permission_set=permission_set,
            trash=trash,
            trashed_at=trashed_at,
        )

        bt_folder_info.additional_properties = d
        return bt_folder_info

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
