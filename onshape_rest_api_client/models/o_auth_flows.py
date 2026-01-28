from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.o_auth_flow import OAuthFlow
    from ..models.o_auth_flows_extensions import OAuthFlowsExtensions


T = TypeVar("T", bound="OAuthFlows")


@_attrs_define
class OAuthFlows:
    """
    Attributes:
        authorization_code (OAuthFlow | Unset):
        client_credentials (OAuthFlow | Unset):
        extensions (OAuthFlowsExtensions | Unset):
        implicit (OAuthFlow | Unset):
        password (OAuthFlow | Unset):
    """

    authorization_code: OAuthFlow | Unset = UNSET
    client_credentials: OAuthFlow | Unset = UNSET
    extensions: OAuthFlowsExtensions | Unset = UNSET
    implicit: OAuthFlow | Unset = UNSET
    password: OAuthFlow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authorization_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authorization_code, Unset):
            authorization_code = self.authorization_code.to_dict()

        client_credentials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_credentials, Unset):
            client_credentials = self.client_credentials.to_dict()

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        implicit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.implicit, Unset):
            implicit = self.implicit.to_dict()

        password: dict[str, Any] | Unset = UNSET
        if not isinstance(self.password, Unset):
            password = self.password.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authorization_code is not UNSET:
            field_dict["authorizationCode"] = authorization_code
        if client_credentials is not UNSET:
            field_dict["clientCredentials"] = client_credentials
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if implicit is not UNSET:
            field_dict["implicit"] = implicit
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_flow import OAuthFlow
        from ..models.o_auth_flows_extensions import OAuthFlowsExtensions

        d = dict(src_dict)
        _authorization_code = d.pop("authorizationCode", UNSET)
        authorization_code: OAuthFlow | Unset
        if isinstance(_authorization_code, Unset):
            authorization_code = UNSET
        else:
            authorization_code = OAuthFlow.from_dict(_authorization_code)

        _client_credentials = d.pop("clientCredentials", UNSET)
        client_credentials: OAuthFlow | Unset
        if isinstance(_client_credentials, Unset):
            client_credentials = UNSET
        else:
            client_credentials = OAuthFlow.from_dict(_client_credentials)

        _extensions = d.pop("extensions", UNSET)
        extensions: OAuthFlowsExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = OAuthFlowsExtensions.from_dict(_extensions)

        _implicit = d.pop("implicit", UNSET)
        implicit: OAuthFlow | Unset
        if isinstance(_implicit, Unset):
            implicit = UNSET
        else:
            implicit = OAuthFlow.from_dict(_implicit)

        _password = d.pop("password", UNSET)
        password: OAuthFlow | Unset
        if isinstance(_password, Unset):
            password = UNSET
        else:
            password = OAuthFlow.from_dict(_password)

        o_auth_flows = cls(
            authorization_code=authorization_code,
            client_credentials=client_credentials,
            extensions=extensions,
            implicit=implicit,
            password=password,
        )

        o_auth_flows.additional_properties = d
        return o_auth_flows

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
