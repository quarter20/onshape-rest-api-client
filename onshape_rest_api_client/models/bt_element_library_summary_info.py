from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTElementLibrarySummaryInfo")


@_attrs_define
class BTElementLibrarySummaryInfo:
    """Element library metadata

    Attributes:
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        library_definition_id (str | Unset): The ID of the definition of the element library.
        library_id (str | Unset): The Id of the library -- unique across Onshape.
        library_version (str | Unset): The current version Id of the library.
        name (str | Unset): Name of the resource.
        owner_id (str | Unset): The owner Id of an element library (either Onshape, company, or user).
        owner_type (int | Unset): The type of library owner, Onshape, user, or company
        source_folder_id (str | Unset): The id of the root folder of the library
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    href: str | Unset = UNSET
    id: str | Unset = UNSET
    library_definition_id: str | Unset = UNSET
    library_id: str | Unset = UNSET
    library_version: str | Unset = UNSET
    name: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: int | Unset = UNSET
    source_folder_id: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        href = self.href

        id = self.id

        library_definition_id = self.library_definition_id

        library_id = self.library_id

        library_version = self.library_version

        name = self.name

        owner_id = self.owner_id

        owner_type = self.owner_type

        source_folder_id = self.source_folder_id

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if library_definition_id is not UNSET:
            field_dict["libraryDefinitionId"] = library_definition_id
        if library_id is not UNSET:
            field_dict["libraryId"] = library_id
        if library_version is not UNSET:
            field_dict["libraryVersion"] = library_version
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if owner_type is not UNSET:
            field_dict["ownerType"] = owner_type
        if source_folder_id is not UNSET:
            field_dict["sourceFolderId"] = source_folder_id
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        library_definition_id = d.pop("libraryDefinitionId", UNSET)

        library_id = d.pop("libraryId", UNSET)

        library_version = d.pop("libraryVersion", UNSET)

        name = d.pop("name", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        owner_type = d.pop("ownerType", UNSET)

        source_folder_id = d.pop("sourceFolderId", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_element_library_summary_info = cls(
            href=href,
            id=id,
            library_definition_id=library_definition_id,
            library_id=library_id,
            library_version=library_version,
            name=name,
            owner_id=owner_id,
            owner_type=owner_type,
            source_folder_id=source_folder_id,
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
