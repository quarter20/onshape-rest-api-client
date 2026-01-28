from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAPIApplicationSummaryInfo")


@_attrs_define
class BTAPIApplicationSummaryInfo:
    """
    Attributes:
        application_owner_type (int | Unset):
        client_id (str | Unset):
        description (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        state (int | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    application_owner_type: int | Unset = UNSET
    client_id: str | Unset = UNSET
    description: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    state: int | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_owner_type = self.application_owner_type

        client_id = self.client_id

        description = self.description

        href = self.href

        id = self.id

        name = self.name

        state = self.state

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_owner_type is not UNSET:
            field_dict["applicationOwnerType"] = application_owner_type
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if description is not UNSET:
            field_dict["description"] = description
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if state is not UNSET:
            field_dict["state"] = state
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        application_owner_type = d.pop("applicationOwnerType", UNSET)

        client_id = d.pop("clientId", UNSET)

        description = d.pop("description", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        state = d.pop("state", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        btapi_application_summary_info = cls(
            application_owner_type=application_owner_type,
            client_id=client_id,
            description=description,
            href=href,
            id=id,
            name=name,
            state=state,
            view_ref=view_ref,
        )

        btapi_application_summary_info.additional_properties = d
        return btapi_application_summary_info

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
