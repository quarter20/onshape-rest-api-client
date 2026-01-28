from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTUserMetricsInfo")


@_attrs_define
class BTUserMetricsInfo:
    """
    Attributes:
        created_documents (int | Unset):
        has_recently_opened_documents (bool | Unset):
        has_shared_documents (bool | Unset):
        has_trashed_documents (bool | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        private_documents (int | Unset):
        public_documents (int | Unset):
        shared_documents (int | Unset):
        user_account_limits_crossed (bool | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    created_documents: int | Unset = UNSET
    has_recently_opened_documents: bool | Unset = UNSET
    has_shared_documents: bool | Unset = UNSET
    has_trashed_documents: bool | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    private_documents: int | Unset = UNSET
    public_documents: int | Unset = UNSET
    shared_documents: int | Unset = UNSET
    user_account_limits_crossed: bool | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_documents = self.created_documents

        has_recently_opened_documents = self.has_recently_opened_documents

        has_shared_documents = self.has_shared_documents

        has_trashed_documents = self.has_trashed_documents

        href = self.href

        id = self.id

        name = self.name

        private_documents = self.private_documents

        public_documents = self.public_documents

        shared_documents = self.shared_documents

        user_account_limits_crossed = self.user_account_limits_crossed

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_documents is not UNSET:
            field_dict["createdDocuments"] = created_documents
        if has_recently_opened_documents is not UNSET:
            field_dict["hasRecentlyOpenedDocuments"] = has_recently_opened_documents
        if has_shared_documents is not UNSET:
            field_dict["hasSharedDocuments"] = has_shared_documents
        if has_trashed_documents is not UNSET:
            field_dict["hasTrashedDocuments"] = has_trashed_documents
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if private_documents is not UNSET:
            field_dict["privateDocuments"] = private_documents
        if public_documents is not UNSET:
            field_dict["publicDocuments"] = public_documents
        if shared_documents is not UNSET:
            field_dict["sharedDocuments"] = shared_documents
        if user_account_limits_crossed is not UNSET:
            field_dict["userAccountLimitsCrossed"] = user_account_limits_crossed
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_documents = d.pop("createdDocuments", UNSET)

        has_recently_opened_documents = d.pop("hasRecentlyOpenedDocuments", UNSET)

        has_shared_documents = d.pop("hasSharedDocuments", UNSET)

        has_trashed_documents = d.pop("hasTrashedDocuments", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        private_documents = d.pop("privateDocuments", UNSET)

        public_documents = d.pop("publicDocuments", UNSET)

        shared_documents = d.pop("sharedDocuments", UNSET)

        user_account_limits_crossed = d.pop("userAccountLimitsCrossed", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_user_metrics_info = cls(
            created_documents=created_documents,
            has_recently_opened_documents=has_recently_opened_documents,
            has_shared_documents=has_shared_documents,
            has_trashed_documents=has_trashed_documents,
            href=href,
            id=id,
            name=name,
            private_documents=private_documents,
            public_documents=public_documents,
            shared_documents=shared_documents,
            user_account_limits_crossed=user_account_limits_crossed,
            view_ref=view_ref,
        )

        bt_user_metrics_info.additional_properties = d
        return bt_user_metrics_info

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
