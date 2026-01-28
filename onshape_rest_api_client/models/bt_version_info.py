from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_thumbnail_info import BTThumbnailInfo
    from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo


T = TypeVar("T", bound="BTVersionInfo")


@_attrs_define
class BTVersionInfo:
    """
    Attributes:
        created_at (datetime.datetime | Unset):
        creator (BTUserBasicSummaryInfo | Unset):
        description (str | Unset):
        document_id (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        last_modifier (BTUserBasicSummaryInfo | Unset):
        metadata_workspace_id (str | Unset):
        microversion (str | Unset):
        modified_at (datetime.datetime | Unset):
        name (str | Unset): Name of the resource.
        override_date (datetime.datetime | Unset):
        parent (str | Unset):
        purpose (int | Unset):
        thumbnail (BTThumbnailInfo | Unset):
        type_ (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    created_at: datetime.datetime | Unset = UNSET
    creator: BTUserBasicSummaryInfo | Unset = UNSET
    description: str | Unset = UNSET
    document_id: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    last_modifier: BTUserBasicSummaryInfo | Unset = UNSET
    metadata_workspace_id: str | Unset = UNSET
    microversion: str | Unset = UNSET
    modified_at: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    override_date: datetime.datetime | Unset = UNSET
    parent: str | Unset = UNSET
    purpose: int | Unset = UNSET
    thumbnail: BTThumbnailInfo | Unset = UNSET
    type_: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        description = self.description

        document_id = self.document_id

        href = self.href

        id = self.id

        last_modifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_modifier, Unset):
            last_modifier = self.last_modifier.to_dict()

        metadata_workspace_id = self.metadata_workspace_id

        microversion = self.microversion

        modified_at: str | Unset = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        name = self.name

        override_date: str | Unset = UNSET
        if not isinstance(self.override_date, Unset):
            override_date = self.override_date.isoformat()

        parent = self.parent

        purpose = self.purpose

        thumbnail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail, Unset):
            thumbnail = self.thumbnail.to_dict()

        type_ = self.type_

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if creator is not UNSET:
            field_dict["creator"] = creator
        if description is not UNSET:
            field_dict["description"] = description
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if last_modifier is not UNSET:
            field_dict["lastModifier"] = last_modifier
        if metadata_workspace_id is not UNSET:
            field_dict["metadataWorkspaceId"] = metadata_workspace_id
        if microversion is not UNSET:
            field_dict["microversion"] = microversion
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if name is not UNSET:
            field_dict["name"] = name
        if override_date is not UNSET:
            field_dict["overrideDate"] = override_date
        if parent is not UNSET:
            field_dict["parent"] = parent
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if type_ is not UNSET:
            field_dict["type"] = type_
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_thumbnail_info import BTThumbnailInfo
        from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo

        d = dict(src_dict)
        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _creator = d.pop("creator", UNSET)
        creator: BTUserBasicSummaryInfo | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = BTUserBasicSummaryInfo.from_dict(_creator)

        description = d.pop("description", UNSET)

        document_id = d.pop("documentId", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _last_modifier = d.pop("lastModifier", UNSET)
        last_modifier: BTUserBasicSummaryInfo | Unset
        if isinstance(_last_modifier, Unset):
            last_modifier = UNSET
        else:
            last_modifier = BTUserBasicSummaryInfo.from_dict(_last_modifier)

        metadata_workspace_id = d.pop("metadataWorkspaceId", UNSET)

        microversion = d.pop("microversion", UNSET)

        _modified_at = d.pop("modifiedAt", UNSET)
        modified_at: datetime.datetime | Unset
        if isinstance(_modified_at, Unset):
            modified_at = UNSET
        else:
            modified_at = isoparse(_modified_at)

        name = d.pop("name", UNSET)

        _override_date = d.pop("overrideDate", UNSET)
        override_date: datetime.datetime | Unset
        if isinstance(_override_date, Unset):
            override_date = UNSET
        else:
            override_date = isoparse(_override_date)

        parent = d.pop("parent", UNSET)

        purpose = d.pop("purpose", UNSET)

        _thumbnail = d.pop("thumbnail", UNSET)
        thumbnail: BTThumbnailInfo | Unset
        if isinstance(_thumbnail, Unset):
            thumbnail = UNSET
        else:
            thumbnail = BTThumbnailInfo.from_dict(_thumbnail)

        type_ = d.pop("type", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_version_info = cls(
            created_at=created_at,
            creator=creator,
            description=description,
            document_id=document_id,
            href=href,
            id=id,
            last_modifier=last_modifier,
            metadata_workspace_id=metadata_workspace_id,
            microversion=microversion,
            modified_at=modified_at,
            name=name,
            override_date=override_date,
            parent=parent,
            purpose=purpose,
            thumbnail=thumbnail,
            type_=type_,
            view_ref=view_ref,
        )

        bt_version_info.additional_properties = d
        return bt_version_info

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
