from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_computed_assembly_property_config import BTComputedAssemblyPropertyConfig
    from ..models.bt_computed_part_property_config import BTComputedPartPropertyConfig
    from ..models.bt_metadata_enum_value import BTMetadataEnumValue


T = TypeVar("T", bound="BTCategoryPropertyConfigInfo")


@_attrs_define
class BTCategoryPropertyConfigInfo:
    """
    Attributes:
        computed_assembly_property_aggregated_property_id (str | Unset):
        computed_assembly_property_aggregation_operator (int | Unset):
        computed_assembly_property_config (BTComputedAssemblyPropertyConfig | Unset):
        computed_assembly_property_error_value_policy (int | Unset):
        computed_assembly_property_filter_inverted (bool | Unset):
        computed_assembly_property_filter_property_id (str | Unset):
        computed_assembly_property_missing_value_policy (int | Unset):
        computed_assembly_property_secondary_property_id (str | Unset):
        computed_part_property_config (BTComputedPartPropertyConfig | Unset):
        computed_property_function_name (str | Unset):
        computed_property_function_namespace (str | Unset):
        computed_property_function_url (str | Unset):
        default_value (str | Unset):
        display_name (str | Unset):
        enum_values (list[BTMetadataEnumValue] | Unset):
        max_count (int | Unset):
        max_date (datetime.datetime | Unset):
        max_length (int | Unset):
        max_value (float | Unset):
        min_count (int | Unset):
        min_date (datetime.datetime | Unset):
        min_length (int | Unset):
        min_value (float | Unset):
        multiline (bool | Unset):
        multivalued (bool | Unset):
        pattern (str | Unset):
        publish_state (int | Unset):
        quantity_type (int | Unset):
        required (bool | Unset):
    """

    computed_assembly_property_aggregated_property_id: str | Unset = UNSET
    computed_assembly_property_aggregation_operator: int | Unset = UNSET
    computed_assembly_property_config: BTComputedAssemblyPropertyConfig | Unset = UNSET
    computed_assembly_property_error_value_policy: int | Unset = UNSET
    computed_assembly_property_filter_inverted: bool | Unset = UNSET
    computed_assembly_property_filter_property_id: str | Unset = UNSET
    computed_assembly_property_missing_value_policy: int | Unset = UNSET
    computed_assembly_property_secondary_property_id: str | Unset = UNSET
    computed_part_property_config: BTComputedPartPropertyConfig | Unset = UNSET
    computed_property_function_name: str | Unset = UNSET
    computed_property_function_namespace: str | Unset = UNSET
    computed_property_function_url: str | Unset = UNSET
    default_value: str | Unset = UNSET
    display_name: str | Unset = UNSET
    enum_values: list[BTMetadataEnumValue] | Unset = UNSET
    max_count: int | Unset = UNSET
    max_date: datetime.datetime | Unset = UNSET
    max_length: int | Unset = UNSET
    max_value: float | Unset = UNSET
    min_count: int | Unset = UNSET
    min_date: datetime.datetime | Unset = UNSET
    min_length: int | Unset = UNSET
    min_value: float | Unset = UNSET
    multiline: bool | Unset = UNSET
    multivalued: bool | Unset = UNSET
    pattern: str | Unset = UNSET
    publish_state: int | Unset = UNSET
    quantity_type: int | Unset = UNSET
    required: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        computed_assembly_property_aggregated_property_id = self.computed_assembly_property_aggregated_property_id

        computed_assembly_property_aggregation_operator = self.computed_assembly_property_aggregation_operator

        computed_assembly_property_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.computed_assembly_property_config, Unset):
            computed_assembly_property_config = self.computed_assembly_property_config.to_dict()

        computed_assembly_property_error_value_policy = self.computed_assembly_property_error_value_policy

        computed_assembly_property_filter_inverted = self.computed_assembly_property_filter_inverted

        computed_assembly_property_filter_property_id = self.computed_assembly_property_filter_property_id

        computed_assembly_property_missing_value_policy = self.computed_assembly_property_missing_value_policy

        computed_assembly_property_secondary_property_id = self.computed_assembly_property_secondary_property_id

        computed_part_property_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.computed_part_property_config, Unset):
            computed_part_property_config = self.computed_part_property_config.to_dict()

        computed_property_function_name = self.computed_property_function_name

        computed_property_function_namespace = self.computed_property_function_namespace

        computed_property_function_url = self.computed_property_function_url

        default_value = self.default_value

        display_name = self.display_name

        enum_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.enum_values, Unset):
            enum_values = []
            for enum_values_item_data in self.enum_values:
                enum_values_item = enum_values_item_data.to_dict()
                enum_values.append(enum_values_item)

        max_count = self.max_count

        max_date: str | Unset = UNSET
        if not isinstance(self.max_date, Unset):
            max_date = self.max_date.isoformat()

        max_length = self.max_length

        max_value = self.max_value

        min_count = self.min_count

        min_date: str | Unset = UNSET
        if not isinstance(self.min_date, Unset):
            min_date = self.min_date.isoformat()

        min_length = self.min_length

        min_value = self.min_value

        multiline = self.multiline

        multivalued = self.multivalued

        pattern = self.pattern

        publish_state = self.publish_state

        quantity_type = self.quantity_type

        required = self.required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if computed_assembly_property_aggregated_property_id is not UNSET:
            field_dict["computedAssemblyPropertyAggregatedPropertyId"] = (
                computed_assembly_property_aggregated_property_id
            )
        if computed_assembly_property_aggregation_operator is not UNSET:
            field_dict["computedAssemblyPropertyAggregationOperator"] = computed_assembly_property_aggregation_operator
        if computed_assembly_property_config is not UNSET:
            field_dict["computedAssemblyPropertyConfig"] = computed_assembly_property_config
        if computed_assembly_property_error_value_policy is not UNSET:
            field_dict["computedAssemblyPropertyErrorValuePolicy"] = computed_assembly_property_error_value_policy
        if computed_assembly_property_filter_inverted is not UNSET:
            field_dict["computedAssemblyPropertyFilterInverted"] = computed_assembly_property_filter_inverted
        if computed_assembly_property_filter_property_id is not UNSET:
            field_dict["computedAssemblyPropertyFilterPropertyId"] = computed_assembly_property_filter_property_id
        if computed_assembly_property_missing_value_policy is not UNSET:
            field_dict["computedAssemblyPropertyMissingValuePolicy"] = computed_assembly_property_missing_value_policy
        if computed_assembly_property_secondary_property_id is not UNSET:
            field_dict["computedAssemblyPropertySecondaryPropertyId"] = computed_assembly_property_secondary_property_id
        if computed_part_property_config is not UNSET:
            field_dict["computedPartPropertyConfig"] = computed_part_property_config
        if computed_property_function_name is not UNSET:
            field_dict["computedPropertyFunctionName"] = computed_property_function_name
        if computed_property_function_namespace is not UNSET:
            field_dict["computedPropertyFunctionNamespace"] = computed_property_function_namespace
        if computed_property_function_url is not UNSET:
            field_dict["computedPropertyFunctionURL"] = computed_property_function_url
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if enum_values is not UNSET:
            field_dict["enumValues"] = enum_values
        if max_count is not UNSET:
            field_dict["maxCount"] = max_count
        if max_date is not UNSET:
            field_dict["maxDate"] = max_date
        if max_length is not UNSET:
            field_dict["maxLength"] = max_length
        if max_value is not UNSET:
            field_dict["maxValue"] = max_value
        if min_count is not UNSET:
            field_dict["minCount"] = min_count
        if min_date is not UNSET:
            field_dict["minDate"] = min_date
        if min_length is not UNSET:
            field_dict["minLength"] = min_length
        if min_value is not UNSET:
            field_dict["minValue"] = min_value
        if multiline is not UNSET:
            field_dict["multiline"] = multiline
        if multivalued is not UNSET:
            field_dict["multivalued"] = multivalued
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if publish_state is not UNSET:
            field_dict["publishState"] = publish_state
        if quantity_type is not UNSET:
            field_dict["quantityType"] = quantity_type
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_computed_assembly_property_config import BTComputedAssemblyPropertyConfig
        from ..models.bt_computed_part_property_config import BTComputedPartPropertyConfig
        from ..models.bt_metadata_enum_value import BTMetadataEnumValue

        d = dict(src_dict)
        computed_assembly_property_aggregated_property_id = d.pop("computedAssemblyPropertyAggregatedPropertyId", UNSET)

        computed_assembly_property_aggregation_operator = d.pop("computedAssemblyPropertyAggregationOperator", UNSET)

        _computed_assembly_property_config = d.pop("computedAssemblyPropertyConfig", UNSET)
        computed_assembly_property_config: BTComputedAssemblyPropertyConfig | Unset
        if isinstance(_computed_assembly_property_config, Unset):
            computed_assembly_property_config = UNSET
        else:
            computed_assembly_property_config = BTComputedAssemblyPropertyConfig.from_dict(
                _computed_assembly_property_config
            )

        computed_assembly_property_error_value_policy = d.pop("computedAssemblyPropertyErrorValuePolicy", UNSET)

        computed_assembly_property_filter_inverted = d.pop("computedAssemblyPropertyFilterInverted", UNSET)

        computed_assembly_property_filter_property_id = d.pop("computedAssemblyPropertyFilterPropertyId", UNSET)

        computed_assembly_property_missing_value_policy = d.pop("computedAssemblyPropertyMissingValuePolicy", UNSET)

        computed_assembly_property_secondary_property_id = d.pop("computedAssemblyPropertySecondaryPropertyId", UNSET)

        _computed_part_property_config = d.pop("computedPartPropertyConfig", UNSET)
        computed_part_property_config: BTComputedPartPropertyConfig | Unset
        if isinstance(_computed_part_property_config, Unset):
            computed_part_property_config = UNSET
        else:
            computed_part_property_config = BTComputedPartPropertyConfig.from_dict(_computed_part_property_config)

        computed_property_function_name = d.pop("computedPropertyFunctionName", UNSET)

        computed_property_function_namespace = d.pop("computedPropertyFunctionNamespace", UNSET)

        computed_property_function_url = d.pop("computedPropertyFunctionURL", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        display_name = d.pop("displayName", UNSET)

        _enum_values = d.pop("enumValues", UNSET)
        enum_values: list[BTMetadataEnumValue] | Unset = UNSET
        if _enum_values is not UNSET:
            enum_values = []
            for enum_values_item_data in _enum_values:
                enum_values_item = BTMetadataEnumValue.from_dict(enum_values_item_data)

                enum_values.append(enum_values_item)

        max_count = d.pop("maxCount", UNSET)

        _max_date = d.pop("maxDate", UNSET)
        max_date: datetime.datetime | Unset
        if isinstance(_max_date, Unset):
            max_date = UNSET
        else:
            max_date = isoparse(_max_date)

        max_length = d.pop("maxLength", UNSET)

        max_value = d.pop("maxValue", UNSET)

        min_count = d.pop("minCount", UNSET)

        _min_date = d.pop("minDate", UNSET)
        min_date: datetime.datetime | Unset
        if isinstance(_min_date, Unset):
            min_date = UNSET
        else:
            min_date = isoparse(_min_date)

        min_length = d.pop("minLength", UNSET)

        min_value = d.pop("minValue", UNSET)

        multiline = d.pop("multiline", UNSET)

        multivalued = d.pop("multivalued", UNSET)

        pattern = d.pop("pattern", UNSET)

        publish_state = d.pop("publishState", UNSET)

        quantity_type = d.pop("quantityType", UNSET)

        required = d.pop("required", UNSET)

        bt_category_property_config_info = cls(
            computed_assembly_property_aggregated_property_id=computed_assembly_property_aggregated_property_id,
            computed_assembly_property_aggregation_operator=computed_assembly_property_aggregation_operator,
            computed_assembly_property_config=computed_assembly_property_config,
            computed_assembly_property_error_value_policy=computed_assembly_property_error_value_policy,
            computed_assembly_property_filter_inverted=computed_assembly_property_filter_inverted,
            computed_assembly_property_filter_property_id=computed_assembly_property_filter_property_id,
            computed_assembly_property_missing_value_policy=computed_assembly_property_missing_value_policy,
            computed_assembly_property_secondary_property_id=computed_assembly_property_secondary_property_id,
            computed_part_property_config=computed_part_property_config,
            computed_property_function_name=computed_property_function_name,
            computed_property_function_namespace=computed_property_function_namespace,
            computed_property_function_url=computed_property_function_url,
            default_value=default_value,
            display_name=display_name,
            enum_values=enum_values,
            max_count=max_count,
            max_date=max_date,
            max_length=max_length,
            max_value=max_value,
            min_count=min_count,
            min_date=min_date,
            min_length=min_length,
            min_value=min_value,
            multiline=multiline,
            multivalued=multivalued,
            pattern=pattern,
            publish_state=publish_state,
            quantity_type=quantity_type,
            required=required,
        )

        bt_category_property_config_info.additional_properties = d
        return bt_category_property_config_info

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
