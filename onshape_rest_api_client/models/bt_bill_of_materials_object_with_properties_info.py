from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_bill_of_materials_object_with_properties_info_header_id_to_value import (
        BTBillOfMaterialsObjectWithPropertiesInfoHeaderIdToValue,
    )


T = TypeVar("T", bound="BTBillOfMaterialsObjectWithPropertiesInfo")


@_attrs_define
class BTBillOfMaterialsObjectWithPropertiesInfo:
    """
    Attributes:
        header_id_to_value (BTBillOfMaterialsObjectWithPropertiesInfoHeaderIdToValue | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    header_id_to_value: BTBillOfMaterialsObjectWithPropertiesInfoHeaderIdToValue | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        header_id_to_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.header_id_to_value, Unset):
            header_id_to_value = self.header_id_to_value.to_dict()

        href = self.href

        id = self.id

        name = self.name

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if header_id_to_value is not UNSET:
            field_dict["headerIdToValue"] = header_id_to_value
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_bill_of_materials_object_with_properties_info_header_id_to_value import (
            BTBillOfMaterialsObjectWithPropertiesInfoHeaderIdToValue,
        )

        d = dict(src_dict)
        _header_id_to_value = d.pop("headerIdToValue", UNSET)
        header_id_to_value: BTBillOfMaterialsObjectWithPropertiesInfoHeaderIdToValue | Unset
        if isinstance(_header_id_to_value, Unset):
            header_id_to_value = UNSET
        else:
            header_id_to_value = BTBillOfMaterialsObjectWithPropertiesInfoHeaderIdToValue.from_dict(_header_id_to_value)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_bill_of_materials_object_with_properties_info = cls(
            header_id_to_value=header_id_to_value,
            href=href,
            id=id,
            name=name,
            view_ref=view_ref,
        )

        bt_bill_of_materials_object_with_properties_info.additional_properties = d
        return bt_bill_of_materials_object_with_properties_info

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
