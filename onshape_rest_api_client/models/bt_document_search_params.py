from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.btes_results_filter import BTESResultsFilter
from ..models.btes_version_workspace_choice import BTESVersionWorkspaceChoice
from ..types import UNSET, Unset

T = TypeVar("T", bound="BTDocumentSearchParams")


@_attrs_define
class BTDocumentSearchParams:
    """
    Attributes:
        document_filter (int | Unset): Type of documents to search: `0: My Documents | 1: Created | 2: Shared | 3: Trash
            | 4: Public | 5: Recent | 6: By Owner | 7: By Company | 9: By Team`
        found_in (BTESVersionWorkspaceChoice | Unset): Search result found in Example: ALL.
        limit (int | Unset): Number of results to return per page. Default value is 20 (also the maximum). Default: 20.
            Example: 1.
        offset (int | Unset): Offset. Determines where search results begin. Default value is 0. Default: 0.
        owner_id (str | Unset): Owner ID. Can be a user ID, company ID, or team ID, depending on `ownerType`.
        parent_id (str | Unset): Search document parent Id  Example: ALL.
        raw_query (str | Unset): Search for documents that contain the given string in the name. Search is not case-
            sensitive.
        sort_column (str | Unset): Column by which to sort search results. `name | modifiedAt | createdAt (default) |
            email | modifiedBy | promotedAt` Default: 'createdAt'.
        sort_order (str | Unset): Type of documents to search: `0: My Documents | 1: Created | 2: Shared | 3: Trash | 4:
            Public | 5: Recent | 6: By Owner | 7: By Company | 9: By Team` Default: 'desc'.
        type_ (str | Unset): Type of owner. `0: User | 1: Company | 2: Onshape`. If the owner is a teamId, leave this
            unspecified.
        when (BTESResultsFilter | Unset): Search result when Example: ALL.
    """

    document_filter: int | Unset = UNSET
    found_in: BTESVersionWorkspaceChoice | Unset = UNSET
    limit: int | Unset = 20
    offset: int | Unset = 0
    owner_id: str | Unset = UNSET
    parent_id: str | Unset = UNSET
    raw_query: str | Unset = UNSET
    sort_column: str | Unset = "createdAt"
    sort_order: str | Unset = "desc"
    type_: str | Unset = UNSET
    when: BTESResultsFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_filter = self.document_filter

        found_in: str | Unset = UNSET
        if not isinstance(self.found_in, Unset):
            found_in = self.found_in.value

        limit = self.limit

        offset = self.offset

        owner_id = self.owner_id

        parent_id = self.parent_id

        raw_query = self.raw_query

        sort_column = self.sort_column

        sort_order = self.sort_order

        type_ = self.type_

        when: str | Unset = UNSET
        if not isinstance(self.when, Unset):
            when = self.when.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_filter is not UNSET:
            field_dict["documentFilter"] = document_filter
        if found_in is not UNSET:
            field_dict["foundIn"] = found_in
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if raw_query is not UNSET:
            field_dict["rawQuery"] = raw_query
        if sort_column is not UNSET:
            field_dict["sortColumn"] = sort_column
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if type_ is not UNSET:
            field_dict["type"] = type_
        if when is not UNSET:
            field_dict["when"] = when

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_filter = d.pop("documentFilter", UNSET)

        _found_in = d.pop("foundIn", UNSET)
        found_in: BTESVersionWorkspaceChoice | Unset
        if isinstance(_found_in, Unset):
            found_in = UNSET
        else:
            found_in = BTESVersionWorkspaceChoice(_found_in)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        parent_id = d.pop("parentId", UNSET)

        raw_query = d.pop("rawQuery", UNSET)

        sort_column = d.pop("sortColumn", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        type_ = d.pop("type", UNSET)

        _when = d.pop("when", UNSET)
        when: BTESResultsFilter | Unset
        if isinstance(_when, Unset):
            when = UNSET
        else:
            when = BTESResultsFilter(_when)

        bt_document_search_params = cls(
            document_filter=document_filter,
            found_in=found_in,
            limit=limit,
            offset=offset,
            owner_id=owner_id,
            parent_id=parent_id,
            raw_query=raw_query,
            sort_column=sort_column,
            sort_order=sort_order,
            type_=type_,
            when=when,
        )

        bt_document_search_params.additional_properties = d
        return bt_document_search_params

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
