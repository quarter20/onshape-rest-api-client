from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.components import Components
    from ..models.external_documentation import ExternalDocumentation
    from ..models.info import Info
    from ..models.open_api_extensions import OpenAPIExtensions
    from ..models.open_api_paths import OpenAPIPaths
    from ..models.open_api_webhooks import OpenAPIWebhooks
    from ..models.security_requirement import SecurityRequirement
    from ..models.server import Server
    from ..models.tag import Tag


T = TypeVar("T", bound="OpenAPI")


@_attrs_define
class OpenAPI:
    """
    Attributes:
        components (Components | Unset):
        extensions (OpenAPIExtensions | Unset):
        external_docs (ExternalDocumentation | Unset):
        info (Info | Unset):
        json_schema_dialect (str | Unset):
        openapi (str | Unset):
        paths (OpenAPIPaths | Unset):
        security (list[SecurityRequirement] | Unset):
        servers (list[Server] | Unset):
        tags (list[Tag] | Unset):
        webhooks (OpenAPIWebhooks | Unset):
    """

    components: Components | Unset = UNSET
    extensions: OpenAPIExtensions | Unset = UNSET
    external_docs: ExternalDocumentation | Unset = UNSET
    info: Info | Unset = UNSET
    json_schema_dialect: str | Unset = UNSET
    openapi: str | Unset = UNSET
    paths: OpenAPIPaths | Unset = UNSET
    security: list[SecurityRequirement] | Unset = UNSET
    servers: list[Server] | Unset = UNSET
    tags: list[Tag] | Unset = UNSET
    webhooks: OpenAPIWebhooks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        components: dict[str, Any] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = self.components.to_dict()

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        external_docs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_docs, Unset):
            external_docs = self.external_docs.to_dict()

        info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        json_schema_dialect = self.json_schema_dialect

        openapi = self.openapi

        paths: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paths, Unset):
            paths = self.paths.to_dict()

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

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        webhooks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhooks, Unset):
            webhooks = self.webhooks.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if components is not UNSET:
            field_dict["components"] = components
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if external_docs is not UNSET:
            field_dict["externalDocs"] = external_docs
        if info is not UNSET:
            field_dict["info"] = info
        if json_schema_dialect is not UNSET:
            field_dict["jsonSchemaDialect"] = json_schema_dialect
        if openapi is not UNSET:
            field_dict["openapi"] = openapi
        if paths is not UNSET:
            field_dict["paths"] = paths
        if security is not UNSET:
            field_dict["security"] = security
        if servers is not UNSET:
            field_dict["servers"] = servers
        if tags is not UNSET:
            field_dict["tags"] = tags
        if webhooks is not UNSET:
            field_dict["webhooks"] = webhooks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.components import Components
        from ..models.external_documentation import ExternalDocumentation
        from ..models.info import Info
        from ..models.open_api_extensions import OpenAPIExtensions
        from ..models.open_api_paths import OpenAPIPaths
        from ..models.open_api_webhooks import OpenAPIWebhooks
        from ..models.security_requirement import SecurityRequirement
        from ..models.server import Server
        from ..models.tag import Tag

        d = dict(src_dict)
        _components = d.pop("components", UNSET)
        components: Components | Unset
        if isinstance(_components, Unset):
            components = UNSET
        else:
            components = Components.from_dict(_components)

        _extensions = d.pop("extensions", UNSET)
        extensions: OpenAPIExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = OpenAPIExtensions.from_dict(_extensions)

        _external_docs = d.pop("externalDocs", UNSET)
        external_docs: ExternalDocumentation | Unset
        if isinstance(_external_docs, Unset):
            external_docs = UNSET
        else:
            external_docs = ExternalDocumentation.from_dict(_external_docs)

        _info = d.pop("info", UNSET)
        info: Info | Unset
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = Info.from_dict(_info)

        json_schema_dialect = d.pop("jsonSchemaDialect", UNSET)

        openapi = d.pop("openapi", UNSET)

        _paths = d.pop("paths", UNSET)
        paths: OpenAPIPaths | Unset
        if isinstance(_paths, Unset):
            paths = UNSET
        else:
            paths = OpenAPIPaths.from_dict(_paths)

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

        _tags = d.pop("tags", UNSET)
        tags: list[Tag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = Tag.from_dict(tags_item_data)

                tags.append(tags_item)

        _webhooks = d.pop("webhooks", UNSET)
        webhooks: OpenAPIWebhooks | Unset
        if isinstance(_webhooks, Unset):
            webhooks = UNSET
        else:
            webhooks = OpenAPIWebhooks.from_dict(_webhooks)

        open_api = cls(
            components=components,
            extensions=extensions,
            external_docs=external_docs,
            info=info,
            json_schema_dialect=json_schema_dialect,
            openapi=openapi,
            paths=paths,
            security=security,
            servers=servers,
            tags=tags,
            webhooks=webhooks,
        )

        open_api.additional_properties = d
        return open_api

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
