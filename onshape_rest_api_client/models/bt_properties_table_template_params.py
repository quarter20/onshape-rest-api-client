from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_properties_table_template_type import BTPropertiesTableTemplateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTPropertiesTableTemplateParams")


@_attrs_define
class BTPropertiesTableTemplateParams:
    """
    Attributes:
        company_id (str | Unset):
        is_all_caps (bool | Unset):
        is_indented (bool | Unset):
        name (str | Unset):
        property_columns (list[str] | Unset):
        table_type (BTPropertiesTableTemplateType | Unset):
    """

    company_id: str | Unset = UNSET
    is_all_caps: bool | Unset = UNSET
    is_indented: bool | Unset = UNSET
    name: str | Unset = UNSET
    property_columns: list[str] | Unset = UNSET
    table_type: BTPropertiesTableTemplateType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        is_all_caps = self.is_all_caps

        is_indented = self.is_indented

        name = self.name

        property_columns: list[str] | Unset = UNSET
        if not isinstance(self.property_columns, Unset):
            property_columns = self.property_columns

        table_type: str | Unset = UNSET
        if not isinstance(self.table_type, Unset):
            table_type = self.table_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company_id = d.pop("companyId", UNSET)

        is_all_caps = d.pop("isAllCaps", UNSET)

        is_indented = d.pop("isIndented", UNSET)

        name = d.pop("name", UNSET)

        property_columns = cast(list[str], d.pop("propertyColumns", UNSET))

        _table_type = d.pop("tableType", UNSET)
        table_type: BTPropertiesTableTemplateType | Unset
        if isinstance(_table_type, Unset):
            table_type = UNSET
        else:
            table_type = BTPropertiesTableTemplateType(_table_type)

        bt_properties_table_template_params = cls(
            company_id=company_id,
            is_all_caps=is_all_caps,
            is_indented=is_indented,
            name=name,
            property_columns=property_columns,
            table_type=table_type,
        )

        bt_properties_table_template_params.additional_properties = d
        return bt_properties_table_template_params

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
