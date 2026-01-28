from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_property_value_param import BTPropertyValueParam
    from ..models.bt_task_item_params import BTTaskItemParams


T = TypeVar("T", bound="BTCreateTaskParams")


@_attrs_define
class BTCreateTaskParams:
    """
    Attributes:
        company_id (str): Id of the company that owns the task.
        description (str | Unset): Description of the task.
        description_param_value (str | Unset):
        document_id (str | Unset): Id of a document to associate the task to.
        item_params (list[BTTaskItemParams] | Unset): References to include in the task.
        name (str | Unset): Name of the task.
        name_param_value (str | Unset):
        property_values (list[BTPropertyValueParam] | Unset): Set Task metadata properties.
    """

    company_id: str
    description: str | Unset = UNSET
    description_param_value: str | Unset = UNSET
    document_id: str | Unset = UNSET
    item_params: list[BTTaskItemParams] | Unset = UNSET
    name: str | Unset = UNSET
    name_param_value: str | Unset = UNSET
    property_values: list[BTPropertyValueParam] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        description = self.description

        description_param_value = self.description_param_value

        document_id = self.document_id

        item_params: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.item_params, Unset):
            item_params = []
            for item_params_item_data in self.item_params:
                item_params_item = item_params_item_data.to_dict()
                item_params.append(item_params_item)

        name = self.name

        name_param_value = self.name_param_value

        property_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.property_values, Unset):
            property_values = []
            for property_values_item_data in self.property_values:
                property_values_item = property_values_item_data.to_dict()
                property_values.append(property_values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "companyId": company_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if description_param_value is not UNSET:
            field_dict["descriptionParamValue"] = description_param_value
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if item_params is not UNSET:
            field_dict["itemParams"] = item_params
        if name is not UNSET:
            field_dict["name"] = name
        if name_param_value is not UNSET:
            field_dict["nameParamValue"] = name_param_value
        if property_values is not UNSET:
            field_dict["propertyValues"] = property_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_property_value_param import BTPropertyValueParam
        from ..models.bt_task_item_params import BTTaskItemParams

        d = dict(src_dict)
        company_id = d.pop("companyId")

        description = d.pop("description", UNSET)

        description_param_value = d.pop("descriptionParamValue", UNSET)

        document_id = d.pop("documentId", UNSET)

        _item_params = d.pop("itemParams", UNSET)
        item_params: list[BTTaskItemParams] | Unset = UNSET
        if _item_params is not UNSET:
            item_params = []
            for item_params_item_data in _item_params:
                item_params_item = BTTaskItemParams.from_dict(item_params_item_data)

                item_params.append(item_params_item)

        name = d.pop("name", UNSET)

        name_param_value = d.pop("nameParamValue", UNSET)

        _property_values = d.pop("propertyValues", UNSET)
        property_values: list[BTPropertyValueParam] | Unset = UNSET
        if _property_values is not UNSET:
            property_values = []
            for property_values_item_data in _property_values:
                property_values_item = BTPropertyValueParam.from_dict(property_values_item_data)

                property_values.append(property_values_item)

        bt_create_task_params = cls(
            company_id=company_id,
            description=description,
            description_param_value=description_param_value,
            document_id=document_id,
            item_params=item_params,
            name=name,
            name_param_value=name_param_value,
            property_values=property_values,
        )

        bt_create_task_params.additional_properties = d
        return bt_create_task_params

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
