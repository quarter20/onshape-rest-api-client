from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo


T = TypeVar("T", bound="BTDocumentBaseSummaryInfo")


@_attrs_define
class BTDocumentBaseSummaryInfo:
    """Summary information about the document containing the reference.

    Attributes:
        created_by (BTUserBasicSummaryInfo | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        modified_by (BTUserBasicSummaryInfo | Unset):
        name (str | Unset): Name of the resource.
        state (int | Unset):
        storage_size (int | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    created_by: BTUserBasicSummaryInfo | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    modified_by: BTUserBasicSummaryInfo | Unset = UNSET
    name: str | Unset = UNSET
    state: int | Unset = UNSET
    storage_size: int | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        href = self.href

        id = self.id

        modified_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.modified_by, Unset):
            modified_by = self.modified_by.to_dict()

        name = self.name

        state = self.state

        storage_size = self.storage_size

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if name is not UNSET:
            field_dict["name"] = name
        if state is not UNSET:
            field_dict["state"] = state
        if storage_size is not UNSET:
            field_dict["storageSize"] = storage_size
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_user_basic_summary_info import BTUserBasicSummaryInfo

        d = dict(src_dict)
        _created_by = d.pop("createdBy", UNSET)
        created_by: BTUserBasicSummaryInfo | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = BTUserBasicSummaryInfo.from_dict(_created_by)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        _modified_by = d.pop("modifiedBy", UNSET)
        modified_by: BTUserBasicSummaryInfo | Unset
        if isinstance(_modified_by, Unset):
            modified_by = UNSET
        else:
            modified_by = BTUserBasicSummaryInfo.from_dict(_modified_by)

        name = d.pop("name", UNSET)

        state = d.pop("state", UNSET)

        storage_size = d.pop("storageSize", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_document_base_summary_info = cls(
            created_by=created_by,
            href=href,
            id=id,
            modified_by=modified_by,
            name=name,
            state=state,
            storage_size=storage_size,
            view_ref=view_ref,
        )

        bt_document_base_summary_info.additional_properties = d
        return bt_document_base_summary_info

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
