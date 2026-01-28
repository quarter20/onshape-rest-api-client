from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbtui_hint import GBTUIHint
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_editing_logic_2350 import BTEditingLogic2350
    from ..models.bt_feature_spec_129_parameter_id_to_spec import BTFeatureSpec129ParameterIdToSpec
    from ..models.bt_location_info_226 import BTLocationInfo226
    from ..models.bt_parameter_group_spec_3469 import BTParameterGroupSpec3469
    from ..models.bt_parameter_spec_6 import BTParameterSpec6


T = TypeVar("T", bound="BTFeatureSpec129")


@_attrs_define
class BTFeatureSpec129:
    """
    Attributes:
        additional_localized_strings (int | Unset):
        all_parameters (list[BTParameterSpec6] | Unset):
        bt_type (str | Unset): Type of JSON object.
        computed_part_property_spec (bool | Unset):
        description_image_uri (str | Unset):
        editing_logic (BTEditingLogic2350 | Unset):
        feature_name_template (str | Unset):
        feature_type (str | Unset):
        feature_type_description (str | Unset):
        feature_type_name (str | Unset):
        filter_selectors (list[str] | Unset):
        full_feature_type (str | Unset):
        groups (list[BTParameterGroupSpec3469] | Unset):
        icon_uri (str | Unset):
        language_version (int | Unset):
        linked_location_name (str | Unset):
        localizable_name (str | Unset):
        localized_name (str | Unset):
        location_infos (list[BTLocationInfo226] | Unset):
        manipulator_change_function (str | Unset):
        namespace (str | Unset):
        namespace_including_enums (str | Unset):
        namespace_the_source (bool | Unset):
        parameter_id_to_spec (BTFeatureSpec129ParameterIdToSpec | Unset):
        parameter_library_definition_ids (list[str] | Unset):
        parameters (list[BTParameterSpec6] | Unset):
        signature (str | Unset):
        source_location (BTLocationInfo226 | Unset):
        source_microversion_id (str | Unset):
        strings_to_localize (list[str] | Unset):
        table_spec (bool | Unset):
        tolerance_spec (bool | Unset):
        tooltip_template (str | Unset):
        ui_hints (list[GBTUIHint] | Unset):
        variable_studio_reference_spec (bool | Unset):
    """

    additional_localized_strings: int | Unset = UNSET
    all_parameters: list[BTParameterSpec6] | Unset = UNSET
    bt_type: str | Unset = UNSET
    computed_part_property_spec: bool | Unset = UNSET
    description_image_uri: str | Unset = UNSET
    editing_logic: BTEditingLogic2350 | Unset = UNSET
    feature_name_template: str | Unset = UNSET
    feature_type: str | Unset = UNSET
    feature_type_description: str | Unset = UNSET
    feature_type_name: str | Unset = UNSET
    filter_selectors: list[str] | Unset = UNSET
    full_feature_type: str | Unset = UNSET
    groups: list[BTParameterGroupSpec3469] | Unset = UNSET
    icon_uri: str | Unset = UNSET
    language_version: int | Unset = UNSET
    linked_location_name: str | Unset = UNSET
    localizable_name: str | Unset = UNSET
    localized_name: str | Unset = UNSET
    location_infos: list[BTLocationInfo226] | Unset = UNSET
    manipulator_change_function: str | Unset = UNSET
    namespace: str | Unset = UNSET
    namespace_including_enums: str | Unset = UNSET
    namespace_the_source: bool | Unset = UNSET
    parameter_id_to_spec: BTFeatureSpec129ParameterIdToSpec | Unset = UNSET
    parameter_library_definition_ids: list[str] | Unset = UNSET
    parameters: list[BTParameterSpec6] | Unset = UNSET
    signature: str | Unset = UNSET
    source_location: BTLocationInfo226 | Unset = UNSET
    source_microversion_id: str | Unset = UNSET
    strings_to_localize: list[str] | Unset = UNSET
    table_spec: bool | Unset = UNSET
    tolerance_spec: bool | Unset = UNSET
    tooltip_template: str | Unset = UNSET
    ui_hints: list[GBTUIHint] | Unset = UNSET
    variable_studio_reference_spec: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_localized_strings = self.additional_localized_strings

        all_parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_parameters, Unset):
            all_parameters = []
            for all_parameters_item_data in self.all_parameters:
                all_parameters_item = all_parameters_item_data.to_dict()
                all_parameters.append(all_parameters_item)

        bt_type = self.bt_type

        computed_part_property_spec = self.computed_part_property_spec

        description_image_uri = self.description_image_uri

        editing_logic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.editing_logic, Unset):
            editing_logic = self.editing_logic.to_dict()

        feature_name_template = self.feature_name_template

        feature_type = self.feature_type

        feature_type_description = self.feature_type_description

        feature_type_name = self.feature_type_name

        filter_selectors: list[str] | Unset = UNSET
        if not isinstance(self.filter_selectors, Unset):
            filter_selectors = self.filter_selectors

        full_feature_type = self.full_feature_type

        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        icon_uri = self.icon_uri

        language_version = self.language_version

        linked_location_name = self.linked_location_name

        localizable_name = self.localizable_name

        localized_name = self.localized_name

        location_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.location_infos, Unset):
            location_infos = []
            for location_infos_item_data in self.location_infos:
                location_infos_item = location_infos_item_data.to_dict()
                location_infos.append(location_infos_item)

        manipulator_change_function = self.manipulator_change_function

        namespace = self.namespace

        namespace_including_enums = self.namespace_including_enums

        namespace_the_source = self.namespace_the_source

        parameter_id_to_spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameter_id_to_spec, Unset):
            parameter_id_to_spec = self.parameter_id_to_spec.to_dict()

        parameter_library_definition_ids: list[str] | Unset = UNSET
        if not isinstance(self.parameter_library_definition_ids, Unset):
            parameter_library_definition_ids = self.parameter_library_definition_ids

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        signature = self.signature

        source_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_location, Unset):
            source_location = self.source_location.to_dict()

        source_microversion_id = self.source_microversion_id

        strings_to_localize: list[str] | Unset = UNSET
        if not isinstance(self.strings_to_localize, Unset):
            strings_to_localize = self.strings_to_localize

        table_spec = self.table_spec

        tolerance_spec = self.tolerance_spec

        tooltip_template = self.tooltip_template

        ui_hints: list[str] | Unset = UNSET
        if not isinstance(self.ui_hints, Unset):
            ui_hints = []
            for ui_hints_item_data in self.ui_hints:
                ui_hints_item = ui_hints_item_data.value
                ui_hints.append(ui_hints_item)

        variable_studio_reference_spec = self.variable_studio_reference_spec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_localized_strings is not UNSET:
            field_dict["additionalLocalizedStrings"] = additional_localized_strings
        if all_parameters is not UNSET:
            field_dict["allParameters"] = all_parameters
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if computed_part_property_spec is not UNSET:
            field_dict["computedPartPropertySpec"] = computed_part_property_spec
        if description_image_uri is not UNSET:
            field_dict["descriptionImageUri"] = description_image_uri
        if editing_logic is not UNSET:
            field_dict["editingLogic"] = editing_logic
        if feature_name_template is not UNSET:
            field_dict["featureNameTemplate"] = feature_name_template
        if feature_type is not UNSET:
            field_dict["featureType"] = feature_type
        if feature_type_description is not UNSET:
            field_dict["featureTypeDescription"] = feature_type_description
        if feature_type_name is not UNSET:
            field_dict["featureTypeName"] = feature_type_name
        if filter_selectors is not UNSET:
            field_dict["filterSelectors"] = filter_selectors
        if full_feature_type is not UNSET:
            field_dict["fullFeatureType"] = full_feature_type
        if groups is not UNSET:
            field_dict["groups"] = groups
        if icon_uri is not UNSET:
            field_dict["iconUri"] = icon_uri
        if language_version is not UNSET:
            field_dict["languageVersion"] = language_version
        if linked_location_name is not UNSET:
            field_dict["linkedLocationName"] = linked_location_name
        if localizable_name is not UNSET:
            field_dict["localizableName"] = localizable_name
        if localized_name is not UNSET:
            field_dict["localizedName"] = localized_name
        if location_infos is not UNSET:
            field_dict["locationInfos"] = location_infos
        if manipulator_change_function is not UNSET:
            field_dict["manipulatorChangeFunction"] = manipulator_change_function
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if namespace_including_enums is not UNSET:
            field_dict["namespaceIncludingEnums"] = namespace_including_enums
        if namespace_the_source is not UNSET:
            field_dict["namespaceTheSource"] = namespace_the_source
        if parameter_id_to_spec is not UNSET:
            field_dict["parameterIdToSpec"] = parameter_id_to_spec
        if parameter_library_definition_ids is not UNSET:
            field_dict["parameterLibraryDefinitionIds"] = parameter_library_definition_ids
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if signature is not UNSET:
            field_dict["signature"] = signature
        if source_location is not UNSET:
            field_dict["sourceLocation"] = source_location
        if source_microversion_id is not UNSET:
            field_dict["sourceMicroversionId"] = source_microversion_id
        if strings_to_localize is not UNSET:
            field_dict["stringsToLocalize"] = strings_to_localize
        if table_spec is not UNSET:
            field_dict["tableSpec"] = table_spec
        if tolerance_spec is not UNSET:
            field_dict["toleranceSpec"] = tolerance_spec
        if tooltip_template is not UNSET:
            field_dict["tooltipTemplate"] = tooltip_template
        if ui_hints is not UNSET:
            field_dict["uiHints"] = ui_hints
        if variable_studio_reference_spec is not UNSET:
            field_dict["variableStudioReferenceSpec"] = variable_studio_reference_spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_editing_logic_2350 import BTEditingLogic2350
        from ..models.bt_feature_spec_129_parameter_id_to_spec import BTFeatureSpec129ParameterIdToSpec
        from ..models.bt_location_info_226 import BTLocationInfo226
        from ..models.bt_parameter_group_spec_3469 import BTParameterGroupSpec3469
        from ..models.bt_parameter_spec_6 import BTParameterSpec6

        d = dict(src_dict)
        additional_localized_strings = d.pop("additionalLocalizedStrings", UNSET)

        _all_parameters = d.pop("allParameters", UNSET)
        all_parameters: list[BTParameterSpec6] | Unset = UNSET
        if _all_parameters is not UNSET:
            all_parameters = []
            for all_parameters_item_data in _all_parameters:
                all_parameters_item = BTParameterSpec6.from_dict(all_parameters_item_data)

                all_parameters.append(all_parameters_item)

        bt_type = d.pop("btType", UNSET)

        computed_part_property_spec = d.pop("computedPartPropertySpec", UNSET)

        description_image_uri = d.pop("descriptionImageUri", UNSET)

        _editing_logic = d.pop("editingLogic", UNSET)
        editing_logic: BTEditingLogic2350 | Unset
        if isinstance(_editing_logic, Unset):
            editing_logic = UNSET
        else:
            editing_logic = BTEditingLogic2350.from_dict(_editing_logic)

        feature_name_template = d.pop("featureNameTemplate", UNSET)

        feature_type = d.pop("featureType", UNSET)

        feature_type_description = d.pop("featureTypeDescription", UNSET)

        feature_type_name = d.pop("featureTypeName", UNSET)

        filter_selectors = cast(list[str], d.pop("filterSelectors", UNSET))

        full_feature_type = d.pop("fullFeatureType", UNSET)

        _groups = d.pop("groups", UNSET)
        groups: list[BTParameterGroupSpec3469] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = BTParameterGroupSpec3469.from_dict(groups_item_data)

                groups.append(groups_item)

        icon_uri = d.pop("iconUri", UNSET)

        language_version = d.pop("languageVersion", UNSET)

        linked_location_name = d.pop("linkedLocationName", UNSET)

        localizable_name = d.pop("localizableName", UNSET)

        localized_name = d.pop("localizedName", UNSET)

        _location_infos = d.pop("locationInfos", UNSET)
        location_infos: list[BTLocationInfo226] | Unset = UNSET
        if _location_infos is not UNSET:
            location_infos = []
            for location_infos_item_data in _location_infos:
                location_infos_item = BTLocationInfo226.from_dict(location_infos_item_data)

                location_infos.append(location_infos_item)

        manipulator_change_function = d.pop("manipulatorChangeFunction", UNSET)

        namespace = d.pop("namespace", UNSET)

        namespace_including_enums = d.pop("namespaceIncludingEnums", UNSET)

        namespace_the_source = d.pop("namespaceTheSource", UNSET)

        _parameter_id_to_spec = d.pop("parameterIdToSpec", UNSET)
        parameter_id_to_spec: BTFeatureSpec129ParameterIdToSpec | Unset
        if isinstance(_parameter_id_to_spec, Unset):
            parameter_id_to_spec = UNSET
        else:
            parameter_id_to_spec = BTFeatureSpec129ParameterIdToSpec.from_dict(_parameter_id_to_spec)

        parameter_library_definition_ids = cast(list[str], d.pop("parameterLibraryDefinitionIds", UNSET))

        _parameters = d.pop("parameters", UNSET)
        parameters: list[BTParameterSpec6] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = BTParameterSpec6.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        signature = d.pop("signature", UNSET)

        _source_location = d.pop("sourceLocation", UNSET)
        source_location: BTLocationInfo226 | Unset
        if isinstance(_source_location, Unset):
            source_location = UNSET
        else:
            source_location = BTLocationInfo226.from_dict(_source_location)

        source_microversion_id = d.pop("sourceMicroversionId", UNSET)

        strings_to_localize = cast(list[str], d.pop("stringsToLocalize", UNSET))

        table_spec = d.pop("tableSpec", UNSET)

        tolerance_spec = d.pop("toleranceSpec", UNSET)

        tooltip_template = d.pop("tooltipTemplate", UNSET)

        _ui_hints = d.pop("uiHints", UNSET)
        ui_hints: list[GBTUIHint] | Unset = UNSET
        if _ui_hints is not UNSET:
            ui_hints = []
            for ui_hints_item_data in _ui_hints:
                ui_hints_item = GBTUIHint(ui_hints_item_data)

                ui_hints.append(ui_hints_item)

        variable_studio_reference_spec = d.pop("variableStudioReferenceSpec", UNSET)

        bt_feature_spec_129 = cls(
            additional_localized_strings=additional_localized_strings,
            all_parameters=all_parameters,
            bt_type=bt_type,
            computed_part_property_spec=computed_part_property_spec,
            description_image_uri=description_image_uri,
            editing_logic=editing_logic,
            feature_name_template=feature_name_template,
            feature_type=feature_type,
            feature_type_description=feature_type_description,
            feature_type_name=feature_type_name,
            filter_selectors=filter_selectors,
            full_feature_type=full_feature_type,
            groups=groups,
            icon_uri=icon_uri,
            language_version=language_version,
            linked_location_name=linked_location_name,
            localizable_name=localizable_name,
            localized_name=localized_name,
            location_infos=location_infos,
            manipulator_change_function=manipulator_change_function,
            namespace=namespace,
            namespace_including_enums=namespace_including_enums,
            namespace_the_source=namespace_the_source,
            parameter_id_to_spec=parameter_id_to_spec,
            parameter_library_definition_ids=parameter_library_definition_ids,
            parameters=parameters,
            signature=signature,
            source_location=source_location,
            source_microversion_id=source_microversion_id,
            strings_to_localize=strings_to_localize,
            table_spec=table_spec,
            tolerance_spec=tolerance_spec,
            tooltip_template=tooltip_template,
            ui_hints=ui_hints,
            variable_studio_reference_spec=variable_studio_reference_spec,
        )

        bt_feature_spec_129.additional_properties = d
        return bt_feature_spec_129

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
