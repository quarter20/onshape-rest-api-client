from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_document_with_version_and_element_id import BTDocumentWithVersionAndElementId
    from ..models.bt_document_with_version_id import BTDocumentWithVersionId
    from ..models.bt_element_reference_725 import BTElementReference725
    from ..models.bt_instance_with_reference_custom_data import BTInstanceWithReferenceCustomData
    from ..models.bt_microversion_id_366 import BTMicroversionId366
    from ..models.bt_node_with_reference import BTNodeWithReference
    from ..models.btm_parameter_1 import BTMParameter1
    from ..models.btm_parameter_reference_with_configuration_3028 import BTMParameterReferenceWithConfiguration3028


T = TypeVar("T", bound="BTInstanceWithReference")


@_attrs_define
class BTInstanceWithReference:
    """
    Attributes:
        configuration (list[BTMParameter1] | Unset):
        custom_data (BTInstanceWithReferenceCustomData | Unset):
        derived_assembly_mirror (bool | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        element_reference (BTElementReference725 | Unset):
        external_document_with_version (BTDocumentWithVersionId | Unset):
        external_document_with_version_and_element_id (BTDocumentWithVersionAndElementId | Unset):
        locked (bool | Unset):
        locked_state (BTInstanceWithReference | Unset):
        microversion_id (BTMicroversionId366 | Unset):
        node_id (str | Unset):
        node_with_reference_list (list[BTNodeWithReference] | Unset):
        reference_parameter (BTMParameterReferenceWithConfiguration3028 | Unset):
        standard_content (bool | Unset):
        standard_content_parameters_id (str | Unset):
        valid_revision_reference (bool | Unset):
        version_id (str | Unset):
        version_id_if_external (str | Unset):
    """

    configuration: list[BTMParameter1] | Unset = UNSET
    custom_data: BTInstanceWithReferenceCustomData | Unset = UNSET
    derived_assembly_mirror: bool | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_reference: BTElementReference725 | Unset = UNSET
    external_document_with_version: BTDocumentWithVersionId | Unset = UNSET
    external_document_with_version_and_element_id: BTDocumentWithVersionAndElementId | Unset = UNSET
    locked: bool | Unset = UNSET
    locked_state: BTInstanceWithReference | Unset = UNSET
    microversion_id: BTMicroversionId366 | Unset = UNSET
    node_id: str | Unset = UNSET
    node_with_reference_list: list[BTNodeWithReference] | Unset = UNSET
    reference_parameter: BTMParameterReferenceWithConfiguration3028 | Unset = UNSET
    standard_content: bool | Unset = UNSET
    standard_content_parameters_id: str | Unset = UNSET
    valid_revision_reference: bool | Unset = UNSET
    version_id: str | Unset = UNSET
    version_id_if_external: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = []
            for configuration_item_data in self.configuration:
                configuration_item = configuration_item_data.to_dict()
                configuration.append(configuration_item)

        custom_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_data, Unset):
            custom_data = self.custom_data.to_dict()

        derived_assembly_mirror = self.derived_assembly_mirror

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

        locked = self.locked

        locked_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.locked_state, Unset):
            locked_state = self.locked_state.to_dict()

        microversion_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_id, Unset):
            microversion_id = self.microversion_id.to_dict()

        node_id = self.node_id

        node_with_reference_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.node_with_reference_list, Unset):
            node_with_reference_list = []
            for node_with_reference_list_item_data in self.node_with_reference_list:
                node_with_reference_list_item = node_with_reference_list_item_data.to_dict()
                node_with_reference_list.append(node_with_reference_list_item)

        reference_parameter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reference_parameter, Unset):
            reference_parameter = self.reference_parameter.to_dict()

        standard_content = self.standard_content

        standard_content_parameters_id = self.standard_content_parameters_id

        valid_revision_reference = self.valid_revision_reference

        version_id = self.version_id

        version_id_if_external = self.version_id_if_external

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if custom_data is not UNSET:
            field_dict["customData"] = custom_data
        if derived_assembly_mirror is not UNSET:
            field_dict["derivedAssemblyMirror"] = derived_assembly_mirror
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
        if locked is not UNSET:
            field_dict["locked"] = locked
        if locked_state is not UNSET:
            field_dict["lockedState"] = locked_state
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if node_with_reference_list is not UNSET:
            field_dict["nodeWithReferenceList"] = node_with_reference_list
        if reference_parameter is not UNSET:
            field_dict["referenceParameter"] = reference_parameter
        if standard_content is not UNSET:
            field_dict["standardContent"] = standard_content
        if standard_content_parameters_id is not UNSET:
            field_dict["standardContentParametersId"] = standard_content_parameters_id
        if valid_revision_reference is not UNSET:
            field_dict["validRevisionReference"] = valid_revision_reference
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if version_id_if_external is not UNSET:
            field_dict["versionIdIfExternal"] = version_id_if_external

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_document_with_version_and_element_id import BTDocumentWithVersionAndElementId
        from ..models.bt_document_with_version_id import BTDocumentWithVersionId
        from ..models.bt_element_reference_725 import BTElementReference725
        from ..models.bt_instance_with_reference_custom_data import BTInstanceWithReferenceCustomData
        from ..models.bt_microversion_id_366 import BTMicroversionId366
        from ..models.bt_node_with_reference import BTNodeWithReference
        from ..models.btm_parameter_1 import BTMParameter1
        from ..models.btm_parameter_reference_with_configuration_3028 import BTMParameterReferenceWithConfiguration3028

        d = dict(src_dict)
        _configuration = d.pop("configuration", UNSET)
        configuration: list[BTMParameter1] | Unset = UNSET
        if _configuration is not UNSET:
            configuration = []
            for configuration_item_data in _configuration:
                configuration_item = BTMParameter1.from_dict(configuration_item_data)

                configuration.append(configuration_item)

        _custom_data = d.pop("customData", UNSET)
        custom_data: BTInstanceWithReferenceCustomData | Unset
        if isinstance(_custom_data, Unset):
            custom_data = UNSET
        else:
            custom_data = BTInstanceWithReferenceCustomData.from_dict(_custom_data)

        derived_assembly_mirror = d.pop("derivedAssemblyMirror", UNSET)

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

        locked = d.pop("locked", UNSET)

        _locked_state = d.pop("lockedState", UNSET)
        locked_state: BTInstanceWithReference | Unset
        if isinstance(_locked_state, Unset):
            locked_state = UNSET
        else:
            locked_state = BTInstanceWithReference.from_dict(_locked_state)

        _microversion_id = d.pop("microversionId", UNSET)
        microversion_id: BTMicroversionId366 | Unset
        if isinstance(_microversion_id, Unset):
            microversion_id = UNSET
        else:
            microversion_id = BTMicroversionId366.from_dict(_microversion_id)

        node_id = d.pop("nodeId", UNSET)

        _node_with_reference_list = d.pop("nodeWithReferenceList", UNSET)
        node_with_reference_list: list[BTNodeWithReference] | Unset = UNSET
        if _node_with_reference_list is not UNSET:
            node_with_reference_list = []
            for node_with_reference_list_item_data in _node_with_reference_list:
                node_with_reference_list_item = BTNodeWithReference.from_dict(node_with_reference_list_item_data)

                node_with_reference_list.append(node_with_reference_list_item)

        _reference_parameter = d.pop("referenceParameter", UNSET)
        reference_parameter: BTMParameterReferenceWithConfiguration3028 | Unset
        if isinstance(_reference_parameter, Unset):
            reference_parameter = UNSET
        else:
            reference_parameter = BTMParameterReferenceWithConfiguration3028.from_dict(_reference_parameter)

        standard_content = d.pop("standardContent", UNSET)

        standard_content_parameters_id = d.pop("standardContentParametersId", UNSET)

        valid_revision_reference = d.pop("validRevisionReference", UNSET)

        version_id = d.pop("versionId", UNSET)

        version_id_if_external = d.pop("versionIdIfExternal", UNSET)

        bt_instance_with_reference = cls(
            configuration=configuration,
            custom_data=custom_data,
            derived_assembly_mirror=derived_assembly_mirror,
            document_id=document_id,
            element_id=element_id,
            element_reference=element_reference,
            external_document_with_version=external_document_with_version,
            external_document_with_version_and_element_id=external_document_with_version_and_element_id,
            locked=locked,
            locked_state=locked_state,
            microversion_id=microversion_id,
            node_id=node_id,
            node_with_reference_list=node_with_reference_list,
            reference_parameter=reference_parameter,
            standard_content=standard_content,
            standard_content_parameters_id=standard_content_parameters_id,
            valid_revision_reference=valid_revision_reference,
            version_id=version_id,
            version_id_if_external=version_id_if_external,
        )

        bt_instance_with_reference.additional_properties = d
        return bt_instance_with_reference

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
