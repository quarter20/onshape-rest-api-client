from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTTaskRbacRoleInfo")


@_attrs_define
class BTTaskRbacRoleInfo:
    """
    Attributes:
        acted (bool | Unset):
        active (bool | Unset):
        description (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        predefined_role (int | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    acted: bool | Unset = UNSET
    active: bool | Unset = UNSET
    description: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    predefined_role: int | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acted = self.acted

        active = self.active

        description = self.description

        href = self.href

        id = self.id

        name = self.name

        predefined_role = self.predefined_role

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acted is not UNSET:
            field_dict["acted"] = acted
        if active is not UNSET:
            field_dict["active"] = active
        if description is not UNSET:
            field_dict["description"] = description
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if predefined_role is not UNSET:
            field_dict["predefinedRole"] = predefined_role
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        acted = d.pop("acted", UNSET)

        active = d.pop("active", UNSET)

        description = d.pop("description", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        predefined_role = d.pop("predefinedRole", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_task_rbac_role_info = cls(
            acted=acted,
            active=active,
            description=description,
            href=href,
            id=id,
            name=name,
            predefined_role=predefined_role,
            view_ref=view_ref,
        )

        bt_task_rbac_role_info.additional_properties = d
        return bt_task_rbac_role_info

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
