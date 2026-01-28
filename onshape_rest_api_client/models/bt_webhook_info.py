from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_user_summary_info import BTUserSummaryInfo
    from ..models.bt_webhook_options import BTWebhookOptions


T = TypeVar("T", bound="BTWebhookInfo")


@_attrs_define
class BTWebhookInfo:
    """
    Attributes:
        company_id (str | Unset): Company admins can register webhooks to listen to all company events.
        created_by (BTUserSummaryInfo | Unset):
        data (str | Unset):
        description (str | Unset):
        dropped_event_count (int | Unset):
        events (list[str] | Unset): List of events for which webhook callback is invoked.
        external_session_id (str | Unset): Applications can pass this parameter as X-Session-ID with every REST call to
            distinguish webhooks triggered by self.
        filter_ (str | Unset):
        folder_id (str | Unset):
        href (str | Unset): URI to fetch complete information of the resource.
        id (str | Unset): Id of the resource.
        is_transient (bool | Unset): Transient webhooks are automatically cleaned up after a period of inactivity.
            Default: True.
        name (str | Unset): Name of the resource.
        options (BTWebhookOptions | Unset):
        project_id (str | Unset):
        url (str | Unset):
        view_ref (str | Unset): URI to visualize the resource in a webclient if applicable.
    """

    company_id: str | Unset = UNSET
    created_by: BTUserSummaryInfo | Unset = UNSET
    data: str | Unset = UNSET
    description: str | Unset = UNSET
    dropped_event_count: int | Unset = UNSET
    events: list[str] | Unset = UNSET
    external_session_id: str | Unset = UNSET
    filter_: str | Unset = UNSET
    folder_id: str | Unset = UNSET
    href: str | Unset = UNSET
    id: str | Unset = UNSET
    is_transient: bool | Unset = True
    name: str | Unset = UNSET
    options: BTWebhookOptions | Unset = UNSET
    project_id: str | Unset = UNSET
    url: str | Unset = UNSET
    view_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_id = self.company_id

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        data = self.data

        description = self.description

        dropped_event_count = self.dropped_event_count

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        external_session_id = self.external_session_id

        filter_ = self.filter_

        folder_id = self.folder_id

        href = self.href

        id = self.id

        is_transient = self.is_transient

        name = self.name

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        project_id = self.project_id

        url = self.url

        view_ref = self.view_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_id is not UNSET:
            field_dict["companyId"] = company_id
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if data is not UNSET:
            field_dict["data"] = data
        if description is not UNSET:
            field_dict["description"] = description
        if dropped_event_count is not UNSET:
            field_dict["droppedEventCount"] = dropped_event_count
        if events is not UNSET:
            field_dict["events"] = events
        if external_session_id is not UNSET:
            field_dict["externalSessionId"] = external_session_id
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if href is not UNSET:
            field_dict["href"] = href
        if id is not UNSET:
            field_dict["id"] = id
        if is_transient is not UNSET:
            field_dict["isTransient"] = is_transient
        if name is not UNSET:
            field_dict["name"] = name
        if options is not UNSET:
            field_dict["options"] = options
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if url is not UNSET:
            field_dict["url"] = url
        if view_ref is not UNSET:
            field_dict["viewRef"] = view_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_user_summary_info import BTUserSummaryInfo
        from ..models.bt_webhook_options import BTWebhookOptions

        d = dict(src_dict)
        company_id = d.pop("companyId", UNSET)

        _created_by = d.pop("createdBy", UNSET)
        created_by: BTUserSummaryInfo | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = BTUserSummaryInfo.from_dict(_created_by)

        data = d.pop("data", UNSET)

        description = d.pop("description", UNSET)

        dropped_event_count = d.pop("droppedEventCount", UNSET)

        events = cast(list[str], d.pop("events", UNSET))

        external_session_id = d.pop("externalSessionId", UNSET)

        filter_ = d.pop("filter", UNSET)

        folder_id = d.pop("folderId", UNSET)

        href = d.pop("href", UNSET)

        id = d.pop("id", UNSET)

        is_transient = d.pop("isTransient", UNSET)

        name = d.pop("name", UNSET)

        _options = d.pop("options", UNSET)
        options: BTWebhookOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = BTWebhookOptions.from_dict(_options)

        project_id = d.pop("projectId", UNSET)

        url = d.pop("url", UNSET)

        view_ref = d.pop("viewRef", UNSET)

        bt_webhook_info = cls(
            company_id=company_id,
            created_by=created_by,
            data=data,
            description=description,
            dropped_event_count=dropped_event_count,
            events=events,
            external_session_id=external_session_id,
            filter_=filter_,
            folder_id=folder_id,
            href=href,
            id=id,
            is_transient=is_transient,
            name=name,
            options=options,
            project_id=project_id,
            url=url,
            view_ref=view_ref,
        )

        bt_webhook_info.additional_properties = d
        return bt_webhook_info

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
