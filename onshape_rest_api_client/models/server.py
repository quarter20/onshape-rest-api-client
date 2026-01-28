from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_extensions import ServerExtensions
    from ..models.server_variables import ServerVariables


T = TypeVar("T", bound="Server")


@_attrs_define
class Server:
    """
    Attributes:
        description (str | Unset):
        extensions (ServerExtensions | Unset):
        url (str | Unset):
        variables (ServerVariables | Unset):
    """

    description: str | Unset = UNSET
    extensions: ServerExtensions | Unset = UNSET
    url: str | Unset = UNSET
    variables: ServerVariables | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        url = self.url

        variables: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if url is not UNSET:
            field_dict["url"] = url
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_extensions import ServerExtensions
        from ..models.server_variables import ServerVariables

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: ServerExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = ServerExtensions.from_dict(_extensions)

        url = d.pop("url", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: ServerVariables | Unset
        if isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = ServerVariables.from_dict(_variables)

        server = cls(
            description=description,
            extensions=extensions,
            url=url,
            variables=variables,
        )

        server.additional_properties = d
        return server

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
