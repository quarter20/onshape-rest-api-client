from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_api_paths_extensions import OpenAPIPathsExtensions
    from ..models.path_item import PathItem


T = TypeVar("T", bound="OpenAPIPaths")


@_attrs_define
class OpenAPIPaths:
    """
    Attributes:
        extensions (OpenAPIPathsExtensions | Unset):
        empty (bool | Unset):
    """

    extensions: OpenAPIPathsExtensions | Unset = UNSET
    empty: bool | Unset = UNSET
    additional_properties: dict[str, PathItem] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        empty = self.empty

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if empty is not UNSET:
            field_dict["empty"] = empty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_api_paths_extensions import OpenAPIPathsExtensions
        from ..models.path_item import PathItem

        d = dict(src_dict)
        _extensions = d.pop("extensions", UNSET)
        extensions: OpenAPIPathsExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = OpenAPIPathsExtensions.from_dict(_extensions)

        empty = d.pop("empty", UNSET)

        open_api_paths = cls(
            extensions=extensions,
            empty=empty,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = PathItem.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        open_api_paths.additional_properties = additional_properties
        return open_api_paths

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> PathItem:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: PathItem) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
