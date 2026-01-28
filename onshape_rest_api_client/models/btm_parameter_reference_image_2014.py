from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_parameter_library_relation_type import GBTParameterLibraryRelationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_element_library_reference_data_3133 import BTElementLibraryReferenceData3133


T = TypeVar("T", bound="BTMParameterReferenceImage2014")


@_attrs_define
class BTMParameterReferenceImage2014:
    """
    Attributes:
        bt_type (str | Unset): Type of JSON object.
        import_microversion (str | Unset): Element microversion that is being imported.
        library_relation_type (GBTParameterLibraryRelationType | Unset):
        node_id (str | Unset): ID of the parameter's node.
        parameter_id (str | Unset): Unique ID of the parameter.
        parameter_name (str | Unset):
        value_string (str | Unset):
        document_id (str | Unset):
        document_version_id (str | Unset):
        element_id (str | Unset):
        element_library_data (BTElementLibraryReferenceData3133 | Unset):
        feature_script_type (str | Unset):
        ids (list[str] | Unset):
        microversion_id (str | Unset):
        namespace (str | Unset):
    """

    bt_type: str | Unset = UNSET
    import_microversion: str | Unset = UNSET
    library_relation_type: GBTParameterLibraryRelationType | Unset = UNSET
    node_id: str | Unset = UNSET
    parameter_id: str | Unset = UNSET
    parameter_name: str | Unset = UNSET
    value_string: str | Unset = UNSET
    document_id: str | Unset = UNSET
    document_version_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_library_data: BTElementLibraryReferenceData3133 | Unset = UNSET
    feature_script_type: str | Unset = UNSET
    ids: list[str] | Unset = UNSET
    microversion_id: str | Unset = UNSET
    namespace: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bt_type = self.bt_type

        import_microversion = self.import_microversion

        library_relation_type: str | Unset = UNSET
        if not isinstance(self.library_relation_type, Unset):
            library_relation_type = self.library_relation_type.value

        node_id = self.node_id

        parameter_id = self.parameter_id

        parameter_name = self.parameter_name

        value_string = self.value_string

        document_id = self.document_id

        document_version_id = self.document_version_id

        element_id = self.element_id

        element_library_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.element_library_data, Unset):
            element_library_data = self.element_library_data.to_dict()

        feature_script_type = self.feature_script_type

        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        microversion_id = self.microversion_id

        namespace = self.namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bt_type is not UNSET:
            field_dict["btType"] = bt_type
        if import_microversion is not UNSET:
            field_dict["importMicroversion"] = import_microversion
        if library_relation_type is not UNSET:
            field_dict["libraryRelationType"] = library_relation_type
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if parameter_id is not UNSET:
            field_dict["parameterId"] = parameter_id
        if parameter_name is not UNSET:
            field_dict["parameterName"] = parameter_name
        if value_string is not UNSET:
            field_dict["valueString"] = value_string
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if document_version_id is not UNSET:
            field_dict["documentVersionId"] = document_version_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_library_data is not UNSET:
            field_dict["elementLibraryData"] = element_library_data
        if feature_script_type is not UNSET:
            field_dict["featureScriptType"] = feature_script_type
        if ids is not UNSET:
            field_dict["ids"] = ids
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_element_library_reference_data_3133 import BTElementLibraryReferenceData3133

        d = dict(src_dict)
        bt_type = d.pop("btType", UNSET)

        import_microversion = d.pop("importMicroversion", UNSET)

        _library_relation_type = d.pop("libraryRelationType", UNSET)
        library_relation_type: GBTParameterLibraryRelationType | Unset
        if isinstance(_library_relation_type, Unset):
            library_relation_type = UNSET
        else:
            library_relation_type = GBTParameterLibraryRelationType(_library_relation_type)

        node_id = d.pop("nodeId", UNSET)

        parameter_id = d.pop("parameterId", UNSET)

        parameter_name = d.pop("parameterName", UNSET)

        value_string = d.pop("valueString", UNSET)

        document_id = d.pop("documentId", UNSET)

        document_version_id = d.pop("documentVersionId", UNSET)

        element_id = d.pop("elementId", UNSET)

        _element_library_data = d.pop("elementLibraryData", UNSET)
        element_library_data: BTElementLibraryReferenceData3133 | Unset
        if isinstance(_element_library_data, Unset):
            element_library_data = UNSET
        else:
            element_library_data = BTElementLibraryReferenceData3133.from_dict(_element_library_data)

        feature_script_type = d.pop("featureScriptType", UNSET)

        ids = cast(list[str], d.pop("ids", UNSET))

        microversion_id = d.pop("microversionId", UNSET)

        namespace = d.pop("namespace", UNSET)

        btm_parameter_reference_image_2014 = cls(
            bt_type=bt_type,
            import_microversion=import_microversion,
            library_relation_type=library_relation_type,
            node_id=node_id,
            parameter_id=parameter_id,
            parameter_name=parameter_name,
            value_string=value_string,
            document_id=document_id,
            document_version_id=document_version_id,
            element_id=element_id,
            element_library_data=element_library_data,
            feature_script_type=feature_script_type,
            ids=ids,
            microversion_id=microversion_id,
            namespace=namespace,
        )

        btm_parameter_reference_image_2014.additional_properties = d
        return btm_parameter_reference_image_2014

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
