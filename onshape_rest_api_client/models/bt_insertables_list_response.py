from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_insertable_info import BTInsertableInfo
    from ..models.bt_insertables_list_response_configuration import BTInsertablesListResponseConfiguration


T = TypeVar("T", bound="BTInsertablesListResponse")


@_attrs_define
class BTInsertablesListResponse:
    """
    Attributes:
        can_save_version (bool | Unset):
        changes_since_version_save (int | Unset):
        configuration (BTInsertablesListResponseConfiguration | Unset):
        configuration_key (str | Unset):
        has_multiple_versions (bool | Unset):
        href (str | Unset): URI for current page of resources.
        items (list[BTInsertableInfo] | Unset): Array of items in the current page.
        next_ (str | Unset): URI for next page of the resources if more are available.
        previous (str | Unset): URI for previous page of the resources.
        updated_thumbnail_uri (str | Unset):
    """

    can_save_version: bool | Unset = UNSET
    changes_since_version_save: int | Unset = UNSET
    configuration: BTInsertablesListResponseConfiguration | Unset = UNSET
    configuration_key: str | Unset = UNSET
    has_multiple_versions: bool | Unset = UNSET
    href: str | Unset = UNSET
    items: list[BTInsertableInfo] | Unset = UNSET
    next_: str | Unset = UNSET
    previous: str | Unset = UNSET
    updated_thumbnail_uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_save_version = self.can_save_version

        changes_since_version_save = self.changes_since_version_save

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        configuration_key = self.configuration_key

        has_multiple_versions = self.has_multiple_versions

        href = self.href

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        next_ = self.next_

        previous = self.previous

        updated_thumbnail_uri = self.updated_thumbnail_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_save_version is not UNSET:
            field_dict["canSaveVersion"] = can_save_version
        if changes_since_version_save is not UNSET:
            field_dict["changesSinceVersionSave"] = changes_since_version_save
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if configuration_key is not UNSET:
            field_dict["configurationKey"] = configuration_key
        if has_multiple_versions is not UNSET:
            field_dict["hasMultipleVersions"] = has_multiple_versions
        if href is not UNSET:
            field_dict["href"] = href
        if items is not UNSET:
            field_dict["items"] = items
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous
        if updated_thumbnail_uri is not UNSET:
            field_dict["updatedThumbnailUri"] = updated_thumbnail_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_insertable_info import BTInsertableInfo
        from ..models.bt_insertables_list_response_configuration import BTInsertablesListResponseConfiguration

        d = dict(src_dict)
        can_save_version = d.pop("canSaveVersion", UNSET)

        changes_since_version_save = d.pop("changesSinceVersionSave", UNSET)

        _configuration = d.pop("configuration", UNSET)
        configuration: BTInsertablesListResponseConfiguration | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = BTInsertablesListResponseConfiguration.from_dict(_configuration)

        configuration_key = d.pop("configurationKey", UNSET)

        has_multiple_versions = d.pop("hasMultipleVersions", UNSET)

        href = d.pop("href", UNSET)

        _items = d.pop("items", UNSET)
        items: list[BTInsertableInfo] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = BTInsertableInfo.from_dict(items_item_data)

                items.append(items_item)

        next_ = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        updated_thumbnail_uri = d.pop("updatedThumbnailUri", UNSET)

        bt_insertables_list_response = cls(
            can_save_version=can_save_version,
            changes_since_version_save=changes_since_version_save,
            configuration=configuration,
            configuration_key=configuration_key,
            has_multiple_versions=has_multiple_versions,
            href=href,
            items=items,
            next_=next_,
            previous=previous,
            updated_thumbnail_uri=updated_thumbnail_uri,
        )

        bt_insertables_list_response.additional_properties = d
        return bt_insertables_list_response

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
