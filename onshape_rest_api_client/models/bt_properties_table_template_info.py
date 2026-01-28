from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_properties_table_template_type import BTPropertiesTableTemplateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_simple_property_info import BTSimplePropertyInfo


T = TypeVar("T", bound="BTPropertiesTableTemplateInfo")


@_attrs_define
class BTPropertiesTableTemplateInfo:
    """
    Attributes:
        company_id (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        is_active (bool | Unset):
        is_all_caps (bool | Unset):
        is_indented (bool | Unset):
        name (str | Unset): Name of the resource.
        property_columns (list[BTSimplePropertyInfo] | Unset):
        table_type (BTPropertiesTableTemplateType | Unset):
        template_group_id (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    company_id: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_all_caps: bool | Unset = UNSET
    is_indented: bool | Unset = UNSET
    name: str | Unset = UNSET
    property_columns: list[BTSimplePropertyInfo] | Unset = UNSET
    table_type: BTPropertiesTableTemplateType | Unset = UNSET
    template_group_id: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        href = self.href

        id = self.id

        is_active = self.is_active

        is_all_caps = self.is_all_caps

        is_indented = self.is_indented

        name = self.name

        property_columns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.property_columns, Unset):
            property_columns = []
            for property_columns_item_data in self.property_columns:
                property_columns_item = property_columns_item_data.to_dict()
                property_columns.append(property_columns_item)

        table_type: str | Unset = UNSET
        if not isinstance(self.table_type, Unset):
            table_type = self.table_type.value

        template_group_id = self.template_group_id

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if is_all_caps is not UNSET:
            field_dict["isAllCaps"] = is_all_caps
        if is_indented is not UNSET:
            field_dict["isIndented"] = is_indented
        if name is not UNSET:
            field_dict["name"] = name
        if property_columns is not UNSET:
            field_dict["propertyColumns"] = property_columns
        if table_type is not UNSET:
            field_dict["tableType"] = table_type
        if template_group_id is not UNSET:
            field_dict["templateGroupId"] = template_group_id
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_simple_property_info import BTSimplePropertyInfo

        d = dict(src_dict)
        company_id = d.pop("companyId", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        is_active = d.pop("isActive", UNSET)

        is_all_caps = d.pop("isAllCaps", UNSET)

        is_indented = d.pop("isIndented", UNSET)

        name = d.pop("name", UNSET)

        _property_columns = d.pop("propertyColumns", UNSET)
        property_columns: list[BTSimplePropertyInfo] | Unset = UNSET
        if _property_columns is not UNSET:
            property_columns = []
            for property_columns_item_data in _property_columns:
                property_columns_item = BTSimplePropertyInfo.from_dict(property_columns_item_data)

                property_columns.append(property_columns_item)

        _table_type = d.pop("tableType", UNSET)
        table_type: BTPropertiesTableTemplateType | Unset
        if isinstance(_table_type, Unset):
            table_type = UNSET
        else:
            table_type = BTPropertiesTableTemplateType(_table_type)

        template_group_id = d.pop("templateGroupId", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_properties_table_template_info = cls(
            company_id=company_id,
            href=href,
            id=id,
            is_active=is_active,
            is_all_caps=is_all_caps,
            is_indented=is_indented,
            name=name,
            property_columns=property_columns,
            table_type=table_type,
            template_group_id=template_group_id,
            view_ref=view_ref,
        )

        bt_properties_table_template_info.additional_properties = d
        return bt_properties_table_template_info

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
