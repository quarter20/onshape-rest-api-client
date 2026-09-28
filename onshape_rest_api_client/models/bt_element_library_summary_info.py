from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_owner_type import BTOwnerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTElementLibrarySummaryInfo")


@_attrs_define
class BTElementLibrarySummaryInfo:
    """Element library metadata

    Attributes:
        current_public_version (str | Unset): If present, this library is public and this field contains the version Id
            of the current public version. If not present, this library is not public.
        definition_name (str | Unset): What this library is for, e.g. frames profiles.
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        library_definition_id (str | Unset): The ID of the definition of the element library.
        library_id (str | Unset): The Id of the library -- unique across Onshape.
        library_owner_type (BTOwnerType | Unset): The type of library owner, Onshape, user, or company.
        library_version (str | Unset): The current version Id of the library.
        modified_at (datetime.datetime | Unset): Time of the last modification to the library.
        name (str | Unset): Name of the resource.
        owner_id (str | Unset): The owner Id of an element library (either Onshape, company, or user).
        owner_name (str | Unset): The name of the owner of the library.
        source_folder_id (str | Unset): The id of the root folder of the library.
        subscribed (bool | Unset): If true, the current user is subscribed to this library. Applies only to public
            libraries.
        version_name (str | Unset): The name of the current version of the library.
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    current_public_version: str | Unset = UNSET
    definition_name: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    library_definition_id: str | Unset = UNSET
    library_id: str | Unset = UNSET
    library_owner_type: BTOwnerType | Unset = UNSET
    library_version: str | Unset = UNSET
    modified_at: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_name: str | Unset = UNSET
    source_folder_id: str | Unset = UNSET
    subscribed: bool | Unset = UNSET
    version_name: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_public_version = self.current_public_version

        definition_name = self.definition_name

        href = self.href

        id = self.id

        library_definition_id = self.library_definition_id

        library_id = self.library_id

        library_owner_type: str | Unset = UNSET
        if not isinstance(self.library_owner_type, Unset):
            library_owner_type = self.library_owner_type.value

        library_version = self.library_version

        modified_at: str | Unset = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        name = self.name

        owner_id = self.owner_id

        owner_name = self.owner_name

        source_folder_id = self.source_folder_id

        subscribed = self.subscribed

        version_name = self.version_name

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_public_version is not UNSET:
            field_dict["currentPublicVersion"] = current_public_version
        if definition_name is not UNSET:
            field_dict["definitionName"] = definition_name
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if library_definition_id is not UNSET:
            field_dict["libraryDefinitionId"] = library_definition_id
        if library_id is not UNSET:
            field_dict["libraryId"] = library_id
        if library_owner_type is not UNSET:
            field_dict["libraryOwnerType"] = library_owner_type
        if library_version is not UNSET:
            field_dict["libraryVersion"] = library_version
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if owner_name is not UNSET:
            field_dict["ownerName"] = owner_name
        if source_folder_id is not UNSET:
            field_dict["sourceFolderId"] = source_folder_id
        if subscribed is not UNSET:
            field_dict["subscribed"] = subscribed
        if version_name is not UNSET:
            field_dict["versionName"] = version_name
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_public_version = d.pop("currentPublicVersion", UNSET)

        definition_name = d.pop("definitionName", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        library_definition_id = d.pop("libraryDefinitionId", UNSET)

        library_id = d.pop("libraryId", UNSET)

        _library_owner_type = d.pop("libraryOwnerType", UNSET)
        library_owner_type: BTOwnerType | Unset
        if isinstance(_library_owner_type, Unset):
            library_owner_type = UNSET
        else:
            library_owner_type = BTOwnerType(_library_owner_type)

        library_version = d.pop("libraryVersion", UNSET)

        _modified_at = d.pop("modifiedAt", UNSET)
        modified_at: datetime.datetime | Unset
        if isinstance(_modified_at, Unset):
            modified_at = UNSET
        else:
            modified_at = datetime.datetime.fromisoformat(_modified_at)

        name = d.pop("name", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        owner_name = d.pop("ownerName", UNSET)

        source_folder_id = d.pop("sourceFolderId", UNSET)

        subscribed = d.pop("subscribed", UNSET)

        version_name = d.pop("versionName", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_element_library_summary_info = cls(
            current_public_version=current_public_version,
            definition_name=definition_name,
            href=href,
            id=id,
            library_definition_id=library_definition_id,
            library_id=library_id,
            library_owner_type=library_owner_type,
            library_version=library_version,
            modified_at=modified_at,
            name=name,
            owner_id=owner_id,
            owner_name=owner_name,
            source_folder_id=source_folder_id,
            subscribed=subscribed,
            version_name=version_name,
            view_ref=view_ref,
        )

        bt_element_library_summary_info.additional_properties = d
        return bt_element_library_summary_info

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
