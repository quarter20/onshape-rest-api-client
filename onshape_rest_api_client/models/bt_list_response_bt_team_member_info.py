from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_team_member_info import BTTeamMemberInfo


T = TypeVar("T", bound="BTListResponseBTTeamMemberInfo")


@_attrs_define
class BTListResponseBTTeamMemberInfo:
    """A list of resources that typically supports paging.

    Attributes:
        href (str | Unset): URI for current page of resources.
        items (list[BTTeamMemberInfo] | Unset): Array of items in the current page.
        next_ (str | Unset): URI for next page of the resources if more are available.
        previous (str | Unset): URI for previous page of the resources.
    """

    href: str | Unset = UNSET
    items: list[BTTeamMemberInfo] | Unset = UNSET
    next_: str | Unset = UNSET
    previous: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        href = self.href

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        next_ = self.next_

        previous = self.previous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if href is not UNSET:
            field_dict["href"] = href
        if items is not UNSET:
            field_dict["items"] = items
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_team_member_info import BTTeamMemberInfo

        d = dict(src_dict)
        href = d.pop("href", UNSET)

        _items = d.pop("items", UNSET)
        items: list[BTTeamMemberInfo] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = BTTeamMemberInfo.from_dict(items_item_data)

                items.append(items_item)

        next_ = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        bt_list_response_bt_team_member_info = cls(
            href=href,
            items=items,
            next_=next_,
            previous=previous,
        )

        bt_list_response_bt_team_member_info.additional_properties = d
        return bt_list_response_bt_team_member_info

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
