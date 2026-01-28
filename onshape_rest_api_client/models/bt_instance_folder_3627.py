from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_instance_base_2263_custom_data import BTInstanceBase2263CustomData
    from ..models.bt_object_id import BTObjectId
    from ..models.bt_revision_custom_data_2090 import BTRevisionCustomData2090
    from ..models.btm_parameter_1 import BTMParameter1
    from ..models.btm_suppression_state_1924 import BTMSuppressionState1924


T = TypeVar("T", bound="BTInstanceFolder3627")


@_attrs_define
class BTInstanceFolder3627:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Microversion that resulted from the import.
        node_id (str | Unset):
        assembly_instance (bool | Unset):
        assembly_mirror (bool | Unset):
        assembly_pattern (bool | Unset):
        assembly_replicate (bool | Unset):
        cloned_instance (bool | Unset):
        custom_data (BTInstanceBase2263CustomData | Unset):
        derived_assembly_mirror (bool | Unset):
        instance_folder (bool | Unset):
        instance_name (str | Unset):
        is_flattened_part (bool | Unset):
        locked (bool | Unset):
        parametric_instance (bool | Unset):
        parametric_output_instance (bool | Unset):
        parametric_part_studio_child_instance (bool | Unset):
        parametric_part_studio_instance (bool | Unset):
        part_instance (bool | Unset):
        releasable (bool | Unset):
        revision_custom_data (BTRevisionCustomData2090 | Unset):
        standard_content (bool | Unset):
        standard_content_parameters_id (str | Unset):
        suppressed (bool | Unset):
        suppressed_field_index (int | Unset):
        suppression_configured (bool | Unset): `true` if the suppression is configured in the Part Studio.
        suppression_state (BTMSuppressionState1924 | Unset):
        suppression_state_field_index (int | Unset):
        valid_revision_reference (bool | Unset):
        version (int | Unset):
        feature_folder (bool | Unset):
        folder_end (bool | Unset):
        folder_start (bool | Unset):
        name (str | Unset):
        parameter_libraries (list[BTMParameter1] | Unset):
        parameters (list[BTMParameter1] | Unset):
        start_node_id (str | Unset):
        start_node_id_raw (BTObjectId | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    node_id: str | Unset = UNSET
    assembly_instance: bool | Unset = UNSET
    assembly_mirror: bool | Unset = UNSET
    assembly_pattern: bool | Unset = UNSET
    assembly_replicate: bool | Unset = UNSET
    cloned_instance: bool | Unset = UNSET
    custom_data: BTInstanceBase2263CustomData | Unset = UNSET
    derived_assembly_mirror: bool | Unset = UNSET
    instance_folder: bool | Unset = UNSET
    instance_name: str | Unset = UNSET
    is_flattened_part: bool | Unset = UNSET
    locked: bool | Unset = UNSET
    parametric_instance: bool | Unset = UNSET
    parametric_output_instance: bool | Unset = UNSET
    parametric_part_studio_child_instance: bool | Unset = UNSET
    parametric_part_studio_instance: bool | Unset = UNSET
    part_instance: bool | Unset = UNSET
    releasable: bool | Unset = UNSET
    revision_custom_data: BTRevisionCustomData2090 | Unset = UNSET
    standard_content: bool | Unset = UNSET
    standard_content_parameters_id: str | Unset = UNSET
    suppressed: bool | Unset = UNSET
    suppressed_field_index: int | Unset = UNSET
    suppression_configured: bool | Unset = UNSET
    suppression_state: BTMSuppressionState1924 | Unset = UNSET
    suppression_state_field_index: int | Unset = UNSET
    valid_revision_reference: bool | Unset = UNSET
    version: int | Unset = UNSET
    feature_folder: bool | Unset = UNSET
    folder_end: bool | Unset = UNSET
    folder_start: bool | Unset = UNSET
    name: str | Unset = UNSET
    parameter_libraries: list[BTMParameter1] | Unset = UNSET
    parameters: list[BTMParameter1] | Unset = UNSET
    start_node_id: str | Unset = UNSET
    start_node_id_raw: BTObjectId | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        node_id = self.node_id

        assembly_instance = self.assembly_instance

        assembly_mirror = self.assembly_mirror

        assembly_pattern = self.assembly_pattern

        assembly_replicate = self.assembly_replicate

        cloned_instance = self.cloned_instance

        custom_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_data, Unset):
            custom_data = self.custom_data.to_dict()

        derived_assembly_mirror = self.derived_assembly_mirror

        instance_folder = self.instance_folder

        instance_name = self.instance_name

        is_flattened_part = self.is_flattened_part

        locked = self.locked

        parametric_instance = self.parametric_instance

        parametric_output_instance = self.parametric_output_instance

        parametric_part_studio_child_instance = self.parametric_part_studio_child_instance

        parametric_part_studio_instance = self.parametric_part_studio_instance

        part_instance = self.part_instance

        releasable = self.releasable

        revision_custom_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.revision_custom_data, Unset):
            revision_custom_data = self.revision_custom_data.to_dict()

        standard_content = self.standard_content

        standard_content_parameters_id = self.standard_content_parameters_id

        suppressed = self.suppressed

        suppressed_field_index = self.suppressed_field_index

        suppression_configured = self.suppression_configured

        suppression_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suppression_state, Unset):
            suppression_state = self.suppression_state.to_dict()

        suppression_state_field_index = self.suppression_state_field_index

        valid_revision_reference = self.valid_revision_reference

        version = self.version

        feature_folder = self.feature_folder

        folder_end = self.folder_end

        folder_start = self.folder_start

        name = self.name

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

        start_node_id = self.start_node_id

        start_node_id_raw: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start_node_id_raw, Unset):
            start_node_id_raw = self.start_node_id_raw.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if assembly_instance is not UNSET:
            field_dict["assemblyInstance"] = assembly_instance
        if assembly_mirror is not UNSET:
            field_dict["assemblyMirror"] = assembly_mirror
        if assembly_pattern is not UNSET:
            field_dict["assemblyPattern"] = assembly_pattern
        if assembly_replicate is not UNSET:
            field_dict["assemblyReplicate"] = assembly_replicate
        if cloned_instance is not UNSET:
            field_dict["clonedInstance"] = cloned_instance
        if custom_data is not UNSET:
            field_dict["customData"] = custom_data
        if derived_assembly_mirror is not UNSET:
            field_dict["derivedAssemblyMirror"] = derived_assembly_mirror
        if instance_folder is not UNSET:
            field_dict["instanceFolder"] = instance_folder
        if instance_name is not UNSET:
            field_dict["instanceName"] = instance_name
        if is_flattened_part is not UNSET:
            field_dict["isFlattenedPart"] = is_flattened_part
        if locked is not UNSET:
            field_dict["locked"] = locked
        if parametric_instance is not UNSET:
            field_dict["parametricInstance"] = parametric_instance
        if parametric_output_instance is not UNSET:
            field_dict["parametricOutputInstance"] = parametric_output_instance
        if parametric_part_studio_child_instance is not UNSET:
            field_dict["parametricPartStudioChildInstance"] = parametric_part_studio_child_instance
        if parametric_part_studio_instance is not UNSET:
            field_dict["parametricPartStudioInstance"] = parametric_part_studio_instance
        if part_instance is not UNSET:
            field_dict["partInstance"] = part_instance
        if releasable is not UNSET:
            field_dict["releasable"] = releasable
        if revision_custom_data is not UNSET:
            field_dict["revisionCustomData"] = revision_custom_data
        if standard_content is not UNSET:
            field_dict["standardContent"] = standard_content
        if standard_content_parameters_id is not UNSET:
            field_dict["standardContentParametersId"] = standard_content_parameters_id
        if suppressed is not UNSET:
            field_dict["suppressed"] = suppressed
        if suppressed_field_index is not UNSET:
            field_dict["suppressedFieldIndex"] = suppressed_field_index
        if suppression_configured is not UNSET:
            field_dict["suppressionConfigured"] = suppression_configured
        if suppression_state is not UNSET:
            field_dict["suppressionState"] = suppression_state
        if suppression_state_field_index is not UNSET:
            field_dict["suppressionStateFieldIndex"] = suppression_state_field_index
        if valid_revision_reference is not UNSET:
            field_dict["validRevisionReference"] = valid_revision_reference
        if version is not UNSET:
            field_dict["version"] = version
        if feature_folder is not UNSET:
            field_dict["featureFolder"] = feature_folder
        if folder_end is not UNSET:
            field_dict["folderEnd"] = folder_end
        if folder_start is not UNSET:
            field_dict["folderStart"] = folder_start
        if name is not UNSET:
            field_dict["name"] = name
        if parameter_libraries is not UNSET:
            field_dict["parameterLibraries"] = parameter_libraries
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if start_node_id is not UNSET:
            field_dict["startNodeId"] = start_node_id
        if start_node_id_raw is not UNSET:
            field_dict["startNodeIdRaw"] = start_node_id_raw

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_instance_base_2263_custom_data import BTInstanceBase2263CustomData
        from ..models.bt_object_id import BTObjectId
        from ..models.bt_revision_custom_data_2090 import BTRevisionCustomData2090
        from ..models.btm_parameter_1 import BTMParameter1
        from ..models.btm_suppression_state_1924 import BTMSuppressionState1924

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        node_id = d.pop("nodeId", UNSET)

        assembly_instance = d.pop("assemblyInstance", UNSET)

        assembly_mirror = d.pop("assemblyMirror", UNSET)

        assembly_pattern = d.pop("assemblyPattern", UNSET)

        assembly_replicate = d.pop("assemblyReplicate", UNSET)

        cloned_instance = d.pop("clonedInstance", UNSET)

        _custom_data = d.pop("customData", UNSET)
        custom_data: BTInstanceBase2263CustomData | Unset
        if isinstance(_custom_data, Unset):
            custom_data = UNSET
        else:
            custom_data = BTInstanceBase2263CustomData.from_dict(_custom_data)

        derived_assembly_mirror = d.pop("derivedAssemblyMirror", UNSET)

        instance_folder = d.pop("instanceFolder", UNSET)

        instance_name = d.pop("instanceName", UNSET)

        is_flattened_part = d.pop("isFlattenedPart", UNSET)

        locked = d.pop("locked", UNSET)

        parametric_instance = d.pop("parametricInstance", UNSET)

        parametric_output_instance = d.pop("parametricOutputInstance", UNSET)

        parametric_part_studio_child_instance = d.pop("parametricPartStudioChildInstance", UNSET)

        parametric_part_studio_instance = d.pop("parametricPartStudioInstance", UNSET)

        part_instance = d.pop("partInstance", UNSET)

        releasable = d.pop("releasable", UNSET)

        _revision_custom_data = d.pop("revisionCustomData", UNSET)
        revision_custom_data: BTRevisionCustomData2090 | Unset
        if isinstance(_revision_custom_data, Unset):
            revision_custom_data = UNSET
        else:
            revision_custom_data = BTRevisionCustomData2090.from_dict(_revision_custom_data)

        standard_content = d.pop("standardContent", UNSET)

        standard_content_parameters_id = d.pop("standardContentParametersId", UNSET)

        suppressed = d.pop("suppressed", UNSET)

        suppressed_field_index = d.pop("suppressedFieldIndex", UNSET)

        suppression_configured = d.pop("suppressionConfigured", UNSET)

        _suppression_state = d.pop("suppressionState", UNSET)
        suppression_state: BTMSuppressionState1924 | Unset
        if isinstance(_suppression_state, Unset):
            suppression_state = UNSET
        else:
            suppression_state = BTMSuppressionState1924.from_dict(_suppression_state)

        suppression_state_field_index = d.pop("suppressionStateFieldIndex", UNSET)

        valid_revision_reference = d.pop("validRevisionReference", UNSET)

        version = d.pop("version", UNSET)

        feature_folder = d.pop("featureFolder", UNSET)

        folder_end = d.pop("folderEnd", UNSET)

        folder_start = d.pop("folderStart", UNSET)

        name = d.pop("name", UNSET)

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

        start_node_id = d.pop("startNodeId", UNSET)

        _start_node_id_raw = d.pop("startNodeIdRaw", UNSET)
        start_node_id_raw: BTObjectId | Unset
        if isinstance(_start_node_id_raw, Unset):
            start_node_id_raw = UNSET
        else:
            start_node_id_raw = BTObjectId.from_dict(_start_node_id_raw)

        bt_instance_folder_3627 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            node_id=node_id,
            assembly_instance=assembly_instance,
            assembly_mirror=assembly_mirror,
            assembly_pattern=assembly_pattern,
            assembly_replicate=assembly_replicate,
            cloned_instance=cloned_instance,
            custom_data=custom_data,
            derived_assembly_mirror=derived_assembly_mirror,
            instance_folder=instance_folder,
            instance_name=instance_name,
            is_flattened_part=is_flattened_part,
            locked=locked,
            parametric_instance=parametric_instance,
            parametric_output_instance=parametric_output_instance,
            parametric_part_studio_child_instance=parametric_part_studio_child_instance,
            parametric_part_studio_instance=parametric_part_studio_instance,
            part_instance=part_instance,
            releasable=releasable,
            revision_custom_data=revision_custom_data,
            standard_content=standard_content,
            standard_content_parameters_id=standard_content_parameters_id,
            suppressed=suppressed,
            suppressed_field_index=suppressed_field_index,
            suppression_configured=suppression_configured,
            suppression_state=suppression_state,
            suppression_state_field_index=suppression_state_field_index,
            valid_revision_reference=valid_revision_reference,
            version=version,
            feature_folder=feature_folder,
            folder_end=folder_end,
            folder_start=folder_start,
            name=name,
            parameter_libraries=parameter_libraries,
            parameters=parameters,
            start_node_id=start_node_id,
            start_node_id_raw=start_node_id_raw,
        )

        bt_instance_folder_3627.additional_properties = d
        return bt_instance_folder_3627

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
