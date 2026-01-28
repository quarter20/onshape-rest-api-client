from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTWorkflowStateInfo")


@_attrs_define
class BTWorkflowStateInfo:
    """
    Attributes:
        approver_source_property (str | Unset):
        display_name (str | Unset):
        edit_permissions (list[str] | Unset):
        editable_properties (list[str] | Unset):
        name (str | Unset):
        non_editable_properties (list[str] | Unset):
        notifier_source_property (str | Unset):
        required_item_properties (list[str] | Unset):
        required_properties (list[str] | Unset):
    """

    approver_source_property: str | Unset = UNSET
    display_name: str | Unset = UNSET
    edit_permissions: list[str] | Unset = UNSET
    editable_properties: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    non_editable_properties: list[str] | Unset = UNSET
    notifier_source_property: str | Unset = UNSET
    required_item_properties: list[str] | Unset = UNSET
    required_properties: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approver_source_property = self.approver_source_property

        display_name = self.display_name

        edit_permissions: list[str] | Unset = UNSET
        if not isinstance(self.edit_permissions, Unset):
            edit_permissions = self.edit_permissions

        editable_properties: list[str] | Unset = UNSET
        if not isinstance(self.editable_properties, Unset):
            editable_properties = self.editable_properties

        name = self.name

        non_editable_properties: list[str] | Unset = UNSET
        if not isinstance(self.non_editable_properties, Unset):
            non_editable_properties = self.non_editable_properties

        notifier_source_property = self.notifier_source_property

        required_item_properties: list[str] | Unset = UNSET
        if not isinstance(self.required_item_properties, Unset):
            required_item_properties = self.required_item_properties

        required_properties: list[str] | Unset = UNSET
        if not isinstance(self.required_properties, Unset):
            required_properties = self.required_properties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approver_source_property is not UNSET:
            field_dict["approverSourceProperty"] = approver_source_property
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if edit_permissions is not UNSET:
            field_dict["editPermissions"] = edit_permissions
        if editable_properties is not UNSET:
            field_dict["editableProperties"] = editable_properties
        if name is not UNSET:
            field_dict["name"] = name
        if non_editable_properties is not UNSET:
            field_dict["nonEditableProperties"] = non_editable_properties
        if notifier_source_property is not UNSET:
            field_dict["notifierSourceProperty"] = notifier_source_property
        if required_item_properties is not UNSET:
            field_dict["requiredItemProperties"] = required_item_properties
        if required_properties is not UNSET:
            field_dict["requiredProperties"] = required_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        approver_source_property = d.pop("approverSourceProperty", UNSET)

        display_name = d.pop("displayName", UNSET)

        edit_permissions = cast(list[str], d.pop("editPermissions", UNSET))

        editable_properties = cast(list[str], d.pop("editableProperties", UNSET))

        name = d.pop("name", UNSET)

        non_editable_properties = cast(list[str], d.pop("nonEditableProperties", UNSET))

        notifier_source_property = d.pop("notifierSourceProperty", UNSET)

        required_item_properties = cast(list[str], d.pop("requiredItemProperties", UNSET))

        required_properties = cast(list[str], d.pop("requiredProperties", UNSET))

        bt_workflow_state_info = cls(
            approver_source_property=approver_source_property,
            display_name=display_name,
            edit_permissions=edit_permissions,
            editable_properties=editable_properties,
            name=name,
            non_editable_properties=non_editable_properties,
            notifier_source_property=notifier_source_property,
            required_item_properties=required_item_properties,
            required_properties=required_properties,
        )

        bt_workflow_state_info.additional_properties = d
        return bt_workflow_state_info

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
