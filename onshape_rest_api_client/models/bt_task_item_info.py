from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_view_data_info import BTViewDataInfo


T = TypeVar("T", bound="BTTaskItemInfo")


@_attrs_define
class BTTaskItemInfo:
    """
    Attributes:
        assembly_features (list[str] | Unset):
        body_type (str | Unset):
        configuration (str | Unset):
        data_type (str | Unset):
        document_id (str | Unset):
        element_feature (str | Unset):
        element_id (str | Unset):
        element_occurrences (list[str] | Unset):
        element_query (str | Unset):
        element_type (int | Unset):
        file_name (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        mime_type (str | Unset):
        name (str | Unset): Name of the resource.
        part_id (str | Unset):
        release_state (int | Unset):
        revision_id (str | Unset):
        version_id (str | Unset):
        view_data (BTViewDataInfo | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        workspace_id (str | Unset):
    """

    assembly_features: list[str] | Unset = UNSET
    body_type: str | Unset = UNSET
    configuration: str | Unset = UNSET
    data_type: str | Unset = UNSET
    document_id: str | Unset = UNSET
    element_feature: str | Unset = UNSET
    element_id: str | Unset = UNSET
    element_occurrences: list[str] | Unset = UNSET
    element_query: str | Unset = UNSET
    element_type: int | Unset = UNSET
    file_name: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    name: str | Unset = UNSET
    part_id: str | Unset = UNSET
    release_state: int | Unset = UNSET
    revision_id: str | Unset = UNSET
    version_id: str | Unset = UNSET
    view_data: BTViewDataInfo | Unset = UNSET
    view_ref: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assembly_features: list[str] | Unset = UNSET
        if not isinstance(self.assembly_features, Unset):
            assembly_features = self.assembly_features

        body_type = self.body_type

        configuration = self.configuration

        data_type = self.data_type

        document_id = self.document_id

        element_feature = self.element_feature

        element_id = self.element_id

        element_occurrences: list[str] | Unset = UNSET
        if not isinstance(self.element_occurrences, Unset):
            element_occurrences = self.element_occurrences

        element_query = self.element_query

        element_type = self.element_type

        file_name = self.file_name

        href = self.href

        id = self.id

        mime_type = self.mime_type

        name = self.name

        part_id = self.part_id

        release_state = self.release_state

        revision_id = self.revision_id

        version_id = self.version_id

        view_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.view_data, Unset):
            view_data = self.view_data.to_dict()

        view_ref = self.view_ref

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assembly_features is not UNSET:
            field_dict["assemblyFeatures"] = assembly_features
        if body_type is not UNSET:
            field_dict["bodyType"] = body_type
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_feature is not UNSET:
            field_dict["elementFeature"] = element_feature
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if element_occurrences is not UNSET:
            field_dict["elementOccurrences"] = element_occurrences
        if element_query is not UNSET:
            field_dict["elementQuery"] = element_query
        if element_type is not UNSET:
            field_dict["elementType"] = element_type
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if name is not UNSET:
            field_dict["name"] = name
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if release_state is not UNSET:
            field_dict["releaseState"] = release_state
        if revision_id is not UNSET:
            field_dict["revisionId"] = revision_id
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if view_data is not UNSET:
            field_dict["viewData"] = view_data
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_view_data_info import BTViewDataInfo

        d = dict(src_dict)
        assembly_features = cast(list[str], d.pop("assemblyFeatures", UNSET))

        body_type = d.pop("bodyType", UNSET)

        configuration = d.pop("configuration", UNSET)

        data_type = d.pop("dataType", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_feature = d.pop("elementFeature", UNSET)

        element_id = d.pop("elementId", UNSET)

        element_occurrences = cast(list[str], d.pop("elementOccurrences", UNSET))

        element_query = d.pop("elementQuery", UNSET)

        element_type = d.pop("elementType", UNSET)

        file_name = d.pop("fileName", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        name = d.pop("name", UNSET)

        part_id = d.pop("partId", UNSET)

        release_state = d.pop("releaseState", UNSET)

        revision_id = d.pop("revisionId", UNSET)

        version_id = d.pop("versionId", UNSET)

        _view_data = d.pop("viewData", UNSET)
        view_data: BTViewDataInfo | Unset
        if isinstance(_view_data, Unset):
            view_data = UNSET
        else:
            view_data = BTViewDataInfo.from_dict(_view_data)

        view_ref = d.pop("viewRef", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_task_item_info = cls(
            assembly_features=assembly_features,
            body_type=body_type,
            configuration=configuration,
            data_type=data_type,
            document_id=document_id,
            element_feature=element_feature,
            element_id=element_id,
            element_occurrences=element_occurrences,
            element_query=element_query,
            element_type=element_type,
            file_name=file_name,
            href=href,
            id=id,
            mime_type=mime_type,
            name=name,
            part_id=part_id,
            release_state=release_state,
            revision_id=revision_id,
            version_id=version_id,
            view_data=view_data,
            view_ref=view_ref,
            workspace_id=workspace_id,
        )

        bt_task_item_info.additional_properties = d
        return bt_task_item_info

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
