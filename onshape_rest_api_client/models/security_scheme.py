from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.in_ import In
from ..models.type_ import Type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.o_auth_flows import OAuthFlows
    from ..models.security_scheme_extensions import SecuritySchemeExtensions


T = TypeVar("T", bound="SecurityScheme")


@_attrs_define
class SecurityScheme:
    """
    Attributes:
        bearer_format (str | Unset):
        description (str | Unset):
        extensions (SecuritySchemeExtensions | Unset):
        flows (OAuthFlows | Unset):
        getref (str | Unset):
        in_ (In | Unset):
        name (str | Unset):
        open_id_connect_url (str | Unset):
        scheme (str | Unset):
        type_ (Type | Unset):
    """

    bearer_format: str | Unset = UNSET
    description: str | Unset = UNSET
    extensions: SecuritySchemeExtensions | Unset = UNSET
    flows: OAuthFlows | Unset = UNSET
    getref: str | Unset = UNSET
    in_: In | Unset = UNSET
    name: str | Unset = UNSET
    open_id_connect_url: str | Unset = UNSET
    scheme: str | Unset = UNSET
    type_: Type | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bearer_format = self.bearer_format

        description = self.description

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        flows: dict[str, Any] | Unset = UNSET
        if not isinstance(self.flows, Unset):
            flows = self.flows.to_dict()

        getref = self.getref

        in_: str | Unset = UNSET
        if not isinstance(self.in_, Unset):
            in_ = self.in_.value

        name = self.name

        open_id_connect_url = self.open_id_connect_url

        scheme = self.scheme

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bearer_format is not UNSET:
            field_dict["bearerFormat"] = bearer_format
        if description is not UNSET:
            field_dict["description"] = description
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if flows is not UNSET:
            field_dict["flows"] = flows
        if getref is not UNSET:
            field_dict["get$ref"] = getref
        if in_ is not UNSET:
            field_dict["in"] = in_
        if name is not UNSET:
            field_dict["name"] = name
        if open_id_connect_url is not UNSET:
            field_dict["openIdConnectUrl"] = open_id_connect_url
        if scheme is not UNSET:
            field_dict["scheme"] = scheme
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.o_auth_flows import OAuthFlows
        from ..models.security_scheme_extensions import SecuritySchemeExtensions

        d = dict(src_dict)
        bearer_format = d.pop("bearerFormat", UNSET)

        description = d.pop("description", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: SecuritySchemeExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = SecuritySchemeExtensions.from_dict(_extensions)

        _flows = d.pop("flows", UNSET)
        flows: OAuthFlows | Unset
        if isinstance(_flows, Unset):
            flows = UNSET
        else:
            flows = OAuthFlows.from_dict(_flows)

        getref = d.pop("get$ref", UNSET)

        _in_ = d.pop("in", UNSET)
        in_: In | Unset
        if isinstance(_in_, Unset):
            in_ = UNSET
        else:
            in_ = In(_in_)

        name = d.pop("name", UNSET)

        open_id_connect_url = d.pop("openIdConnectUrl", UNSET)

        scheme = d.pop("scheme", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Type | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = Type(_type_)

        security_scheme = cls(
            bearer_format=bearer_format,
            description=description,
            extensions=extensions,
            flows=flows,
            getref=getref,
            in_=in_,
            name=name,
            open_id_connect_url=open_id_connect_url,
            scheme=scheme,
            type_=type_,
        )

        security_scheme.additional_properties = d
        return security_scheme

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
