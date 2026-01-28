from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_property_value_param import BTPropertyValueParam
    from ..models.bt_release_package_item_params import BTReleasePackageItemParams


T = TypeVar("T", bound="BTUpdateReleasePackageParams")


@_attrs_define
class BTUpdateReleasePackageParams:
    """
    Attributes:
        empty (bool | Unset):
        item_ids (list[str] | Unset):
        items (list[BTReleasePackageItemParams] | Unset):
        properties (list[BTPropertyValueParam] | Unset):
    """

    empty: bool | Unset = UNSET
    item_ids: list[str] | Unset = UNSET
    items: list[BTReleasePackageItemParams] | Unset = UNSET
    properties: list[BTPropertyValueParam] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        empty = self.empty

        item_ids: list[str] | Unset = UNSET
        if not isinstance(self.item_ids, Unset):
            item_ids = self.item_ids

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if empty is not UNSET:
            field_dict["empty"] = empty
        if item_ids is not UNSET:
            field_dict["itemIds"] = item_ids
        if items is not UNSET:
            field_dict["items"] = items
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_property_value_param import BTPropertyValueParam
        from ..models.bt_release_package_item_params import BTReleasePackageItemParams

        d = dict(src_dict)
        empty = d.pop("empty", UNSET)

        item_ids = cast(list[str], d.pop("itemIds", UNSET))

        _items = d.pop("items", UNSET)
        items: list[BTReleasePackageItemParams] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = BTReleasePackageItemParams.from_dict(items_item_data)

                items.append(items_item)

        _properties = d.pop("properties", UNSET)
        properties: list[BTPropertyValueParam] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = BTPropertyValueParam.from_dict(properties_item_data)

                properties.append(properties_item)

        bt_update_release_package_params = cls(
            empty=empty,
            item_ids=item_ids,
            items=items,
            properties=properties,
        )

        bt_update_release_package_params.additional_properties = d
        return bt_update_release_package_params

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
