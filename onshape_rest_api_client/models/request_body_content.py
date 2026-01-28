from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_type import MediaType


T = TypeVar("T", bound="RequestBodyContent")


@_attrs_define
class RequestBodyContent:
    """
    Attributes:
        empty (bool | Unset):
    """

    empty: bool | Unset = UNSET
    additional_properties: dict[str, MediaType] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        empty = self.empty

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})
        if empty is not UNSET:
            field_dict["empty"] = empty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_type import MediaType

        d = dict(src_dict)
        empty = d.pop("empty", UNSET)

        request_body_content = cls(
            empty=empty,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = MediaType.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        request_body_content.additional_properties = additional_properties
        return request_body_content

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> MediaType:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: MediaType) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
