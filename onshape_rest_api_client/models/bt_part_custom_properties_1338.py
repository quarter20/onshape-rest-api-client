from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_part_custom_properties_1338_properties import BTPartCustomProperties1338Properties


T = TypeVar("T", bound="BTPartCustomProperties1338")


@_attrs_define
class BTPartCustomProperties1338:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        description (str | Unset):
        part_number (str | Unset):
        product_line (str | Unset):
        project (str | Unset):
        properties (BTPartCustomProperties1338Properties | Unset):
        revision (str | Unset):
        tessellation_setting (str | Unset):
        title1 (str | Unset):
        title2 (str | Unset):
        title3 (str | Unset):
        vendor (str | Unset):
    """

    bt_type: str | Unset = UNSET
    description: str | Unset = UNSET
    part_number: str | Unset = UNSET
    product_line: str | Unset = UNSET
    project: str | Unset = UNSET
    properties: BTPartCustomProperties1338Properties | Unset = UNSET
    revision: str | Unset = UNSET
    tessellation_setting: str | Unset = UNSET
    title1: str | Unset = UNSET
    title2: str | Unset = UNSET
    title3: str | Unset = UNSET
    vendor: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        description = self.description

        part_number = self.part_number

        product_line = self.product_line

        project = self.project

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        revision = self.revision

        tessellation_setting = self.tessellation_setting

        title1 = self.title1

        title2 = self.title2

        title3 = self.title3

        vendor = self.vendor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if description is not UNSET:
            field_dict["description"] = description
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if product_line is not UNSET:
            field_dict["productLine"] = product_line
        if project is not UNSET:
            field_dict["project"] = project
        if properties is not UNSET:
            field_dict["properties"] = properties
        if revision is not UNSET:
            field_dict["revision"] = revision
        if tessellation_setting is not UNSET:
            field_dict["tessellationSetting"] = tessellation_setting
        if title1 is not UNSET:
            field_dict["title1"] = title1
        if title2 is not UNSET:
            field_dict["title2"] = title2
        if title3 is not UNSET:
            field_dict["title3"] = title3
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_part_custom_properties_1338_properties import BTPartCustomProperties1338Properties

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        description = d.pop("description", UNSET)

        part_number = d.pop("partNumber", UNSET)

        product_line = d.pop("productLine", UNSET)

        project = d.pop("project", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: BTPartCustomProperties1338Properties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = BTPartCustomProperties1338Properties.from_dict(_properties)

        revision = d.pop("revision", UNSET)

        tessellation_setting = d.pop("tessellationSetting", UNSET)

        title1 = d.pop("title1", UNSET)

        title2 = d.pop("title2", UNSET)

        title3 = d.pop("title3", UNSET)

        vendor = d.pop("vendor", UNSET)

        bt_part_custom_properties_1338 = cls(
            bt_type=bt_type,
            description=description,
            part_number=part_number,
            product_line=product_line,
            project=project,
            properties=properties,
            revision=revision,
            tessellation_setting=tessellation_setting,
            title1=title1,
            title2=title2,
            title3=title3,
            vendor=vendor,
        )

        bt_part_custom_properties_1338.additional_properties = d
        return bt_part_custom_properties_1338

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
