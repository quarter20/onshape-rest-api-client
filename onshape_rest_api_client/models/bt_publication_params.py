from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_publication_item_params import BTPublicationItemParams


T = TypeVar("T", bound="BTPublicationParams")


@_attrs_define
class BTPublicationParams:
    """
    Attributes:
        description (str | Unset):
        items (list[BTPublicationItemParams] | Unset):
        name (str | Unset):
        notes (str | Unset):
        old_client_notes (str | Unset):
        owner_id (str | Unset):
        owner_type (int | Unset):
        parent_id (str | Unset):
        project_id (str | Unset):
    """

    description: str | Unset = UNSET
    items: list[BTPublicationItemParams] | Unset = UNSET
    name: str | Unset = UNSET
    notes: str | Unset = UNSET
    old_client_notes: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    owner_type: int | Unset = UNSET
    parent_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        name = self.name

        notes = self.notes

        old_client_notes = self.old_client_notes

        owner_id = self.owner_id

        owner_type = self.owner_type

        parent_id = self.parent_id

        project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if items is not UNSET:
            field_dict["items"] = items
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if old_client_notes is not UNSET:
            field_dict["oldClientNotes"] = old_client_notes
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if owner_type is not UNSET:
            field_dict["ownerType"] = owner_type
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_publication_item_params import BTPublicationItemParams

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _items = d.pop("items", UNSET)
        items: list[BTPublicationItemParams] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = BTPublicationItemParams.from_dict(items_item_data)

                items.append(items_item)

        name = d.pop("name", UNSET)

        notes = d.pop("notes", UNSET)

        old_client_notes = d.pop("oldClientNotes", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        owner_type = d.pop("ownerType", UNSET)

        parent_id = d.pop("parentId", UNSET)

        project_id = d.pop("projectId", UNSET)

        bt_publication_params = cls(
            description=description,
            items=items,
            name=name,
            notes=notes,
            old_client_notes=old_client_notes,
            owner_id=owner_id,
            owner_type=owner_type,
            parent_id=parent_id,
            project_id=project_id,
        )

        bt_publication_params.additional_properties = d
        return bt_publication_params

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
