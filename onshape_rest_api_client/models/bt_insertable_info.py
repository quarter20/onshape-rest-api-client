from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gbt_body_type import GBTBodyType
from ..models.gbt_element_type import GBTElementType
from ..models.gbt_mesh_state import GBTMeshState
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTInsertableInfo")


@_attrs_define
class BTInsertableInfo:
    """Array of items in the current page.

    Attributes:
        body_type (GBTBodyType | Unset):
        class_type (int | Unset):
        configuration (str | Unset):
        configuration_parameter_values (list[str] | Unset):
        configuration_parameters (list[str] | Unset):
        data_type (str | Unset):
        deterministic_id (str | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        element_name (str | Unset):
        element_type (GBTElementType | Unset):
        feature_id (str | Unset):
        feature_name (str | Unset):
        feature_spec (list[str] | Unset):
        feature_type (str | Unset):
        fs_computed_part_property_spec (list[str] | Unset):
        fs_table_spec (list[str] | Unset):
        has_faults (bool | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        insertable_query (str | Unset):
        is_flattened_body (bool | Unset):
        is_mesh (bool | Unset):
        mesh_state (GBTMeshState | Unset):
        microversion_id (str | Unset):
        name (str | Unset): Name of the resource.
        parent_id (str | Unset):
        part_identity (str | Unset):
        part_name (str | Unset):
        predictable_thumbnail_id (str | Unset):
        source_file_extension (str | Unset):
        thumbnail_uri (str | Unset):
        unflattened_part_deterministic_id (str | Unset):
        variable_name (str | Unset):
        version_id (str | Unset):
        version_name (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        workspace_id (str | Unset):
        workspace_name (str | Unset):
    """

    body_type: GBTBodyType | Unset = UNSET
    class_type: int | Unset = UNSET
    configuration: str | Unset = UNSET
    configuration_parameter_values: list[str] | Unset = UNSET
    configuration_parameters: list[str] | Unset = UNSET
    data_type: str | Unset = UNSET
    deterministic_id: str | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_name: str | Unset = UNSET
    element_type: GBTElementType | Unset = UNSET
    feature_id: str | Unset = UNSET
    feature_name: str | Unset = UNSET
    feature_spec: list[str] | Unset = UNSET
    feature_type: str | Unset = UNSET
    fs_computed_part_property_spec: list[str] | Unset = UNSET
    fs_table_spec: list[str] | Unset = UNSET
    has_faults: bool | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    insertable_query: str | Unset = UNSET
    is_flattened_body: bool | Unset = UNSET
    is_mesh: bool | Unset = UNSET
    mesh_state: GBTMeshState | Unset = UNSET
    microversion_id: str | Unset = UNSET
    name: str | Unset = UNSET
    parent_id: str | Unset = UNSET
    part_identity: str | Unset = UNSET
    part_name: str | Unset = UNSET
    predictable_thumbnail_id: str | Unset = UNSET
    source_file_extension: str | Unset = UNSET
    thumbnail_uri: str | Unset = UNSET
    unflattened_part_deterministic_id: str | Unset = UNSET
    variable_name: str | Unset = UNSET
    version_id: str | Unset = UNSET
    version_name: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    workspace_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body_type: str | Unset = UNSET
        if not isinstance(self.body_type, Unset):
            body_type = self.body_type.value

        class_type = self.class_type

        configuration = self.configuration

        configuration_parameter_values: list[str] | Unset = UNSET
        if not isinstance(self.configuration_parameter_values, Unset):
            configuration_parameter_values = self.configuration_parameter_values

        configuration_parameters: list[str] | Unset = UNSET
        if not isinstance(self.configuration_parameters, Unset):
            configuration_parameters = self.configuration_parameters

        data_type = self.data_type

        deterministic_id = self.deterministic_id

        document_id = self.document_id

        element_id = self.element_id

        element_name = self.element_name

        element_type: str | Unset = UNSET
        if not isinstance(self.element_type, Unset):
            element_type = self.element_type.value

        feature_id = self.feature_id

        feature_name = self.feature_name

        feature_spec: list[str] | Unset = UNSET
        if not isinstance(self.feature_spec, Unset):
            feature_spec = self.feature_spec

        feature_type = self.feature_type

        fs_computed_part_property_spec: list[str] | Unset = UNSET
        if not isinstance(self.fs_computed_part_property_spec, Unset):
            fs_computed_part_property_spec = self.fs_computed_part_property_spec

        fs_table_spec: list[str] | Unset = UNSET
        if not isinstance(self.fs_table_spec, Unset):
            fs_table_spec = self.fs_table_spec

        has_faults = self.has_faults

        href = self.href

        id = self.id

        insertable_query = self.insertable_query

        is_flattened_body = self.is_flattened_body

        is_mesh = self.is_mesh

        mesh_state: str | Unset = UNSET
        if not isinstance(self.mesh_state, Unset):
            mesh_state = self.mesh_state.value

        microversion_id = self.microversion_id

        name = self.name

        parent_id = self.parent_id

        part_identity = self.part_identity

        part_name = self.part_name

        predictable_thumbnail_id = self.predictable_thumbnail_id

        source_file_extension = self.source_file_extension

        thumbnail_uri = self.thumbnail_uri

        unflattened_part_deterministic_id = self.unflattened_part_deterministic_id

        variable_name = self.variable_name

        version_id = self.version_id

        version_name = self.version_name

        view_ref = self.view_ref

        workspace_id = self.workspace_id

        workspace_name = self.workspace_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body_type is not UNSET:
            field_dict["bodyType"] = body_type
        if class_type is not UNSET:
            field_dict["classType"] = class_type
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if configuration_parameter_values is not UNSET:
            field_dict["configurationParameterValues"] = configuration_parameter_values
        if configuration_parameters is not UNSET:
            field_dict["configurationParameters"] = configuration_parameters
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if deterministic_id is not UNSET:
            field_dict["deterministicId"] = deterministic_id
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_name is not UNSET:
            field_dict["elementName"] = element_name
        if element_type is not UNSET:
            field_dict["elementType"] = element_type
        if feature_id is not UNSET:
            field_dict["featureId"] = feature_id
        if feature_name is not UNSET:
            field_dict["featureName"] = feature_name
        if feature_spec is not UNSET:
            field_dict["featureSpec"] = feature_spec
        if feature_type is not UNSET:
            field_dict["featureType"] = feature_type
        if fs_computed_part_property_spec is not UNSET:
            field_dict["fsComputedPartPropertySpec"] = fs_computed_part_property_spec
        if fs_table_spec is not UNSET:
            field_dict["fsTableSpec"] = fs_table_spec
        if has_faults is not UNSET:
            field_dict["hasFaults"] = has_faults
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if insertable_query is not UNSET:
            field_dict["insertableQuery"] = insertable_query
        if is_flattened_body is not UNSET:
            field_dict["isFlattenedBody"] = is_flattened_body
        if is_mesh is not UNSET:
            field_dict["isMesh"] = is_mesh
        if mesh_state is not UNSET:
            field_dict["meshState"] = mesh_state
        if microversion_id is not UNSET:
            field_dict["microversionId"] = microversion_id
        if name is not UNSET:
            field_dict["name"] = name
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if part_identity is not UNSET:
            field_dict["partIdentity"] = part_identity
        if part_name is not UNSET:
            field_dict["partName"] = part_name
        if predictable_thumbnail_id is not UNSET:
            field_dict["predictableThumbnailId"] = predictable_thumbnail_id
        if source_file_extension is not UNSET:
            field_dict["sourceFileExtension"] = source_file_extension
        if thumbnail_uri is not UNSET:
            field_dict["thumbnailUri"] = thumbnail_uri
        if unflattened_part_deterministic_id is not UNSET:
            field_dict["unflattenedPartDeterministicId"] = unflattened_part_deterministic_id
        if variable_name is not UNSET:
            field_dict["variableName"] = variable_name
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if version_name is not UNSET:
            field_dict["versionName"] = version_name
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if workspace_name is not UNSET:
            field_dict["workspaceName"] = workspace_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _body_type = d.pop("bodyType", UNSET)
        body_type: GBTBodyType | Unset
        if isinstance(_body_type, Unset):
            body_type = UNSET
        else:
            body_type = GBTBodyType(_body_type)

        class_type = d.pop("classType", UNSET)

        configuration = d.pop("configuration", UNSET)

        configuration_parameter_values = cast(list[str], d.pop("configurationParameterValues", UNSET))

        configuration_parameters = cast(list[str], d.pop("configurationParameters", UNSET))

        data_type = d.pop("dataType", UNSET)

        deterministic_id = d.pop("deterministicId", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        element_name = d.pop("elementName", UNSET)

        _element_type = d.pop("elementType", UNSET)
        element_type: GBTElementType | Unset
        if isinstance(_element_type, Unset):
            element_type = UNSET
        else:
            element_type = GBTElementType(_element_type)

        feature_id = d.pop("featureId", UNSET)

        feature_name = d.pop("featureName", UNSET)

        feature_spec = cast(list[str], d.pop("featureSpec", UNSET))

        feature_type = d.pop("featureType", UNSET)

        fs_computed_part_property_spec = cast(list[str], d.pop("fsComputedPartPropertySpec", UNSET))

        fs_table_spec = cast(list[str], d.pop("fsTableSpec", UNSET))

        has_faults = d.pop("hasFaults", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        insertable_query = d.pop("insertableQuery", UNSET)

        is_flattened_body = d.pop("isFlattenedBody", UNSET)

        is_mesh = d.pop("isMesh", UNSET)

        _mesh_state = d.pop("meshState", UNSET)
        mesh_state: GBTMeshState | Unset
        if isinstance(_mesh_state, Unset):
            mesh_state = UNSET
        else:
            mesh_state = GBTMeshState(_mesh_state)

        microversion_id = d.pop("microversionId", UNSET)

        name = d.pop("name", UNSET)

        parent_id = d.pop("parentId", UNSET)

        part_identity = d.pop("partIdentity", UNSET)

        part_name = d.pop("partName", UNSET)

        predictable_thumbnail_id = d.pop("predictableThumbnailId", UNSET)

        source_file_extension = d.pop("sourceFileExtension", UNSET)

        thumbnail_uri = d.pop("thumbnailUri", UNSET)

        unflattened_part_deterministic_id = d.pop("unflattenedPartDeterministicId", UNSET)

        variable_name = d.pop("variableName", UNSET)

        version_id = d.pop("versionId", UNSET)

        version_name = d.pop("versionName", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        workspace_name = d.pop("workspaceName", UNSET)

        bt_insertable_info = cls(
            body_type=body_type,
            class_type=class_type,
            configuration=configuration,
            configuration_parameter_values=configuration_parameter_values,
            configuration_parameters=configuration_parameters,
            data_type=data_type,
            deterministic_id=deterministic_id,
            document_id=document_id,
            element_id=element_id,
            element_name=element_name,
            element_type=element_type,
            feature_id=feature_id,
            feature_name=feature_name,
            feature_spec=feature_spec,
            feature_type=feature_type,
            fs_computed_part_property_spec=fs_computed_part_property_spec,
            fs_table_spec=fs_table_spec,
            has_faults=has_faults,
            href=href,
            id=id,
            insertable_query=insertable_query,
            is_flattened_body=is_flattened_body,
            is_mesh=is_mesh,
            mesh_state=mesh_state,
            microversion_id=microversion_id,
            name=name,
            parent_id=parent_id,
            part_identity=part_identity,
            part_name=part_name,
            predictable_thumbnail_id=predictable_thumbnail_id,
            source_file_extension=source_file_extension,
            thumbnail_uri=thumbnail_uri,
            unflattened_part_deterministic_id=unflattened_part_deterministic_id,
            variable_name=variable_name,
            version_id=version_id,
            version_name=version_name,
            view_ref=view_ref,
            workspace_id=workspace_id,
            workspace_name=workspace_name,
        )

        bt_insertable_info.additional_properties = d
        return bt_insertable_info

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
