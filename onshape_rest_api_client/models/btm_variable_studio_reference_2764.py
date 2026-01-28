from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_api_configuration import BTApiConfiguration
    from ..models.bt_microversion_id_366 import BTMicroversionId366
    from ..models.bt_tree_edit_13 import BTTreeEdit13
    from ..models.btm_feature_134 import BTMFeature134
    from ..models.btm_parameter_1 import BTMParameter1
    from ..models.btm_parameter_reference_with_configuration_3028 import BTMParameterReferenceWithConfiguration3028
    from ..models.btm_suppression_state_1924 import BTMSuppressionState1924


T = TypeVar("T", bound="BTMVariableStudioReference2764")


@_attrs_define
class BTMVariableStudioReference2764:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        feature_id (str | Unset): Unique ID of the feature instance within this Part Studio.
        feature_type (str | Unset): The name of the feature spec that this feature instantiates.
        import_microversion (str | Unset): Element microversion that is being imported.
        mate_connector_feature (bool | Unset):
        name (str | Unset): User-visible name of the feature.
        namespace (str | Unset): Indicates where the feature definition lives. Features in the FeatureScript standard
            library have a namespace value of `""`. Custom features identify the Feature Studio that contains the
            definition.
        node_id (str | Unset): ID for the feature node.
        parameter_libraries (list[BTMParameter1] | Unset):
        parameters (list[BTMParameter1] | Unset): A list of parameter values for instantiation of the feature spec.
            Parameters are present for all defined parameters, even if not used in a specific instantiation.
        return_after_subfeatures (bool | Unset): For internal use only. Should always be `false`.
        sub_features (list[BTMFeature134] | Unset): List of subfeatures belonging to the feature.
        suppressed (bool | Unset): If `true`, the feature is suppressed. It will skip regeneration, denoted by a line
            through the name in the Feature list.
        suppression_configured (bool | Unset): `true` if the suppression is configured in the Part Studio.
        suppression_state (BTMSuppressionState1924 | Unset):
        variable_studio_reference (bool | Unset): If `true`, the feature references a Variable Studio.
        api_configuration (BTApiConfiguration | Unset):
        configuration (list[BTMParameter1] | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        entire_variable_studio (bool | Unset):
        is_automatic (bool | Unset):
        microversion_id (BTMicroversionId366 | Unset):
        partial_reference (bool | Unset):
        reference_id (str | Unset):
        reference_namespace (str | Unset):
        reference_parameter (BTMParameterReferenceWithConfiguration3028 | Unset):
        referencing_anything (bool | Unset):
        unset_automatic_edit (BTTreeEdit13 | Unset):
        valid_revision_reference (bool | Unset):
        variable_names (list[str] | Unset):
        version_id (str | Unset):
    """

    bt_type: str | Unset = UNSET
    feature_id: str | Unset = UNSET
    feature_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    mate_connector_feature: bool | Unset = UNSET
    name: str | Unset = UNSET
    namespace: str | Unset = UNSET
    node_id: str | Unset = UNSET
    parameter_libraries: list[BTMParameter1] | Unset = UNSET
    parameters: list[BTMParameter1] | Unset = UNSET
    return_after_subfeatures: bool | Unset = UNSET
    sub_features: list[BTMFeature134] | Unset = UNSET
    suppressed: bool | Unset = UNSET
    suppression_configured: bool | Unset = UNSET
    suppression_state: BTMSuppressionState1924 | Unset = UNSET
    variable_studio_reference: bool | Unset = UNSET
    api_configuration: BTApiConfiguration | Unset = UNSET
    configuration: list[BTMParameter1] | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    entire_variable_studio: bool | Unset = UNSET
    is_automatic: bool | Unset = UNSET
    microversion_id: BTMicroversionId366 | Unset = UNSET
    partial_reference: bool | Unset = UNSET
    reference_id: str | Unset = UNSET
    reference_namespace: str | Unset = UNSET
    reference_parameter: BTMParameterReferenceWithConfiguration3028 | Unset = UNSET
    referencing_anything: bool | Unset = UNSET
    unset_automatic_edit: BTTreeEdit13 | Unset = UNSET
    valid_revision_reference: bool | Unset = UNSET
    variable_names: list[str] | Unset = UNSET
    version_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        feature_id = self.feature_id

        feature_type = self.feature_type

        import_microversion = self.import_microversion

        mate_connector_feature = self.mate_connector_feature

        name = self.name

        namespace = self.namespace

        node_id = self.node_id

        parameter_libraries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameter_libraries, Unset):
            parameter_libraries = []
            for parameter_libraries_item_data in self.parameter_libraries:
                parameter_libraries_item = parameter_libraries_item_data.to_dict()
                parameter_libraries.append(parameter_libraries_item)

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        return_after_subfeatures = self.return_after_subfeatures

        sub_features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sub_features, Unset):
            sub_features = []
            for sub_features_item_data in self.sub_features:
                sub_features_item = sub_features_item_data.to_dict()
                sub_features.append(sub_features_item)

        suppressed = self.suppressed

        suppression_configured = self.suppression_configured

        suppression_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suppression_state, Unset):
            suppression_state = self.suppression_state.to_dict()

        variable_studio_reference = self.variable_studio_reference

        api_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.api_configuration, Unset):
            api_configuration = self.api_configuration.to_dict()

        configuration: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = []
            for configuration_item_data in self.configuration:
                configuration_item = configuration_item_data.to_dict()
                configuration.append(configuration_item)

        document_id = self.document_id

        element_id = self.element_id

        entire_variable_studio = self.entire_variable_studio

        is_automatic = self.is_automatic

        microversion_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_id, Unset):
            microversion_id = self.microversion_id.to_dict()

        partial_reference = self.partial_reference

        reference_id = self.reference_id

        reference_namespace = self.reference_namespace

        reference_parameter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reference_parameter, Unset):
            reference_parameter = self.reference_parameter.to_dict()

        referencing_anything = self.referencing_anything

        unset_automatic_edit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unset_automatic_edit, Unset):
            unset_automatic_edit = self.unset_automatic_edit.to_dict()

        valid_revision_reference = self.valid_revision_reference

        variable_names: list[str] | Unset = UNSET
        if not isinstance(self.variable_names, Unset):
            variable_names = self.variable_names

        version_id = self.version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if feature_id is not UNSET:
            field_dict["featureId"] = feature_id
        if feature_type is not UNSET:
            field_dict["featureType"] = feature_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if mate_connector_feature is not UNSET:
            field_dict["mateConnectorFeature"] = mate_connector_feature
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if parameter_libraries is not UNSET:
            field_dict["parameterLibraries"] = parameter_libraries
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if return_after_subfeatures is not UNSET:
            field_dict["returnAfterSubfeatures"] = return_after_subfeatures
        if sub_features is not UNSET:
            field_dict["subFeatures"] = sub_features
        if suppressed is not UNSET:
            field_dict["suppressed"] = suppressed
        if suppression_configured is not UNSET:
            field_dict["suppressionConfigured"] = suppression_configured
        if suppression_state is not UNSET:
            field_dict["suppressionState"] = suppression_state
        if variable_studio_reference is not UNSET:
            field_dict["variableStudioReference"] = variable_studio_reference
        if api_configuration is not UNSET:
            field_dict["apiConfiguration"] = api_configuration
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if entire_variable_studio is not UNSET:
            field_dict["entireVariableStudio"] = entire_variable_studio
        if is_automatic is not UNSET:
            field_dict["isAutomatic"] = is_automatic
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id
        if partial_reference is not UNSET:
            field_dict["partialReference"] = partial_reference
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if reference_namespace is not UNSET:
            field_dict["referenceNamespace"] = reference_namespace
        if reference_parameter is not UNSET:
            field_dict["referenceParameter"] = reference_parameter
        if referencing_anything is not UNSET:
            field_dict["referencingAnything"] = referencing_anything
        if unset_automatic_edit is not UNSET:
            field_dict["unsetAutomaticEdit"] = unset_automatic_edit
        if valid_revision_reference is not UNSET:
            field_dict["validRevisionReference"] = valid_revision_reference
        if variable_names is not UNSET:
            field_dict["variableNames"] = variable_names
        if version_id is not UNSET:
            field_dict["versionId"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_api_configuration import BTApiConfiguration
        from ..models.bt_microversion_id_366 import BTMicroversionId366
        from ..models.bt_tree_edit_13 import BTTreeEdit13
        from ..models.btm_feature_134 import BTMFeature134
        from ..models.btm_parameter_1 import BTMParameter1
        from ..models.btm_parameter_reference_with_configuration_3028 import BTMParameterReferenceWithConfiguration3028
        from ..models.btm_suppression_state_1924 import BTMSuppressionState1924

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        feature_id = d.pop("featureId", UNSET)

        feature_type = d.pop("featureType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        mate_connector_feature = d.pop("mateConnectorFeature", UNSET)

        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _parameter_libraries = d.pop("parameterLibraries", UNSET)
        parameter_libraries: list[BTMParameter1] | Unset = UNSET
        if _parameter_libraries is not UNSET:
            parameter_libraries = []
            for parameter_libraries_item_data in _parameter_libraries:
                parameter_libraries_item = BTMParameter1.from_dict(parameter_libraries_item_data)

                parameter_libraries.append(parameter_libraries_item)

        _parameters = d.pop("parameters", UNSET)
        parameters: list[BTMParameter1] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = BTMParameter1.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        return_after_subfeatures = d.pop("returnAfterSubfeatures", UNSET)

        _sub_features = d.pop("subFeatures", UNSET)
        sub_features: list[BTMFeature134] | Unset = UNSET
        if _sub_features is not UNSET:
            sub_features = []
            for sub_features_item_data in _sub_features:
                sub_features_item = BTMFeature134.from_dict(sub_features_item_data)

                sub_features.append(sub_features_item)

        suppressed = d.pop("suppressed", UNSET)

        suppression_configured = d.pop("suppressionConfigured", UNSET)

        _suppression_state = d.pop("suppressionState", UNSET)
        suppression_state: BTMSuppressionState1924 | Unset
        if isinstance(_suppression_state, Unset):
            suppression_state = UNSET
        else:
            suppression_state = BTMSuppressionState1924.from_dict(_suppression_state)

        variable_studio_reference = d.pop("variableStudioReference", UNSET)

        _api_configuration = d.pop("apiConfiguration", UNSET)
        api_configuration: BTApiConfiguration | Unset
        if isinstance(_api_configuration, Unset):
            api_configuration = UNSET
        else:
            api_configuration = BTApiConfiguration.from_dict(_api_configuration)

        _configuration = d.pop("configuration", UNSET)
        configuration: list[BTMParameter1] | Unset = UNSET
        if _configuration is not UNSET:
            configuration = []
            for configuration_item_data in _configuration:
                configuration_item = BTMParameter1.from_dict(configuration_item_data)

                configuration.append(configuration_item)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        entire_variable_studio = d.pop("entireVariableStudio", UNSET)

        is_automatic = d.pop("isAutomatic", UNSET)

        _microversion_id = d.pop("microversionId", UNSET)
        microversion_id: BTMicroversionId366 | Unset
        if isinstance(_microversion_id, Unset):
            microversion_id = UNSET
        else:
            microversion_id = BTMicroversionId366.from_dict(_microversion_id)

        partial_reference = d.pop("partialReference", UNSET)

        reference_id = d.pop("referenceId", UNSET)

        reference_namespace = d.pop("referenceNamespace", UNSET)

        _reference_parameter = d.pop("referenceParameter", UNSET)
        reference_parameter: BTMParameterReferenceWithConfiguration3028 | Unset
        if isinstance(_reference_parameter, Unset):
            reference_parameter = UNSET
        else:
            reference_parameter = BTMParameterReferenceWithConfiguration3028.from_dict(_reference_parameter)

        referencing_anything = d.pop("referencingAnything", UNSET)

        _unset_automatic_edit = d.pop("unsetAutomaticEdit", UNSET)
        unset_automatic_edit: BTTreeEdit13 | Unset
        if isinstance(_unset_automatic_edit, Unset):
            unset_automatic_edit = UNSET
        else:
            unset_automatic_edit = BTTreeEdit13.from_dict(_unset_automatic_edit)

        valid_revision_reference = d.pop("validRevisionReference", UNSET)

        variable_names = cast(list[str], d.pop("variableNames", UNSET))

        version_id = d.pop("versionId", UNSET)

        btm_variable_studio_reference_2764 = cls(
            bt_type=bt_type,
            feature_id=feature_id,
            feature_type=feature_type,
            import_microversion=import_microversion,
            mate_connector_feature=mate_connector_feature,
            name=name,
            namespace=namespace,
            node_id=node_id,
            parameter_libraries=parameter_libraries,
            parameters=parameters,
            return_after_subfeatures=return_after_subfeatures,
            sub_features=sub_features,
            suppressed=suppressed,
            suppression_configured=suppression_configured,
            suppression_state=suppression_state,
            variable_studio_reference=variable_studio_reference,
            api_configuration=api_configuration,
            configuration=configuration,
            document_id=document_id,
            element_id=element_id,
            entire_variable_studio=entire_variable_studio,
            is_automatic=is_automatic,
            microversion_id=microversion_id,
            partial_reference=partial_reference,
            reference_id=reference_id,
            reference_namespace=reference_namespace,
            reference_parameter=reference_parameter,
            referencing_anything=referencing_anything,
            unset_automatic_edit=unset_automatic_edit,
            valid_revision_reference=valid_revision_reference,
            variable_names=variable_names,
            version_id=version_id,
        )

        btm_variable_studio_reference_2764.additional_properties = d
        return btm_variable_studio_reference_2764

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
