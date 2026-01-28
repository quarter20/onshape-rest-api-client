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
    from ..models.bt_thumbnail_info import BTThumbnailInfo
    from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo


T = TypeVar("T", bound="BTCloudStorageObjectInfo")


@_attrs_define
class BTCloudStorageObjectInfo:
    """
    Attributes:
        can_move (bool | Unset):
        cloud_storage_account_id (str | Unset):
        cloud_storage_object_id (str | Unset):
        cloud_storage_provider (int | Unset):
        connection_name (str | Unset):
        connection_names (list[str] | Unset):
        created_at (datetime.datetime | Unset):
        created_by (BTUserBasicSummaryInfo | Unset):
        created_by_id (str | Unset):
        description (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        icon_link (str | Unset):
        id (str | Unset): Id of the resource.
        is_container (bool | Unset):
        is_enterprise_owned (bool | Unset):
        is_external_connection_resource (bool | Unset):
        is_mutable (bool | Unset):
        mime_type (str | Unset):
        modified_at (datetime.datetime | Unset):
        modified_by (BTUserBasicSummaryInfo | Unset):
        modified_by_id (str | Unset):
        name (str | Unset): Name of the resource.
        owner (BTOwnerInfo | Unset):
        parent_id (str | Unset):
        project_id (str | Unset):
        resource_type (str | Unset):
        size_bytes (int | Unset):
        thumbnail_info (BTThumbnailInfo | Unset):
        tree_href (str | Unset):
        unparent_href (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        web_view_link (str | Unset):
    """

    can_move: bool | Unset = UNSET
    cloud_storage_account_id: str | Unset = UNSET
    cloud_storage_object_id: str | Unset = UNSET
    cloud_storage_provider: int | Unset = UNSET
    connection_name: str | Unset = UNSET
    connection_names: list[str] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    created_by: BTUserBasicSummaryInfo | Unset = UNSET
    created_by_id: str | Unset = UNSET
    description: str | Unset = UNSET
    href: str | Unset = UNSET
    icon_link: str | Unset = UNSET
    id: str | Unset = UNSET
    is_container: bool | Unset = UNSET
    is_enterprise_owned: bool | Unset = UNSET
    is_external_connection_resource: bool | Unset = UNSET
    is_mutable: bool | Unset = UNSET
    mime_type: str | Unset = UNSET
    modified_at: datetime.datetime | Unset = UNSET
    modified_by: BTUserBasicSummaryInfo | Unset = UNSET
    modified_by_id: str | Unset = UNSET
    name: str | Unset = UNSET
    owner: BTOwnerInfo | Unset = UNSET
    parent_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    resource_type: str | Unset = UNSET
    size_bytes: int | Unset = UNSET
    thumbnail_info: BTThumbnailInfo | Unset = UNSET
    tree_href: str | Unset = UNSET
    unparent_href: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    web_view_link: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_move = self.can_move

        cloud_storage_account_id = self.cloud_storage_account_id

        cloud_storage_object_id = self.cloud_storage_object_id

        cloud_storage_provider = self.cloud_storage_provider

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

        created_by_id = self.created_by_id

        description = self.description

        href = self.href

        icon_link = self.icon_link

        id = self.id

        is_container = self.is_container

        is_enterprise_owned = self.is_enterprise_owned

        is_external_connection_resource = self.is_external_connection_resource

        is_mutable = self.is_mutable

        mime_type = self.mime_type

        modified_at: str | Unset = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        modified_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.modified_by, Unset):
            modified_by = self.modified_by.to_dict()

        modified_by_id = self.modified_by_id

        name = self.name

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        parent_id = self.parent_id

        project_id = self.project_id

        resource_type = self.resource_type

        size_bytes = self.size_bytes

        thumbnail_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail_info, Unset):
            thumbnail_info = self.thumbnail_info.to_dict()

        tree_href = self.tree_href

        unparent_href = self.unparent_href

        view_ref = self.view_ref

        web_view_link = self.web_view_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_move is not UNSET:
            field_dict["canMove"] = can_move
        if cloud_storage_account_id is not UNSET:
            field_dict["cloudStorageAccountId"] = cloud_storage_account_id
        if cloud_storage_object_id is not UNSET:
            field_dict["cloudStorageObjectId"] = cloud_storage_object_id
        if cloud_storage_provider is not UNSET:
            field_dict["cloudStorageProvider"] = cloud_storage_provider
        if connection_name is not UNSET:
            field_dict["connectionName"] = connection_name
        if connection_names is not UNSET:
            field_dict["connectionNames"] = connection_names
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_id is not UNSET:
            field_dict["createdById"] = created_by_id
        if description is not UNSET:
            field_dict["description"] = description
        if href is not UNSET:
            field_dict["href"] = href
        if icon_link is not UNSET:
            field_dict["iconLink"] = icon_link
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
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if modified_by_id is not UNSET:
            field_dict["modifiedById"] = modified_by_id
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
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if thumbnail_info is not UNSET:
            field_dict["thumbnailInfo"] = thumbnail_info
        if tree_href is not UNSET:
            field_dict["treeHref"] = tree_href
        if unparent_href is not UNSET:
            field_dict["unparentHref"] = unparent_href
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if web_view_link is not UNSET:
            field_dict["webViewLink"] = web_view_link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_owner_info import BTOwnerInfo
        from ..models.bt_thumbnail_info import BTThumbnailInfo
        from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo

        d = dict(src_dict)
        can_move = d.pop("canMove", UNSET)

        cloud_storage_account_id = d.pop("cloudStorageAccountId", UNSET)

        cloud_storage_object_id = d.pop("cloudStorageObjectId", UNSET)

        cloud_storage_provider = d.pop("cloudStorageProvider", UNSET)

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

        created_by_id = d.pop("createdById", UNSET)

        description = d.pop("description", UNSET)

        href = d.pop("href", UNSET)

        icon_link = d.pop("iconLink", UNSET)

        id = d.pop("id", UNSET)

        is_container = d.pop("isContainer", UNSET)

        is_enterprise_owned = d.pop("isEnterpriseOwned", UNSET)

        is_external_connection_resource = d.pop("isExternalConnectionResource", UNSET)

        is_mutable = d.pop("isMutable", UNSET)

        mime_type = d.pop("mimeType", UNSET)

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

        modified_by_id = d.pop("modifiedById", UNSET)

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

        size_bytes = d.pop("sizeBytes", UNSET)

        _thumbnail_info = d.pop("thumbnailInfo", UNSET)
        thumbnail_info: BTThumbnailInfo | Unset
        if isinstance(_thumbnail_info, Unset):
            thumbnail_info = UNSET
        else:
            thumbnail_info = BTThumbnailInfo.from_dict(_thumbnail_info)

        tree_href = d.pop("treeHref", UNSET)

        unparent_href = d.pop("unparentHref", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        web_view_link = d.pop("webViewLink", UNSET)

        bt_cloud_storage_object_info = cls(
            can_move=can_move,
            cloud_storage_account_id=cloud_storage_account_id,
            cloud_storage_object_id=cloud_storage_object_id,
            cloud_storage_provider=cloud_storage_provider,
            connection_name=connection_name,
            connection_names=connection_names,
            created_at=created_at,
            created_by=created_by,
            created_by_id=created_by_id,
            description=description,
            href=href,
            icon_link=icon_link,
            id=id,
            is_container=is_container,
            is_enterprise_owned=is_enterprise_owned,
            is_external_connection_resource=is_external_connection_resource,
            is_mutable=is_mutable,
            mime_type=mime_type,
            modified_at=modified_at,
            modified_by=modified_by,
            modified_by_id=modified_by_id,
            name=name,
            owner=owner,
            parent_id=parent_id,
            project_id=project_id,
            resource_type=resource_type,
            size_bytes=size_bytes,
            thumbnail_info=thumbnail_info,
            tree_href=tree_href,
            unparent_href=unparent_href,
            view_ref=view_ref,
            web_view_link=web_view_link,
        )

        bt_cloud_storage_object_info.additional_properties = d
        return bt_cloud_storage_object_info

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
