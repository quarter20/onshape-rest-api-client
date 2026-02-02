from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_view_data_params import BTViewDataParams
    from ..models.coordinates_params import CoordinatesParams


T = TypeVar("T", bound="BTCommentParams")


@_attrs_define
class BTCommentParams:
    """
    Attributes:
        annotation_id (str | Unset):
        annotation_type (int | Unset):
        assembly_feature (str | Unset):
        assignee (str | Unset): Assign the comment during creation. Comments cannot be reassigned during an update at
            this time.
        coordinates (CoordinatesParams | Unset):
        dimension_constraint_id (str | Unset):
        dimension_feature_id (str | Unset):
        dimension_parameter_id (str | Unset):
        dimension_part_query (str | Unset):
        document_id (str | Unset):
        element_feature (str | Unset):
        element_id (str | Unset):
        element_occurrence (str | Unset):
        element_query (str | Unset):
        id (str | Unset):
        message (str | Unset):
        object_id (str | Unset):
        object_type (int | Unset):
        parent_id (str | Unset):
        version_id (str | Unset):
        view_data (BTViewDataParams | Unset):
        workspace_id (str | Unset):
    """

    annotation_id: str | Unset = UNSET
    annotation_type: int | Unset = UNSET
    assembly_feature: str | Unset = UNSET
    assignee: str | Unset = UNSET
    coordinates: CoordinatesParams | Unset = UNSET
    dimension_constraint_id: str | Unset = UNSET
    dimension_feature_id: str | Unset = UNSET
    dimension_parameter_id: str | Unset = UNSET
    dimension_part_query: str | Unset = UNSET
    document_id: str | Unset = UNSET
    element_feature: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_occurrence: str | Unset = UNSET
    element_query: str | Unset = UNSET
    id: str | Unset = UNSET
    message: str | Unset = UNSET
    object_id: str | Unset = UNSET
    object_type: int | Unset = UNSET
    parent_id: str | Unset = UNSET
    version_id: str | Unset = UNSET
    view_data: BTViewDataParams | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annotation_id = self.annotation_id

        annotation_type = self.annotation_type

        assembly_feature = self.assembly_feature

        assignee = self.assignee

        coordinates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = self.coordinates.to_dict()

        dimension_constraint_id = self.dimension_constraint_id

        dimension_feature_id = self.dimension_feature_id

        dimension_parameter_id = self.dimension_parameter_id

        dimension_part_query = self.dimension_part_query

        document_id = self.document_id

        element_feature = self.element_feature

        element_id = self.element_id

        element_occurrence = self.element_occurrence

        element_query = self.element_query

        id = self.id

        message = self.message

        object_id = self.object_id

        object_type = self.object_type

        parent_id = self.parent_id

        version_id = self.version_id

        view_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.view_data, Unset):
            view_data = self.view_data.to_dict()

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotation_id is not UNSET:
            field_dict["annotationId"] = annotation_id
        if annotation_type is not UNSET:
            field_dict["annotationType"] = annotation_type
        if assembly_feature is not UNSET:
            field_dict["assemblyFeature"] = assembly_feature
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if dimension_constraint_id is not UNSET:
            field_dict["dimensionConstraintId"] = dimension_constraint_id
        if dimension_feature_id is not UNSET:
            field_dict["dimensionFeatureId"] = dimension_feature_id
        if dimension_parameter_id is not UNSET:
            field_dict["dimensionParameterId"] = dimension_parameter_id
        if dimension_part_query is not UNSET:
            field_dict["dimensionPartQuery"] = dimension_part_query
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_feature is not UNSET:
            field_dict["elementFeature"] = element_feature
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_occurrence is not UNSET:
            field_dict["elementOccurrence"] = element_occurrence
        if element_query is not UNSET:
            field_dict["elementQuery"] = element_query
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if view_data is not UNSET:
            field_dict["viewData"] = view_data
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_view_data_params import BTViewDataParams
        from ..models.coordinates_params import CoordinatesParams

        d = dict(src_dict)
        annotation_id = d.pop("annotationId", UNSET)

        annotation_type = d.pop("annotationType", UNSET)

        assembly_feature = d.pop("assemblyFeature", UNSET)

        assignee = d.pop("assignee", UNSET)

        _coordinates = d.pop("coordinates", UNSET)
        coordinates: CoordinatesParams | Unset
        if isinstance(_coordinates, Unset):
            coordinates = UNSET
        else:
            coordinates = CoordinatesParams.from_dict(_coordinates)

        dimension_constraint_id = d.pop("dimensionConstraintId", UNSET)

        dimension_feature_id = d.pop("dimensionFeatureId", UNSET)

        dimension_parameter_id = d.pop("dimensionParameterId", UNSET)

        dimension_part_query = d.pop("dimensionPartQuery", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_feature = d.pop("elementFeature", UNSET)

        element_id = d.pop("elementId", UNSET)

        element_occurrence = d.pop("elementOccurrence", UNSET)

        element_query = d.pop("elementQuery", UNSET)

        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        object_id = d.pop("objectId", UNSET)

        object_type = d.pop("objectType", UNSET)

        parent_id = d.pop("parentId", UNSET)

        version_id = d.pop("versionId", UNSET)

        _view_data = d.pop("viewData", UNSET)
        view_data: BTViewDataParams | Unset
        if isinstance(_view_data, Unset):
            view_data = UNSET
        else:
            view_data = BTViewDataParams.from_dict(_view_data)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_comment_params = cls(
            annotation_id=annotation_id,
            annotation_type=annotation_type,
            assembly_feature=assembly_feature,
            assignee=assignee,
            coordinates=coordinates,
            dimension_constraint_id=dimension_constraint_id,
            dimension_feature_id=dimension_feature_id,
            dimension_parameter_id=dimension_parameter_id,
            dimension_part_query=dimension_part_query,
            document_id=document_id,
            element_feature=element_feature,
            element_id=element_id,
            element_occurrence=element_occurrence,
            element_query=element_query,
            id=id,
            message=message,
            object_id=object_id,
            object_type=object_type,
            parent_id=parent_id,
            version_id=version_id,
            view_data=view_data,
            workspace_id=workspace_id,
        )

        bt_comment_params.additional_properties = d
        return bt_comment_params

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
