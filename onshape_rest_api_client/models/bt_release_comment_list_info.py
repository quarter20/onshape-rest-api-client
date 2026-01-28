from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bt_comment_info import BTCommentInfo


T = TypeVar("T", bound="BTReleaseCommentListInfo")


@_attrs_define
class BTReleaseCommentListInfo:
    """
    Attributes:
        comments (list[BTCommentInfo] | Unset):
        rp_id (str | Unset):
        rp_name (str | Unset):
    """

    comments: list[BTCommentInfo] | Unset = UNSET
    rp_id: str | Unset = UNSET
    rp_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()
                comments.append(comments_item)

        rp_id = self.rp_id

        rp_name = self.rp_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comments is not UNSET:
            field_dict["comments"] = comments
        if rp_id is not UNSET:
            field_dict["rpId"] = rp_id
        if rp_name is not UNSET:
            field_dict["rpName"] = rp_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bt_comment_info import BTCommentInfo

        d = dict(src_dict)
        _comments = d.pop("comments", UNSET)
        comments: list[BTCommentInfo] | Unset = UNSET
        if _comments is not UNSET:
            comments = []
            for comments_item_data in _comments:
                comments_item = BTCommentInfo.from_dict(comments_item_data)

                comments.append(comments_item)

        rp_id = d.pop("rpId", UNSET)

        rp_name = d.pop("rpName", UNSET)

        bt_release_comment_list_info = cls(
            comments=comments,
            rp_id=rp_id,
            rp_name=rp_name,
        )

        bt_release_comment_list_info.additional_properties = d
        return bt_release_comment_list_info

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
