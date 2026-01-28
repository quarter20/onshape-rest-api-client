from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_search_entity_type import BTSearchEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_document_search_hit_info_highlighted_fields import BTDocumentSearchHitInfoHighlightedFields
    from ..models.bt_document_search_hit_info_source_map import BTDocumentSearchHitInfoSourceMap
    from ..models.bt_legacy_search_hit import BTLegacySearchHit


T = TypeVar("T", bound="BTDocumentSearchHitInfo")


@_attrs_define
class BTDocumentSearchHitInfo:
    """
    Attributes:
        document_id (str | Unset):
        element_name (str | Unset):
        folder_id (str | Unset):
        highlighted_fields (BTDocumentSearchHitInfoHighlightedFields | Unset):
        hit (BTLegacySearchHit | Unset):
        hit_id (str | Unset):
        mesh_state (int | Unset):
        name (str | Unset):
        project_id (str | Unset):
        source_map (BTDocumentSearchHitInfoSourceMap | Unset):
        type_ (BTSearchEntityType | Unset):
        version_or_workspace_name (str | Unset):
    """

    document_id: str | Unset = UNSET
    element_name: str | Unset = UNSET
    folder_id: str | Unset = UNSET
    highlighted_fields: BTDocumentSearchHitInfoHighlightedFields | Unset = UNSET
    hit: BTLegacySearchHit | Unset = UNSET
    hit_id: str | Unset = UNSET
    mesh_state: int | Unset = UNSET
    name: str | Unset = UNSET
    project_id: str | Unset = UNSET
    source_map: BTDocumentSearchHitInfoSourceMap | Unset = UNSET
    type_: BTSearchEntityType | Unset = UNSET
    version_or_workspace_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        element_name = self.element_name

        folder_id = self.folder_id

        highlighted_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.highlighted_fields, Unset):
            highlighted_fields = self.highlighted_fields.to_dict()

        hit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hit, Unset):
            hit = self.hit.to_dict()

        hit_id = self.hit_id

        mesh_state = self.mesh_state

        name = self.name

        project_id = self.project_id

        source_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_map, Unset):
            source_map = self.source_map.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        version_or_workspace_name = self.version_or_workspace_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_name is not UNSET:
            field_dict["elementName"] = element_name
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if highlighted_fields is not UNSET:
            field_dict["highlightedFields"] = highlighted_fields
        if hit is not UNSET:
            field_dict["hit"] = hit
        if hit_id is not UNSET:
            field_dict["hitId"] = hit_id
        if mesh_state is not UNSET:
            field_dict["meshState"] = mesh_state
        if name is not UNSET:
            field_dict["name"] = name
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if source_map is not UNSET:
            field_dict["sourceMap"] = source_map
        if type_ is not UNSET:
            field_dict["type"] = type_
        if version_or_workspace_name is not UNSET:
            field_dict["versionOrWorkspaceName"] = version_or_workspace_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_document_search_hit_info_highlighted_fields import BTDocumentSearchHitInfoHighlightedFields
        from ..models.bt_document_search_hit_info_source_map import BTDocumentSearchHitInfoSourceMap
        from ..models.bt_legacy_search_hit import BTLegacySearchHit

        d = dict(src_dict)
        document_id = d.pop("documentId", UNSET)

        element_name = d.pop("elementName", UNSET)

        folder_id = d.pop("folderId", UNSET)

        _highlighted_fields = d.pop("highlightedFields", UNSET)
        highlighted_fields: BTDocumentSearchHitInfoHighlightedFields | Unset
        if isinstance(_highlighted_fields, Unset):
            highlighted_fields = UNSET
        else:
            highlighted_fields = BTDocumentSearchHitInfoHighlightedFields.from_dict(_highlighted_fields)

        _hit = d.pop("hit", UNSET)
        hit: BTLegacySearchHit | Unset
        if isinstance(_hit, Unset):
            hit = UNSET
        else:
            hit = BTLegacySearchHit.from_dict(_hit)

        hit_id = d.pop("hitId", UNSET)

        mesh_state = d.pop("meshState", UNSET)

        name = d.pop("name", UNSET)

        project_id = d.pop("projectId", UNSET)

        _source_map = d.pop("sourceMap", UNSET)
        source_map: BTDocumentSearchHitInfoSourceMap | Unset
        if isinstance(_source_map, Unset):
            source_map = UNSET
        else:
            source_map = BTDocumentSearchHitInfoSourceMap.from_dict(_source_map)

        _type_ = d.pop("type", UNSET)
        type_: BTSearchEntityType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BTSearchEntityType(_type_)

        version_or_workspace_name = d.pop("versionOrWorkspaceName", UNSET)

        bt_document_search_hit_info = cls(
            document_id=document_id,
            element_name=element_name,
            folder_id=folder_id,
            highlighted_fields=highlighted_fields,
            hit=hit,
            hit_id=hit_id,
            mesh_state=mesh_state,
            name=name,
            project_id=project_id,
            source_map=source_map,
            type_=type_,
            version_or_workspace_name=version_or_workspace_name,
        )

        bt_document_search_hit_info.additional_properties = d
        return bt_document_search_hit_info

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
