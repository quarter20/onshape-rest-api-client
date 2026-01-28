from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTAPIApplicationExtensionInfo")


@_attrs_define
class BTAPIApplicationExtensionInfo:
    """
    Attributes:
        action_body (str | Unset):
        action_type (int | Unset):
        action_url (str | Unset):
        application_id (str | Unset):
        client_id (str | Unset):
        description (str | Unset):
        extension_context (int | Unset):
        extension_location (int | Unset):
        has_icon (bool | Unset):
        has_pending_icon (bool | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        icon_url (str | Unset):
        id (str | Unset): Id of the resource.
        name (str | Unset): Name of the resource.
        parent_app_primary_format (str | Unset):
        plus_menu_app (bool | Unset):
        show_beta_label (bool | Unset):
        show_response (bool | Unset):
        show_upgrade_label (bool | Unset):
        system_app_extension (bool | Unset):
        system_app_icon_name (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
        visibility_rule (str | Unset):
    """

    action_body: str | Unset = UNSET
    action_type: int | Unset = UNSET
    action_url: str | Unset = UNSET
    application_id: str | Unset = UNSET
    client_id: str | Unset = UNSET
    description: str | Unset = UNSET
    extension_context: int | Unset = UNSET
    extension_location: int | Unset = UNSET
    has_icon: bool | Unset = UNSET
    has_pending_icon: bool | Unset = UNSET
    href: str | Unset = UNSET
    icon_url: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    parent_app_primary_format: str | Unset = UNSET
    plus_menu_app: bool | Unset = UNSET
    show_beta_label: bool | Unset = UNSET
    show_response: bool | Unset = UNSET
    show_upgrade_label: bool | Unset = UNSET
    system_app_extension: bool | Unset = UNSET
    system_app_icon_name: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    visibility_rule: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_body = self.action_body

        action_type = self.action_type

        action_url = self.action_url

        application_id = self.application_id

        client_id = self.client_id

        description = self.description

        extension_context = self.extension_context

        extension_location = self.extension_location

        has_icon = self.has_icon

        has_pending_icon = self.has_pending_icon

        href = self.href

        icon_url = self.icon_url

        id = self.id

        name = self.name

        parent_app_primary_format = self.parent_app_primary_format

        plus_menu_app = self.plus_menu_app

        show_beta_label = self.show_beta_label

        show_response = self.show_response

        show_upgrade_label = self.show_upgrade_label

        system_app_extension = self.system_app_extension

        system_app_icon_name = self.system_app_icon_name

        view_ref = self.view_ref

        visibility_rule = self.visibility_rule

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_body is not UNSET:
            field_dict["actionBody"] = action_body
        if action_type is not UNSET:
            field_dict["actionType"] = action_type
        if action_url is not UNSET:
            field_dict["actionUrl"] = action_url
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if description is not UNSET:
            field_dict["description"] = description
        if extension_context is not UNSET:
            field_dict["extensionContext"] = extension_context
        if extension_location is not UNSET:
            field_dict["extensionLocation"] = extension_location
        if has_icon is not UNSET:
            field_dict["hasIcon"] = has_icon
        if has_pending_icon is not UNSET:
            field_dict["hasPendingIcon"] = has_pending_icon
        if href is not UNSET:
            field_dict["href"] = href
        if icon_url is not UNSET:
            field_dict["iconUrl"] = icon_url
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if parent_app_primary_format is not UNSET:
            field_dict["parentAppPrimaryFormat"] = parent_app_primary_format
        if plus_menu_app is not UNSET:
            field_dict["plusMenuApp"] = plus_menu_app
        if show_beta_label is not UNSET:
            field_dict["showBetaLabel"] = show_beta_label
        if show_response is not UNSET:
            field_dict["showResponse"] = show_response
        if show_upgrade_label is not UNSET:
            field_dict["showUpgradeLabel"] = show_upgrade_label
        if system_app_extension is not UNSET:
            field_dict["systemAppExtension"] = system_app_extension
        if system_app_icon_name is not UNSET:
            field_dict["systemAppIconName"] = system_app_icon_name
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref
        if visibility_rule is not UNSET:
            field_dict["visibilityRule"] = visibility_rule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action_body = d.pop("actionBody", UNSET)

        action_type = d.pop("actionType", UNSET)

        action_url = d.pop("actionUrl", UNSET)

        application_id = d.pop("applicationId", UNSET)

        client_id = d.pop("clientId", UNSET)

        description = d.pop("description", UNSET)

        extension_context = d.pop("extensionContext", UNSET)

        extension_location = d.pop("extensionLocation", UNSET)

        has_icon = d.pop("hasIcon", UNSET)

        has_pending_icon = d.pop("hasPendingIcon", UNSET)

        href = d.pop("href", UNSET)

        icon_url = d.pop("iconUrl", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        parent_app_primary_format = d.pop("parentAppPrimaryFormat", UNSET)

        plus_menu_app = d.pop("plusMenuApp", UNSET)

        show_beta_label = d.pop("showBetaLabel", UNSET)

        show_response = d.pop("showResponse", UNSET)

        show_upgrade_label = d.pop("showUpgradeLabel", UNSET)

        system_app_extension = d.pop("systemAppExtension", UNSET)

        system_app_icon_name = d.pop("systemAppIconName", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        visibility_rule = d.pop("visibilityRule", UNSET)

        btapi_application_extension_info = cls(
            action_body=action_body,
            action_type=action_type,
            action_url=action_url,
            application_id=application_id,
            client_id=client_id,
            description=description,
            extension_context=extension_context,
            extension_location=extension_location,
            has_icon=has_icon,
            has_pending_icon=has_pending_icon,
            href=href,
            icon_url=icon_url,
            id=id,
            name=name,
            parent_app_primary_format=parent_app_primary_format,
            plus_menu_app=plus_menu_app,
            show_beta_label=show_beta_label,
            show_response=show_response,
            show_upgrade_label=show_upgrade_label,
            system_app_extension=system_app_extension,
            system_app_icon_name=system_app_icon_name,
            view_ref=view_ref,
            visibility_rule=visibility_rule,
        )

        btapi_application_extension_info.additional_properties = d
        return btapi_application_extension_info

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
