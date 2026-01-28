from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.btm_feature_134 import BTMFeature134
    from ..models.btm_parameter_1 import BTMParameter1
    from ..models.btm_sketch_constraint_2 import BTMSketchConstraint2
    from ..models.btm_sketch_geom_entity_5 import BTMSketchGeomEntity5
    from ..models.btm_suppression_state_1924 import BTMSuppressionState1924


T = TypeVar("T", bound="BTMSketch151")


@_attrs_define
class BTMSketch151:
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
        constraints (list[BTMSketchConstraint2] | Unset):
        entities (list[BTMSketchGeomEntity5] | Unset):
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
    constraints: list[BTMSketchConstraint2] | Unset = UNSET
    entities: list[BTMSketchGeomEntity5] | Unset = UNSET
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

        constraints: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.constraints, Unset):
            constraints = []
            for constraints_item_data in self.constraints:
                constraints_item = constraints_item_data.to_dict()
                constraints.append(constraints_item)

        entities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entities, Unset):
            entities = []
            for entities_item_data in self.entities:
                entities_item = entities_item_data.to_dict()
                entities.append(entities_item)

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
        if constraints is not UNSET:
            field_dict["constraints"] = constraints
        if entities is not UNSET:
            field_dict["entities"] = entities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.btm_feature_134 import BTMFeature134
        from ..models.btm_parameter_1 import BTMParameter1
        from ..models.btm_sketch_constraint_2 import BTMSketchConstraint2
        from ..models.btm_sketch_geom_entity_5 import BTMSketchGeomEntity5
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

        _constraints = d.pop("constraints", UNSET)
        constraints: list[BTMSketchConstraint2] | Unset = UNSET
        if _constraints is not UNSET:
            constraints = []
            for constraints_item_data in _constraints:
                constraints_item = BTMSketchConstraint2.from_dict(constraints_item_data)

                constraints.append(constraints_item)

        _entities = d.pop("entities", UNSET)
        entities: list[BTMSketchGeomEntity5] | Unset = UNSET
        if _entities is not UNSET:
            entities = []
            for entities_item_data in _entities:
                entities_item = BTMSketchGeomEntity5.from_dict(entities_item_data)

                entities.append(entities_item)

        btm_sketch_151 = cls(
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
            constraints=constraints,
            entities=entities,
        )

        btm_sketch_151.additional_properties = d
        return btm_sketch_151

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
