from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_property_value_param import BTPropertyValueParam
    from ..models.bt_task_item_params import BTTaskItemParams


T = TypeVar("T", bound="BTUpdateTaskParams")


@_attrs_define
class BTUpdateTaskParams:
    """
    Attributes:
        company_id (str | Unset): Use to transfer task ownership to the company.
        delete_item_ids (list[str] | Unset): References to remove from the task.
        description_param_value (str | Unset):
        item_params (list[BTTaskItemParams] | Unset): References to add to the task.
        name_param_value (str | Unset):
        property_values (list[BTPropertyValueParam] | Unset): Task metadata properties.
        workflow_id (str | Unset):
    """

    company_id: str | Unset = UNSET
    delete_item_ids: list[str] | Unset = UNSET
    description_param_value: str | Unset = UNSET
    item_params: list[BTTaskItemParams] | Unset = UNSET
    name_param_value: str | Unset = UNSET
    property_values: list[BTPropertyValueParam] | Unset = UNSET
    workflow_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        delete_item_ids: list[str] | Unset = UNSET
        if not isinstance(self.delete_item_ids, Unset):
            delete_item_ids = self.delete_item_ids

        description_param_value = self.description_param_value

        item_params: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.item_params, Unset):
            item_params = []
            for item_params_item_data in self.item_params:
                item_params_item = item_params_item_data.to_dict()
                item_params.append(item_params_item)

        name_param_value = self.name_param_value

        property_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.property_values, Unset):
            property_values = []
            for property_values_item_data in self.property_values:
                property_values_item = property_values_item_data.to_dict()
                property_values.append(property_values_item)

        workflow_id = self.workflow_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if delete_item_ids is not UNSET:
            field_dict["deleteItemIds"] = delete_item_ids
        if description_param_value is not UNSET:
            field_dict["descriptionParamValue"] = description_param_value
        if item_params is not UNSET:
            field_dict["itemParams"] = item_params
        if name_param_value is not UNSET:
            field_dict["nameParamValue"] = name_param_value
        if property_values is not UNSET:
            field_dict["propertyValues"] = property_values
        if workflow_id is not UNSET:
            field_dict["workflowId"] = workflow_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_property_value_param import BTPropertyValueParam
        from ..models.bt_task_item_params import BTTaskItemParams

        d = dict(src_dict)
        company_id = d.pop("companyId", UNSET)

        delete_item_ids = cast(list[str], d.pop("deleteItemIds", UNSET))

        description_param_value = d.pop("descriptionParamValue", UNSET)

        _item_params = d.pop("itemParams", UNSET)
        item_params: list[BTTaskItemParams] | Unset = UNSET
        if _item_params is not UNSET:
            item_params = []
            for item_params_item_data in _item_params:
                item_params_item = BTTaskItemParams.from_dict(item_params_item_data)

                item_params.append(item_params_item)

        name_param_value = d.pop("nameParamValue", UNSET)

        _property_values = d.pop("propertyValues", UNSET)
        property_values: list[BTPropertyValueParam] | Unset = UNSET
        if _property_values is not UNSET:
            property_values = []
            for property_values_item_data in _property_values:
                property_values_item = BTPropertyValueParam.from_dict(property_values_item_data)

                property_values.append(property_values_item)

        workflow_id = d.pop("workflowId", UNSET)

        bt_update_task_params = cls(
            company_id=company_id,
            delete_item_ids=delete_item_ids,
            description_param_value=description_param_value,
            item_params=item_params,
            name_param_value=name_param_value,
            property_values=property_values,
            workflow_id=workflow_id,
        )

        bt_update_task_params.additional_properties = d
        return bt_update_task_params

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
