from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_named_views_info_named_views import BTNamedViewsInfoNamedViews


T = TypeVar("T", bound="BTNamedViewsInfo")


@_attrs_define
class BTNamedViewsInfo:
    """
    Attributes:
        named_views (BTNamedViewsInfoNamedViews | Unset):
    """

    named_views: BTNamedViewsInfoNamedViews | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        named_views: dict[str, Any] | Unset = UNSET
        if not isinstance(self.named_views, Unset):
            named_views = self.named_views.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if named_views is not UNSET:
            field_dict["namedViews"] = named_views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_named_views_info_named_views import BTNamedViewsInfoNamedViews

        d = dict(src_dict)
        _named_views = d.pop("namedViews", UNSET)
        named_views: BTNamedViewsInfoNamedViews | Unset
        if isinstance(_named_views, Unset):
            named_views = UNSET
        else:
            named_views = BTNamedViewsInfoNamedViews.from_dict(_named_views)

        bt_named_views_info = cls(
            named_views=named_views,
        )

        bt_named_views_info.additional_properties = d
        return bt_named_views_info

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
