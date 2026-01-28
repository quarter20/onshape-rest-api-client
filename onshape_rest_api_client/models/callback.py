from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.callback_extensions import CallbackExtensions
    from ..models.path_item import PathItem


T = TypeVar("T", bound="Callback")


@_attrs_define
class Callback:
    """
    Attributes:
        empty (bool | Unset):
        extensions (CallbackExtensions | Unset):
        getref (str | Unset):
    """

    empty: bool | Unset = UNSET
    extensions: CallbackExtensions | Unset = UNSET
    getref: str | Unset = UNSET
    additional_properties: dict[str, PathItem] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        empty = self.empty

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        getref = self.getref

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})
        if empty is not UNSET:
            field_dict["empty"] = empty
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if getref is not UNSET:
            field_dict["get$ref"] = getref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.callback_extensions import CallbackExtensions
        from ..models.path_item import PathItem

        d = dict(src_dict)
        empty = d.pop("empty", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: CallbackExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = CallbackExtensions.from_dict(_extensions)

        getref = d.pop("get$ref", UNSET)

        callback = cls(
            empty=empty,
            extensions=extensions,
            getref=getref,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = PathItem.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        callback.additional_properties = additional_properties
        return callback

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
