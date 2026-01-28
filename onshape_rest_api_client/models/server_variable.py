from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_variable_extensions import ServerVariableExtensions


T = TypeVar("T", bound="ServerVariable")


@_attrs_define
class ServerVariable:
    """
    Attributes:
        default (str | Unset):
        description (str | Unset):
        enum (list[str] | Unset):
        extensions (ServerVariableExtensions | Unset):
    """

    default: str | Unset = UNSET
    description: str | Unset = UNSET
    enum: list[str] | Unset = UNSET
    extensions: ServerVariableExtensions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default = self.default

        description = self.description

        enum: list[str] | Unset = UNSET
        if not isinstance(self.enum, Unset):
            enum = self.enum

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if enum is not UNSET:
            field_dict["enum"] = enum
        if extensions is not UNSET:
            field_dict["extensions"] = extensions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_variable_extensions import ServerVariableExtensions

        d = dict(src_dict)
        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        enum = cast(list[str], d.pop("enum", UNSET))

        _extensions = d.pop("extensions", UNSET)
        extensions: ServerVariableExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = ServerVariableExtensions.from_dict(_extensions)

        server_variable = cls(
            default=default,
            description=description,
            enum=enum,
            extensions=extensions,
        )

        server_variable.additional_properties = d
        return server_variable

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
