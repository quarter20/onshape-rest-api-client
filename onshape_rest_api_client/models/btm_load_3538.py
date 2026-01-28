from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_load_type import GBTLoadType
from ..models.gbt_quantity_type import GBTQuantityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btm_feature_134 import BTMFeature134
    from ..models.btm_individual_query_with_occurrence_base_904 import BTMIndividualQueryWithOccurrenceBase904
    from ..models.btm_load_3538_load_component_parameter_ids import BTMLoad3538LoadComponentParameterIds
    from ..models.btm_load_3538_suppressed_in_simulations import BTMLoad3538SuppressedInSimulations
    from ..models.btm_mate_connector_66 import BTMMateConnector66
    from ..models.btm_parameter_1 import BTMParameter1
    from ..models.btm_suppression_state_1924 import BTMSuppressionState1924


T = TypeVar("T", bound="BTMLoad3538")


@_attrs_define
class BTMLoad3538:
    """
    Attributes:
        auxiliary_tree_feature (bool | Unset):
        bt_type (str | Unset): Type of JSON object.
        defined_by_components (bool | Unset):
        direction_flipped (bool | Unset):
        feature_folder (bool | Unset):
        feature_id (str | Unset): Unique ID of the feature instance within this Part Studio.
        feature_list_field_index (int | Unset):
        feature_type (str | Unset): The name of the feature spec that this feature instantiates.
        fgs_base_units (str | Unset):
        field_index_for_owned_mate_connectors (int | Unset):
        import_microversion (str | Unset): Element microversion that is being imported.
        load_component_parameter_ids (BTMLoad3538LoadComponentParameterIds | Unset):
        load_region_parameter_id (str | Unset):
        load_type (GBTLoadType | Unset):
        magnitude_parameter_id (str | Unset):
        magnitude_quantity_type (GBTQuantityType | Unset):
        mate_connector_feature (bool | Unset):
        mate_connectors (list[BTMMateConnector66] | Unset):
        name (str | Unset): User-visible name of the feature.
        namespace (str | Unset): Indicates where the feature definition lives. Features in the FeatureScript standard
            library have a namespace value of `""`. Custom features identify the Feature Studio that contains the
            definition.
        node_id (str | Unset): ID for the feature node.
        occurrence_queries_from_all_configurations (list[BTMIndividualQueryWithOccurrenceBase904] | Unset):
        parameter_libraries (list[BTMParameter1] | Unset):
        parametric_instance_feature (bool | Unset):
        return_after_subfeatures (bool | Unset): For internal use only. Should always be `false`.
        structural_load (bool | Unset):
        sub_features (list[BTMFeature134] | Unset): List of subfeatures belonging to the feature.
        sub_features_not_used_in_query (list[BTMFeature134] | Unset):
        suppressed (bool | Unset): If `true`, the feature is suppressed. It will skip regeneration, denoted by a line
            through the name in the Feature list.
        suppressed_in_simulations (BTMLoad3538SuppressedInSimulations | Unset):
        suppression_configured (bool | Unset): `true` if the suppression is configured in the Part Studio.
        suppression_state (BTMSuppressionState1924 | Unset):
        variable_studio_reference (bool | Unset): If `true`, the feature references a Variable Studio.
        version (int | Unset):
    """

    auxiliary_tree_feature: bool | Unset = UNSET
    bt_type: str | Unset = UNSET
    defined_by_components: bool | Unset = UNSET
    direction_flipped: bool | Unset = UNSET
    feature_folder: bool | Unset = UNSET
    feature_id: str | Unset = UNSET
    feature_list_field_index: int | Unset = UNSET
    feature_type: str | Unset = UNSET
    fgs_base_units: str | Unset = UNSET
    field_index_for_owned_mate_connectors: int | Unset = UNSET
    import_microversion: str | Unset = UNSET
    load_component_parameter_ids: BTMLoad3538LoadComponentParameterIds | Unset = UNSET
    load_region_parameter_id: str | Unset = UNSET
    load_type: GBTLoadType | Unset = UNSET
    magnitude_parameter_id: str | Unset = UNSET
    magnitude_quantity_type: GBTQuantityType | Unset = UNSET
    mate_connector_feature: bool | Unset = UNSET
    mate_connectors: list[BTMMateConnector66] | Unset = UNSET
    name: str | Unset = UNSET
    namespace: str | Unset = UNSET
    node_id: str | Unset = UNSET
    occurrence_queries_from_all_configurations: list[BTMIndividualQueryWithOccurrenceBase904] | Unset = UNSET
    parameter_libraries: list[BTMParameter1] | Unset = UNSET
    parametric_instance_feature: bool | Unset = UNSET
    return_after_subfeatures: bool | Unset = UNSET
    structural_load: bool | Unset = UNSET
    sub_features: list[BTMFeature134] | Unset = UNSET
    sub_features_not_used_in_query: list[BTMFeature134] | Unset = UNSET
    suppressed: bool | Unset = UNSET
    suppressed_in_simulations: BTMLoad3538SuppressedInSimulations | Unset = UNSET
    suppression_configured: bool | Unset = UNSET
    suppression_state: BTMSuppressionState1924 | Unset = UNSET
    variable_studio_reference: bool | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auxiliary_tree_feature = self.auxiliary_tree_feature

        bt_type = self.bt_type

        defined_by_components = self.defined_by_components

        direction_flipped = self.direction_flipped

        feature_folder = self.feature_folder

        feature_id = self.feature_id

        feature_list_field_index = self.feature_list_field_index

        feature_type = self.feature_type

        fgs_base_units = self.fgs_base_units

        field_index_for_owned_mate_connectors = self.field_index_for_owned_mate_connectors

        import_microversion = self.import_microversion

        load_component_parameter_ids: dict[str, Any] | Unset = UNSET
        if not isinstance(self.load_component_parameter_ids, Unset):
            load_component_parameter_ids = self.load_component_parameter_ids.to_dict()

        load_region_parameter_id = self.load_region_parameter_id

        load_type: str | Unset = UNSET
        if not isinstance(self.load_type, Unset):
            load_type = self.load_type.value

        magnitude_parameter_id = self.magnitude_parameter_id

        magnitude_quantity_type: str | Unset = UNSET
        if not isinstance(self.magnitude_quantity_type, Unset):
            magnitude_quantity_type = self.magnitude_quantity_type.value

        mate_connector_feature = self.mate_connector_feature

        mate_connectors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mate_connectors, Unset):
            mate_connectors = []
            for mate_connectors_item_data in self.mate_connectors:
                mate_connectors_item = mate_connectors_item_data.to_dict()
                mate_connectors.append(mate_connectors_item)

        name = self.name

        namespace = self.namespace

        node_id = self.node_id

        occurrence_queries_from_all_configurations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.occurrence_queries_from_all_configurations, Unset):
            occurrence_queries_from_all_configurations = []
            for occurrence_queries_from_all_configurations_item_data in self.occurrence_queries_from_all_configurations:
                occurrence_queries_from_all_configurations_item = (
                    occurrence_queries_from_all_configurations_item_data.to_dict()
                )
                occurrence_queries_from_all_configurations.append(occurrence_queries_from_all_configurations_item)

        parameter_libraries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameter_libraries, Unset):
            parameter_libraries = []
            for parameter_libraries_item_data in self.parameter_libraries:
                parameter_libraries_item = parameter_libraries_item_data.to_dict()
                parameter_libraries.append(parameter_libraries_item)

        parametric_instance_feature = self.parametric_instance_feature

        return_after_subfeatures = self.return_after_subfeatures

        structural_load = self.structural_load

        sub_features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sub_features, Unset):
            sub_features = []
            for sub_features_item_data in self.sub_features:
                sub_features_item = sub_features_item_data.to_dict()
                sub_features.append(sub_features_item)

        sub_features_not_used_in_query: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sub_features_not_used_in_query, Unset):
            sub_features_not_used_in_query = []
            for sub_features_not_used_in_query_item_data in self.sub_features_not_used_in_query:
                sub_features_not_used_in_query_item = sub_features_not_used_in_query_item_data.to_dict()
                sub_features_not_used_in_query.append(sub_features_not_used_in_query_item)

        suppressed = self.suppressed

        suppressed_in_simulations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suppressed_in_simulations, Unset):
            suppressed_in_simulations = self.suppressed_in_simulations.to_dict()

        suppression_configured = self.suppression_configured

        suppression_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suppression_state, Unset):
            suppression_state = self.suppression_state.to_dict()

        variable_studio_reference = self.variable_studio_reference

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auxiliary_tree_feature is not UNSET:
            field_dict["auxiliaryTreeFeature"] = auxiliary_tree_feature
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if defined_by_components is not UNSET:
            field_dict["definedByComponents"] = defined_by_components
        if direction_flipped is not UNSET:
            field_dict["directionFlipped"] = direction_flipped
        if feature_folder is not UNSET:
            field_dict["featureFolder"] = feature_folder
        if feature_id is not UNSET:
            field_dict["featureId"] = feature_id
        if feature_list_field_index is not UNSET:
            field_dict["featureListFieldIndex"] = feature_list_field_index
        if feature_type is not UNSET:
            field_dict["featureType"] = feature_type
        if fgs_base_units is not UNSET:
            field_dict["fgsBaseUnits"] = fgs_base_units
        if field_index_for_owned_mate_connectors is not UNSET:
            field_dict["fieldIndexForOwnedMateConnectors"] = field_index_for_owned_mate_connectors
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if load_component_parameter_ids is not UNSET:
            field_dict["loadComponentParameterIds"] = load_component_parameter_ids
        if load_region_parameter_id is not UNSET:
            field_dict["loadRegionParameterId"] = load_region_parameter_id
        if load_type is not UNSET:
            field_dict["loadType"] = load_type
        if magnitude_parameter_id is not UNSET:
            field_dict["magnitudeParameterId"] = magnitude_parameter_id
        if magnitude_quantity_type is not UNSET:
            field_dict["magnitudeQuantityType"] = magnitude_quantity_type
        if mate_connector_feature is not UNSET:
            field_dict["mateConnectorFeature"] = mate_connector_feature
        if mate_connectors is not UNSET:
            field_dict["mateConnectors"] = mate_connectors
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if occurrence_queries_from_all_configurations is not UNSET:
            field_dict["occurrenceQueriesFromAllConfigurations"] = occurrence_queries_from_all_configurations
        if parameter_libraries is not UNSET:
            field_dict["parameterLibraries"] = parameter_libraries
        if parametric_instance_feature is not UNSET:
            field_dict["parametricInstanceFeature"] = parametric_instance_feature
        if return_after_subfeatures is not UNSET:
            field_dict["returnAfterSubfeatures"] = return_after_subfeatures
        if structural_load is not UNSET:
            field_dict["structuralLoad"] = structural_load
        if sub_features is not UNSET:
            field_dict["subFeatures"] = sub_features
        if sub_features_not_used_in_query is not UNSET:
            field_dict["subFeaturesNotUsedInQuery"] = sub_features_not_used_in_query
        if suppressed is not UNSET:
            field_dict["suppressed"] = suppressed
        if suppressed_in_simulations is not UNSET:
            field_dict["suppressedInSimulations"] = suppressed_in_simulations
        if suppression_configured is not UNSET:
            field_dict["suppressionConfigured"] = suppression_configured
        if suppression_state is not UNSET:
            field_dict["suppressionState"] = suppression_state
        if variable_studio_reference is not UNSET:
            field_dict["variableStudioReference"] = variable_studio_reference
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btm_feature_134 import BTMFeature134
        from ..models.btm_individual_query_with_occurrence_base_904 import BTMIndividualQueryWithOccurrenceBase904
        from ..models.btm_load_3538_load_component_parameter_ids import BTMLoad3538LoadComponentParameterIds
        from ..models.btm_load_3538_suppressed_in_simulations import BTMLoad3538SuppressedInSimulations
        from ..models.btm_mate_connector_66 import BTMMateConnector66
        from ..models.btm_parameter_1 import BTMParameter1
        from ..models.btm_suppression_state_1924 import BTMSuppressionState1924

        d = dict(src_dict)
        auxiliary_tree_feature = d.pop("auxiliaryTreeFeature", UNSET)

        bt_type = d.pop("btType", UNSET)

        defined_by_components = d.pop("definedByComponents", UNSET)

        direction_flipped = d.pop("directionFlipped", UNSET)

        feature_folder = d.pop("featureFolder", UNSET)

        feature_id = d.pop("featureId", UNSET)

        feature_list_field_index = d.pop("featureListFieldIndex", UNSET)

        feature_type = d.pop("featureType", UNSET)

        fgs_base_units = d.pop("fgsBaseUnits", UNSET)

        field_index_for_owned_mate_connectors = d.pop("fieldIndexForOwnedMateConnectors", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        _load_component_parameter_ids = d.pop("loadComponentParameterIds", UNSET)
        load_component_parameter_ids: BTMLoad3538LoadComponentParameterIds | Unset
        if isinstance(_load_component_parameter_ids, Unset):
            load_component_parameter_ids = UNSET
        else:
            load_component_parameter_ids = BTMLoad3538LoadComponentParameterIds.from_dict(_load_component_parameter_ids)

        load_region_parameter_id = d.pop("loadRegionParameterId", UNSET)

        _load_type = d.pop("loadType", UNSET)
        load_type: GBTLoadType | Unset
        if isinstance(_load_type, Unset):
            load_type = UNSET
        else:
            load_type = GBTLoadType(_load_type)

        magnitude_parameter_id = d.pop("magnitudeParameterId", UNSET)

        _magnitude_quantity_type = d.pop("magnitudeQuantityType", UNSET)
        magnitude_quantity_type: GBTQuantityType | Unset
        if isinstance(_magnitude_quantity_type, Unset):
            magnitude_quantity_type = UNSET
        else:
            magnitude_quantity_type = GBTQuantityType(_magnitude_quantity_type)

        mate_connector_feature = d.pop("mateConnectorFeature", UNSET)

        _mate_connectors = d.pop("mateConnectors", UNSET)
        mate_connectors: list[BTMMateConnector66] | Unset = UNSET
        if _mate_connectors is not UNSET:
            mate_connectors = []
            for mate_connectors_item_data in _mate_connectors:
                mate_connectors_item = BTMMateConnector66.from_dict(mate_connectors_item_data)

                mate_connectors.append(mate_connectors_item)

        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _occurrence_queries_from_all_configurations = d.pop("occurrenceQueriesFromAllConfigurations", UNSET)
        occurrence_queries_from_all_configurations: list[BTMIndividualQueryWithOccurrenceBase904] | Unset = UNSET
        if _occurrence_queries_from_all_configurations is not UNSET:
            occurrence_queries_from_all_configurations = []
            for occurrence_queries_from_all_configurations_item_data in _occurrence_queries_from_all_configurations:
                occurrence_queries_from_all_configurations_item = BTMIndividualQueryWithOccurrenceBase904.from_dict(
                    occurrence_queries_from_all_configurations_item_data
                )

                occurrence_queries_from_all_configurations.append(occurrence_queries_from_all_configurations_item)

        _parameter_libraries = d.pop("parameterLibraries", UNSET)
        parameter_libraries: list[BTMParameter1] | Unset = UNSET
        if _parameter_libraries is not UNSET:
            parameter_libraries = []
            for parameter_libraries_item_data in _parameter_libraries:
                parameter_libraries_item = BTMParameter1.from_dict(parameter_libraries_item_data)

                parameter_libraries.append(parameter_libraries_item)

        parametric_instance_feature = d.pop("parametricInstanceFeature", UNSET)

        return_after_subfeatures = d.pop("returnAfterSubfeatures", UNSET)

        structural_load = d.pop("structuralLoad", UNSET)

        _sub_features = d.pop("subFeatures", UNSET)
        sub_features: list[BTMFeature134] | Unset = UNSET
        if _sub_features is not UNSET:
            sub_features = []
            for sub_features_item_data in _sub_features:
                sub_features_item = BTMFeature134.from_dict(sub_features_item_data)

                sub_features.append(sub_features_item)

        _sub_features_not_used_in_query = d.pop("subFeaturesNotUsedInQuery", UNSET)
        sub_features_not_used_in_query: list[BTMFeature134] | Unset = UNSET
        if _sub_features_not_used_in_query is not UNSET:
            sub_features_not_used_in_query = []
            for sub_features_not_used_in_query_item_data in _sub_features_not_used_in_query:
                sub_features_not_used_in_query_item = BTMFeature134.from_dict(sub_features_not_used_in_query_item_data)

                sub_features_not_used_in_query.append(sub_features_not_used_in_query_item)

        suppressed = d.pop("suppressed", UNSET)

        _suppressed_in_simulations = d.pop("suppressedInSimulations", UNSET)
        suppressed_in_simulations: BTMLoad3538SuppressedInSimulations | Unset
        if isinstance(_suppressed_in_simulations, Unset):
            suppressed_in_simulations = UNSET
        else:
            suppressed_in_simulations = BTMLoad3538SuppressedInSimulations.from_dict(_suppressed_in_simulations)

        suppression_configured = d.pop("suppressionConfigured", UNSET)

        _suppression_state = d.pop("suppressionState", UNSET)
        suppression_state: BTMSuppressionState1924 | Unset
        if isinstance(_suppression_state, Unset):
            suppression_state = UNSET
        else:
            suppression_state = BTMSuppressionState1924.from_dict(_suppression_state)

        variable_studio_reference = d.pop("variableStudioReference", UNSET)

        version = d.pop("version", UNSET)

        btm_load_3538 = cls(
            auxiliary_tree_feature=auxiliary_tree_feature,
            bt_type=bt_type,
            defined_by_components=defined_by_components,
            direction_flipped=direction_flipped,
            feature_folder=feature_folder,
            feature_id=feature_id,
            feature_list_field_index=feature_list_field_index,
            feature_type=feature_type,
            fgs_base_units=fgs_base_units,
            field_index_for_owned_mate_connectors=field_index_for_owned_mate_connectors,
            import_microversion=import_microversion,
            load_component_parameter_ids=load_component_parameter_ids,
            load_region_parameter_id=load_region_parameter_id,
            load_type=load_type,
            magnitude_parameter_id=magnitude_parameter_id,
            magnitude_quantity_type=magnitude_quantity_type,
            mate_connector_feature=mate_connector_feature,
            mate_connectors=mate_connectors,
            name=name,
            namespace=namespace,
            node_id=node_id,
            occurrence_queries_from_all_configurations=occurrence_queries_from_all_configurations,
            parameter_libraries=parameter_libraries,
            parametric_instance_feature=parametric_instance_feature,
            return_after_subfeatures=return_after_subfeatures,
            structural_load=structural_load,
            sub_features=sub_features,
            sub_features_not_used_in_query=sub_features_not_used_in_query,
            suppressed=suppressed,
            suppressed_in_simulations=suppressed_in_simulations,
            suppression_configured=suppression_configured,
            suppression_state=suppression_state,
            variable_studio_reference=variable_studio_reference,
            version=version,
        )

        btm_load_3538.additional_properties = d
        return btm_load_3538

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
