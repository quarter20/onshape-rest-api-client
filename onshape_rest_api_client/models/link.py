from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_extensions import LinkExtensions
    from ..models.link_headers import LinkHeaders
    from ..models.link_parameters import LinkParameters
    from ..models.link_request_body import LinkRequestBody
    from ..models.server import Server


T = TypeVar("T", bound="Link")


@_attrs_define
class Link:
    """
    Attributes:
        description (str | Unset):
        extensions (LinkExtensions | Unset):
        getref (str | Unset):
        headers (LinkHeaders | Unset):
        operation_id (str | Unset):
        operation_ref (str | Unset):
        parameters (LinkParameters | Unset):
        request_body (LinkRequestBody | Unset):
        server (Server | Unset):
    """

    description: str | Unset = UNSET
    extensions: LinkExtensions | Unset = UNSET
    getref: str | Unset = UNSET
    headers: LinkHeaders | Unset = UNSET
    operation_id: str | Unset = UNSET
    operation_ref: str | Unset = UNSET
    parameters: LinkParameters | Unset = UNSET
    request_body: LinkRequestBody | Unset = UNSET
    server: Server | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        getref = self.getref

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        operation_id = self.operation_id

        operation_ref = self.operation_ref

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        request_body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request_body, Unset):
            request_body = self.request_body.to_dict()

        server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if getref is not UNSET:
            field_dict["get$ref"] = getref
        if headers is not UNSET:
            field_dict["headers"] = headers
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id
        if operation_ref is not UNSET:
            field_dict["operationRef"] = operation_ref
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if request_body is not UNSET:
            field_dict["requestBody"] = request_body
        if server is not UNSET:
            field_dict["server"] = server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link_extensions import LinkExtensions
        from ..models.link_headers import LinkHeaders
        from ..models.link_parameters import LinkParameters
        from ..models.link_request_body import LinkRequestBody
        from ..models.server import Server

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: LinkExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = LinkExtensions.from_dict(_extensions)

        getref = d.pop("get$ref", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: LinkHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = LinkHeaders.from_dict(_headers)

        operation_id = d.pop("operationId", UNSET)

        operation_ref = d.pop("operationRef", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: LinkParameters | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = LinkParameters.from_dict(_parameters)

        _request_body = d.pop("requestBody", UNSET)
        request_body: LinkRequestBody | Unset
        if isinstance(_request_body, Unset):
            request_body = UNSET
        else:
            request_body = LinkRequestBody.from_dict(_request_body)

        _server = d.pop("server", UNSET)
        server: Server | Unset
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = Server.from_dict(_server)

        link = cls(
            description=description,
            extensions=extensions,
            getref=getref,
            headers=headers,
            operation_id=operation_id,
            operation_ref=operation_ref,
            parameters=parameters,
            request_body=request_body,
            server=server,
        )

        link.additional_properties = d
        return link

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
