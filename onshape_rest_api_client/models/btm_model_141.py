from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_cache_data_path_191 import BTCacheDataPath191
    from ..models.bt_configurable_tree_node import BTConfigurableTreeNode
    from ..models.bt_default_features_119 import BTDefaultFeatures119
    from ..models.bt_model_annotations_3945 import BTModelAnnotations3945
    from ..models.bt_model_properties_1258 import BTModelProperties1258
    from ..models.bt_part_properties_293 import BTPartProperties293
    from ..models.btm_configuration_data_1560 import BTMConfigurationData1560
    from ..models.btm_feature_134 import BTMFeature134
    from ..models.btm_import_136 import BTMImport136
    from ..models.btm_model_141_child_node_id_to_index import BTMModel141ChildNodeIdToIndex
    from ..models.btm_model_141_deep_imports import BTMModel141DeepImports
    from ..models.btm_model_141_feature_imports import BTMModel141FeatureImports
    from ..models.btm_rollback_150 import BTMRollback150
    from ..models.btm_units_default_160 import BTMUnitsDefault160
    from ..models.btm_variable_studio_reference_2764 import BTMVariableStudioReference2764
    from ..models.btp_module_id_235 import BTPModuleId235


T = TypeVar("T", bound="BTMModel141")


@_attrs_define
class BTMModel141:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Microversion that resulted from the import.
        node_id (str | Unset):
        all_features (list[BTMFeature134] | Unset):
        all_features_and_other_references (list[BTMFeature134] | Unset):
        all_features_and_sub_features (list[BTMFeature134] | Unset):
        all_features_and_sub_features_and_other_references (list[BTMFeature134] | Unset):
        child_node_id_to_index (BTMModel141ChildNodeIdToIndex | Unset):
        configurable_tree_nodes (list[BTConfigurableTreeNode] | Unset):
        configuration_data (BTMConfigurationData1560 | Unset):
        configured (bool | Unset):
        deep_imports (BTMModel141DeepImports | Unset):
        default_features (BTDefaultFeatures119 | Unset):
        default_units (BTMUnitsDefault160 | Unset):
        feature_imports (BTMModel141FeatureImports | Unset):
        first_rollback_index (int | Unset):
        import_set (list[BTPModuleId235] | Unset):
        imports (list[BTMImport136] | Unset):
        is_variable_studio (bool | Unset):
        last_feature_before_roll_back (BTMFeature134 | Unset):
        model_annotations (BTModelAnnotations3945 | Unset):
        name (str | Unset):
        part_properties (BTPartProperties293 | Unset):
        path_to_cache (BTCacheDataPath191 | Unset):
        properties (BTModelProperties1258 | Unset):
        rollback_bar (BTMRollback150 | Unset):
        rolled_back_to_end (bool | Unset):
        variable_studios (list[BTMVariableStudioReference2764] | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    node_id: str | Unset = UNSET
    all_features: list[BTMFeature134] | Unset = UNSET
    all_features_and_other_references: list[BTMFeature134] | Unset = UNSET
    all_features_and_sub_features: list[BTMFeature134] | Unset = UNSET
    all_features_and_sub_features_and_other_references: list[BTMFeature134] | Unset = UNSET
    child_node_id_to_index: BTMModel141ChildNodeIdToIndex | Unset = UNSET
    configurable_tree_nodes: list[BTConfigurableTreeNode] | Unset = UNSET
    configuration_data: BTMConfigurationData1560 | Unset = UNSET
    configured: bool | Unset = UNSET
    deep_imports: BTMModel141DeepImports | Unset = UNSET
    default_features: BTDefaultFeatures119 | Unset = UNSET
    default_units: BTMUnitsDefault160 | Unset = UNSET
    feature_imports: BTMModel141FeatureImports | Unset = UNSET
    first_rollback_index: int | Unset = UNSET
    import_set: list[BTPModuleId235] | Unset = UNSET
    imports: list[BTMImport136] | Unset = UNSET
    is_variable_studio: bool | Unset = UNSET
    last_feature_before_roll_back: BTMFeature134 | Unset = UNSET
    model_annotations: BTModelAnnotations3945 | Unset = UNSET
    name: str | Unset = UNSET
    part_properties: BTPartProperties293 | Unset = UNSET
    path_to_cache: BTCacheDataPath191 | Unset = UNSET
    properties: BTModelProperties1258 | Unset = UNSET
    rollback_bar: BTMRollback150 | Unset = UNSET
    rolled_back_to_end: bool | Unset = UNSET
    variable_studios: list[BTMVariableStudioReference2764] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        node_id = self.node_id

        all_features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_features, Unset):
            all_features = []
            for all_features_item_data in self.all_features:
                all_features_item = all_features_item_data.to_dict()
                all_features.append(all_features_item)

        all_features_and_other_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_features_and_other_references, Unset):
            all_features_and_other_references = []
            for all_features_and_other_references_item_data in self.all_features_and_other_references:
                all_features_and_other_references_item = all_features_and_other_references_item_data.to_dict()
                all_features_and_other_references.append(all_features_and_other_references_item)

        all_features_and_sub_features: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_features_and_sub_features, Unset):
            all_features_and_sub_features = []
            for all_features_and_sub_features_item_data in self.all_features_and_sub_features:
                all_features_and_sub_features_item = all_features_and_sub_features_item_data.to_dict()
                all_features_and_sub_features.append(all_features_and_sub_features_item)

        all_features_and_sub_features_and_other_references: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_features_and_sub_features_and_other_references, Unset):
            all_features_and_sub_features_and_other_references = []
            for (
                all_features_and_sub_features_and_other_references_item_data
            ) in self.all_features_and_sub_features_and_other_references:
                all_features_and_sub_features_and_other_references_item = (
                    all_features_and_sub_features_and_other_references_item_data.to_dict()
                )
                all_features_and_sub_features_and_other_references.append(
                    all_features_and_sub_features_and_other_references_item
                )

        child_node_id_to_index: dict[str, Any] | Unset = UNSET
        if not isinstance(self.child_node_id_to_index, Unset):
            child_node_id_to_index = self.child_node_id_to_index.to_dict()

        configurable_tree_nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configurable_tree_nodes, Unset):
            configurable_tree_nodes = []
            for configurable_tree_nodes_item_data in self.configurable_tree_nodes:
                configurable_tree_nodes_item = configurable_tree_nodes_item_data.to_dict()
                configurable_tree_nodes.append(configurable_tree_nodes_item)

        configuration_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration_data, Unset):
            configuration_data = self.configuration_data.to_dict()

        configured = self.configured

        deep_imports: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deep_imports, Unset):
            deep_imports = self.deep_imports.to_dict()

        default_features: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_features, Unset):
            default_features = self.default_features.to_dict()

        default_units: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_units, Unset):
            default_units = self.default_units.to_dict()

        feature_imports: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_imports, Unset):
            feature_imports = self.feature_imports.to_dict()

        first_rollback_index = self.first_rollback_index

        import_set: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.import_set, Unset):
            import_set = []
            for import_set_item_data in self.import_set:
                import_set_item = import_set_item_data.to_dict()
                import_set.append(import_set_item)

        imports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.imports, Unset):
            imports = []
            for imports_item_data in self.imports:
                imports_item = imports_item_data.to_dict()
                imports.append(imports_item)

        is_variable_studio = self.is_variable_studio

        last_feature_before_roll_back: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_feature_before_roll_back, Unset):
            last_feature_before_roll_back = self.last_feature_before_roll_back.to_dict()

        model_annotations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_annotations, Unset):
            model_annotations = self.model_annotations.to_dict()

        name = self.name

        part_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.part_properties, Unset):
            part_properties = self.part_properties.to_dict()

        path_to_cache: dict[str, Any] | Unset = UNSET
        if not isinstance(self.path_to_cache, Unset):
            path_to_cache = self.path_to_cache.to_dict()

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        rollback_bar: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rollback_bar, Unset):
            rollback_bar = self.rollback_bar.to_dict()

        rolled_back_to_end = self.rolled_back_to_end

        variable_studios: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.variable_studios, Unset):
            variable_studios = []
            for variable_studios_item_data in self.variable_studios:
                variable_studios_item = variable_studios_item_data.to_dict()
                variable_studios.append(variable_studios_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if all_features is not UNSET:
            field_dict["allFeatures"] = all_features
        if all_features_and_other_references is not UNSET:
            field_dict["allFeaturesAndOtherReferences"] = all_features_and_other_references
        if all_features_and_sub_features is not UNSET:
            field_dict["allFeaturesAndSubFeatures"] = all_features_and_sub_features
        if all_features_and_sub_features_and_other_references is not UNSET:
            field_dict["allFeaturesAndSubFeaturesAndOtherReferences"] = (
                all_features_and_sub_features_and_other_references
            )
        if child_node_id_to_index is not UNSET:
            field_dict["childNodeIdToIndex"] = child_node_id_to_index
        if configurable_tree_nodes is not UNSET:
            field_dict["configurableTreeNodes"] = configurable_tree_nodes
        if configuration_data is not UNSET:
            field_dict["configurationData"] = configuration_data
        if configured is not UNSET:
            field_dict["configured"] = configured
        if deep_imports is not UNSET:
            field_dict["deepImports"] = deep_imports
        if default_features is not UNSET:
            field_dict["defaultFeatures"] = default_features
        if default_units is not UNSET:
            field_dict["defaultUnits"] = default_units
        if feature_imports is not UNSET:
            field_dict["featureImports"] = feature_imports
        if first_rollback_index is not UNSET:
            field_dict["firstRollbackIndex"] = first_rollback_index
        if import_set is not UNSET:
            field_dict["importSet"] = import_set
        if imports is not UNSET:
            field_dict["imports"] = imports
        if is_variable_studio is not UNSET:
            field_dict["isVariableStudio"] = is_variable_studio
        if last_feature_before_roll_back is not UNSET:
            field_dict["lastFeatureBeforeRollBack"] = last_feature_before_roll_back
        if model_annotations is not UNSET:
            field_dict["modelAnnotations"] = model_annotations
        if name is not UNSET:
            field_dict["name"] = name
        if part_properties is not UNSET:
            field_dict["partProperties"] = part_properties
        if path_to_cache is not UNSET:
            field_dict["pathToCache"] = path_to_cache
        if properties is not UNSET:
            field_dict["properties"] = properties
        if rollback_bar is not UNSET:
            field_dict["rollbackBar"] = rollback_bar
        if rolled_back_to_end is not UNSET:
            field_dict["rolledBackToEnd"] = rolled_back_to_end
        if variable_studios is not UNSET:
            field_dict["variableStudios"] = variable_studios

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_cache_data_path_191 import BTCacheDataPath191
        from ..models.bt_configurable_tree_node import BTConfigurableTreeNode
        from ..models.bt_default_features_119 import BTDefaultFeatures119
        from ..models.bt_model_annotations_3945 import BTModelAnnotations3945
        from ..models.bt_model_properties_1258 import BTModelProperties1258
        from ..models.bt_part_properties_293 import BTPartProperties293
        from ..models.btm_configuration_data_1560 import BTMConfigurationData1560
        from ..models.btm_feature_134 import BTMFeature134
        from ..models.btm_import_136 import BTMImport136
        from ..models.btm_model_141_child_node_id_to_index import BTMModel141ChildNodeIdToIndex
        from ..models.btm_model_141_deep_imports import BTMModel141DeepImports
        from ..models.btm_model_141_feature_imports import BTMModel141FeatureImports
        from ..models.btm_rollback_150 import BTMRollback150
        from ..models.btm_units_default_160 import BTMUnitsDefault160
        from ..models.btm_variable_studio_reference_2764 import BTMVariableStudioReference2764
        from ..models.btp_module_id_235 import BTPModuleId235

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _all_features = d.pop("allFeatures", UNSET)
        all_features: list[BTMFeature134] | Unset = UNSET
        if _all_features is not UNSET:
            all_features = []
            for all_features_item_data in _all_features:
                all_features_item = BTMFeature134.from_dict(all_features_item_data)

                all_features.append(all_features_item)

        _all_features_and_other_references = d.pop("allFeaturesAndOtherReferences", UNSET)
        all_features_and_other_references: list[BTMFeature134] | Unset = UNSET
        if _all_features_and_other_references is not UNSET:
            all_features_and_other_references = []
            for all_features_and_other_references_item_data in _all_features_and_other_references:
                all_features_and_other_references_item = BTMFeature134.from_dict(
                    all_features_and_other_references_item_data
                )

                all_features_and_other_references.append(all_features_and_other_references_item)

        _all_features_and_sub_features = d.pop("allFeaturesAndSubFeatures", UNSET)
        all_features_and_sub_features: list[BTMFeature134] | Unset = UNSET
        if _all_features_and_sub_features is not UNSET:
            all_features_and_sub_features = []
            for all_features_and_sub_features_item_data in _all_features_and_sub_features:
                all_features_and_sub_features_item = BTMFeature134.from_dict(all_features_and_sub_features_item_data)

                all_features_and_sub_features.append(all_features_and_sub_features_item)

        _all_features_and_sub_features_and_other_references = d.pop(
            "allFeaturesAndSubFeaturesAndOtherReferences", UNSET
        )
        all_features_and_sub_features_and_other_references: list[BTMFeature134] | Unset = UNSET
        if _all_features_and_sub_features_and_other_references is not UNSET:
            all_features_and_sub_features_and_other_references = []
            for (
                all_features_and_sub_features_and_other_references_item_data
            ) in _all_features_and_sub_features_and_other_references:
                all_features_and_sub_features_and_other_references_item = BTMFeature134.from_dict(
                    all_features_and_sub_features_and_other_references_item_data
                )

                all_features_and_sub_features_and_other_references.append(
                    all_features_and_sub_features_and_other_references_item
                )

        _child_node_id_to_index = d.pop("childNodeIdToIndex", UNSET)
        child_node_id_to_index: BTMModel141ChildNodeIdToIndex | Unset
        if isinstance(_child_node_id_to_index, Unset):
            child_node_id_to_index = UNSET
        else:
            child_node_id_to_index = BTMModel141ChildNodeIdToIndex.from_dict(_child_node_id_to_index)

        _configurable_tree_nodes = d.pop("configurableTreeNodes", UNSET)
        configurable_tree_nodes: list[BTConfigurableTreeNode] | Unset = UNSET
        if _configurable_tree_nodes is not UNSET:
            configurable_tree_nodes = []
            for configurable_tree_nodes_item_data in _configurable_tree_nodes:
                configurable_tree_nodes_item = BTConfigurableTreeNode.from_dict(configurable_tree_nodes_item_data)

                configurable_tree_nodes.append(configurable_tree_nodes_item)

        _configuration_data = d.pop("configurationData", UNSET)
        configuration_data: BTMConfigurationData1560 | Unset
        if isinstance(_configuration_data, Unset):
            configuration_data = UNSET
        else:
            configuration_data = BTMConfigurationData1560.from_dict(_configuration_data)

        configured = d.pop("configured", UNSET)

        _deep_imports = d.pop("deepImports", UNSET)
        deep_imports: BTMModel141DeepImports | Unset
        if isinstance(_deep_imports, Unset):
            deep_imports = UNSET
        else:
            deep_imports = BTMModel141DeepImports.from_dict(_deep_imports)

        _default_features = d.pop("defaultFeatures", UNSET)
        default_features: BTDefaultFeatures119 | Unset
        if isinstance(_default_features, Unset):
            default_features = UNSET
        else:
            default_features = BTDefaultFeatures119.from_dict(_default_features)

        _default_units = d.pop("defaultUnits", UNSET)
        default_units: BTMUnitsDefault160 | Unset
        if isinstance(_default_units, Unset):
            default_units = UNSET
        else:
            default_units = BTMUnitsDefault160.from_dict(_default_units)

        _feature_imports = d.pop("featureImports", UNSET)
        feature_imports: BTMModel141FeatureImports | Unset
        if isinstance(_feature_imports, Unset):
            feature_imports = UNSET
        else:
            feature_imports = BTMModel141FeatureImports.from_dict(_feature_imports)

        first_rollback_index = d.pop("firstRollbackIndex", UNSET)

        _import_set = d.pop("importSet", UNSET)
        import_set: list[BTPModuleId235] | Unset = UNSET
        if _import_set is not UNSET:
            import_set = []
            for import_set_item_data in _import_set:
                import_set_item = BTPModuleId235.from_dict(import_set_item_data)

                import_set.append(import_set_item)

        _imports = d.pop("imports", UNSET)
        imports: list[BTMImport136] | Unset = UNSET
        if _imports is not UNSET:
            imports = []
            for imports_item_data in _imports:
                imports_item = BTMImport136.from_dict(imports_item_data)

                imports.append(imports_item)

        is_variable_studio = d.pop("isVariableStudio", UNSET)

        _last_feature_before_roll_back = d.pop("lastFeatureBeforeRollBack", UNSET)
        last_feature_before_roll_back: BTMFeature134 | Unset
        if isinstance(_last_feature_before_roll_back, Unset):
            last_feature_before_roll_back = UNSET
        else:
            last_feature_before_roll_back = BTMFeature134.from_dict(_last_feature_before_roll_back)

        _model_annotations = d.pop("modelAnnotations", UNSET)
        model_annotations: BTModelAnnotations3945 | Unset
        if isinstance(_model_annotations, Unset):
            model_annotations = UNSET
        else:
            model_annotations = BTModelAnnotations3945.from_dict(_model_annotations)

        name = d.pop("name", UNSET)

        _part_properties = d.pop("partProperties", UNSET)
        part_properties: BTPartProperties293 | Unset
        if isinstance(_part_properties, Unset):
            part_properties = UNSET
        else:
            part_properties = BTPartProperties293.from_dict(_part_properties)

        _path_to_cache = d.pop("pathToCache", UNSET)
        path_to_cache: BTCacheDataPath191 | Unset
        if isinstance(_path_to_cache, Unset):
            path_to_cache = UNSET
        else:
            path_to_cache = BTCacheDataPath191.from_dict(_path_to_cache)

        _properties = d.pop("properties", UNSET)
        properties: BTModelProperties1258 | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = BTModelProperties1258.from_dict(_properties)

        _rollback_bar = d.pop("rollbackBar", UNSET)
        rollback_bar: BTMRollback150 | Unset
        if isinstance(_rollback_bar, Unset):
            rollback_bar = UNSET
        else:
            rollback_bar = BTMRollback150.from_dict(_rollback_bar)

        rolled_back_to_end = d.pop("rolledBackToEnd", UNSET)

        _variable_studios = d.pop("variableStudios", UNSET)
        variable_studios: list[BTMVariableStudioReference2764] | Unset = UNSET
        if _variable_studios is not UNSET:
            variable_studios = []
            for variable_studios_item_data in _variable_studios:
                variable_studios_item = BTMVariableStudioReference2764.from_dict(variable_studios_item_data)

                variable_studios.append(variable_studios_item)

        btm_model_141 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            node_id=node_id,
            all_features=all_features,
            all_features_and_other_references=all_features_and_other_references,
            all_features_and_sub_features=all_features_and_sub_features,
            all_features_and_sub_features_and_other_references=all_features_and_sub_features_and_other_references,
            child_node_id_to_index=child_node_id_to_index,
            configurable_tree_nodes=configurable_tree_nodes,
            configuration_data=configuration_data,
            configured=configured,
            deep_imports=deep_imports,
            default_features=default_features,
            default_units=default_units,
            feature_imports=feature_imports,
            first_rollback_index=first_rollback_index,
            import_set=import_set,
            imports=imports,
            is_variable_studio=is_variable_studio,
            last_feature_before_roll_back=last_feature_before_roll_back,
            model_annotations=model_annotations,
            name=name,
            part_properties=part_properties,
            path_to_cache=path_to_cache,
            properties=properties,
            rollback_bar=rollback_bar,
            rolled_back_to_end=rolled_back_to_end,
            variable_studios=variable_studios,
        )

        btm_model_141.additional_properties = d
        return btm_model_141

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
