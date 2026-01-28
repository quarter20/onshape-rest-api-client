from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTStandardContentHierarchyItem")


@_attrs_define
class BTStandardContentHierarchyItem:
    """Describes a single instance of standard content.

    Attributes:
        category (str | Unset): Category for the corresponding standard content.
        class_ (str | Unset): Class for the corresponding standard content.
        component (str | Unset): Component for the corresponding standard content.
        id (str | Unset): Document ID for the corresponding standard content.
        standard (str | Unset): Standard for the corresponding standard content.
    """

    category: str | Unset = UNSET
    class_: str | Unset = UNSET
    component: str | Unset = UNSET
    id: str | Unset = UNSET
    standard: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        class_ = self.class_

        component = self.component

        id = self.id

        standard = self.standard

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if class_ is not UNSET:
            field_dict["class"] = class_
        if component is not UNSET:
            field_dict["component"] = component
        if id is not UNSET:
            field_dict["id"] = id
        if standard is not UNSET:
            field_dict["standard"] = standard

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        class_ = d.pop("class", UNSET)

        component = d.pop("component", UNSET)

        id = d.pop("id", UNSET)

        standard = d.pop("standard", UNSET)

        bt_standard_content_hierarchy_item = cls(
            category=category,
            class_=class_,
            component=component,
            id=id,
            standard=standard,
        )

        bt_standard_content_hierarchy_item.additional_properties = d
        return bt_standard_content_hierarchy_item

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
