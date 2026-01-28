from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.bt_object_state import BTObjectState
from ..models.bt_workspace_protection_rule_options import BTWorkspaceProtectionRuleOptions
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_thumbnail_info import BTThumbnailInfo
    from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo
    from ..models.bt_version_info import BTVersionInfo


T = TypeVar("T", bound="BTWorkspaceInfo")


@_attrs_define
class BTWorkspaceInfo:
    """
    Attributes:
        can_delete (bool | Unset):
        created_at (datetime.datetime | Unset):
        creator (BTUserBasicSummaryInfo | Unset):
        description (str | Unset):
        document_id (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        is_read_only (bool | Unset):
        last_modifier (BTUserBasicSummaryInfo | Unset):
        microversion (str | Unset):
        modified_at (datetime.datetime | Unset):
        name (str | Unset): Name of the resource.
        override_date (datetime.datetime | Unset):
        parent (str | Unset):
        parents (list[BTVersionInfo] | Unset):
        protection_rule (BTWorkspaceProtectionRuleOptions | Unset):
        state (BTObjectState | Unset):
        thumbnail (BTThumbnailInfo | Unset):
        type_ (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    can_delete: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    creator: BTUserBasicSummaryInfo | Unset = UNSET
    description: str | Unset = UNSET
    document_id: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    is_read_only: bool | Unset = UNSET
    last_modifier: BTUserBasicSummaryInfo | Unset = UNSET
    microversion: str | Unset = UNSET
    modified_at: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    override_date: datetime.datetime | Unset = UNSET
    parent: str | Unset = UNSET
    parents: list[BTVersionInfo] | Unset = UNSET
    protection_rule: BTWorkspaceProtectionRuleOptions | Unset = UNSET
    state: BTObjectState | Unset = UNSET
    thumbnail: BTThumbnailInfo | Unset = UNSET
    type_: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_delete = self.can_delete

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

        is_read_only = self.is_read_only

        last_modifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_modifier, Unset):
            last_modifier = self.last_modifier.to_dict()

        microversion = self.microversion

        modified_at: str | Unset = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        name = self.name

        override_date: str | Unset = UNSET
        if not isinstance(self.override_date, Unset):
            override_date = self.override_date.isoformat()

        parent = self.parent

        parents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parents, Unset):
            parents = []
            for parents_item_data in self.parents:
                parents_item = parents_item_data.to_dict()
                parents.append(parents_item)

        protection_rule: str | Unset = UNSET
        if not isinstance(self.protection_rule, Unset):
            protection_rule = self.protection_rule.value

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        thumbnail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail, Unset):
            thumbnail = self.thumbnail.to_dict()

        type_ = self.type_

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_delete is not UNSET:
            field_dict["canDelete"] = can_delete
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
        if is_read_only is not UNSET:
            field_dict["isReadOnly"] = is_read_only
        if last_modifier is not UNSET:
            field_dict["lastModifier"] = last_modifier
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
        if parents is not UNSET:
            field_dict["parents"] = parents
        if protection_rule is not UNSET:
            field_dict["protectionRule"] = protection_rule
        if state is not UNSET:
            field_dict["state"] = state
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
        from ..models.bt_version_info import BTVersionInfo

        d = dict(src_dict)
        can_delete = d.pop("canDelete", UNSET)

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

        is_read_only = d.pop("isReadOnly", UNSET)

        _last_modifier = d.pop("lastModifier", UNSET)
        last_modifier: BTUserBasicSummaryInfo | Unset
        if isinstance(_last_modifier, Unset):
            last_modifier = UNSET
        else:
            last_modifier = BTUserBasicSummaryInfo.from_dict(_last_modifier)

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

        _parents = d.pop("parents", UNSET)
        parents: list[BTVersionInfo] | Unset = UNSET
        if _parents is not UNSET:
            parents = []
            for parents_item_data in _parents:
                parents_item = BTVersionInfo.from_dict(parents_item_data)

                parents.append(parents_item)

        _protection_rule = d.pop("protectionRule", UNSET)
        protection_rule: BTWorkspaceProtectionRuleOptions | Unset
        if isinstance(_protection_rule, Unset):
            protection_rule = UNSET
        else:
            protection_rule = BTWorkspaceProtectionRuleOptions(_protection_rule)

        _state = d.pop("state", UNSET)
        state: BTObjectState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = BTObjectState(_state)

        _thumbnail = d.pop("thumbnail", UNSET)
        thumbnail: BTThumbnailInfo | Unset
        if isinstance(_thumbnail, Unset):
            thumbnail = UNSET
        else:
            thumbnail = BTThumbnailInfo.from_dict(_thumbnail)

        type_ = d.pop("type", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_workspace_info = cls(
            can_delete=can_delete,
            created_at=created_at,
            creator=creator,
            description=description,
            document_id=document_id,
            href=href,
            id=id,
            is_read_only=is_read_only,
            last_modifier=last_modifier,
            microversion=microversion,
            modified_at=modified_at,
            name=name,
            override_date=override_date,
            parent=parent,
            parents=parents,
            protection_rule=protection_rule,
            state=state,
            thumbnail=thumbnail,
            type_=type_,
            view_ref=view_ref,
        )

        bt_workspace_info.additional_properties = d
        return bt_workspace_info

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
