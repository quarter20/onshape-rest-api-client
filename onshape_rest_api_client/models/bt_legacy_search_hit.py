from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bt_search_entity_type import BTSearchEntityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_legacy_search_hit_highlighted_fields import BTLegacySearchHitHighlightedFields
    from ..models.bt_legacy_search_hit_source_map import BTLegacySearchHitSourceMap


T = TypeVar("T", bound="BTLegacySearchHit")


@_attrs_define
class BTLegacySearchHit:
    """
    Attributes:
        document_id (str | Unset):
        folder_id (str | Unset):
        highlighted_fields (BTLegacySearchHitHighlightedFields | Unset):
        hit_id (str | Unset):
        name (str | Unset):
        project_id (str | Unset):
        source_map (BTLegacySearchHitSourceMap | Unset):
        type_ (BTSearchEntityType | Unset):
    """

    document_id: str | Unset = UNSET
    folder_id: str | Unset = UNSET
    highlighted_fields: BTLegacySearchHitHighlightedFields | Unset = UNSET
    hit_id: str | Unset = UNSET
    name: str | Unset = UNSET
    project_id: str | Unset = UNSET
    source_map: BTLegacySearchHitSourceMap | Unset = UNSET
    type_: BTSearchEntityType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        folder_id = self.folder_id

        highlighted_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.highlighted_fields, Unset):
            highlighted_fields = self.highlighted_fields.to_dict()

        hit_id = self.hit_id

        name = self.name

        project_id = self.project_id

        source_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_map, Unset):
            source_map = self.source_map.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if highlighted_fields is not UNSET:
            field_dict["highlightedFields"] = highlighted_fields
        if hit_id is not UNSET:
            field_dict["hitId"] = hit_id
        if name is not UNSET:
            field_dict["name"] = name
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if source_map is not UNSET:
            field_dict["sourceMap"] = source_map
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_legacy_search_hit_highlighted_fields import BTLegacySearchHitHighlightedFields
        from ..models.bt_legacy_search_hit_source_map import BTLegacySearchHitSourceMap

        d = dict(src_dict)
        document_id = d.pop("documentId", UNSET)

        folder_id = d.pop("folderId", UNSET)

        _highlighted_fields = d.pop("highlightedFields", UNSET)
        highlighted_fields: BTLegacySearchHitHighlightedFields | Unset
        if isinstance(_highlighted_fields, Unset):
            highlighted_fields = UNSET
        else:
            highlighted_fields = BTLegacySearchHitHighlightedFields.from_dict(_highlighted_fields)

        hit_id = d.pop("hitId", UNSET)

        name = d.pop("name", UNSET)

        project_id = d.pop("projectId", UNSET)

        _source_map = d.pop("sourceMap", UNSET)
        source_map: BTLegacySearchHitSourceMap | Unset
        if isinstance(_source_map, Unset):
            source_map = UNSET
        else:
            source_map = BTLegacySearchHitSourceMap.from_dict(_source_map)

        _type_ = d.pop("type", UNSET)
        type_: BTSearchEntityType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BTSearchEntityType(_type_)

        bt_legacy_search_hit = cls(
            document_id=document_id,
            folder_id=folder_id,
            highlighted_fields=highlighted_fields,
            hit_id=hit_id,
            name=name,
            project_id=project_id,
            source_map=source_map,
            type_=type_,
        )

        bt_legacy_search_hit.additional_properties = d
        return bt_legacy_search_hit

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
