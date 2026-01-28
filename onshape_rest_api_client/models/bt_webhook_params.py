from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_webhook_options import BTWebhookOptions


T = TypeVar("T", bound="BTWebhookParams")


@_attrs_define
class BTWebhookParams:
    """
    Attributes:
        client_id (str | Unset):
        company_id (str | Unset): Company admins can register webhooks to listen to all company events.
        data (str | Unset):
        description (str | Unset):
        document_id (str | Unset):
        element_id (str | Unset):
        events (list[str] | Unset): List of events for which webhook callback is invoked.
        external_session_id (str | Unset): Applications can pass this parameter as X-Session-ID with every REST call to
            distinguish webhooks triggered by self.
        filter_ (str | Unset):
        folder_id (str | Unset):
        id (str | Unset):
        is_transient (bool | Unset): Transient webhooks are automatically cleaned up after a period of inactivity.
            Default: True.
        link_document_id (str | Unset):
        options (BTWebhookOptions | Unset):
        part_id (str | Unset):
        project_id (str | Unset):
        url (str | Unset):
        user_id (str | Unset):
        version_id (str | Unset):
        workspace_id (str | Unset):
    """

    client_id: str | Unset = UNSET
    company_id: str | Unset = UNSET
    data: str | Unset = UNSET
    description: str | Unset = UNSET
    document_id: str | Unset = UNSET
    element_id: str | Unset = UNSET
    events: list[str] | Unset = UNSET
    external_session_id: str | Unset = UNSET
    filter_: str | Unset = UNSET
    folder_id: str | Unset = UNSET
    id: str | Unset = UNSET
    is_transient: bool | Unset = True
    link_document_id: str | Unset = UNSET
    options: BTWebhookOptions | Unset = UNSET
    part_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    url: str | Unset = UNSET
    user_id: str | Unset = UNSET
    version_id: str | Unset = UNSET
    workspace_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        company_id = self.company_id

        data = self.data

        description = self.description

        document_id = self.document_id

        element_id = self.element_id

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        external_session_id = self.external_session_id

        filter_ = self.filter_

        folder_id = self.folder_id

        id = self.id

        is_transient = self.is_transient

        link_document_id = self.link_document_id

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        part_id = self.part_id

        project_id = self.project_id

        url = self.url

        user_id = self.user_id

        version_id = self.version_id

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if data is not UNSET:
            field_dict["data"] = data
        if description is not UNSET:
            field_dict["description"] = description
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if element_id is not UNSET:
            field_dict["elementId"] = element_id
        if events is not UNSET:
            field_dict["events"] = events
        if external_session_id is not UNSET:
            field_dict["externalSessionId"] = external_session_id
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if id is not UNSET:
            field_dict["id"] = id
        if is_transient is not UNSET:
            field_dict["isTransient"] = is_transient
        if link_document_id is not UNSET:
            field_dict["linkDocumentId"] = link_document_id
        if options is not UNSET:
            field_dict["options"] = options
        if part_id is not UNSET:
            field_dict["partId"] = part_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if url is not UNSET:
            field_dict["url"] = url
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_webhook_options import BTWebhookOptions

        d = dict(src_dict)
        client_id = d.pop("clientId", UNSET)

        company_id = d.pop("companyId", UNSET)

        data = d.pop("data", UNSET)

        description = d.pop("description", UNSET)

        document_id = d.pop("documentId", UNSET)

        element_id = d.pop("elementId", UNSET)

        events = cast(list[str], d.pop("events", UNSET))

        external_session_id = d.pop("externalSessionId", UNSET)

        filter_ = d.pop("filter", UNSET)

        folder_id = d.pop("folderId", UNSET)

        id = d.pop("id", UNSET)

        is_transient = d.pop("isTransient", UNSET)

        link_document_id = d.pop("linkDocumentId", UNSET)

        _options = d.pop("options", UNSET)
        options: BTWebhookOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = BTWebhookOptions.from_dict(_options)

        part_id = d.pop("partId", UNSET)

        project_id = d.pop("projectId", UNSET)

        url = d.pop("url", UNSET)

        user_id = d.pop("userId", UNSET)

        version_id = d.pop("versionId", UNSET)

        workspace_id = d.pop("workspaceId", UNSET)

        bt_webhook_params = cls(
            client_id=client_id,
            company_id=company_id,
            data=data,
            description=description,
            document_id=document_id,
            element_id=element_id,
            events=events,
            external_session_id=external_session_id,
            filter_=filter_,
            folder_id=folder_id,
            id=id,
            is_transient=is_transient,
            link_document_id=link_document_id,
            options=options,
            part_id=part_id,
            project_id=project_id,
            url=url,
            user_id=user_id,
            version_id=version_id,
            workspace_id=workspace_id,
        )

        bt_webhook_params.additional_properties = d
        return bt_webhook_params

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
