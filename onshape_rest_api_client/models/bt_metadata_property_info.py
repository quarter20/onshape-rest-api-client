from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_metadata_enum_value_info import BTMetadataEnumValueInfo
    from ..models.bt_metadata_property_info_default_value import BTMetadataPropertyInfoDefaultValue
    from ..models.bt_metadata_property_info_initial_value import BTMetadataPropertyInfoInitialValue
    from ..models.bt_metadata_property_info_value import BTMetadataPropertyInfoValue
    from ..models.bt_metadata_property_ui_hints_info import BTMetadataPropertyUiHintsInfo
    from ..models.bt_metadata_property_validator_info import BTMetadataPropertyValidatorInfo


T = TypeVar("T", bound="BTMetadataPropertyInfo")


@_attrs_define
class BTMetadataPropertyInfo:
    """
    Attributes:
        aggregation_skipped_filtered_out_values (bool | Unset):
        computed_assembly_property (bool | Unset):
        computed_property (bool | Unset):
        computed_property_error (str | Unset):
        computed_property_eval_info (str | Unset):
        date_format (str | Unset):
        default_value (BTMetadataPropertyInfoDefaultValue | Unset):
        dirty (bool | Unset):
        editable (bool | Unset):
        editable_in_ui (bool | Unset):
        enum_values (list[BTMetadataEnumValueInfo] | Unset):
        initial_value (BTMetadataPropertyInfoInitialValue | Unset):
        multivalued (bool | Unset):
        name (str | Unset):
        property_id (str | Unset):
        property_override_status (int | Unset): 0: Unknown | 1: Not computed | 2: Computed without override | 3:
            Computed with override | 4: Computed with subassembly overrides | 5: Overridden
        property_source (int | Unset):
        required (bool | Unset):
        schema_id (str | Unset):
        ui_hints (BTMetadataPropertyUiHintsInfo | Unset):
        validator (BTMetadataPropertyValidatorInfo | Unset):
        value (BTMetadataPropertyInfoValue | Unset):
        value_type (str | Unset):
    """

    aggregation_skipped_filtered_out_values: bool | Unset = UNSET
    computed_assembly_property: bool | Unset = UNSET
    computed_property: bool | Unset = UNSET
    computed_property_error: str | Unset = UNSET
    computed_property_eval_info: str | Unset = UNSET
    date_format: str | Unset = UNSET
    default_value: BTMetadataPropertyInfoDefaultValue | Unset = UNSET
    dirty: bool | Unset = UNSET
    editable: bool | Unset = UNSET
    editable_in_ui: bool | Unset = UNSET
    enum_values: list[BTMetadataEnumValueInfo] | Unset = UNSET
    initial_value: BTMetadataPropertyInfoInitialValue | Unset = UNSET
    multivalued: bool | Unset = UNSET
    name: str | Unset = UNSET
    property_id: str | Unset = UNSET
    property_override_status: int | Unset = UNSET
    property_source: int | Unset = UNSET
    required: bool | Unset = UNSET
    schema_id: str | Unset = UNSET
    ui_hints: BTMetadataPropertyUiHintsInfo | Unset = UNSET
    validator: BTMetadataPropertyValidatorInfo | Unset = UNSET
    value: BTMetadataPropertyInfoValue | Unset = UNSET
    value_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregation_skipped_filtered_out_values = self.aggregation_skipped_filtered_out_values

        computed_assembly_property = self.computed_assembly_property

        computed_property = self.computed_property

        computed_property_error = self.computed_property_error

        computed_property_eval_info = self.computed_property_eval_info

        date_format = self.date_format

        default_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_value, Unset):
            default_value = self.default_value.to_dict()

        dirty = self.dirty

        editable = self.editable

        editable_in_ui = self.editable_in_ui

        enum_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.enum_values, Unset):
            enum_values = []
            for enum_values_item_data in self.enum_values:
                enum_values_item = enum_values_item_data.to_dict()
                enum_values.append(enum_values_item)

        initial_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.initial_value, Unset):
            initial_value = self.initial_value.to_dict()

        multivalued = self.multivalued

        name = self.name

        property_id = self.property_id

        property_override_status = self.property_override_status

        property_source = self.property_source

        required = self.required

        schema_id = self.schema_id

        ui_hints: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ui_hints, Unset):
            ui_hints = self.ui_hints.to_dict()

        validator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.validator, Unset):
            validator = self.validator.to_dict()

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        value_type = self.value_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregation_skipped_filtered_out_values is not UNSET:
            field_dict["aggregationSkippedFilteredOutValues"] = aggregation_skipped_filtered_out_values
        if computed_assembly_property is not UNSET:
            field_dict["computedAssemblyProperty"] = computed_assembly_property
        if computed_property is not UNSET:
            field_dict["computedProperty"] = computed_property
        if computed_property_error is not UNSET:
            field_dict["computedPropertyError"] = computed_property_error
        if computed_property_eval_info is not UNSET:
            field_dict["computedPropertyEvalInfo"] = computed_property_eval_info
        if date_format is not UNSET:
            field_dict["dateFormat"] = date_format
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if dirty is not UNSET:
            field_dict["dirty"] = dirty
        if editable is not UNSET:
            field_dict["editable"] = editable
        if editable_in_ui is not UNSET:
            field_dict["editableInUi"] = editable_in_ui
        if enum_values is not UNSET:
            field_dict["enumValues"] = enum_values
        if initial_value is not UNSET:
            field_dict["initialValue"] = initial_value
        if multivalued is not UNSET:
            field_dict["multivalued"] = multivalued
        if name is not UNSET:
            field_dict["name"] = name
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if property_override_status is not UNSET:
            field_dict["propertyOverrideStatus"] = property_override_status
        if property_source is not UNSET:
            field_dict["propertySource"] = property_source
        if required is not UNSET:
            field_dict["required"] = required
        if schema_id is not UNSET:
            field_dict["schemaId"] = schema_id
        if ui_hints is not UNSET:
            field_dict["uiHints"] = ui_hints
        if validator is not UNSET:
            field_dict["validator"] = validator
        if value is not UNSET:
            field_dict["value"] = value
        if value_type is not UNSET:
            field_dict["valueType"] = value_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_metadata_enum_value_info import BTMetadataEnumValueInfo
        from ..models.bt_metadata_property_info_default_value import BTMetadataPropertyInfoDefaultValue
        from ..models.bt_metadata_property_info_initial_value import BTMetadataPropertyInfoInitialValue
        from ..models.bt_metadata_property_info_value import BTMetadataPropertyInfoValue
        from ..models.bt_metadata_property_ui_hints_info import BTMetadataPropertyUiHintsInfo
        from ..models.bt_metadata_property_validator_info import BTMetadataPropertyValidatorInfo

        d = dict(src_dict)
        aggregation_skipped_filtered_out_values = d.pop("aggregationSkippedFilteredOutValues", UNSET)

        computed_assembly_property = d.pop("computedAssemblyProperty", UNSET)

        computed_property = d.pop("computedProperty", UNSET)

        computed_property_error = d.pop("computedPropertyError", UNSET)

        computed_property_eval_info = d.pop("computedPropertyEvalInfo", UNSET)

        date_format = d.pop("dateFormat", UNSET)

        _default_value = d.pop("defaultValue", UNSET)
        default_value: BTMetadataPropertyInfoDefaultValue | Unset
        if isinstance(_default_value, Unset):
            default_value = UNSET
        else:
            default_value = BTMetadataPropertyInfoDefaultValue.from_dict(_default_value)

        dirty = d.pop("dirty", UNSET)

        editable = d.pop("editable", UNSET)

        editable_in_ui = d.pop("editableInUi", UNSET)

        _enum_values = d.pop("enumValues", UNSET)
        enum_values: list[BTMetadataEnumValueInfo] | Unset = UNSET
        if _enum_values is not UNSET:
            enum_values = []
            for enum_values_item_data in _enum_values:
                enum_values_item = BTMetadataEnumValueInfo.from_dict(enum_values_item_data)

                enum_values.append(enum_values_item)

        _initial_value = d.pop("initialValue", UNSET)
        initial_value: BTMetadataPropertyInfoInitialValue | Unset
        if isinstance(_initial_value, Unset):
            initial_value = UNSET
        else:
            initial_value = BTMetadataPropertyInfoInitialValue.from_dict(_initial_value)

        multivalued = d.pop("multivalued", UNSET)

        name = d.pop("name", UNSET)

        property_id = d.pop("propertyId", UNSET)

        property_override_status = d.pop("propertyOverrideStatus", UNSET)

        property_source = d.pop("propertySource", UNSET)

        required = d.pop("required", UNSET)

        schema_id = d.pop("schemaId", UNSET)

        _ui_hints = d.pop("uiHints", UNSET)
        ui_hints: BTMetadataPropertyUiHintsInfo | Unset
        if isinstance(_ui_hints, Unset):
            ui_hints = UNSET
        else:
            ui_hints = BTMetadataPropertyUiHintsInfo.from_dict(_ui_hints)

        _validator = d.pop("validator", UNSET)
        validator: BTMetadataPropertyValidatorInfo | Unset
        if isinstance(_validator, Unset):
            validator = UNSET
        else:
            validator = BTMetadataPropertyValidatorInfo.from_dict(_validator)

        _value = d.pop("value", UNSET)
        value: BTMetadataPropertyInfoValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = BTMetadataPropertyInfoValue.from_dict(_value)

        value_type = d.pop("valueType", UNSET)

        bt_metadata_property_info = cls(
            aggregation_skipped_filtered_out_values=aggregation_skipped_filtered_out_values,
            computed_assembly_property=computed_assembly_property,
            computed_property=computed_property,
            computed_property_error=computed_property_error,
            computed_property_eval_info=computed_property_eval_info,
            date_format=date_format,
            default_value=default_value,
            dirty=dirty,
            editable=editable,
            editable_in_ui=editable_in_ui,
            enum_values=enum_values,
            initial_value=initial_value,
            multivalued=multivalued,
            name=name,
            property_id=property_id,
            property_override_status=property_override_status,
            property_source=property_source,
            required=required,
            schema_id=schema_id,
            ui_hints=ui_hints,
            validator=validator,
            value=value,
            value_type=value_type,
        )

        bt_metadata_property_info.additional_properties = d
        return bt_metadata_property_info

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
