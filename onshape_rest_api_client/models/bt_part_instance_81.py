from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_part_studio_instance_type import GBTPartStudioInstanceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_document_with_version_and_element_id import BTDocumentWithVersionAndElementId
    from ..models.bt_document_with_version_id import BTDocumentWithVersionId
    from ..models.bt_element_reference_725 import BTElementReference725
    from ..models.bt_instance_base_2263_custom_data import BTInstanceBase2263CustomData
    from ..models.bt_microversion_id_366 import BTMicroversionId366
    from ..models.bt_node_with_reference import BTNodeWithReference
    from ..models.bt_revision_custom_data_2090 import BTRevisionCustomData2090
    from ..models.btm_parameter_1 import BTMParameter1
    from ..models.btm_parameter_reference_part_studio_3302 import BTMParameterReferencePartStudio3302
    from ..models.btm_parameter_reference_with_configuration_3028 import BTMParameterReferenceWithConfiguration3028
    from ..models.btm_suppression_state_1924 import BTMSuppressionState1924
    from ..models.btpso_identity_2741 import BTPSOIdentity2741


T = TypeVar("T", bound="BTPartInstance81")


@_attrs_define
class BTPartInstance81:
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
        parent_suppressed (bool | Unset):
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
        configuration (list[BTMParameter1] | Unset):
        configured (bool | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        element_reference (BTElementReference725 | Unset):
        external_document_with_version (BTDocumentWithVersionId | Unset):
        external_document_with_version_and_element_id (BTDocumentWithVersionAndElementId | Unset):
        locked_state (BTMParameter1 | Unset): A list of parameter values for instantiation of the feature spec.
            Parameters are present for all defined parameters, even if not used in a specific instantiation.
        microversion_id (BTMicroversionId366 | Unset):
        name (str | Unset):
        node_with_reference_list (list[BTNodeWithReference] | Unset):
        parameter_libraries (list[BTMParameter1] | Unset):
        parameters (list[BTMParameter1] | Unset):
        reference_parameter (BTMParameterReferenceWithConfiguration3028 | Unset):
        version_id (str | Unset):
        version_id_if_external (str | Unset):
        part_identity (BTPSOIdentity2741 | Unset):
        part_query (str | Unset):
        part_reference (BTMParameterReferencePartStudio3302 | Unset):
        type_ (GBTPartStudioInstanceType | Unset):
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
    parent_suppressed: bool | Unset = UNSET
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
    configuration: list[BTMParameter1] | Unset = UNSET
    configured: bool | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_reference: BTElementReference725 | Unset = UNSET
    external_document_with_version: BTDocumentWithVersionId | Unset = UNSET
    external_document_with_version_and_element_id: BTDocumentWithVersionAndElementId | Unset = UNSET
    locked_state: BTMParameter1 | Unset = UNSET
    microversion_id: BTMicroversionId366 | Unset = UNSET
    name: str | Unset = UNSET
    node_with_reference_list: list[BTNodeWithReference] | Unset = UNSET
    parameter_libraries: list[BTMParameter1] | Unset = UNSET
    parameters: list[BTMParameter1] | Unset = UNSET
    reference_parameter: BTMParameterReferenceWithConfiguration3028 | Unset = UNSET
    version_id: str | Unset = UNSET
    version_id_if_external: str | Unset = UNSET
    part_identity: BTPSOIdentity2741 | Unset = UNSET
    part_query: str | Unset = UNSET
    part_reference: BTMParameterReferencePartStudio3302 | Unset = UNSET
    type_: GBTPartStudioInstanceType | Unset = UNSET
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

        parent_suppressed = self.parent_suppressed

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

        configuration: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = []
            for configuration_item_data in self.configuration:
                configuration_item = configuration_item_data.to_dict()
                configuration.append(configuration_item)

        configured = self.configured

        document_id = self.document_id

        element_id = self.element_id

        element_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.element_reference, Unset):
            element_reference = self.element_reference.to_dict()

        external_document_with_version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_document_with_version, Unset):
            external_document_with_version = self.external_document_with_version.to_dict()

        external_document_with_version_and_element_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_document_with_version_and_element_id, Unset):
            external_document_with_version_and_element_id = self.external_document_with_version_and_element_id.to_dict()

        locked_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.locked_state, Unset):
            locked_state = self.locked_state.to_dict()

        microversion_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_id, Unset):
            microversion_id = self.microversion_id.to_dict()

        name = self.name

        node_with_reference_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.node_with_reference_list, Unset):
            node_with_reference_list = []
            for node_with_reference_list_item_data in self.node_with_reference_list:
                node_with_reference_list_item = node_with_reference_list_item_data.to_dict()
                node_with_reference_list.append(node_with_reference_list_item)

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

        reference_parameter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reference_parameter, Unset):
            reference_parameter = self.reference_parameter.to_dict()

        version_id = self.version_id

        version_id_if_external = self.version_id_if_external

        part_identity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.part_identity, Unset):
            part_identity = self.part_identity.to_dict()

        part_query = self.part_query

        part_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.part_reference, Unset):
            part_reference = self.part_reference.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

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
        if parent_suppressed is not UNSET:
            field_dict["parentSuppressed"] = parent_suppressed
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
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if configured is not UNSET:
            field_dict["configured"] = configured
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_reference is not UNSET:
            field_dict["elementReference"] = element_reference
        if external_document_with_version is not UNSET:
            field_dict["externalDocumentWithVersion"] = external_document_with_version
        if external_document_with_version_and_element_id is not UNSET:
            field_dict["externalDocumentWithVersionAndElementId"] = external_document_with_version_and_element_id
        if locked_state is not UNSET:
            field_dict["lockedState"] = locked_state
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id
        if name is not UNSET:
            field_dict["name"] = name
        if node_with_reference_list is not UNSET:
            field_dict["nodeWithReferenceList"] = node_with_reference_list
        if parameter_libraries is not UNSET:
            field_dict["parameterLibraries"] = parameter_libraries
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if reference_parameter is not UNSET:
            field_dict["referenceParameter"] = reference_parameter
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if version_id_if_external is not UNSET:
            field_dict["versionIdIfExternal"] = version_id_if_external
        if part_identity is not UNSET:
            field_dict["partIdentity"] = part_identity
        if part_query is not UNSET:
            field_dict["partQuery"] = part_query
        if part_reference is not UNSET:
            field_dict["partReference"] = part_reference
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_document_with_version_and_element_id import BTDocumentWithVersionAndElementId
        from ..models.bt_document_with_version_id import BTDocumentWithVersionId
        from ..models.bt_element_reference_725 import BTElementReference725
        from ..models.bt_instance_base_2263_custom_data import BTInstanceBase2263CustomData
        from ..models.bt_microversion_id_366 import BTMicroversionId366
        from ..models.bt_node_with_reference import BTNodeWithReference
        from ..models.bt_revision_custom_data_2090 import BTRevisionCustomData2090
        from ..models.btm_parameter_1 import BTMParameter1
        from ..models.btm_parameter_reference_part_studio_3302 import BTMParameterReferencePartStudio3302
        from ..models.btm_parameter_reference_with_configuration_3028 import BTMParameterReferenceWithConfiguration3028
        from ..models.btm_suppression_state_1924 import BTMSuppressionState1924
        from ..models.btpso_identity_2741 import BTPSOIdentity2741

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

        parent_suppressed = d.pop("parentSuppressed", UNSET)

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

        _configuration = d.pop("configuration", UNSET)
        configuration: list[BTMParameter1] | Unset = UNSET
        if _configuration is not UNSET:
            configuration = []
            for configuration_item_data in _configuration:
                configuration_item = BTMParameter1.from_dict(configuration_item_data)

                configuration.append(configuration_item)

        configured = d.pop("configured", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        _element_reference = d.pop("elementReference", UNSET)
        element_reference: BTElementReference725 | Unset
        if isinstance(_element_reference, Unset):
            element_reference = UNSET
        else:
            element_reference = BTElementReference725.from_dict(_element_reference)

        _external_document_with_version = d.pop("externalDocumentWithVersion", UNSET)
        external_document_with_version: BTDocumentWithVersionId | Unset
        if isinstance(_external_document_with_version, Unset):
            external_document_with_version = UNSET
        else:
            external_document_with_version = BTDocumentWithVersionId.from_dict(_external_document_with_version)

        _external_document_with_version_and_element_id = d.pop("externalDocumentWithVersionAndElementId", UNSET)
        external_document_with_version_and_element_id: BTDocumentWithVersionAndElementId | Unset
        if isinstance(_external_document_with_version_and_element_id, Unset):
            external_document_with_version_and_element_id = UNSET
        else:
            external_document_with_version_and_element_id = BTDocumentWithVersionAndElementId.from_dict(
                _external_document_with_version_and_element_id
            )

        _locked_state = d.pop("lockedState", UNSET)
        locked_state: BTMParameter1 | Unset
        if isinstance(_locked_state, Unset):
            locked_state = UNSET
        else:
            locked_state = BTMParameter1.from_dict(_locked_state)

        _microversion_id = d.pop("microversionId", UNSET)
        microversion_id: BTMicroversionId366 | Unset
        if isinstance(_microversion_id, Unset):
            microversion_id = UNSET
        else:
            microversion_id = BTMicroversionId366.from_dict(_microversion_id)

        name = d.pop("name", UNSET)

        _node_with_reference_list = d.pop("nodeWithReferenceList", UNSET)
        node_with_reference_list: list[BTNodeWithReference] | Unset = UNSET
        if _node_with_reference_list is not UNSET:
            node_with_reference_list = []
            for node_with_reference_list_item_data in _node_with_reference_list:
                node_with_reference_list_item = BTNodeWithReference.from_dict(node_with_reference_list_item_data)

                node_with_reference_list.append(node_with_reference_list_item)

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

        _reference_parameter = d.pop("referenceParameter", UNSET)
        reference_parameter: BTMParameterReferenceWithConfiguration3028 | Unset
        if isinstance(_reference_parameter, Unset):
            reference_parameter = UNSET
        else:
            reference_parameter = BTMParameterReferenceWithConfiguration3028.from_dict(_reference_parameter)

        version_id = d.pop("versionId", UNSET)

        version_id_if_external = d.pop("versionIdIfExternal", UNSET)

        _part_identity = d.pop("partIdentity", UNSET)
        part_identity: BTPSOIdentity2741 | Unset
        if isinstance(_part_identity, Unset):
            part_identity = UNSET
        else:
            part_identity = BTPSOIdentity2741.from_dict(_part_identity)

        part_query = d.pop("partQuery", UNSET)

        _part_reference = d.pop("partReference", UNSET)
        part_reference: BTMParameterReferencePartStudio3302 | Unset
        if isinstance(_part_reference, Unset):
            part_reference = UNSET
        else:
            part_reference = BTMParameterReferencePartStudio3302.from_dict(_part_reference)

        _type_ = d.pop("type", UNSET)
        type_: GBTPartStudioInstanceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GBTPartStudioInstanceType(_type_)

        bt_part_instance_81 = cls(
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
            parent_suppressed=parent_suppressed,
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
            configuration=configuration,
            configured=configured,
            document_id=document_id,
            element_id=element_id,
            element_reference=element_reference,
            external_document_with_version=external_document_with_version,
            external_document_with_version_and_element_id=external_document_with_version_and_element_id,
            locked_state=locked_state,
            microversion_id=microversion_id,
            name=name,
            node_with_reference_list=node_with_reference_list,
            parameter_libraries=parameter_libraries,
            parameters=parameters,
            reference_parameter=reference_parameter,
            version_id=version_id,
            version_id_if_external=version_id_if_external,
            part_identity=part_identity,
            part_query=part_query,
            part_reference=part_reference,
            type_=type_,
        )

        bt_part_instance_81.additional_properties = d
        return bt_part_instance_81

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
