from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTBillOfMaterialsHeaderInfo")


@_attrs_define
class BTBillOfMaterialsHeaderInfo:
    """
    Attributes:
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        property_name (str | Unset):
        value_type (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        visible (bool | Unset):
    """

    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    property_name: str | Unset = UNSET
    value_type: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    visible: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        href = self.href

        id = self.id

        name = self.name

        property_name = self.property_name

        value_type = self.value_type

        view_ref = self.view_ref

        visible = self.visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if property_name is not UNSET:
            field_dict["propertyName"] = property_name
        if value_type is not UNSET:
            field_dict["valueType"] = value_type
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if visible is not UNSET:
            field_dict["visible"] = visible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        property_name = d.pop("propertyName", UNSET)

        value_type = d.pop("valueType", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        visible = d.pop("visible", UNSET)

        bt_bill_of_materials_header_info = cls(
            href=href,
            id=id,
            name=name,
            property_name=property_name,
            value_type=value_type,
            view_ref=view_ref,
            visible=visible,
        )

        bt_bill_of_materials_header_info.additional_properties = d
        return bt_bill_of_materials_header_info

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
