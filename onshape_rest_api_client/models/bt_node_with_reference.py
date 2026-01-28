from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_microversion_id_366 import BTMicroversionId366
    from ..models.btm_parameter_1 import BTMParameter1
    from ..models.btm_parameter_reference_with_configuration_3028 import BTMParameterReferenceWithConfiguration3028


T = TypeVar("T", bound="BTNodeWithReference")


@_attrs_define
class BTNodeWithReference:
    """
    Attributes:
        configuration (list[BTMParameter1] | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        microversion_id (BTMicroversionId366 | Unset):
        node_id (str | Unset):
        reference_parameter (BTMParameterReferenceWithConfiguration3028 | Unset):
        valid_revision_reference (bool | Unset):
        version_id (str | Unset):
    """

    configuration: list[BTMParameter1] | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    microversion_id: BTMicroversionId366 | Unset = UNSET
    node_id: str | Unset = UNSET
    reference_parameter: BTMParameterReferenceWithConfiguration3028 | Unset = UNSET
    valid_revision_reference: bool | Unset = UNSET
    version_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = []
            for configuration_item_data in self.configuration:
                configuration_item = configuration_item_data.to_dict()
                configuration.append(configuration_item)

        document_id = self.document_id

        element_id = self.element_id

        microversion_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.microversion_id, Unset):
            microversion_id = self.microversion_id.to_dict()

        node_id = self.node_id

        reference_parameter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reference_parameter, Unset):
            reference_parameter = self.reference_parameter.to_dict()

        valid_revision_reference = self.valid_revision_reference

        version_id = self.version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if reference_parameter is not UNSET:
            field_dict["referenceParameter"] = reference_parameter
        if valid_revision_reference is not UNSET:
            field_dict["validRevisionReference"] = valid_revision_reference
        if version_id is not UNSET:
            field_dict["versionId"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_microversion_id_366 import BTMicroversionId366
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

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        _microversion_id = d.pop("microversionId", UNSET)
        microversion_id: BTMicroversionId366 | Unset
        if isinstance(_microversion_id, Unset):
            microversion_id = UNSET
        else:
            microversion_id = BTMicroversionId366.from_dict(_microversion_id)

        node_id = d.pop("nodeId", UNSET)

        _reference_parameter = d.pop("referenceParameter", UNSET)
        reference_parameter: BTMParameterReferenceWithConfiguration3028 | Unset
        if isinstance(_reference_parameter, Unset):
            reference_parameter = UNSET
        else:
            reference_parameter = BTMParameterReferenceWithConfiguration3028.from_dict(_reference_parameter)

        valid_revision_reference = d.pop("validRevisionReference", UNSET)

        version_id = d.pop("versionId", UNSET)

        bt_node_with_reference = cls(
            configuration=configuration,
            document_id=document_id,
            element_id=element_id,
            microversion_id=microversion_id,
            node_id=node_id,
            reference_parameter=reference_parameter,
            valid_revision_reference=valid_revision_reference,
            version_id=version_id,
        )

        bt_node_with_reference.additional_properties = d
        return bt_node_with_reference

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
