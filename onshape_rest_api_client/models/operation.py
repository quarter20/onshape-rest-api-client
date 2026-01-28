from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_documentation import ExternalDocumentation
    from ..models.operation_callbacks import OperationCallbacks
    from ..models.operation_extensions import OperationExtensions
    from ..models.operation_responses import OperationResponses
    from ..models.parameter import Parameter
    from ..models.request_body import RequestBody
    from ..models.security_requirement import SecurityRequirement
    from ..models.server import Server


T = TypeVar("T", bound="Operation")


@_attrs_define
class Operation:
    """
    Attributes:
        callbacks (OperationCallbacks | Unset):
        deprecated (bool | Unset):
        description (str | Unset):
        extensions (OperationExtensions | Unset):
        external_docs (ExternalDocumentation | Unset):
        operation_id (str | Unset):
        parameters (list[Parameter] | Unset):
        request_body (RequestBody | Unset):
        responses (OperationResponses | Unset):
        security (list[SecurityRequirement] | Unset):
        servers (list[Server] | Unset):
        summary (str | Unset):
        tags (list[str] | Unset):
    """

    callbacks: OperationCallbacks | Unset = UNSET
    deprecated: bool | Unset = UNSET
    description: str | Unset = UNSET
    extensions: OperationExtensions | Unset = UNSET
    external_docs: ExternalDocumentation | Unset = UNSET
    operation_id: str | Unset = UNSET
    parameters: list[Parameter] | Unset = UNSET
    request_body: RequestBody | Unset = UNSET
    responses: OperationResponses | Unset = UNSET
    security: list[SecurityRequirement] | Unset = UNSET
    servers: list[Server] | Unset = UNSET
    summary: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        callbacks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.callbacks, Unset):
            callbacks = self.callbacks.to_dict()

        deprecated = self.deprecated

        description = self.description

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        external_docs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_docs, Unset):
            external_docs = self.external_docs.to_dict()

        operation_id = self.operation_id

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)

        request_body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request_body, Unset):
            request_body = self.request_body.to_dict()

        responses: dict[str, Any] | Unset = UNSET
        if not isinstance(self.responses, Unset):
            responses = self.responses.to_dict()

        security: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.security, Unset):
            security = []
            for security_item_data in self.security:
                security_item = security_item_data.to_dict()
                security.append(security_item)

        servers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)

        summary = self.summary

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if callbacks is not UNSET:
            field_dict["callbacks"] = callbacks
        if deprecated is not UNSET:
            field_dict["deprecated"] = deprecated
        if description is not UNSET:
            field_dict["description"] = description
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if external_docs is not UNSET:
            field_dict["externalDocs"] = external_docs
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if request_body is not UNSET:
            field_dict["requestBody"] = request_body
        if responses is not UNSET:
            field_dict["responses"] = responses
        if security is not UNSET:
            field_dict["security"] = security
        if servers is not UNSET:
            field_dict["servers"] = servers
        if summary is not UNSET:
            field_dict["summary"] = summary
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_documentation import ExternalDocumentation
        from ..models.operation_callbacks import OperationCallbacks
        from ..models.operation_extensions import OperationExtensions
        from ..models.operation_responses import OperationResponses
        from ..models.parameter import Parameter
        from ..models.request_body import RequestBody
        from ..models.security_requirement import SecurityRequirement
        from ..models.server import Server

        d = dict(src_dict)
        _callbacks = d.pop("callbacks", UNSET)
        callbacks: OperationCallbacks | Unset
        if isinstance(_callbacks, Unset):
            callbacks = UNSET
        else:
            callbacks = OperationCallbacks.from_dict(_callbacks)

        deprecated = d.pop("deprecated", UNSET)

        description = d.pop("description", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: OperationExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = OperationExtensions.from_dict(_extensions)

        _external_docs = d.pop("externalDocs", UNSET)
        external_docs: ExternalDocumentation | Unset
        if isinstance(_external_docs, Unset):
            external_docs = UNSET
        else:
            external_docs = ExternalDocumentation.from_dict(_external_docs)

        operation_id = d.pop("operationId", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: list[Parameter] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = Parameter.from_dict(parameters_item_data)

                parameters.append(parameters_item)

        _request_body = d.pop("requestBody", UNSET)
        request_body: RequestBody | Unset
        if isinstance(_request_body, Unset):
            request_body = UNSET
        else:
            request_body = RequestBody.from_dict(_request_body)

        _responses = d.pop("responses", UNSET)
        responses: OperationResponses | Unset
        if isinstance(_responses, Unset):
            responses = UNSET
        else:
            responses = OperationResponses.from_dict(_responses)

        _security = d.pop("security", UNSET)
        security: list[SecurityRequirement] | Unset = UNSET
        if _security is not UNSET:
            security = []
            for security_item_data in _security:
                security_item = SecurityRequirement.from_dict(security_item_data)

                security.append(security_item)

        _servers = d.pop("servers", UNSET)
        servers: list[Server] | Unset = UNSET
        if _servers is not UNSET:
            servers = []
            for servers_item_data in _servers:
                servers_item = Server.from_dict(servers_item_data)

                servers.append(servers_item)

        summary = d.pop("summary", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        operation = cls(
            callbacks=callbacks,
            deprecated=deprecated,
            description=description,
            extensions=extensions,
            external_docs=external_docs,
            operation_id=operation_id,
            parameters=parameters,
            request_body=request_body,
            responses=responses,
            security=security,
            servers=servers,
            summary=summary,
            tags=tags,
        )

        operation.additional_properties = d
        return operation

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
