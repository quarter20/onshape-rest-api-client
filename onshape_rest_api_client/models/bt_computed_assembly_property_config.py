from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_computed_assembly_property_aggregation_operator import BTComputedAssemblyPropertyAggregationOperator
from ..models.bt_computed_assembly_property_error_policy import BTComputedAssemblyPropertyErrorPolicy
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTComputedAssemblyPropertyConfig")


@_attrs_define
class BTComputedAssemblyPropertyConfig:
    """
    Attributes:
        aggregated_property_id (str | Unset):
        aggregation_operator (BTComputedAssemblyPropertyAggregationOperator | Unset):
        error_value_policy (BTComputedAssemblyPropertyErrorPolicy | Unset):
        filter_property_id (str | Unset):
        is_filter_property_inverted (bool | Unset):
        missing_value_policy (BTComputedAssemblyPropertyErrorPolicy | Unset):
        secondary_property_id (str | Unset):
    """

    aggregated_property_id: str | Unset = UNSET
    aggregation_operator: BTComputedAssemblyPropertyAggregationOperator | Unset = UNSET
    error_value_policy: BTComputedAssemblyPropertyErrorPolicy | Unset = UNSET
    filter_property_id: str | Unset = UNSET
    is_filter_property_inverted: bool | Unset = UNSET
    missing_value_policy: BTComputedAssemblyPropertyErrorPolicy | Unset = UNSET
    secondary_property_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregated_property_id = self.aggregated_property_id

        aggregation_operator: str | Unset = UNSET
        if not isinstance(self.aggregation_operator, Unset):
            aggregation_operator = self.aggregation_operator.value

        error_value_policy: str | Unset = UNSET
        if not isinstance(self.error_value_policy, Unset):
            error_value_policy = self.error_value_policy.value

        filter_property_id = self.filter_property_id

        is_filter_property_inverted = self.is_filter_property_inverted

        missing_value_policy: str | Unset = UNSET
        if not isinstance(self.missing_value_policy, Unset):
            missing_value_policy = self.missing_value_policy.value

        secondary_property_id = self.secondary_property_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregated_property_id is not UNSET:
            field_dict["aggregatedPropertyId"] = aggregated_property_id
        if aggregation_operator is not UNSET:
            field_dict["aggregationOperator"] = aggregation_operator
        if error_value_policy is not UNSET:
            field_dict["errorValuePolicy"] = error_value_policy
        if filter_property_id is not UNSET:
            field_dict["filterPropertyId"] = filter_property_id
        if is_filter_property_inverted is not UNSET:
            field_dict["isFilterPropertyInverted"] = is_filter_property_inverted
        if missing_value_policy is not UNSET:
            field_dict["missingValuePolicy"] = missing_value_policy
        if secondary_property_id is not UNSET:
            field_dict["secondaryPropertyId"] = secondary_property_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aggregated_property_id = d.pop("aggregatedPropertyId", UNSET)

        _aggregation_operator = d.pop("aggregationOperator", UNSET)
        aggregation_operator: BTComputedAssemblyPropertyAggregationOperator | Unset
        if isinstance(_aggregation_operator, Unset):
            aggregation_operator = UNSET
        else:
            aggregation_operator = BTComputedAssemblyPropertyAggregationOperator(_aggregation_operator)

        _error_value_policy = d.pop("errorValuePolicy", UNSET)
        error_value_policy: BTComputedAssemblyPropertyErrorPolicy | Unset
        if isinstance(_error_value_policy, Unset):
            error_value_policy = UNSET
        else:
            error_value_policy = BTComputedAssemblyPropertyErrorPolicy(_error_value_policy)

        filter_property_id = d.pop("filterPropertyId", UNSET)

        is_filter_property_inverted = d.pop("isFilterPropertyInverted", UNSET)

        _missing_value_policy = d.pop("missingValuePolicy", UNSET)
        missing_value_policy: BTComputedAssemblyPropertyErrorPolicy | Unset
        if isinstance(_missing_value_policy, Unset):
            missing_value_policy = UNSET
        else:
            missing_value_policy = BTComputedAssemblyPropertyErrorPolicy(_missing_value_policy)

        secondary_property_id = d.pop("secondaryPropertyId", UNSET)

        bt_computed_assembly_property_config = cls(
            aggregated_property_id=aggregated_property_id,
            aggregation_operator=aggregation_operator,
            error_value_policy=error_value_policy,
            filter_property_id=filter_property_id,
            is_filter_property_inverted=is_filter_property_inverted,
            missing_value_policy=missing_value_policy,
            secondary_property_id=secondary_property_id,
        )

        bt_computed_assembly_property_config.additional_properties = d
        return bt_computed_assembly_property_config

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
