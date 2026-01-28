from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.o_auth_flow_extensions import OAuthFlowExtensions
    from ..models.o_auth_flow_scopes import OAuthFlowScopes


T = TypeVar("T", bound="OAuthFlow")


@_attrs_define
class OAuthFlow:
    """
    Attributes:
        authorization_url (str | Unset):
        extensions (OAuthFlowExtensions | Unset):
        refresh_url (str | Unset):
        scopes (OAuthFlowScopes | Unset):
        token_url (str | Unset):
    """

    authorization_url: str | Unset = UNSET
    extensions: OAuthFlowExtensions | Unset = UNSET
    refresh_url: str | Unset = UNSET
    scopes: OAuthFlowScopes | Unset = UNSET
    token_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authorization_url = self.authorization_url

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        refresh_url = self.refresh_url

        scopes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes.to_dict()

        token_url = self.token_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorization_url is not UNSET:
            field_dict["authorizationUrl"] = authorization_url
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if refresh_url is not UNSET:
            field_dict["refreshUrl"] = refresh_url
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if token_url is not UNSET:
            field_dict["tokenUrl"] = token_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_flow_extensions import OAuthFlowExtensions
        from ..models.o_auth_flow_scopes import OAuthFlowScopes

        d = dict(src_dict)
        authorization_url = d.pop("authorizationUrl", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: OAuthFlowExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = OAuthFlowExtensions.from_dict(_extensions)

        refresh_url = d.pop("refreshUrl", UNSET)

        _scopes = d.pop("scopes", UNSET)
        scopes: OAuthFlowScopes | Unset
        if isinstance(_scopes, Unset):
            scopes = UNSET
        else:
            scopes = OAuthFlowScopes.from_dict(_scopes)

        token_url = d.pop("tokenUrl", UNSET)

        o_auth_flow = cls(
            authorization_url=authorization_url,
            extensions=extensions,
            refresh_url=refresh_url,
            scopes=scopes,
            token_url=token_url,
        )

        o_auth_flow.additional_properties = d
        return o_auth_flow

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
