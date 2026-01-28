from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.components_callbacks import ComponentsCallbacks
    from ..models.components_examples import ComponentsExamples
    from ..models.components_extensions import ComponentsExtensions
    from ..models.components_headers import ComponentsHeaders
    from ..models.components_links import ComponentsLinks
    from ..models.components_parameters import ComponentsParameters
    from ..models.components_path_items import ComponentsPathItems
    from ..models.components_request_bodies import ComponentsRequestBodies
    from ..models.components_responses import ComponentsResponses
    from ..models.components_schemas import ComponentsSchemas
    from ..models.components_security_schemes import ComponentsSecuritySchemes


T = TypeVar("T", bound="Components")


@_attrs_define
class Components:
    """
    Attributes:
        callbacks (ComponentsCallbacks | Unset):
        examples (ComponentsExamples | Unset):
        extensions (ComponentsExtensions | Unset):
        headers (ComponentsHeaders | Unset):
        links (ComponentsLinks | Unset):
        parameters (ComponentsParameters | Unset):
        path_items (ComponentsPathItems | Unset):
        request_bodies (ComponentsRequestBodies | Unset):
        responses (ComponentsResponses | Unset):
        schemas (ComponentsSchemas | Unset):
        security_schemes (ComponentsSecuritySchemes | Unset):
    """

    callbacks: ComponentsCallbacks | Unset = UNSET
    examples: ComponentsExamples | Unset = UNSET
    extensions: ComponentsExtensions | Unset = UNSET
    headers: ComponentsHeaders | Unset = UNSET
    links: ComponentsLinks | Unset = UNSET
    parameters: ComponentsParameters | Unset = UNSET
    path_items: ComponentsPathItems | Unset = UNSET
    request_bodies: ComponentsRequestBodies | Unset = UNSET
    responses: ComponentsResponses | Unset = UNSET
    schemas: ComponentsSchemas | Unset = UNSET
    security_schemes: ComponentsSecuritySchemes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        callbacks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.callbacks, Unset):
            callbacks = self.callbacks.to_dict()

        examples: dict[str, Any] | Unset = UNSET
        if not isinstance(self.examples, Unset):
            examples = self.examples.to_dict()

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        path_items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.path_items, Unset):
            path_items = self.path_items.to_dict()

        request_bodies: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request_bodies, Unset):
            request_bodies = self.request_bodies.to_dict()

        responses: dict[str, Any] | Unset = UNSET
        if not isinstance(self.responses, Unset):
            responses = self.responses.to_dict()

        schemas: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schemas, Unset):
            schemas = self.schemas.to_dict()

        security_schemes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.security_schemes, Unset):
            security_schemes = self.security_schemes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if callbacks is not UNSET:
            field_dict["callbacks"] = callbacks
        if examples is not UNSET:
            field_dict["examples"] = examples
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if headers is not UNSET:
            field_dict["headers"] = headers
        if links is not UNSET:
            field_dict["links"] = links
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if path_items is not UNSET:
            field_dict["pathItems"] = path_items
        if request_bodies is not UNSET:
            field_dict["requestBodies"] = request_bodies
        if responses is not UNSET:
            field_dict["responses"] = responses
        if schemas is not UNSET:
            field_dict["schemas"] = schemas
        if security_schemes is not UNSET:
            field_dict["securitySchemes"] = security_schemes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.components_callbacks import ComponentsCallbacks
        from ..models.components_examples import ComponentsExamples
        from ..models.components_extensions import ComponentsExtensions
        from ..models.components_headers import ComponentsHeaders
        from ..models.components_links import ComponentsLinks
        from ..models.components_parameters import ComponentsParameters
        from ..models.components_path_items import ComponentsPathItems
        from ..models.components_request_bodies import ComponentsRequestBodies
        from ..models.components_responses import ComponentsResponses
        from ..models.components_schemas import ComponentsSchemas
        from ..models.components_security_schemes import ComponentsSecuritySchemes

        d = dict(src_dict)
        _callbacks = d.pop("callbacks", UNSET)
        callbacks: ComponentsCallbacks | Unset
        if isinstance(_callbacks, Unset):
            callbacks = UNSET
        else:
            callbacks = ComponentsCallbacks.from_dict(_callbacks)

        _examples = d.pop("examples", UNSET)
        examples: ComponentsExamples | Unset
        if isinstance(_examples, Unset):
            examples = UNSET
        else:
            examples = ComponentsExamples.from_dict(_examples)

        _extensions = d.pop("extensions", UNSET)
        extensions: ComponentsExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = ComponentsExtensions.from_dict(_extensions)

        _headers = d.pop("headers", UNSET)
        headers: ComponentsHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = ComponentsHeaders.from_dict(_headers)

        _links = d.pop("links", UNSET)
        links: ComponentsLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ComponentsLinks.from_dict(_links)

        _parameters = d.pop("parameters", UNSET)
        parameters: ComponentsParameters | Unset
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = ComponentsParameters.from_dict(_parameters)

        _path_items = d.pop("pathItems", UNSET)
        path_items: ComponentsPathItems | Unset
        if isinstance(_path_items, Unset):
            path_items = UNSET
        else:
            path_items = ComponentsPathItems.from_dict(_path_items)

        _request_bodies = d.pop("requestBodies", UNSET)
        request_bodies: ComponentsRequestBodies | Unset
        if isinstance(_request_bodies, Unset):
            request_bodies = UNSET
        else:
            request_bodies = ComponentsRequestBodies.from_dict(_request_bodies)

        _responses = d.pop("responses", UNSET)
        responses: ComponentsResponses | Unset
        if isinstance(_responses, Unset):
            responses = UNSET
        else:
            responses = ComponentsResponses.from_dict(_responses)

        _schemas = d.pop("schemas", UNSET)
        schemas: ComponentsSchemas | Unset
        if isinstance(_schemas, Unset):
            schemas = UNSET
        else:
            schemas = ComponentsSchemas.from_dict(_schemas)

        _security_schemes = d.pop("securitySchemes", UNSET)
        security_schemes: ComponentsSecuritySchemes | Unset
        if isinstance(_security_schemes, Unset):
            security_schemes = UNSET
        else:
            security_schemes = ComponentsSecuritySchemes.from_dict(_security_schemes)

        components = cls(
            callbacks=callbacks,
            examples=examples,
            extensions=extensions,
            headers=headers,
            links=links,
            parameters=parameters,
            path_items=path_items,
            request_bodies=request_bodies,
            responses=responses,
            schemas=schemas,
            security_schemes=security_schemes,
        )

        components.additional_properties = d
        return components

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
