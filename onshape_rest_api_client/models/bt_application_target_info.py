from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BTApplicationTargetInfo")


@_attrs_define
class BTApplicationTargetInfo:
    """
    Attributes:
        base_href (str | Unset):
        client_id (str | Unset):
        supports_collaboration (bool | Unset):
        tab_icon_href (str | Unset):
    """

    base_href: str | Unset = UNSET
    client_id: str | Unset = UNSET
    supports_collaboration: bool | Unset = UNSET
    tab_icon_href: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_href = self.base_href

        client_id = self.client_id

        supports_collaboration = self.supports_collaboration

        tab_icon_href = self.tab_icon_href

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_href is not UNSET:
            field_dict["baseHref"] = base_href
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if supports_collaboration is not UNSET:
            field_dict["supportsCollaboration"] = supports_collaboration
        if tab_icon_href is not UNSET:
            field_dict["tabIconHref"] = tab_icon_href

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_href = d.pop("baseHref", UNSET)

        client_id = d.pop("clientId", UNSET)

        supports_collaboration = d.pop("supportsCollaboration", UNSET)

        tab_icon_href = d.pop("tabIconHref", UNSET)

        bt_application_target_info = cls(
            base_href=base_href,
            client_id=client_id,
            supports_collaboration=supports_collaboration,
            tab_icon_href=tab_icon_href,
        )

        bt_application_target_info.additional_properties = d
        return bt_application_target_info

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
