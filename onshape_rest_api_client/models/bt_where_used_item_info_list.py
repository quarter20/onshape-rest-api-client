from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_product_structure_item_info import BTProductStructureItemInfo
    from ..models.bt_where_used_version_referenced_info import BTWhereUsedVersionReferencedInfo
    from ..models.config_info import ConfigInfo


T = TypeVar("T", bound="BTWhereUsedItemInfoList")


@_attrs_define
class BTWhereUsedItemInfoList:
    """
    Attributes:
        default_config (list[ConfigInfo] | Unset): The resolved default configuration parameters for the queried
            element. Only populated when the configuration query parameter is set to 'default'.
        href (str | Unset): URI for current page of resources.
        items (list[BTProductStructureItemInfo] | Unset): Array of items in the current page.
        next_ (str | Unset): URI for next page of the resources if more are available.
        previous (str | Unset): URI for previous page of the resources.
        versions (list[BTWhereUsedVersionReferencedInfo] | Unset): List of document versions in which the queried item
            is referenced. Each entry contains the version info, referring document and element details, configuration,
            revision, and part identifiers. Only populated when includeVersionInfo is true.
    """

    default_config: list[ConfigInfo] | Unset = UNSET
    href: str | Unset = UNSET
    items: list[BTProductStructureItemInfo] | Unset = UNSET
    next_: str | Unset = UNSET
    previous: str | Unset = UNSET
    versions: list[BTWhereUsedVersionReferencedInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_config: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.default_config, Unset):
            default_config = []
            for default_config_item_data in self.default_config:
                default_config_item = default_config_item_data.to_dict()
                default_config.append(default_config_item)

        href = self.href

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        next_ = self.next_

        previous = self.previous

        versions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_config is not UNSET:
            field_dict["defaultConfig"] = default_config
        if href is not UNSET:
            field_dict["href"] = href
        if items is not UNSET:
            field_dict["items"] = items
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_product_structure_item_info import BTProductStructureItemInfo
        from ..models.bt_where_used_version_referenced_info import BTWhereUsedVersionReferencedInfo
        from ..models.config_info import ConfigInfo

        d = dict(src_dict)
        _default_config = d.pop("defaultConfig", UNSET)
        default_config: list[ConfigInfo] | Unset = UNSET
        if _default_config is not UNSET:
            default_config = []
            for default_config_item_data in _default_config:
                default_config_item = ConfigInfo.from_dict(default_config_item_data)

                default_config.append(default_config_item)

        href = d.pop("href", UNSET)

        _items = d.pop("items", UNSET)
        items: list[BTProductStructureItemInfo] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = BTProductStructureItemInfo.from_dict(items_item_data)

                items.append(items_item)

        next_ = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        _versions = d.pop("versions", UNSET)
        versions: list[BTWhereUsedVersionReferencedInfo] | Unset = UNSET
        if _versions is not UNSET:
            versions = []
            for versions_item_data in _versions:
                versions_item = BTWhereUsedVersionReferencedInfo.from_dict(versions_item_data)

                versions.append(versions_item)

        bt_where_used_item_info_list = cls(
            default_config=default_config,
            href=href,
            items=items,
            next_=next_,
            previous=previous,
            versions=versions,
        )

        bt_where_used_item_info_list.additional_properties = d
        return bt_where_used_item_info_list

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
