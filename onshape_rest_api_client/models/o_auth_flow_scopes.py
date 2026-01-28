from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.o_auth_flow_scopes_extensions import OAuthFlowScopesExtensions


T = TypeVar("T", bound="OAuthFlowScopes")


@_attrs_define
class OAuthFlowScopes:
    """
    Attributes:
        extensions (OAuthFlowScopesExtensions | Unset):
        empty (bool | Unset):
    """

    extensions: OAuthFlowScopesExtensions | Unset = UNSET
    empty: bool | Unset = UNSET
    additional_properties: dict[str, str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        empty = self.empty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if empty is not UNSET:
            field_dict["empty"] = empty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_flow_scopes_extensions import OAuthFlowScopesExtensions

        d = dict(src_dict)
        _extensions = d.pop("extensions", UNSET)
        extensions: OAuthFlowScopesExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = OAuthFlowScopesExtensions.from_dict(_extensions)

        empty = d.pop("empty", UNSET)

        o_auth_flow_scopes = cls(
            extensions=extensions,
            empty=empty,
        )

        o_auth_flow_scopes.additional_properties = d
        return o_auth_flow_scopes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
