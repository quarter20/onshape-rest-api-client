from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_part_studio_item_type import GBTPartStudioItemType
from ..models.gbt_quantity_type import GBTQuantityType
from ..models.gbtui_hint import GBTUIHint
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_computed_configuration_input_spec_2525 import BTComputedConfigurationInputSpec2525
    from ..models.bt_parameter_visibility_condition_177 import BTParameterVisibilityCondition177
    from ..models.btm_parameter_1 import BTMParameter1


T = TypeVar("T", bound="BTParameterSpecReferencePartStudio1256")


@_attrs_define
class BTParameterSpecReferencePartStudio1256:
    """
    Attributes:
        additional_localized_strings (int | Unset):
        bt_type (str | Unset): Type of JSON object.
        column_name (str | Unset):
        default_value (BTMParameter1 | Unset): A list of parameter values for instantiation of the feature spec.
            Parameters are present for all defined parameters, even if not used in a specific instantiation.
        enum_options (list[str] | Unset):
        icon_uri (str | Unset):
        localizable_name (str | Unset):
        localized_name (str | Unset):
        parameter_description (str | Unset):
        parameter_id (str | Unset):
        parameter_name (str | Unset):
        quantity_type (GBTQuantityType | Unset):
        strings_to_localize (list[str] | Unset):
        ui_hint (str | Unset):
        ui_hints (list[GBTUIHint] | Unset):
        visibility_condition (BTParameterVisibilityCondition177 | Unset):
        library_definition_id (str | Unset):
        allowed_insertable_types (list[GBTPartStudioItemType] | Unset):
        computed_configuration_inputs (list[BTComputedConfigurationInputSpec2525] | Unset):
        max_number_of_picks (int | Unset):
    """

    additional_localized_strings: int | Unset = UNSET
    bt_type: str | Unset = UNSET
    column_name: str | Unset = UNSET
    default_value: BTMParameter1 | Unset = UNSET
    enum_options: list[str] | Unset = UNSET
    icon_uri: str | Unset = UNSET
    localizable_name: str | Unset = UNSET
    localized_name: str | Unset = UNSET
    parameter_description: str | Unset = UNSET
    parameter_id: str | Unset = UNSET
    parameter_name: str | Unset = UNSET
    quantity_type: GBTQuantityType | Unset = UNSET
    strings_to_localize: list[str] | Unset = UNSET
    ui_hint: str | Unset = UNSET
    ui_hints: list[GBTUIHint] | Unset = UNSET
    visibility_condition: BTParameterVisibilityCondition177 | Unset = UNSET
    library_definition_id: str | Unset = UNSET
    allowed_insertable_types: list[GBTPartStudioItemType] | Unset = UNSET
    computed_configuration_inputs: list[BTComputedConfigurationInputSpec2525] | Unset = UNSET
    max_number_of_picks: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_localized_strings = self.additional_localized_strings

        bt_type = self.bt_type

        column_name = self.column_name

        default_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_value, Unset):
            default_value = self.default_value.to_dict()

        enum_options: list[str] | Unset = UNSET
        if not isinstance(self.enum_options, Unset):
            enum_options = self.enum_options

        icon_uri = self.icon_uri

        localizable_name = self.localizable_name

        localized_name = self.localized_name

        parameter_description = self.parameter_description

        parameter_id = self.parameter_id

        parameter_name = self.parameter_name

        quantity_type: str | Unset = UNSET
        if not isinstance(self.quantity_type, Unset):
            quantity_type = self.quantity_type.value

        strings_to_localize: list[str] | Unset = UNSET
        if not isinstance(self.strings_to_localize, Unset):
            strings_to_localize = self.strings_to_localize

        ui_hint = self.ui_hint

        ui_hints: list[str] | Unset = UNSET
        if not isinstance(self.ui_hints, Unset):
            ui_hints = []
            for ui_hints_item_data in self.ui_hints:
                ui_hints_item = ui_hints_item_data.value
                ui_hints.append(ui_hints_item)

        visibility_condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.visibility_condition, Unset):
            visibility_condition = self.visibility_condition.to_dict()

        library_definition_id = self.library_definition_id

        allowed_insertable_types: list[str] | Unset = UNSET
        if not isinstance(self.allowed_insertable_types, Unset):
            allowed_insertable_types = []
            for allowed_insertable_types_item_data in self.allowed_insertable_types:
                allowed_insertable_types_item = allowed_insertable_types_item_data.value
                allowed_insertable_types.append(allowed_insertable_types_item)

        computed_configuration_inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.computed_configuration_inputs, Unset):
            computed_configuration_inputs = []
            for computed_configuration_inputs_item_data in self.computed_configuration_inputs:
                computed_configuration_inputs_item = computed_configuration_inputs_item_data.to_dict()
                computed_configuration_inputs.append(computed_configuration_inputs_item)

        max_number_of_picks = self.max_number_of_picks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_localized_strings is not UNSET:
            field_dict["additionalLocalizedStrings"] = additional_localized_strings
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if column_name is not UNSET:
            field_dict["columnName"] = column_name
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if enum_options is not UNSET:
            field_dict["enumOptions"] = enum_options
        if icon_uri is not UNSET:
            field_dict["iconUri"] = icon_uri
        if localizable_name is not UNSET:
            field_dict["localizableName"] = localizable_name
        if localized_name is not UNSET:
            field_dict["localizedName"] = localized_name
        if parameter_description is not UNSET:
            field_dict["parameterDescription"] = parameter_description
        if parameter_id is not UNSET:
            field_dict["parameterId"] = parameter_id
        if parameter_name is not UNSET:
            field_dict["parameterName"] = parameter_name
        if quantity_type is not UNSET:
            field_dict["quantityType"] = quantity_type
        if strings_to_localize is not UNSET:
            field_dict["stringsToLocalize"] = strings_to_localize
        if ui_hint is not UNSET:
            field_dict["uiHint"] = ui_hint
        if ui_hints is not UNSET:
            field_dict["uiHints"] = ui_hints
        if visibility_condition is not UNSET:
            field_dict["visibilityCondition"] = visibility_condition
        if library_definition_id is not UNSET:
            field_dict["libraryDefinitionId"] = library_definition_id
        if allowed_insertable_types is not UNSET:
            field_dict["allowedInsertableTypes"] = allowed_insertable_types
        if computed_configuration_inputs is not UNSET:
            field_dict["computedConfigurationInputs"] = computed_configuration_inputs
        if max_number_of_picks is not UNSET:
            field_dict["maxNumberOfPicks"] = max_number_of_picks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_computed_configuration_input_spec_2525 import BTComputedConfigurationInputSpec2525
        from ..models.bt_parameter_visibility_condition_177 import BTParameterVisibilityCondition177
        from ..models.btm_parameter_1 import BTMParameter1

        d = dict(src_dict)
        additional_localized_strings = d.pop("additionalLocalizedStrings", UNSET)

        bt_type = d.pop("btType", UNSET)

        column_name = d.pop("columnName", UNSET)

        _default_value = d.pop("defaultValue", UNSET)
        default_value: BTMParameter1 | Unset
        if isinstance(_default_value, Unset):
            default_value = UNSET
        else:
            default_value = BTMParameter1.from_dict(_default_value)

        enum_options = cast(list[str], d.pop("enumOptions", UNSET))

        icon_uri = d.pop("iconUri", UNSET)

        localizable_name = d.pop("localizableName", UNSET)

        localized_name = d.pop("localizedName", UNSET)

        parameter_description = d.pop("parameterDescription", UNSET)

        parameter_id = d.pop("parameterId", UNSET)

        parameter_name = d.pop("parameterName", UNSET)

        _quantity_type = d.pop("quantityType", UNSET)
        quantity_type: GBTQuantityType | Unset
        if isinstance(_quantity_type, Unset):
            quantity_type = UNSET
        else:
            quantity_type = GBTQuantityType(_quantity_type)

        strings_to_localize = cast(list[str], d.pop("stringsToLocalize", UNSET))

        ui_hint = d.pop("uiHint", UNSET)

        _ui_hints = d.pop("uiHints", UNSET)
        ui_hints: list[GBTUIHint] | Unset = UNSET
        if _ui_hints is not UNSET:
            ui_hints = []
            for ui_hints_item_data in _ui_hints:
                ui_hints_item = GBTUIHint(ui_hints_item_data)

                ui_hints.append(ui_hints_item)

        _visibility_condition = d.pop("visibilityCondition", UNSET)
        visibility_condition: BTParameterVisibilityCondition177 | Unset
        if isinstance(_visibility_condition, Unset):
            visibility_condition = UNSET
        else:
            visibility_condition = BTParameterVisibilityCondition177.from_dict(_visibility_condition)

        library_definition_id = d.pop("libraryDefinitionId", UNSET)

        _allowed_insertable_types = d.pop("allowedInsertableTypes", UNSET)
        allowed_insertable_types: list[GBTPartStudioItemType] | Unset = UNSET
        if _allowed_insertable_types is not UNSET:
            allowed_insertable_types = []
            for allowed_insertable_types_item_data in _allowed_insertable_types:
                allowed_insertable_types_item = GBTPartStudioItemType(allowed_insertable_types_item_data)

                allowed_insertable_types.append(allowed_insertable_types_item)

        _computed_configuration_inputs = d.pop("computedConfigurationInputs", UNSET)
        computed_configuration_inputs: list[BTComputedConfigurationInputSpec2525] | Unset = UNSET
        if _computed_configuration_inputs is not UNSET:
            computed_configuration_inputs = []
            for computed_configuration_inputs_item_data in _computed_configuration_inputs:
                computed_configuration_inputs_item = BTComputedConfigurationInputSpec2525.from_dict(
                    computed_configuration_inputs_item_data
                )

                computed_configuration_inputs.append(computed_configuration_inputs_item)

        max_number_of_picks = d.pop("maxNumberOfPicks", UNSET)

        bt_parameter_spec_reference_part_studio_1256 = cls(
            additional_localized_strings=additional_localized_strings,
            bt_type=bt_type,
            column_name=column_name,
            default_value=default_value,
            enum_options=enum_options,
            icon_uri=icon_uri,
            localizable_name=localizable_name,
            localized_name=localized_name,
            parameter_description=parameter_description,
            parameter_id=parameter_id,
            parameter_name=parameter_name,
            quantity_type=quantity_type,
            strings_to_localize=strings_to_localize,
            ui_hint=ui_hint,
            ui_hints=ui_hints,
            visibility_condition=visibility_condition,
            library_definition_id=library_definition_id,
            allowed_insertable_types=allowed_insertable_types,
            computed_configuration_inputs=computed_configuration_inputs,
            max_number_of_picks=max_number_of_picks,
        )

        bt_parameter_spec_reference_part_studio_1256.additional_properties = d
        return bt_parameter_spec_reference_part_studio_1256

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
